* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 22: Denetlenebilir SPSS oturumu.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.

* 1) Eşli veri. Oturum sözleşmesi: filtre, ağırlık ve bölme kapalı.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b22-spss-uygulamalar/uyku_esli.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   ID F8.0
   kosul1 F16.4
   kosul2 F16.4
   fark F16.4.
EXECUTE.

DATASET NAME uyku.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
FREQUENCIES VARIABLES=ID /FORMAT=NOTABLE /STATISTICS=MINIMUM MAXIMUM.
DESCRIPTIVES VARIABLES=kosul1 kosul2 fark /STATISTICS=MEAN STDDEV MIN MAX.
T-TEST PAIRS=kosul2 WITH kosul1 (PAIRED)
 /MISSING=ANALYSIS /CRITERIA=CI(.95).
T-TEST TESTVAL=0 /VARIABLES=fark
 /MISSING=ANALYSIS /CRITERIA=CI(.95).

* 2) Bağımsız gruplar: 1 mg/gün; OJ=1, VC=2.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b22-spss-uygulamalar/dis_veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   len F16.4
   supp F8.0
   dose F16.4.
EXECUTE.

DATASET NAME dis.
VALUE LABELS supp 1 'OJ' 2 'VC'.
FREQUENCIES VARIABLES=dose supp.
COMPUTE doz1 = (dose = 1).
FILTER BY doz1.
T-TEST GROUPS=supp(1 2) /VARIABLES=len
 /MISSING=ANALYSIS /CRITERIA=CI(.95).
FILTER OFF.
FREQUENCIES VARIABLES=dose.

* 3) Çıktıyı kaydetmek için (yalnız SPSS'te; yolu kendinize göre ayarlayın):
* OUTPUT SAVE OUTFILE='uygulamalar/b22-spss-uygulamalar/sonuclar/oturum.spv'.
