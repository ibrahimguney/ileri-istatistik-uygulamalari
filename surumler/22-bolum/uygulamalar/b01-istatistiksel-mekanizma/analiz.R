data <- read.csv("uygulamalar/b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv")
stopifnot(nrow(data) == 80, !anyNA(data), all(data$school == "GP"))
stopifnot(identical(data$kaynak_satir, 1:80))
data$G3_bant <- cut(data$G3, breaks = c(-.5, 9.5, 14.5, 20.5),
                    labels = c("0-9", "10-14", "15-20"))
print(table(data$school))
print(table(factor(data$G3, levels = 0:20)))
print(table(data$G3_bant))
print(100 * prop.table(table(data$G3_bant)))
stopifnot(sum(data$G3) == 1011, mean(data$G3) == 12.6375)
fixed_python_ids <- c(21, 23, 26, 34, 40, 44, 56, 59, 60, 62)
print(mean(data$G3[data$kaynak_satir %in% fixed_python_ids]))
message("Bu kimlikler Python seçim kaydıdır; R aynı tohumla aynı seçimi yaptı denmez.")
systematic_means <- sapply(1:8, function(start) mean(data$G3[seq(start, 80, by = 8)]))
print(systematic_means)
stopifnot(isTRUE(all.equal(mean(systematic_means), mean(data$G3))))
missing_demo <- data
missing_demo$G3[1:4] <- NA
missing_demo$G3_bant <- cut(missing_demo$G3, breaks = c(-.5, 9.5, 14.5, 20.5),
                            labels = c("0-9", "10-14", "15-20"))
print(table(missing_demo$G3_bant, useNA = "always"))
high_count <- sum(missing_demo$G3 >= 15, na.rm = TRUE)
print(c(percent_all = 100 * high_count / 80,
        percent_valid = 100 * high_count / sum(!is.na(missing_demo$G3))))
long_data <- reshape(data[c("kaynak_satir", "school", "G1", "G3")],
                     varying = c("G1", "G3"), v.names = "not", timevar = "donem",
                     times = c("G1", "G3"), idvar = "kaynak_satir", direction = "long")
stopifnot(nrow(long_data) == 160, length(unique(long_data$kaynak_satir)) == 80)
periodic <- rep(c(1, rep(0, 7)), 10)
print(sapply(1:8, function(start) mean(periodic[seq(start, 80, by = 8)])))
message("Eksik örneği değiştirilmiş kopya, döngü örneği kurgudur. Ana dosya değiştirilmez.")
print(sessionInfo())