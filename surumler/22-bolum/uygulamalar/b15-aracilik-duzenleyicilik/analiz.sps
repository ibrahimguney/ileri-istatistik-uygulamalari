* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 15: Aracılık ve düzenleyicilik.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Önce Python betiği veri.csv dosyasını üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b15-aracilik-duzenleyicilik/veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   id F8.0
   x F12.6
   w F12.6
   araci F12.6
   y_aracilik F12.6
   y_duzenleyicilik F12.6.
EXECUTE.

* Aracılık: a yolu (X -> M), b ve c' yolları (X, M -> Y), c toplam etki.
* Dolaylı etkinin bootstrap aralığı için PROCESS makrosu (Model 4) veya
* Python/R betikleri kullanılır; bu sözdizimi yalnız yol katsayılarını verir.
REGRESSION /STATISTICS=COEFF OUTS CI(95) R ANOVA
 /DEPENDENT=araci /METHOD=ENTER x.
REGRESSION /STATISTICS=COEFF OUTS CI(95) R ANOVA
 /DEPENDENT=y_aracilik /METHOD=ENTER x araci.
REGRESSION /STATISTICS=COEFF OUTS CI(95) R ANOVA
 /DEPENDENT=y_aracilik /METHOD=ENTER x.

* Düzenleyicilik: merkezleme ve çarpım terimi.
AGGREGATE /OUTFILE=* MODE=ADDVARIABLES /ort_x=MEAN(x) /ort_w=MEAN(w).
COMPUTE x_c = x - ort_x.
COMPUTE w_c = w - ort_w.
COMPUTE etkilesim = x_c * w_c.
EXECUTE.
REGRESSION /STATISTICS=COEFF OUTS CI(95) R ANOVA BCOV
 /DEPENDENT=y_duzenleyicilik /METHOD=ENTER x_c w_c etkilesim.
* Basit eğim: b(x_c) + d * b(etkileşim); d = -1 SS, 0, +1 SS (w için).
* SH için BCOV tablosundaki varyans ve kovaryanslar kullanılır.
