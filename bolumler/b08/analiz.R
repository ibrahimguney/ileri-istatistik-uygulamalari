arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
kaynak <- read.csv(file.path(directory, "veri.csv"))
stopifnot(identical(names(kaynak), c("kaynak_satir", "school", "age", "G1", "G3")),
          all(kaynak$kaynak_satir == seq_len(80)))
stopifnot(nrow(kaynak) == 80, !anyNA(kaynak), all(kaynak$school == "GP"))
kaynak$age_c <- kaynak$age - 16
kaynak$hedef14 <- as.integer(kaynak$G3 >= 14)
veri <- kaynak[1:60, ]
aktarim <- kaynak[61:80, ]
basit <- lm(G3 ~ G1, data = veri)
coklu <- lm(G3 ~ G1 + age_c, data = veri)
lojistik <- glm(hedef14 ~ G1 + age_c, data = veri, family = binomial())
stopifnot(lojistik$converged)
print(summary(coklu))
print(confint(coklu))
print(anova(basit, coklu))
print(summary(lojistik))
wald <- cbind(katsayi = coef(lojistik),
              alt = coef(lojistik) - qnorm(0.975) * sqrt(diag(vcov(lojistik))),
              ust = coef(lojistik) + qnorm(0.975) * sqrt(diag(vcov(lojistik))))
print(exp(wald))
matris <- model.matrix(coklu)
inverse <- solve(crossprod(matris))
duzeltilmis <- residuals(coklu)^2 / (1 - hatvalues(coklu))^2
hc3 <- inverse %*% crossprod(matris, matris * duzeltilmis) %*% inverse
print(sqrt(diag(hc3)))
print(c(G1 = 1 / (1 - summary(lm(G1 ~ age_c, data = veri))$r.squared),
        age_c = 1 / (1 - summary(lm(age_c ~ G1, data = veri))$r.squared)))
print(coef(lm(G3 ~ G1 + age_c, data = veri[-1, ])))
for (grup in list(veri, aktarim)) {
  olasilik <- predict(lojistik, newdata = grup, type = "response")
  print(c(n = nrow(grup), olay = sum(grup$hedef14),
          Brier = mean((grup$hedef14 - olasilik)^2)))
  for (esik in c(0.3, 0.5, 0.7)) {
    print(esik)
    print(table(gercek = factor(grup$hedef14, levels = 0:1),
                tahmin = factor(as.integer(olasilik >= esik), levels = 0:1)))
  }
}