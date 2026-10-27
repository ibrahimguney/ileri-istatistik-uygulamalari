* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 5: Güç analizi (IBM SPSS Statistics 27 ve üstü).
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.

* Veri dosyası gerekmez. POWER komutu SPSS 27 ile gelmiştir.
* İki bağımsız grup: ortalamalar 0 ve 5 (fark 5), ortak sd 10,
* iki yönlü alfa .05, hedef güç .80, eşit grup oranı.
POWER MEANS INDEPENDENT
 /PARAMETERS TEST=NONDIRECTIONAL SIGNIFICANCE=0.05 POWER=0.80
  NRATIO=1 MEAN=0 5 SD=10.

* Yuvarlama sonrası gerçekleşen güç: grup başına 63 ve 64 kişi.
POWER MEANS INDEPENDENT
 /PARAMETERS TEST=NONDIRECTIONAL SIGNIFICANCE=0.05
  N=63 63 MEAN=0 5 SD=10.
POWER MEANS INDEPENDENT
 /PARAMETERS TEST=NONDIRECTIONAL SIGNIFICANCE=0.05
  N=64 64 MEAN=0 5 SD=10.

* Kayıp payı olmayan 40 kişilik grup için güç.
POWER MEANS INDEPENDENT
 /PARAMETERS TEST=NONDIRECTIONAL SIGNIFICANCE=0.05
  N=40 40 MEAN=0 5 SD=10.
