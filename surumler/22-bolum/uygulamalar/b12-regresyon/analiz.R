veri <- read.csv("uygulamalar/b12-regresyon/not_basari.csv")
stopifnot(nrow(veri) == 60, !anyNA(veri))
model <- lm(G3 ~ G1, data = veri)
print(summary(model))
print(confint(model, level = 0.95))
yeni <- data.frame(G1 = 12)
print(predict(model, newdata = yeni, interval = "confidence", level = 0.95))
print(predict(model, newdata = yeni, interval = "prediction", level = 0.95))
stopifnot(isTRUE(all.equal(unname(coef(model)),
                          c(5.741221241999659, 0.5819927348209655))))
capraz_hata <- numeric(nrow(veri))
egimler <- numeric(nrow(veri))
for (sira in seq_len(nrow(veri))) {
  egitim <- veri[-sira, ]
  deneme <- veri[sira, , drop = FALSE]
  alt_model <- lm(G3 ~ G1, data = egitim)
  capraz_hata[sira] <- deneme$G3 - unname(predict(alt_model, newdata = deneme))
  egimler[sira] <- coef(alt_model)[2]
}
print(c(egitim_RMSE = sqrt(mean(resid(model)^2)),
        LOOCV_RMSE = sqrt(mean(capraz_hata^2))))
print(range(egimler))
tasarim <- model.matrix(model)
bread <- solve(crossprod(tasarim))
duzeltilmis <- as.numeric(resid(model)^2 / (1 - hatvalues(model))^2)
hc3 <- bread %*% crossprod(tasarim, tasarim * duzeltilmis) %*% bread
hc3_se <- sqrt(diag(hc3))
print(hc3_se)
print(coef(model)[2] + c(-1, 1) * qt(0.975, df.residual(model)) * hc3_se[2])
aktarim <- read.csv("uygulamalar/b12-regresyon/aktarim.csv")
print(summary(lm(G3 ~ G1, data = aktarim)))
pdf("uygulamalar/b12-regresyon/tani-R.pdf", width = 8, height = 8)
par(mfrow = c(2, 2))
plot(model)
dev.off()