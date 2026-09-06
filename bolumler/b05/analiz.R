power_ind <- function(count, delta=5, sd=10, alpha=.05, alternative="two.sided") {
  power.t.test(n=count, delta=delta, sd=sd, sig.level=alpha,
               type="two.sample", alternative=alternative, strict=TRUE)$power
}
root <- power.t.test(delta=5, sd=10, sig.level=.05, power=.8,
                     type="two.sample", alternative="two.sided", strict=TRUE)$n
needed <- ceiling(root)
stopifnot(needed == 64, power_ind(needed-1) < .8, power_ind(needed) >= .8)
print(c(surekli_n=root, grup_n=needed, toplam_n=2*needed,
        onceki_guc=power_ind(needed-1), guc=power_ind(needed), guc_n40=power_ind(40)))
print(power.t.test(delta=.5, sd=1, sig.level=.05, power=.8,
                   type="paired", alternative="two.sided", strict=TRUE))
print(uniroot(function(effect) power_ind(40, delta=effect, sd=1)-.8, c(.01,1))$root)
fisher_power <- function(count, rho=.3, alpha=.05) {
  shift <- atanh(rho)*sqrt(count-3)
  critical <- qnorm(1-alpha/2)
  pnorm(critical-shift, lower.tail=FALSE)+pnorm(-critical-shift)
}
counts <- 4:2000
correlation_n <- counts[which(vapply(counts, fisher_power, numeric(1)) >= .8)[1]]
stopifnot(correlation_n == 85)
print(c(korelasyon_yaklasik_n=correlation_n, onceki=fisher_power(84), guc=fisher_power(85)))
retained <- function(enrolled) pbinom(63, enrolled, .85, lower.tail=FALSE)^2
print(c(davet76=retained(76), davet81=retained(81), davet82=retained(82)))
stopifnot(retained(81)<.9, retained(82)>=.9)
arguments <- commandArgs(trailingOnly = FALSE)
file_argument <- arguments[grepl("^--file=", arguments)]
directory <- if (length(file_argument)) dirname(sub("^--file=", "", file_argument[1])) else "."
source <- file.path(directory, "veri.csv")
data <- read.csv(source)
stopifnot(nrow(data)==20, !anyNA(data), !anyDuplicated(data[c("ID","group")]))
wide <- reshape(data[c("ID","group","extra")], idvar="ID", timevar="group", direction="wide")
deviation <- sd(wide$extra.2-wide$extra.1)
for (spread in c(1,deviation,1.5)) {
  result <- power.t.test(delta=.5, sd=spread, power=.8, sig.level=.05,
                         type="paired", alternative="two.sided", strict=TRUE)
  print(c(sigma_D=spread, gereken_cift=ceiling(result$n)))
}
scenarios <- data.frame(delta=c(.2,.3,.5,.8,.5,.5,.5),
                        alpha=c(.05,.05,.05,.05,.05,.01,.05/3),
                        target=c(.8,.8,.8,.8,.9,.8,.8))
for (index in seq_len(nrow(scenarios))) {
  scenario <- scenarios[index,]
  root <- power.t.test(delta=scenario$delta, sd=1, sig.level=scenario$alpha,
                       power=scenario$target, type="two.sample", strict=TRUE)$n
  count <- ceiling(root)
  previous <- power_ind(count-1, delta=scenario$delta, sd=1, alpha=scenario$alpha)
  current <- power_ind(count, delta=scenario$delta, sd=1, alpha=scenario$alpha)
  stopifnot(previous < scenario$target, current >= scenario$target)
  print(c(grup=count, toplam=2*count, onceki=previous, guc=current))
}
power_ratio <- function(count, ratio=2) {
  degrees <- count*(1+ratio)-2
  noncentrality <- .5*sqrt(count*ratio/(1+ratio))
  critical <- qt(.975,degrees)
  pt(-critical,degrees,ncp=noncentrality)+pt(critical,degrees,ncp=noncentrality,lower.tail=FALSE)
}
stopifnot(power_ratio(47)<.8, power_ratio(48)>=.8)
print(c(n1=48,n2=96,guc=power_ratio(48)))
precision <- function(count) qt(.975,2*count-2)*sqrt(2/count)
stopifnot(precision(193)>.2, precision(194)<=.2)
print(c(hassasiyet_grup=194,yari_genislik_sigma=precision(194)))
print(sessionInfo())