# Ölçme değişmezliği — R/lavaan karşılaştırması (çalışma dizini kitap kökü).
if (!requireNamespace("lavaan", quietly = TRUE)) stop("lavaan kurulu olmalı; betik paket kurmaz.")
directory <- "uygulamalar/b20-olcme-degismezligi"
data <- read.csv(file.path(directory, "sonuclar/analiz_verisi.csv"))
data$grup <- factor(data$grup, levels = c("Erkek", "Kadın"))
stopifnot(nrow(data) == 1316)
model <- '
  A =~ A1 + A2 + A3 + A4 + A5
  C =~ C1 + C2 + C3 + C4 + C5
  A1 ~~ A2
  C1 ~~ C2
  C4 ~~ C5
'
fit_level <- function(equal, partial = character(0)) {
  lavaan::cfa(model, data = data, group = "grup", std.lv = TRUE, estimator = "ML",
              group.equal = equal, group.partial = partial)
}
fits <- list(configural = fit_level(character(0)),
             metric = fit_level("loadings"),
             scalar = fit_level(c("loadings", "intercepts")),
             strict = fit_level(c("loadings", "intercepts", "residuals")),
             partial = fit_level(c("loadings", "intercepts"), partial = "A1~1"))
measures <- c("npar", "df", "chisq", "cfi", "tli", "rmsea", "rmsea.ci.lower", "rmsea.ci.upper", "srmr")
print(round(sapply(fits, lavaan::fitMeasures, fit.measures = measures), 4))
print(lavaan::lavTestLRT(fits$configural, fits$metric, fits$scalar, fits$strict))
print(lavaan::lavTestLRT(fits$metric, fits$partial))
print(lavaan::lavTestScore(fits$scalar)$uni)
estimates <- lavaan::parameterEstimates(fits$scalar)
print(estimates[estimates$op == "~1" & estimates$lhs %in% c("A", "C"), ])
print(sessionInfo())
