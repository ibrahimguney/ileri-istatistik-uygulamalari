* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Tekrarlı ölçümler ve karma desenler.
* Çalışma dizini kitap kökü olmalıdır. Önce analiz.py çalıştırılarak
* sonuclar/ klasöründeki geniş ve uzun dosyalar üretilir.
* CD '/kitap/kok/dizini'.
* Not: GLM /WSFACTOR ve MIXED komutları IBM SPSS Statistics içindir;
* GNU PSPP bu iki komutu desteklemez (yalnız DESCRIPTIVES/T-TEST kısmı çalışır).
* ------------------------------------------------------------------.
SET DECIMAL=DOT.

* 1) Uyku yoksunluğu: 18 kişi, 2.–9. günler (8 tekrarlı ölçüm).
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b08-tekrarli-olcumler/sonuclar/uyku_genis.csv'
 /ENCODING='UTF8' /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES= kisi A8 gun2 F10.4 gun3 F10.4 gun4 F10.4 gun5 F10.4
   gun6 F10.4 gun7 F10.4 gun8 F10.4 gun9 F10.4.
EXECUTE.
DATASET NAME uyku.

DESCRIPTIVES VARIABLES=gun2 TO gun9 /STATISTICS=MEAN STDDEV MIN MAX.

* Tek yönlü tekrarlı ölçümler ANOVA; Mauchly, GG/HF ve çok değişkenli testler
* çıktıda kendiliğinden verilir. Polinom karşıtlıklar doğrusal eğilimi ayırır.
GLM gun2 gun3 gun4 gun5 gun6 gun7 gun8 gun9
 /WSFACTOR=gun 8 Polynomial
 /METHOD=SSTYPE(3)
 /PRINT=DESCRIPTIVE ETASQ
 /EMMEANS=TABLES(gun)
 /WSDESIGN=gun.

* Eşli t: 9. gün ile temel (2. gün).
T-TEST PAIRS=gun9 WITH gun2 (PAIRED).

* 2) Karma etkiler modeli: uzun biçim, rastgele kesişim ve eğim (UN kovaryans).
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b08-tekrarli-olcumler/sonuclar/uyku_uzun.csv'
 /ENCODING='UTF8' /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES= kisi A8 gun F4.0 gunB F4.0 tepki F10.4.
EXECUTE.
DATASET NAME uyku_uzun.
MIXED tepki WITH gunB
 /FIXED=gunB
 /RANDOM=INTERCEPT gunB | SUBJECT(kisi) COVTYPE(UN)
 /METHOD=REML
 /PRINT=SOLUTION TESTCOV.

* 3) Orthodont: cinsiyet (arası) x yaş (içi) karma desen.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b08-tekrarli-olcumler/sonuclar/orthodont_genis.csv'
 /ENCODING='UTF8' /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES= kisi A4 cinsiyet F1.0 yas8 F6.1 yas10 F6.1 yas12 F6.1 yas14 F6.1.
EXECUTE.
DATASET NAME orthodont.
VALUE LABELS cinsiyet 1 'Erkek' 2 'Kız'.

GLM yas8 yas10 yas12 yas14 BY cinsiyet
 /WSFACTOR=yas 4 Polynomial
 /METHOD=SSTYPE(3)
 /PRINT=DESCRIPTIVE ETASQ HOMOGENEITY
 /EMMEANS=TABLES(cinsiyet*yas) COMPARE(cinsiyet) ADJ(BONFERRONI)
 /WSDESIGN=yas
 /DESIGN=cinsiyet.
