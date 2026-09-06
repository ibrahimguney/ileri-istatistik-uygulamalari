arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
klasor <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
veri <- read.csv(file.path(klasor, "ToothGrowth.csv"))
stopifnot(nrow(veri) == 60, !anyNA(veri),
          isTRUE(all.equal(veri$len, datasets::ToothGrowth$len)),
          identical(as.character(veri$supp), as.character(datasets::ToothGrowth$supp)),
          isTRUE(all.equal(veri$dose, datasets::ToothGrowth$dose)))
veri$supp <- factor(veri$supp, levels = c("OJ", "VC"))
veri$dose_f <- factor(veri$dose, levels = c(0.5, 1, 2))
stopifnot(all(table(veri$supp, veri$dose_f) == 10))
for (uygulama in c("OJ", "VC")) {
  alt <- veri[veri$supp == uygulama, ]
  model <- aov(len ~ dose_f, data = alt)
  print(uygulama)
  print(summary(model))
  print(TukeyHSD(model, conf.level = .95))
  print(oneway.test(len ~ dose_f, data = alt, var.equal = FALSE))
  gruplar <- split(alt$len, alt$dose_f)
  ciftler <- combn(seq_along(gruplar), 2)
  for (sira in seq_len(ncol(ciftler))) {
    altgrup <- gruplar[[ciftler[1, sira]]]
    ustgrup <- gruplar[[ciftler[2, sira]]]
    bilesen <- c(var(altgrup)/length(altgrup), var(ustgrup)/length(ustgrup))
    derece <- sum(bilesen)^2 / sum(bilesen^2 / (c(length(altgrup), length(ustgrup))-1))
    olcek <- sqrt(sum(bilesen)/2)
    fark <- mean(ustgrup)-mean(altgrup)
    kritik <- qtukey(.95, nmeans = 3, df = derece)
    print(c(fark = fark, GH_p = ptukey(abs(fark)/olcek, nmeans = 3,
                                      df = derece, lower.tail = FALSE),
            alt = fark-kritik*olcek, ust = fark+kritik*olcek))
  }
}
model_tam <- lm(len ~ supp * dose_f, data = veri,
                 contrasts = list(supp = "contr.sum", dose_f = "contr.sum"))
print(anova(model_tam))
hata <- deviance(model_tam)/df.residual(model_tam)
kritik <- qt(1-.05/(2*3), df.residual(model_tam))
for (doz in c(.5, 1, 2)) {
  fark <- mean(veri$len[veri$supp == "OJ" & veri$dose == doz]) -
          mean(veri$len[veri$supp == "VC" & veri$dose == doz])
  standart <- sqrt(hata*(1/10+1/10))
  olasilik <- 2*pt(-abs(fark/standart), df.residual(model_tam))
  print(c(doz = doz, fark = fark, Bonferroni_p = min(1, 3*olasilik),
          alt = fark-kritik*standart, ust = fark+kritik*standart))
}