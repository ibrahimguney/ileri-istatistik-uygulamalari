if (!requireNamespace("lavaan", quietly = TRUE)) {
  stop("lavaan kurulu olmalı; betik paket kurmaz.")
}
arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
data <- read.csv(file.path(directory, "sonuclar", "standartlastirilmis.csv"))
items <- c(paste0("A", 1:5), paste0("C", 1:5))
stopifnot(nrow(data) == 97, !anyNA(data[, items]), !anyDuplicated(data$kaynak_satir))
sample_covariance <- cov(data[, items])
measurement <- '
  A =~ 1*A1 + A2 + A3 + A4 + A5
  C =~ 1*C1 + C2 + C3 + C4 + C5
'
forward_model <- paste0(measurement, '
  C ~ gamma*A
  A ~~ varA*A
  C ~~ psi*C
  A ~~ 0*C
  beta := gamma*sqrt(varA/(gamma^2*varA+psi))
  latent_R2 := gamma^2*varA/(gamma^2*varA+psi)
')
reverse_model <- paste0(measurement, '
  A ~ delta*C
  C ~~ varC*C
  A ~~ psiA*A
  A ~~ 0*C
')
zero_model <- paste0(measurement, '
  C ~ 0*A
  A ~~ 0*C
')
fit_model <- function(model) {
  lavaan::sem(model, sample.cov = sample_covariance, sample.nobs = nrow(data),
              sample.cov.rescale = FALSE, likelihood = "wishart", estimator = "ML",
              meanstructure = FALSE, std.lv = FALSE, fixed.x = FALSE,
              information = "expected")
}
forward <- fit_model(forward_model)
reverse <- fit_model(reverse_model)
zero <- fit_model(zero_model)
stopifnot(lavaan::lavInspect(forward, "converged"), lavaan::lavInspect(reverse, "converged"),
          lavaan::lavInspect(zero, "converged"))
stopifnot(max(abs(lavaan::fitted(forward)$cov - lavaan::fitted(reverse)$cov)) < 1e-5)
python_covariance <- as.matrix(read.csv(file.path(directory, "sonuclar/forward_kovaryans.csv"), row.names = 1))
stopifnot(max(abs(lavaan::fitted(forward)$cov - python_covariance)) < 1e-4)
output <- file.path(directory, "sonuclar_R")
dir.create(output, showWarnings = FALSE)
write.csv(lavaan::parameterEstimates(forward, standardized = TRUE, ci = TRUE),
          file.path(output, "forward_parametreler.csv"), row.names = FALSE)
write.csv(lavaan::standardizedSolution(forward), file.path(output, "forward_standart.csv"), row.names = FALSE)
capture.output(summary(forward, fit.measures = TRUE, standardized = TRUE, rsquare = TRUE),
               summary(reverse, fit.measures = TRUE, standardized = TRUE, rsquare = TRUE),
               lavaan::lavTestLRT(zero, forward), sessionInfo(),
               file = file.path(output, "rapor.txt"))
print(lavaan::lavTestLRT(zero, forward))
