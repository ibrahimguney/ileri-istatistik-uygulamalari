# Tekrarlı ölçümler ve karma desenler — R karşılaştırması (çalışma dizini kitap kökü).
for (package in c("afex", "lme4", "emmeans")) {
  if (!requireNamespace(package, quietly = TRUE)) stop(package, " kurulu olmalı; betik paket kurmaz.")
}
suppressMessages(library(afex))
directory <- "uygulamalar/b08-tekrarli-olcumler"
sleep <- read.csv(file.path(directory, "kaynak/sleepstudy.csv"))
sleep <- subset(sleep, Days >= 2)
sleep$Subject <- factor(sleep$Subject)
sleep$Day <- factor(sleep$Days)
sleep$DaysB <- sleep$Days - 2
stopifnot(nrow(sleep) == 144)
oneway <- aov_ez("Subject", "Reaction", sleep, within = "Day")
print(summary(oneway))
print(nice(oneway, es = c("ges", "pes"), correction = "GG"))
print(summary(oneway$Anova, multivariate = TRUE)$multivariate.tests$Day)
model <- lme4::lmer(Reaction ~ DaysB + (DaysB | Subject), data = sleep, REML = TRUE)
print(summary(model))
ortho <- read.csv(file.path(directory, "kaynak/Orthodont.csv"))
ortho$age <- factor(ortho$age)
mixed <- aov_ez("Subject", "distance", ortho, between = "Sex", within = "age")
print(summary(mixed))
print(nice(mixed, es = c("ges", "pes"), correction = "GG"))
print(emmeans::emmeans(mixed, ~ Sex | age) |> pairs())
print(sessionInfo())
