* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 2: Betimsel istatistik.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b02-betimsel-istatistik/notlar.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   school A2
   G1 F8.0
   G3 F8.0
   fark_G3_G1 F8.0.
EXECUTE.

FREQUENCIES VARIABLES=G1 G3
 /FORMAT=NOTABLE
 /STATISTICS=MEAN MEDIAN MODE STDDEV VARIANCE RANGE MINIMUM MAXIMUM
 /ORDER=ANALYSIS.

* EXAMINE çeyrek yöntemi açıkça yazılır. HAVERAGE, R'nin type=7
* tanımıyla aynı değildir; kitapta type=7 değerleri ayrıca verilir.
EXAMINE VARIABLES=G1 G3
 /PLOT=BOXPLOT
 /PERCENTILES(25,50,75)=HAVERAGE
 /STATISTICS=DESCRIPTIVES EXTREME
 /MISSING=LISTWISE.

DESCRIPTIVES VARIABLES=fark_G3_G1 /STATISTICS=MEAN STDDEV VARIANCE MIN MAX.

* Kovaryans ve korelasyon aynı 80 kayıttan hesaplanır.
CORRELATIONS /VARIABLES=G1 G3
 /PRINT=TWOTAIL
 /STATISTICS=XPROD
 /MISSING=LISTWISE.
