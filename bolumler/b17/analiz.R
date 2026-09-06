if (!requireNamespace("emmeans", quietly = TRUE)) {
  stop("Kurulu emmeans gerekli; bu betik paket kurmaz.")
}
arguments <- commandArgs(trailingOnly = FALSE)
script_argument <- arguments[startsWith(arguments, "--file=")]
if (length(script_argument) != 1L) stop("Bu dosyayı Rscript ile çalıştırın.")
directory <- dirname(sub("^--file=", "", script_argument))
data <- read.csv(file.path(directory, "ToothGrowth.csv"))
data$supp <- factor(data$supp, levels = c("VC", "OJ"))
data$dose_c <- data$dose - 1
stopifnot(nrow(data) == 60, !anyNA(data), all(table(data$supp, data$dose) == 10))
common <- lm(len ~ supp + dose_c, data = data)
separate <- lm(len ~ supp * dose_c, data = data)
cells <- lm(len ~ supp * factor(dose), data = data)
print(summary(common))
print(summary(separate))
print(anova(lm(len ~ dose_c, data = data), common))
print(anova(lm(len ~ supp, data = data), common))
print(anova(common, separate))
print(anova(separate, cells))
stopifnot(df.residual(common) == 57, df.residual(separate) == 56, df.residual(cells) == 54)
common_means <- emmeans::emmeans(common, ~ supp, at = list(dose_c = 0))
print(confint(common_means))
print(summary(pairs(common_means, reverse = TRUE), infer = c(TRUE, TRUE)))
separate_means <- emmeans::emmeans(separate, ~ supp | dose_c,
                                  at = list(dose_c = c(-.5, 0, 1)))
print(summary(pairs(separate_means, reverse = TRUE), by = NULL,
              adjust = "bonferroni", infer = c(TRUE, TRUE)))
cell_means <- emmeans::emmeans(cells, ~ supp | dose)
print(summary(pairs(cell_means, reverse = TRUE), by = NULL,
              adjust = "bonferroni", infer = c(TRUE, TRUE)))
print(emmeans::emtrends(separate, ~ supp, var = "dose_c"))
hc3 <- function(model) {
  matrix <- model.matrix(model)
  inverse <- solve(crossprod(matrix))
  weights <- residuals(model)^2 / (1 - hatvalues(model))^2
  inverse %*% crossprod(matrix, matrix * weights) %*% inverse
}
robust_means <- emmeans::emmeans(cells, ~ supp | dose, vcov. = hc3(cells),
                                df = df.residual(cells))
print(summary(pairs(robust_means, reverse = TRUE), by = NULL,
              adjust = "bonferroni", infer = c(TRUE, TRUE)))
message("Her modelin üç doz kontrastı tek ailedir; model seçimi için düzeltme değildir.")
message("Bu betik çalıştırılmadıkça R ile doğrulama iddiası yapılmaz.")
print(sessionInfo())