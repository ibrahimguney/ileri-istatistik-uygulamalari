arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
klasor <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
data <- read.csv(file.path(klasor, "sonuclar", "puanlanmis.csv"))
item_names <- c(paste0("A", 1:5), paste0("C", 1:5))
values <- as.matrix(data[item_names])
stopifnot(nrow(values) == 97, !anyNA(values), all(values %in% 1:6))
correlation <- cor(values)
count <- ncol(values)
smc <- function(matrix) 1 - 1 / diag(solve(matrix))
spectrum <- function(matrix, reduced = FALSE) {
  if (reduced) diag(matrix) <- smc(matrix)
  eigen(matrix, symmetric = TRUE, only.values = TRUE)$values
}
principal_axes <- function(matrix, factors) {
  communalities <- smc(matrix)
  for (iteration in 1:2000) {
    reduced <- matrix
    diag(reduced) <- communalities
    decomposition <- eigen(reduced, symmetric = TRUE)
    stopifnot(all(decomposition$values[1:factors] > 0))
    loadings <- sweep(decomposition$vectors[, 1:factors, drop = FALSE],
                      2, sqrt(decomposition$values[1:factors]), "*")
    updated <- rowSums(loadings^2)
    change <- sqrt(sum((updated - communalities)^2))
    communalities <- updated
    if (change < 1e-10) break
  }
  stopifnot(change < 1e-10)
  residual <- matrix - tcrossprod(loadings) - diag(1 - communalities)
  rownames(loadings) <- item_names[match(rownames(matrix), item_names)]
  list(loadings = loadings, communalities = communalities,
       RMSR = sqrt(mean(residual[upper.tri(residual)]^2)), iterations = iteration)
}
inverse <- solve(correlation)
partial <- -inverse / sqrt(outer(diag(inverse), diag(inverse)))
diag(partial) <- 0
off_diagonal <- correlation - diag(count)
squares <- colSums(off_diagonal^2)
partial_squares <- colSums(partial^2)
bartlett <- -(nrow(values) - 1 - (2 * count + 5) / 6) * as.numeric(determinant(correlation, logarithm = TRUE)$modulus)
print(list(n = nrow(values), KMO = sum(squares) / sum(squares + partial_squares),
           MSA = squares / (squares + partial_squares), Bartlett = bartlett,
           df = count * (count - 1) / 2,
           p = pchisq(bartlett, count * (count - 1) / 2, lower.tail = FALSE)))
for (factors in 1:3) print(principal_axes(correlation, factors))
main_model <- principal_axes(correlation, 2)
if (requireNamespace("GPArotation", quietly = TRUE)) {
  rotated <- GPArotation::oblimin(main_model$loadings, gam = 0, normalize = FALSE,
                                  eps = 1e-8, maxit = 10000)
  pattern <- as.matrix(rotated$loadings)
  phi <- rotated$Phi
  stopifnot(max(abs(pattern %*% phi %*% t(pattern) - tcrossprod(main_model$loadings))) < 1e-6)
  print(pattern)
  print(phi)
  print(pattern %*% phi)
}
set.seed(20261401)
component_draws <- matrix(NA_real_, 2000, count)
reduced_draws <- matrix(NA_real_, 2000, count)
for (iteration in 1:2000) {
  permuted <- apply(values, 2, sample)
  reference <- cor(permuted)
  component_draws[iteration, ] <- spectrum(reference)
  reduced_draws[iteration, ] <- spectrum(reference, TRUE)
}
for (reduced in c(FALSE, TRUE)) {
  draws <- if (reduced) reduced_draws else component_draws
  bounds <- apply(draws, 2, quantile, probs = .95, type = 7)
  observed <- spectrum(correlation, reduced)
  print(data.frame(reduced = reduced, position = 1:count, observed = observed, reference95 = bounds))
  print(sum(cumprod(observed > bounds)))
}
message("R/Python RNG, faktör işareti ve sırası farkları hesaba katılmalıdır.")
print(sessionInfo())