if (!requireNamespace("lavaan", quietly = TRUE)) {
  stop("lavaan kurulu olmalı; betik paket kurmaz.")
}
# Çalışma dizini kitap kökü olmalı; önce Bölüm 18 ve Bölüm 21 Python betikleri çalıştırılır.
directory <- "uygulamalar/b21-yapisal-esitlik"
data <- read.csv(file.path(directory, "standartlastirilmis.csv"))
items <- c(paste0("A", 1:5), paste0("C", 1:5))
stopifnot(nrow(data) == 1316, !anyNA(data[, c(items, "K")]))
S_all <- cov(data[, c(items, "K")])
S_items <- S_all[items, items]
measurement <- '
  A =~ 1*A1 + A2 + A3 + A4 + A5
  C =~ 1*C1 + C2 + C3 + C4 + C5
  A1 ~~ A2
  C1 ~~ C2
  C4 ~~ C5
'
forward_model <- paste0(measurement, '
  C ~ gamma*A
  A ~~ varA*A
  C ~~ psi*C
  beta := gamma*sqrt(varA/(gamma^2*varA+psi))
  R2_C := gamma^2*varA/(gamma^2*varA+psi)
')
reverse_model <- paste0(measurement, '
  A ~ delta*C
')
zero_model <- paste0(measurement, '
  A ~~ 0*C
')
mediation_model <- paste0(measurement, '
  A ~ a*K
  C ~ b*A + cp*K
  indirect := a*b
  total := cp + a*b
')
fit_model <- function(model, S) {
  lavaan::sem(model, sample.cov = S, sample.nobs = 1316,
              sample.cov.rescale = FALSE, likelihood = "wishart", estimator = "ML",
              meanstructure = FALSE, std.lv = FALSE, fixed.x = FALSE,
              information = "expected")
}
fits <- list(forward = fit_model(forward_model, S_items),
             reverse = fit_model(reverse_model, S_items),
             zero = fit_model(zero_model, S_items),
             mediation = fit_model(mediation_model, S_all))
for (name in names(fits)) {
  stopifnot(lavaan::lavInspect(fits[[name]], "converged"))
  cat("\nMODEL:", name, "\n")
  print(lavaan::fitMeasures(fits[[name]], c("npar", "df", "chisq", "pvalue", "cfi", "tli", "rmsea",
                                             "rmsea.ci.lower", "rmsea.ci.upper", "srmr")))
}
stopifnot(max(abs(lavaan::fitted(fits$forward)$cov - lavaan::fitted(fits$reverse)$cov)) < 1e-5)
python_covariance <- as.matrix(read.csv(file.path(directory, "sonuclar/forward_kovaryans.csv"), row.names = 1))
stopifnot(max(abs(lavaan::fitted(fits$forward)$cov[items, items] - python_covariance[items, items])) < 1e-4)
print(lavaan::lavTestLRT(fits$zero, fits$forward))
estimates <- lavaan::parameterEstimates(fits$forward)
print(estimates[estimates$op %in% c("~", ":=", "~~") & estimates$lhs %in% c("C", "A", "beta", "R2_C"), ])
cat("\nAracılık (ham ölçek, delta yöntemi):\n")
estimates <- lavaan::parameterEstimates(fits$mediation)
print(estimates[estimates$label %in% c("a", "b", "cp", "indirect", "total"), ])
cat("\nAracılık (std.nox: gizil değişkenler standart, K ham 0/1):\n")
standard <- lavaan::standardizedSolution(fits$mediation, type = "std.nox")
print(standard[standard$label %in% c("a", "b", "cp", "indirect", "total"), ])
# İsteğe bağlı: lavaan'ın kendi bootstrap'i (ham veri üzerinde, maddeler çekiliş içinde yeniden
# standartlaştırılmaz; Python'un yüzdelik aralığıyla yakın ama birebir aynı değildir).
if (identical(Sys.getenv("B17_BOOTSTRAP"), "1")) {
  set.seed(20261701)
  boot <- lavaan::sem(mediation_model, data = data[, c(items, "K")], likelihood = "wishart",
                      meanstructure = FALSE, fixed.x = FALSE, se = "bootstrap", bootstrap = 1000)
  print(lavaan::parameterEstimates(boot, boot.ci.type = "perc")[c(29:30), ])
}
print(sessionInfo())
