arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
klasor <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
dis <- read.csv(file.path(klasor, "ToothGrowth.csv"))
uyku <- read.csv(file.path(klasor, "sleep.csv"))
blok <- read.csv(file.path(klasor, "rounding-times.csv"))
stopifnot(nrow(dis)==60, nrow(uyku)==20, nrow(blok)==22,
          !anyNA(dis), !anyNA(uyku), !anyNA(blok))
ilk <- uyku[uyku$group==1, c("ID", "extra")]
ikinci <- uyku[uyku$group==2, c("ID", "extra")]
esli <- merge(ilk, ikinci, by="ID", suffixes=c("1", "2"))
stopifnot(nrow(esli)==10, !anyDuplicated(esli$ID))
fark <- round(esli$extra2-esli$extra1, 1)
print(wilcox.test(fark, exact=FALSE, correct=TRUE))
sifirsiz <- fark[fark!=0]
siralar <- rank(abs(sifirsiz))
pozitif <- sum(siralar[sifirsiz>0])
oruntuler <- as.matrix(expand.grid(rep(list(c(0, 1)), length(siralar))))
toplamlar <- drop(oruntuler %*% siralar)
print(c(W_plus=pozitif, p_exact=min(1, 2*min(mean(toplamlar<=pozitif), mean(toplamlar>=pozitif)))))
oj <- dis$len[dis$supp=="OJ" & dis$dose==1]
vc <- dis$len[dis$supp=="VC" & dis$dose==1]
print(wilcox.test(oj, vc, exact=FALSE, correct=TRUE))
for (uygulama in c("OJ", "VC")) {
  alt <- dis[dis$supp==uygulama, ]
  print(kruskal.test(len ~ factor(dose), data=alt))
  siralar <- rank(alt$len)
  ort <- tapply(siralar, alt$dose, mean)
  adet <- table(alt$dose)
  ciftler <- combn(seq_along(ort), 2)
  ham <- numeric(ncol(ciftler))
  for (sira in seq_len(ncol(ciftler))) {
    grup1 <- ciftler[1,sira]
    grup2 <- ciftler[2,sira]
    standart <- sqrt(var(siralar)*(1/adet[grup1]+1/adet[grup2]))
    ham[sira] <- 2*pnorm(-abs((ort[grup2]-ort[grup1])/standart))
  }
  print(data.frame(uygulama=uygulama, cift=c("1-0.5","2-0.5","2-1"),
                   p_raw=ham, p_holm=p.adjust(ham, method="holm")))
}
matris <- as.matrix(blok[, -1])
print(friedman.test(matris))
ciftler <- combn(1:3, 2)
ham <- apply(ciftler, 2, function(cift) {
  fark <- round(matris[,cift[2]]-matris[,cift[1]], 2)
  wilcox.test(fark, exact=FALSE, correct=TRUE)$p.value
})
print(p.adjust(ham, method="holm"))
tablo <- table(dis$supp, dis$len>=20)
print(tablo)
print(chisq.test(tablo, correct=FALSE))
print(fisher.test(tablo))