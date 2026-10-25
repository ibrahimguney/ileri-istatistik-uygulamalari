* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 12: Basit doğrusal regresyon.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b12-regresyon/not_basari.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   school A2
   G1 F8.0
   G3 F8.0.
EXECUTE.

REGRESSION
 /MISSING=LISTWISE
 /STATISTICS=COEFF OUTS CI(95) R ANOVA
 /CRITERIA=PIN(.05) POUT(.10)
 /NOORIGIN
 /DEPENDENT=G3
 /METHOD=ENTER G1
 /SCATTERPLOT=(*ZRESID, *ZPRED)
 /RESIDUALS=HISTOGRAM(ZRESID) NORMPROB(ZRESID)
 /SAVE=PRED MCIN ICIN ZRESID COOK LEVER.

* G1 = 12 olan kayıtlar için ortalama yanıt (MCIN) ve bireysel
* tahmin (ICIN) aralıkları. Aynı G1 değerinde tahmin aynıdır.
TEMPORARY.
SELECT IF (G1 = 12).
LIST VARIABLES=kaynak_satir G1 G3 PRE_1 LMCI_1 UMCI_1 LICI_1 UICI_1.
