arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
kaynak <- read.csv(file.path(directory, "veri.csv"))
stopifnot(nrow(kaynak) == 80, !anyNA(kaynak))
veri <- kaynak[1:60, ]
aktarim <- kaynak[61:80, ]
print(cor.test(veri$G1, veri$G3, method = "pearson"))
print(cor.test(veri$G1, veri$G3, method = "spearman", exact = FALSE))
sira_G1 <- rank(veri$G1, ties.method = "average")
sira_G3 <- rank(veri$G3, ties.method = "average")
stopifnot(isTRUE(all.equal(cor(sira_G1, sira_G3),
                          cor(veri$G1, veri$G3, method = "spearman"))))
print(c(pearson_haric = cor(veri$G1[-1], veri$G3[-1]),
        spearman_haric = cor(veri$G1[-1], veri$G3[-1], method = "spearman")))
print(c(aktarim_pearson = cor(aktarim$G1, aktarim$G3),
        aktarim_spearman = cor(aktarim$G1, aktarim$G3, method = "spearman")))
set.seed(202606)
tekrar <- 19999
esik <- abs(cor(sira_G1, sira_G3))
permute <- replicate(tekrar, abs(cor(sira_G1, sample(sira_G3))))
print(c(permute_asiri = sum(permute >= esik - 1e-14),
        permute_p = (1 + sum(permute >= esik - 1e-14)) / (tekrar + 1)))
model <- lm(G3 ~ G1, data = veri)
stopifnot(isTRUE(all.equal(cor(veri$G1, veri$G3)^2, summary(model)$r.squared)))
figures <- file.path(directory, "grafikler")
dir.create(figures, showWarnings = FALSE)
pdf(file.path(figures, "grafikler-R.pdf"), width = 8, height = 4)
par(mfrow = c(1, 2))
plot(veri$G1, veri$G3, xlab = "G1", ylab = "G3")
plot(sira_G1, sira_G3, xlab = "G1 sırası", ylab = "G3 sırası")
dev.off()