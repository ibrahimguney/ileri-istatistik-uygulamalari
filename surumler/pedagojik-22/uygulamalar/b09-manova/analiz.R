# MANOVA — R karşılaştırması (çalışma dizini kitap kökü). car kurulu olmalı.
if (!requireNamespace("car", quietly = TRUE)) stop("car kurulu olmalı; betik paket kurmaz.")
directory <- "uygulamalar/b09-manova"
source_data <- read.csv(file.path(directory, "kaynak/sat_act.csv"))
data <- source_data[complete.cases(source_data[, c("ACT", "SATV", "SATQ")]), ]
stopifnot(nrow(data) == 687)
data$gender <- factor(data$gender, labels = c("Erkek", "Kadin"))
data$education <- factor(data$education)
# İki grup: Hotelling T^2 (iki bağımlı değişken)
two <- manova(cbind(SATV, SATQ) ~ gender, data = data)
print(summary(two, test = "Hotelling-Lawley"))
# Tek yönlü: eğitim, dört istatistik
one <- manova(cbind(ACT, SATV, SATQ) ~ education, data = data)
for (test in c("Pillai", "Wilks", "Hotelling-Lawley", "Roy")) print(summary(one, test = test))
print(summary.aov(one))
# İki faktörlü Tip II (car)
options(contrasts = c("contr.sum", "contr.poly"))
fit <- lm(cbind(ACT, SATV, SATQ) ~ gender * education, data = data)
print(car::Manova(fit, type = "II"))
print(summary(car::Manova(fit, type = "II"), multivariate = TRUE, univariate = FALSE)$multivariate.tests$gender)
print(sessionInfo())
