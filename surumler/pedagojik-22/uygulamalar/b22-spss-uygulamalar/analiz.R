directory <- "uygulamalar/b22-spss-uygulamalar"
sleep <- read.csv(file.path(directory, "uyku_esli.csv"))
teeth <- read.csv(file.path(directory, "dis_veri.csv"))
stopifnot(nrow(sleep) == 10, !anyDuplicated(sleep$ID), !anyNA(sleep),
          nrow(teeth) == 60, all(table(teeth$supp, teeth$dose) == 10))
stopifnot(max(abs(sleep$fark - (sleep$kosul2 - sleep$kosul1))) < 1e-8)
paired <- t.test(sleep$kosul2, sleep$kosul1, paired = TRUE)
one <- t.test(sleep$fark, mu = 0)
stopifnot(abs(paired$statistic - one$statistic) < 1e-10)
selected <- subset(teeth, dose == 1)
welch <- t.test(selected$len[selected$supp == 1], selected$len[selected$supp == 2], var.equal = FALSE)
student <- t.test(selected$len[selected$supp == 1], selected$len[selected$supp == 2], var.equal = TRUE)
filtered <- subset(sleep, ID <= 5)
teaching <- sleep
teaching$kosul2[teaching$ID == 1] <- NA
teaching$kosul1[teaching$ID == 2] <- NA
stopifnot(sum(complete.cases(teaching[, c("kosul1", "kosul2")])) == 8)
output <- file.path(directory, "sonuclar_R")
dir.create(output, showWarnings = FALSE)
capture.output(paired, one, welch, student,
               t.test(filtered$kosul2, filtered$kosul1, paired = TRUE),
               t.test(teaching$kosul2, teaching$kosul1, paired = TRUE),
               sessionInfo(), file = file.path(output, "rapor.txt"))
print(paired)
print(welch)