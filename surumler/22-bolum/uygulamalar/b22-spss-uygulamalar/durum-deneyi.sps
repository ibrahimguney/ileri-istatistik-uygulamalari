* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 22: Durum deneyi (karşı örnekler).
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.

* Bu betik ana dosyayı DEĞİŞTİRMEZ; tüm işlemler bellekteki kopyadadır.
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

* Karşı örnek 1: filtre açık unutulursa n değişir.
COMPUTE ilk5 = (ID LE 5).
FILTER BY ilk5.
T-TEST PAIRS=kosul2 WITH kosul1 (PAIRED) /CRITERIA=CI(.95).
FILTER OFF.

* Karşı örnek 2: frekans ağırlığı 2, bağımsız kişi sayısını artırmaz
* ama SPSS n'yi 20 sayar; SH ve p yapay olarak küçülür.
COMPUTE w2 = 2.
WEIGHT BY w2.
T-TEST PAIRS=kosul2 WITH kosul1 (PAIRED) /CRITERIA=CI(.95).
WEIGHT OFF.

* Karşı örnek 3: iki hücre eksik yapılırsa geçerli çift sayısı düşer.
IF (ID = 1) kosul2 = $SYSMIS.
IF (ID = 2) kosul1 = $SYSMIS.
COMPUTE fark = kosul2 - kosul1.
EXECUTE.
T-TEST PAIRS=kosul2 WITH kosul1 (PAIRED) /MISSING=ANALYSIS /CRITERIA=CI(.95).
