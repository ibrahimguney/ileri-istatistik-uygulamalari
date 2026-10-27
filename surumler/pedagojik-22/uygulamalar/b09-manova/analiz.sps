* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — MANOVA (psych::sat.act).
* Çalışma dizini kitap kökü olmalıdır. Önce analiz.py çalıştırılarak
* sonuclar/analiz_verisi.csv (SATQ eksikleri çıkarılmış 687 kayıt) üretilir.
* CD '/kitap/kok/dizini'.
* Not: Çok bağımlı değişkenli GLM IBM SPSS Statistics içindir; GNU PSPP
* GLM'de tek bağımlı değişkeni destekler.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b09-manova/sonuclar/analiz_verisi.csv'
 /ENCODING='UTF8' /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES= kayit F8.0 gender F1.0 education F1.0 age F3.0
   ACT F4.0 SATV F5.0 SATQ F5.0.
EXECUTE.
VALUE LABELS gender 1 'Erkek' 2 'Kadın'.

* Betimsel istatistikler ve korelasyonlar.
MEANS TABLES=ACT SATV SATQ BY education /CELLS=MEAN COUNT STDDEV.
CORRELATIONS /VARIABLES=ACT SATV SATQ.

* Uç değer taraması: REGRESSION ile Mahalanobis uzaklığı (bağımlı değişken
* işlevsizdir, yalnız uzaklıkları kaydetmek için kayıt numarası kullanılır).
REGRESSION /DEPENDENT=kayit /METHOD=ENTER ACT SATV SATQ /SAVE=MAHAL(mah).
COMPUTE uc = (mah > 16.266).
FREQUENCIES VARIABLES=uc.

* İki grup: cinsiyet, iki bağımlı değişken (Hotelling T^2).
GLM SATV SATQ BY gender
 /PRINT=DESCRIPTIVE ETASQ HOMOGENEITY
 /DESIGN=gender.

* Tek yönlü MANOVA: eğitim; Box M ve Levene HOMOGENEITY ile istenir.
GLM ACT SATV SATQ BY education
 /PRINT=DESCRIPTIVE ETASQ HOMOGENEITY
 /DESIGN=education.

* Ayırma fonksiyonları (izleme analizi).
DISCRIMINANT /GROUPS=education(0 5) /VARIABLES=ACT SATV SATQ
 /STATISTICS=MEAN STDDEV COEFF RAW.

* İki faktörlü MANOVA; dengesiz hücrelerde Tip II ile R car::Manova aynıdır.
GLM ACT SATV SATQ BY gender education
 /METHOD=SSTYPE(2)
 /PRINT=ETASQ
 /DESIGN=gender education gender*education.
