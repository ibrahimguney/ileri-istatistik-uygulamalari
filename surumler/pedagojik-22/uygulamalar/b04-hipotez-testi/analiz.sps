* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 4: Eşli t testi.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b04-hipotez-testi/esli_veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   ID F8.0
   kosul1 F12.4
   kosul2 F12.4
   fark F12.4.
EXECUTE.

* Koşul 2 önce yazılır; fark yönü koşul 2 - koşul 1'dir.
T-TEST PAIRS=kosul2 WITH kosul1 (PAIRED)
 /CRITERIA=CI(.95)
 /MISSING=ANALYSIS.

* Aynı test, farklar üzerinde tek örneklem testi olarak.
T-TEST /TESTVAL=0 /VARIABLES=fark /CRITERIA=CI(.95).
