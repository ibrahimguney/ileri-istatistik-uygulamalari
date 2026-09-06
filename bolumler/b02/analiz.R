arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
data <- read.csv(file.path(directory, "veri.csv"))
stopifnot(nrow(data) == 80, !anyNA(data), all(data$school == "GP"))
summary_values <- function(values) {
  quartiles <- quantile(values, c(.25, .5, .75), type = 7)
  spread <- quartiles[3] - quartiles[1]
  lower <- quartiles[1] - 1.5 * spread
  upper <- quartiles[3] + 1.5 * spread
  inside <- values[values >= lower & values <= upper]
  list(n = length(values), mean = mean(values), median = median(values),
       variance = var(values), sd = sd(values), quartiles = quartiles,
       MAD_raw = mad(values, constant = 1), fences = c(lower, upper),
       whiskers = range(inside), flagged = which(values < lower | values > upper))
}
print(lapply(data[c("G1", "G3")], summary_values))
print(cov(data[c("G1", "G3")]))
print(cor(data[c("G1", "G3")]))
difference <- data$G3 - data$G1
print(summary_values(difference))
print(c(positive = sum(difference > 0), zero = sum(difference == 0), negative = sum(difference < 0)))
stopifnot(isTRUE(all.equal(var(difference), var(data$G3) + var(data$G1) - 2 * cov(data$G1, data$G3))))
ordered <- sort(data$G1)
print(c(type7_Q3 = quantile(ordered, .75, type = 7), upper_half_median = median(ordered[41:80])))
print(ordered[60:61])
sensitivity <- subset(data, kaynak_satir != 1)
print(lapply(sensitivity[c("G1", "G3")], summary_values))
print(cor(sensitivity$G1, sensitivity$G3))
block_means <- c(mean(data$G3[1:60]), mean(data$G3[61:80]))
print(c(weighted = weighted.mean(block_means, c(60, 20)), unweighted = mean(block_means)))
print(c(arithmetic_CV = 100 * sd(data$G3) / mean(data$G3),
        shifted_arithmetic_CV = 100 * sd(data$G3 + 10) / mean(data$G3 + 10)))
message("Notların CV oranı göreli yetenek ölçüsü olarak yorumlanmaz; kaynak değiştirilmedi.")
print(sqrt(1.1 * .9) - 1)
print(sessionInfo())