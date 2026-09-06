arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
data <- read.csv(file.path(directory, "veri.csv"))
items <- c(paste0("A", 1:5), paste0("C", 1:5))
stopifnot(nrow(data) == 100, !anyNA(data$kaynak_satir), !anyDuplicated(data$kaynak_satir),
          !anyNA(data$kaynak_kayit), !anyDuplicated(data$kaynak_kayit),
          all(vapply(data[items], is.numeric, logical(1))))
values <- as.matrix(data[items])
stopifnot(all(is.na(values) | values %in% 1:6), sum(is.na(values)) == 3)
scored <- data[items]
reverse <- c("A1", "C4", "C5")
scored[reverse] <- 7 - scored[reverse]
score <- function(block, minimum) {
  count <- rowSums(!is.na(block))
  result <- rowMeans(block, na.rm = TRUE)
  result[count < minimum] <- NA_real_
  result
}
print(colSums(is.na(data[items])))
for (prefix in c("A", "C")) {
  block <- scored[paste0(prefix, 1:5)]
  for (minimum in c(5, 4)) {
    result <- score(block, minimum)
    print(c(prefix = prefix, minimum = minimum, n = sum(!is.na(result)),
            mean = mean(result, na.rm = TRUE)))
  }
}
long <- reshape(data, varying = items, v.names = "yanit", timevar = "madde",
                times = items, idvar = c("kaynak_satir", "kaynak_kayit"), direction = "long")
stopifnot(nrow(long) == 1000, sum(!is.na(long$yanit)) == 997,
          !anyDuplicated(long[c("kaynak_satir", "madde")]))
wide <- reshape(long, v.names = "yanit", timevar = "madde",
                idvar = c("kaynak_satir", "kaynak_kayit"), direction = "wide")
wide <- wide[order(wide$kaynak_satir), ]
stopifnot(isTRUE(all.equal(unname(as.matrix(wide[paste0("yanit.", items)])),
                          unname(values), check.attributes = FALSE)))
synthetic <- rbind(rep(NA_real_, 5), c(6, NA, NA, NA, NA), c(6, 4, 5, 3, NA))
stopifnot(identical(is.na(score(synthetic, 4)), c(TRUE, TRUE, FALSE)),
          score(synthetic, 4)[3] == 4.5)
observed <- data$C1[!is.na(data$C1)]
filled <- data$C1
filled[is.na(filled)] <- mean(observed)
stopifnot(isTRUE(all.equal(var(filled), var(observed) * 98 / 99)))
print(c(observed_var = var(observed), filled_var = var(filled)))
print(sessionInfo())