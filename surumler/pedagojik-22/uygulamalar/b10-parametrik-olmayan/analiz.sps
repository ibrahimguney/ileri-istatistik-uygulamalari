* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 10: Parametrik olmayan testler.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b10-parametrik-olmayan/uyku_genis.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   ID F8.0
   ilac1 F12.4
   ilac2 F12.4.
EXECUTE.

* Wilcoxon işaretli sıralar testi (ilaç 2 - ilaç 1). Sıfır farklar
* SPSS'te 'Ties' satırında gösterilir ve sıralamaya alınmaz.
NPAR TESTS /WILCOXON=ilac2 WITH ilac1 (PAIRED) /SIGN=ilac2 WITH ilac1 (PAIRED)
 /MISSING=ANALYSIS.

GET DATA /TYPE=TXT
 /FILE='uygulamalar/b10-parametrik-olmayan/dis_analiz.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   len F12.4
   supp A2
   dose F12.4
   supp_kod F8.0
   dose_kod F8.0
   esik20 F8.0.
EXECUTE.

VALUE LABELS supp_kod 1 'OJ' 2 'VC' /dose_kod 1 '0.5' 2 '1' 3 '2'
 /esik20 0 'len < 20' 1 'len >= 20'.

* Mann-Whitney U: 1 mg/gün dozunda OJ ve VC.
TEMPORARY.
SELECT IF (dose = 1).
NPAR TESTS /M-W=len BY supp_kod(1 2) /MISSING=ANALYSIS.

* Kruskal-Wallis: OJ grubunda üç doz.
TEMPORARY.
SELECT IF (supp_kod = 1).
NPAR TESTS /K-W=len BY dose_kod(1 3) /MISSING=ANALYSIS.

* Kategorik soru: tüm 60 kayıtta uygulama biçimi x (len >= 20).
CROSSTABS /TABLES=supp_kod BY esik20
 /STATISTICS=CHISQ
 /CELLS=COUNT EXPECTED ROW
 /COUNT ROUND CELL.

GET DATA /TYPE=TXT
 /FILE='uygulamalar/b10-parametrik-olmayan/kaynak/rounding-times.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   blok F8.0
   round_out F12.4
   narrow_angle F12.4
   wide_angle F12.4.
EXECUTE.

* Friedman testi: 22 oyuncu (blok) x 3 koşu yöntemi.
NPAR TESTS /FRIEDMAN=round_out narrow_angle wide_angle /MISSING=LISTWISE.
