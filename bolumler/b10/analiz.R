arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
klasor <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
uyku <- read.csv(file.path(klasor, "sleep.csv"))
dis <- read.csv(file.path(klasor, "ToothGrowth.csv"))
stopifnot(nrow(uyku) == 20, nrow(dis) == 60,
          !anyNA(uyku), !anyNA(dis),
          !anyDuplicated(uyku[c("ID", "group")]))
stopifnot(isTRUE(all.equal(uyku$extra, datasets::sleep$extra)),
          identical(as.character(uyku$group), as.character(datasets::sleep$group)),
          identical(as.character(uyku$ID), as.character(datasets::sleep$ID)),
          isTRUE(all.equal(dis$len, datasets::ToothGrowth$len)),
          identical(as.character(dis$supp), as.character(datasets::ToothGrowth$supp)),
          isTRUE(all.equal(dis$dose, datasets::ToothGrowth$dose)))
esli <- merge(uyku[uyku$group == 1, c("ID", "extra")],
              uyku[uyku$group == 2, c("ID", "extra")],
              by = "ID", suffixes = c("1", "2"))
stopifnot(nrow(esli) == 10)
fark <- esli$extra2 - esli$extra1
print(t.test(esli$extra1, mu = 0))
print(t.test(esli$extra2, esli$extra1, paired = TRUE))
print(t.test(fark, mu = 0))
print(c(d = mean(esli$extra1) / sd(esli$extra1), dz = mean(fark) / sd(fark)))
print(shapiro.test(fark))
for (doz in c(0.5, 1, 2)) {
  oj <- dis$len[dis$dose == doz & dis$supp == "OJ"]
  vc <- dis$len[dis$dose == doz & dis$supp == "VC"]
  print(doz)
  print(t.test(oj, vc, var.equal = FALSE))
  print(t.test(oj, vc, var.equal = TRUE))
  ortak <- sqrt(((length(oj)-1)*var(oj) + (length(vc)-1)*var(vc)) /
                 (length(oj) + length(vc) - 2))
  print(c(d_pooled = (mean(oj)-mean(vc))/ortak))
}
duyarlilik <- lapply(seq_len(nrow(esli)), function(sira) {
  kalan <- fark[-sira]
  test <- t.test(kalan)
  data.frame(ID = esli$ID[sira], fark = mean(kalan), p = test$p.value,
             alt = test$conf.int[1], ust = test$conf.int[2])
})
print(do.call(rbind, duyarlilik))