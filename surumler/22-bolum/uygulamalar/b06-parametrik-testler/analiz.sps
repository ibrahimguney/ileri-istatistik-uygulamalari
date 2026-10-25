* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 6: Parametrik testler.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b06-parametrik-testler/uyku_esli.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   ID F8.0
   ilac1 F12.4
   ilac2 F12.4
   fark F12.4.
EXECUTE.

* Eşli t testi: fark yönü ilaç 2 - ilaç 1.
T-TEST PAIRS=ilac2 WITH ilac1 (PAIRED) /CRITERIA=CI(.95).
T-TEST /TESTVAL=0 /VARIABLES=fark /CRITERIA=CI(.95).
EXAMINE VARIABLES=fark /PLOT=BOXPLOT NPPLOT /STATISTICS=DESCRIPTIVES.

GET DATA /TYPE=TXT
 /FILE='uygulamalar/b06-parametrik-testler/dis_veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   len F12.4
   supp A2
   dose F12.4
   supp_kod F8.0.
EXECUTE.

* Bağımsız t testi yalnız 1 mg/gün dozunda; OJ=1, VC=2.
* 'Equal variances not assumed' satırı Welch sonucudur.
COMPUTE doz1 = (dose = 1).
FILTER BY doz1.
T-TEST GROUPS=supp_kod(1 2) /VARIABLES=len /CRITERIA=CI(.95).
EXAMINE VARIABLES=len BY supp_kod /PLOT=BOXPLOT NPPLOT /STATISTICS=DESCRIPTIVES.
FILTER OFF.
