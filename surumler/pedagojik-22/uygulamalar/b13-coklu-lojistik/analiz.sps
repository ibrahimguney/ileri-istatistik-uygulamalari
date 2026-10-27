* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 13: Çoklu ve lojistik regresyon.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b13-coklu-lojistik/veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   school A2
   age F8.0
   G1 F8.0
   G3 F8.0
   age_c F8.0
   hedef14 F8.0.
EXECUTE.

* Model kurma verisi: ilk 60 kayıt. Sonraki 20 kayıt yalnız aktarım içindir.
COMPUTE kurma = (kaynak_satir LE 60).
FILTER BY kurma.

* Hiyerarşik çoklu regresyon: önce G1, sonra yaş (age_c = age - 16).
REGRESSION
 /MISSING=LISTWISE
 /STATISTICS=COEFF OUTS CI(95) R ANOVA CHANGE COLLIN TOL
 /DEPENDENT=G3
 /METHOD=ENTER G1
 /METHOD=ENTER age_c.

* İkili lojistik regresyon: olay hedef14 = 1 (G3 >= 14).
* SPSS en yüksek kodu olay olarak modeller; kodlama 0/1 olduğundan
* modellenen olay 1'dir. Aralıklar Wald yaklaşımına dayanır.
LOGISTIC REGRESSION VARIABLES=hedef14 WITH G1 age_c
 /PRINT=CI(95) GOODFIT
 /CRITERIA=ITERATE(20) CUT(.5).
FILTER OFF.
