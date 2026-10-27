* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 17: Güvenirlik (Cronbach alfa).
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b17-guvenirlik/puanlanmis_A.csv'
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
   A5 F8.0.
EXECUTE.

* Maddeler Python tarafından zaten anahtarlanmıştır; ikinci kez ters
* kodlama yapılmaz. Tam kayıt sayısı 99 olmalıdır.
RELIABILITY
 /VARIABLES=A1 A2 A3 A4 A5
 /SCALE('A ölçeği') ALL
 /MODEL=ALPHA
 /STATISTICS=DESCRIPTIVE SCALE CORR
 /SUMMARY=TOTAL.

GET DATA /TYPE=TXT
 /FILE='uygulamalar/b17-guvenirlik/puanlanmis_C.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   kaynak_kayit F8.0
   C1 F8.0
   C2 F8.0
   C3 F8.0
   C4 F8.0
   C5 F8.0.
EXECUTE.

* Maddeler Python tarafından zaten anahtarlanmıştır; ikinci kez ters
* kodlama yapılmaz. Tam kayıt sayısı 98 olmalıdır.
RELIABILITY
 /VARIABLES=C1 C2 C3 C4 C5
 /SCALE('C ölçeği') ALL
 /MODEL=ALPHA
 /STATISTICS=DESCRIPTIVE SCALE CORR
 /SUMMARY=TOTAL.
