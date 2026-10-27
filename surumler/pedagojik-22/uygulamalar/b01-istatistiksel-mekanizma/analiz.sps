* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 1: Frekans, yüzde ve payda.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b01-istatistiksel-mekanizma/notlar.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   school A2
   G1 F8.0
   G3 F8.0
   G3_bant A5.
EXECUTE.

* Ana dosya: 80 kayıt, eksik değer yok.
FREQUENCIES VARIABLES=school G3 G3_bant
 /STATISTICS=MEAN
 /ORDER=ANALYSIS.
DESCRIPTIVES VARIABLES=G1 G3 /STATISTICS=MEAN STDDEV MIN MAX.

* Öğretim kopyası: bazı G3 hücreleri bilerek boş bırakılmıştır.
* Boş bant, kullanıcı tanımlı eksik değer olarak işaretlenir; böylece
* 'geçerli yüzde' ile 'tüm kayıtlara göre yüzde' ayrı okunabilir.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b01-istatistiksel-mekanizma/eksik_veri_ogretim.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   school A2
   G1 F8.0
   G3 F8.0
   G3_bant A5.
EXECUTE.

MISSING VALUES G3_bant ('').
FREQUENCIES VARIABLES=G3_bant /ORDER=ANALYSIS.
