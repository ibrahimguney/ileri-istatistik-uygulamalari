* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 11: Korelasyon.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   school A2
   G1 F8.0
   G3 F8.0.
EXECUTE.

* Ana inceleme: ilk 60 kayıt.
TEMPORARY.
SELECT IF (kaynak_satir LE 60).
CORRELATIONS /VARIABLES=G1 G3 /PRINT=TWOTAIL /MISSING=PAIRWISE.
TEMPORARY.
SELECT IF (kaynak_satir LE 60).
NONPAR CORR /VARIABLES=G1 G3 /PRINT=SPEARMAN TWOTAIL /MISSING=PAIRWISE.

* Duyarlılık: G1=0 olan ilk kayıt dışarıda.
TEMPORARY.
SELECT IF (kaynak_satir GE 2 AND kaynak_satir LE 60).
CORRELATIONS /VARIABLES=G1 G3 /PRINT=TWOTAIL.
TEMPORARY.
SELECT IF (kaynak_satir GE 2 AND kaynak_satir LE 60).
NONPAR CORR /VARIABLES=G1 G3 /PRINT=SPEARMAN TWOTAIL.

* Bağımsız çözüm grubu: 61-80. kayıtlar.
TEMPORARY.
SELECT IF (kaynak_satir GE 61).
CORRELATIONS /VARIABLES=G1 G3 /PRINT=TWOTAIL.
TEMPORARY.
SELECT IF (kaynak_satir GE 61).
NONPAR CORR /VARIABLES=G1 G3 /PRINT=SPEARMAN TWOTAIL.
