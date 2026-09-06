arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
data <- read.csv(file.path(directory, "veri.csv"))
stopifnot(nrow(data) == 20, !anyNA(data), !anyDuplicated(data[c("ID", "group")]))
first <- data[data$group == 1, c("ID", "extra")]
second <- data[data$group == 2, c("ID", "extra")]
stopifnot(!anyDuplicated(first$ID), !anyDuplicated(second$ID), setequal(first$ID, second$ID))
wide <- merge(first, second, by = "ID", suffixes = c("_1", "_2"))
stopifnot(nrow(wide) == 10)
difference <- wide$extra_2 - wide$extra_1
paired <- t.test(wide$extra_2, wide$extra_1, paired = TRUE)
one <- t.test(difference, mu = 0)
stopifnot(isTRUE(all.equal(paired$statistic, one$statistic)))
print(paired)
print(t.test(difference, alternative = "greater"))
print(t.test(difference, alternative = "less"))
print(mean(difference)/sd(difference))
summary_test <- function(count, average, deviation, reference) {
  error <- deviation/sqrt(count)
  statistic <- (average-reference)/error
  print(c(t = statistic, df = count-1, two = 2*pt(-abs(statistic), count-1),
          right = pt(statistic, count-1, lower.tail = FALSE), left = pt(statistic, count-1)))
  print(average + c(-1,1)*qt(.975, count-1)*error)
}
summary_test(16,74.5,8,70)
summary_test(25,496,10,500)
summary_test(36,52,12,50)
print(chisq.test(matrix(c(20,30,30,20), nrow = 2), correct = FALSE))
set.seed(20260906)
for (effect in c(0,.5)) {
  samples <- matrix(rnorm(20000*25, mean = effect), nrow = 20000)
  averages <- rowMeans(samples)
  errors <- apply(samples,1,sd)/sqrt(25)
  statistic <- averages/errors
  critical <- qt(.975,24)
  reject <- abs(statistic)>critical
  cover_null <- averages-critical*errors<=0 & averages+critical*errors>=0
  stopifnot(all(reject == !cover_null))
  theory <- pt(-critical,24,ncp=effect*sqrt(25))+pt(critical,24,ncp=effect*sqrt(25),lower.tail=FALSE)
  print(c(d=effect, simulated=mean(reject), theory=theory,
          true_coverage=mean(averages-critical*errors<=effect & averages+critical*errors>=effect)))
}
print(1-.95^20)
print(sessionInfo())