# B18 — Bağımsız R kontrol betiği.
# Depo doğrulaması bu dosyayı çalıştırmaz; gerçek R yürütmesi ayrıca kaydedilmelidir.

sleep <- read.csv("bolumler/b18/sleep.csv")
stopifnot(nrow(sleep) == 20, length(unique(sleep$ID)) == 10)

k1 <- sleep[sleep$group == 1, c("ID", "extra")]
k2 <- sleep[sleep$group == 2, c("ID", "extra")]
names(k1)[2] <- "kosul1"
names(k2)[2] <- "kosul2"
wide <- merge(k1, k2, by = "ID", all = TRUE, sort = TRUE)
wide$fark <- wide$kosul2 - wide$kosul1

print(cor.test(wide$kosul1, wide$kosul2, method = "pearson"))
print(t.test(wide$kosul2, wide$kosul1, paired = TRUE, conf.level = .95))
print(t.test(wide$fark, mu = 0, conf.level = .95))

teeth <- read.csv("bolumler/b18/ToothGrowth.csv")
dose1 <- subset(teeth, dose == 1)
print(t.test(len ~ supp, data = dose1, var.equal = FALSE, conf.level = .95))
print(t.test(len ~ supp, data = dose1, var.equal = TRUE, conf.level = .95))

cat("Not: Levene hesabı temel R'de yerleşik değildir; B18 ana sayısal referansı analiz.py üretir.\n")
