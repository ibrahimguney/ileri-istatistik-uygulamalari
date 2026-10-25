# Bölüm 15: Aracılık ve düzenleyicilik — R karşılığı (kitap kökünden)
#   Rscript uygulamalar/b15-aracilik-duzenleyicilik/analiz.R
# Önce Python betiği veri.csv dosyasını üretir. R'nin rastgele sayı üreteci
# NumPy ile aynı örnekleri vermez; bootstrap aralığının son basamakları farklı
# olabilir, nokta tahminleri aynıdır.
veri <- read.csv("uygulamalar/b15-aracilik-duzenleyicilik/veri.csv")
stopifnot(nrow(veri) == 160, !anyNA(veri))

# Aracılık: a, b, c' ve c yolları
model_a <- lm(araci ~ x, data = veri)
model_b <- lm(y_aracilik ~ x + araci, data = veri)
model_c <- lm(y_aracilik ~ x, data = veri)
a <- coef(model_a)["x"]; b <- coef(model_b)["araci"]
ab <- unname(a * b)
stopifnot(abs(ab - 0.521844) < 5e-7,
          abs(coef(model_c)["x"] - (coef(model_b)["x"] + ab)) < 1e-10)
print(summary(model_a)$coefficients); print(summary(model_b)$coefficients)

set.seed(202610)
boot <- replicate(5000, {
  i <- sample.int(nrow(veri), replace = TRUE)
  d <- veri[i, ]
  coef(lm(araci ~ x, data = d))["x"] * coef(lm(y_aracilik ~ x + araci, data = d))["araci"]
})
cat(sprintf("ab = %.6f; R bootstrap %%95 persentil GA = [%.4f, %.4f]\n",
            ab, quantile(boot, .025), quantile(boot, .975)))

# Düzenleyicilik: merkezleme ve basit eğimler
veri$x_c <- veri$x - mean(veri$x)
veri$w_c <- veri$w - mean(veri$w)
model_mod <- lm(y_duzenleyicilik ~ x_c * w_c, data = veri)
print(summary(model_mod)$coefficients)
V <- vcov(model_mod); s <- sd(veri$w)
for (d in c(-s, 0, s)) {
  est <- coef(model_mod)["x_c"] + d * coef(model_mod)["x_c:w_c"]
  se <- sqrt(V["x_c", "x_c"] + d^2 * V["x_c:w_c", "x_c:w_c"] + 2 * d * V["x_c", "x_c:w_c"])
  cat(sprintf("W = %+.4f: basit eğim %.4f (SH %.4f)\n", d, est, se))
}
