arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
veri <- read.csv(file.path(directory, "veri.csv"))
stopifnot(nrow(veri) == 160, !anyNA(veri), all(veri$kayit == seq_len(160)))
model_a <- lm(araci ~ x, data = veri)
model_b <- lm(y_aracilik ~ x + araci, data = veri)
model_c <- lm(y_aracilik ~ x, data = veri)
carpim <- unname(coef(model_a)["x"] * coef(model_b)["araci"])
stopifnot(isTRUE(all.equal(unname(coef(model_c)["x"]), unname(coef(model_b)["x"]) + carpim)))
print(summary(model_a))
print(summary(model_b))
print(c(dolayli = carpim, dogrudan = coef(model_b)["x"], toplam = coef(model_c)["x"]))
set.seed(202610)
tekrar <- 5000
bootstrap <- numeric(tekrar)
for (sayac in seq_len(tekrar)) {
  secim <- sample.int(nrow(veri), nrow(veri), replace = TRUE)
  ornek <- veri[secim, ]
  alt_a <- lm(araci ~ x, data = ornek)
  alt_b <- lm(y_aracilik ~ x + araci, data = ornek)
  if (alt_a$rank != 2 || alt_b$rank != 3) stop("Rank kaybı; tekrar atlanmadı.")
  bootstrap[sayac] <- coef(alt_a)["x"] * coef(alt_b)["araci"]
}
stopifnot(all(is.finite(bootstrap)))
print(quantile(bootstrap, c(0.025, 0.975), type = 7))
veri$x_c <- veri$x - mean(veri$x)
veri$w_c <- veri$w - mean(veri$w)
model_mod <- lm(y_duzenleyicilik ~ x_c * w_c, data = veri)
model_ham <- lm(y_duzenleyicilik ~ x * w, data = veri)
stopifnot(isTRUE(all.equal(fitted(model_mod), fitted(model_ham))))
print(summary(model_mod))
print(confint(model_mod))
for (duzey in c(-sd(veri$w), 0, sd(veri$w))) {
  kontrast <- c(0, 1, 0, duzey)
  egim <- sum(kontrast * coef(model_mod))
  standart_hata <- sqrt(drop(t(kontrast) %*% vcov(model_mod) %*% kontrast))
  aralik <- egim + c(-1, 1) * qt(0.975, df.residual(model_mod)) * standart_hata
  print(c(w = mean(veri$w) + duzey, egim = egim, SH = standart_hata, alt = aralik[1], ust = aralik[2]))
}