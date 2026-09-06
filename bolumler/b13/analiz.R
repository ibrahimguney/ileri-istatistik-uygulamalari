arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
klasor <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
source_data <- read.csv(file.path(klasor, "bfi-ilk100-AC.csv"))
stopifnot(nrow(source_data) == 100, identical(source_data$kaynak_satir, 1:100))
alpha_raw <- function(values) {
  stopifnot(!anyNA(values), ncol(values) >= 2)
  covariance <- cov(values)
  count <- ncol(values)
  stopifnot(sum(covariance) > 0)
  count / (count - 1) * (1 - sum(diag(covariance)) / sum(covariance))
}
keys <- list(A = "A1", C = c("C4", "C5"))
for (scale_name in names(keys)) {
  item_names <- paste0(scale_name, 1:5)
  raw <- source_data[item_names]
  raw <- raw[complete.cases(raw), , drop = FALSE]
  keyed <- raw
  keyed[keys[[scale_name]]] <- 7 - keyed[keys[[scale_name]]]
  expected_n <- if (scale_name == "A") 99 else 98
  stopifnot(nrow(keyed) == expected_n)
  mean_r <- mean(cor(keyed)[lower.tri(cor(keyed))])
  standard_alpha <- 5 * mean_r / (1 + 4 * mean_r)
  item_table <- do.call(rbind, lapply(item_names, function(item) {
    rest <- keyed[setdiff(item_names, item)]
    data.frame(item = item,
               item_rest_r = cor(keyed[[item]], rowSums(rest)),
               item_total_r = cor(keyed[[item]], rowSums(keyed)),
               alpha_if_deleted_same_cases = alpha_raw(rest))
  }))
  seed <- if (scale_name == "A") 202613 else 202614
  set.seed(seed)
  draws <- replicate(20000, alpha_raw(keyed[sample.int(nrow(keyed), replace = TRUE), ]))
  print(list(scale = scale_name, n = nrow(keyed), raw_alpha = alpha_raw(keyed),
             standard_alpha = standard_alpha, mean_r = mean_r,
             before_reversing = alpha_raw(raw), bootstrap_seed = seed,
             percentile_ci95 = quantile(draws, c(.025, .975), type = 7)))
  print(item_table)
  if (requireNamespace("psych", quietly = TRUE)) {
    comparison <- psych::alpha(keyed, check.keys = FALSE)
    stopifnot(isTRUE(all.equal(unname(comparison$total$raw_alpha), alpha_raw(keyed))),
              isTRUE(all.equal(unname(comparison$total$std.alpha), standard_alpha)))
    print(comparison$item.stats)
    print(comparison$alpha.drop)
  }
}
message("R ve Python RNG farkı nedeniyle bootstrap aralıkları birebir eşleşmeyebilir.")
print(sessionInfo())