# Depo kökünden: Rscript bolumler/b18/analiz.R
# Yalnız temel R kullanır. SPSS yürütmesi değildir.
options(digits = 17)
here <- 'bolumler/b18'
sleep <- read.csv(file.path(here, 'sleep.csv'))
teeth <- read.csv(file.path(here, 'ToothGrowth.csv'))
stopifnot(nrow(sleep) == 20, length(unique(sleep$ID)) == 10,
          !anyNA(sleep), !anyDuplicated(sleep[c('ID','group')]),
          all(table(sleep$ID, sleep$group) == 1), nrow(teeth) == 60,
          !anyNA(teeth), all(table(teeth$dose, teeth$supp) == 10))
k1 <- sleep[sleep$group == 1, c('ID','extra')]
k2 <- sleep[sleep$group == 2, c('ID','extra')]
names(k1)[2] <- 'kosul1'; names(k2)[2] <- 'kosul2'
wide <- merge(k1, k2, by='ID', all=TRUE, sort=TRUE)
wide$fark <- wide$kosul2-wide$kosul1
stopifnot(nrow(wide) == 10, !anyNA(wide))
values <- numeric()
add <- function(prefix, x) {
  names(x) <- paste(prefix, names(x), sep='.')
  values <<- c(values, x)
}
summary_values <- function(x) c(n=length(x), ortalama=mean(x), s=sd(x))
one <- function(x) {
  z <- t.test(x, mu=0, conf.level=.95)
  c(summary_values(x), SH=sd(x)/sqrt(length(x)), t=unname(z$statistic),
    sd=unname(z$parameter), p_iki_yonlu=z$p.value,
    GA95.0=z$conf.int[1], GA95.1=z$conf.int[2])
}
add('uyku_esli.kosul1',summary_values(wide$kosul1))
add('uyku_esli.kosul2',summary_values(wide$kosul2))
prefix <- 'uyku_esli.fark_kosul2_eksi_kosul1'
add(prefix,one(wide$fark));add(prefix,c(dz=mean(wide$fark)/sd(wide$fark)))
paired <- t.test(wide$kosul2,wide$kosul1,paired=TRUE)
stopifnot(isTRUE(all.equal(unname(paired$statistic),unname(t.test(wide$fark)$statistic))))
correlation <- cor.test(wide$kosul1,wide$kosul2)
add('uyku_esli.korelasyon',c(r=unname(correlation$estimate),p=correlation$p.value))
dose1 <- subset(teeth,dose==1)
oj <- subset(dose1,supp=='OJ')$len; vc <- subset(dose1,supp=='VC')$len
add('ToothGrowth_doz1.OJ',summary_values(oj));add('ToothGrowth_doz1.VC',summary_values(vc))
for (model in c('Welch','Student')) {
 z <- t.test(oj,vc,var.equal=(model=='Student'),conf.level=.95)
 delta <- mean(oj)-mean(vc)
 add(paste0('ToothGrowth_doz1.',model),c(fark=delta,SH=delta/unname(z$statistic),
     t=unname(z$statistic),sd=unname(z$parameter),p_iki_yonlu=z$p.value,
     GA95.0=z$conf.int[1],GA95.1=z$conf.int[2]))
}
# Ortalama merkezli Levene: mutlak grup artıkları üzerinde tek yönlü ANOVA.
absolute <- abs(dose1$len-ave(dose1$len,dose1$supp,FUN=mean))
lev <- anova(lm(absolute ~ dose1$supp))
add('ToothGrowth_doz1.Levene_ortalama_merkezli',c(F=lev$'F value'[1],p=lev$'Pr(>F)'[1]))
pooled <- sqrt(((length(oj)-1)*var(oj)+(length(vc)-1)*var(vc))/(length(oj)+length(vc)-2))
add('ToothGrowth_doz1',c(d_pooled=(mean(oj)-mean(vc))/pooled))
add('durum_deneyi.ID_1_5_filtresi',one(wide$fark[wide$ID<=5]))
add('durum_deneyi.agirlik_2_mekanik_tekrar',one(rep(wide$fark,each=2)))
missing <- wide
missing$kosul2[missing$ID==1] <- NA
missing$kosul1[missing$ID==2] <- NA
missing$fark <- missing$kosul2-missing$kosul1
add('durum_deneyi.iki_hucre_gizleme',c(kosul1_gecerli=sum(!is.na(missing$kosul1)),
    kosul2_gecerli=sum(!is.na(missing$kosul2)),tam_cift=sum(complete.cases(missing[c('kosul1','kosul2')]))))
add('durum_deneyi.iki_hucre_gizleme',one(na.omit(missing$fark)))
stopifnot(!anyDuplicated(names(values)), all(is.finite(values)))
out <- file.path(here,'sonuclar','R'); dir.create(out,recursive=TRUE,showWarnings=FALSE)
write.csv(data.frame(metric=names(values),value=unname(values)),file.path(out,'sayisal_kontrol.csv'),row.names=FALSE)
writeLines(capture.output(sessionInfo()),file.path(out,'sessionInfo.txt'))
cat('B18 gerçek R yürütmesi:',length(values),'sayısal sonuç üretildi. SPSS çalıştırılmadı.\n')
