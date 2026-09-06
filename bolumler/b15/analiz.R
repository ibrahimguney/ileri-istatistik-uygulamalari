if (!requireNamespace("lavaan", quietly = TRUE)) {
  stop("Kurulu lavaan gerekli; bu betik paket kurmaz.")
}
arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
klasor <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
source_data <- read.csv(file.path(klasor, "sonuclar", "puanlanmis.csv"))
item_names <- c(paste0("A", 1:5), paste0("C", 1:5))
values <- source_data[item_names]
stopifnot(nrow(values) == 97, !anyNA(values))
sample_covariance <- cor(values)
base_model <- '
 A =~ A1 + A2 + A3 + A4 + A5
 C =~ C1 + C2 + C3 + C4 + C5
'
models <- list(
  orthogonal = paste(base_model, "A ~~ 0*C"),
  correlated = paste(base_model, "A ~~ C"),
  cross_A2 = '
    A =~ A1 + A2 + A3 + A4 + A5
    C =~ C1 + C2 + C3 + C4 + C5 + A2
    A ~~ C
  '
)
fits <- lapply(models, function(model) {
  lavaan::cfa(model, sample.cov = sample_covariance, sample.nobs = 97,
              estimator = "ML", likelihood = "wishart", std.lv = TRUE,
              meanstructure = FALSE, sample.cov.rescale = FALSE,
              information = "expected", se = "standard", test = "standard")
})
for (name in names(fits)) {
  fit <- fits[[name]]
  stopifnot(lavaan::lavInspect(fit, "converged"))
  cat("\nMODEL:", name, "\n")
  measures <- lavaan::fitMeasures(fit, c("npar", "df", "chisq", "pvalue", "cfi", "tli", "rmsea",
                                         "rmsea.ci.lower", "rmsea.ci.upper", "srmr"))
  print(measures)
  print(lavaan::standardizedSolution(fit, type = "std.all", ci = TRUE))
  implied <- lavaan::fitted(fit)$cov
  residual <- (sample_covariance - implied) / sqrt(outer(diag(sample_covariance), diag(sample_covariance)))
  print(list(SRMR_explicit = sqrt(mean(residual[lower.tri(residual, diag = TRUE)]^2)),
             AIC_star = measures["chisq"] + 2 * measures["npar"],
             BIC_star = measures["chisq"] + log(97) * measures["npar"]))
}
print(lavaan::lavTestLRT(fits$orthogonal, fits$correlated))
print(lavaan::lavTestLRT(fits$correlated, fits$cross_A2))
standard <- lavaan::lavInspect(fits$correlated, "std")
for (scale_name in c("A", "C")) {
  names <- paste0(scale_name, 1:5)
  loadings <- standard$lambda[names, scale_name]
  errors <- diag(standard$theta)[names]
  print(list(scale = scale_name, AVE = sum(loadings^2) / sum(loadings^2 + errors),
             CR_standardized_sum = sum(loadings)^2 / (sum(loadings)^2 + sum(errors))))
}
message("A2 fark testinin nominal p değeri veriyle model seçimine göre düzeltilmemiştir.")
message("R çıktısı çalıştırıldığında değerlendirilmelidir; Python dosyalarının doğrulandığı varsayılmaz.")
print(sessionInfo())