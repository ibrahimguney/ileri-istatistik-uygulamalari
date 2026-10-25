* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 18: Açıklayıcı faktör analizi.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b18-faktor-analizi/puanlanmis.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   kaynak_kayit F8.0
   A1 F8.0
   A2 F8.0
   A3 F8.0
   A4 F8.0
   A5 F8.0
   C1 F8.0
   C2 F8.0
   C3 F8.0
   C4 F8.0
   C5 F8.0.
EXECUTE.

* Yarım A: 1316 tam kayıt; maddeler zaten anahtarlanmıştır.
* Temel eksenler (PAF), iki faktör, doğrudan oblimin (delta = 0).
* NOKAISER: kitaptaki normalizasyonsuz çözümle eşleşmek için.
* Varsayılan Kaiser normalizasyonu için NOKAISER yerine KAISER yazın.
FACTOR
 /VARIABLES A1 A2 A3 A4 A5 C1 C2 C3 C4 C5
 /MISSING LISTWISE
 /ANALYSIS A1 A2 A3 A4 A5 C1 C2 C3 C4 C5
 /PRINT INITIAL CORRELATION KMO AIC EXTRACTION ROTATION REPR
 /FORMAT SORT
 /PLOT EIGEN
 /CRITERIA FACTORS(2) ITERATE(200) ECONVERGE(.00001) DELTA(0) NOKAISER
 /EXTRACTION PAF
 /ROTATION OBLIMIN
 /METHOD=CORRELATION.
