* Bölüm 18 — IBM SPSS Uygulamaları.
* Bu syntax, SPSS menü adımlarını denetlenebilir komut kaydına dönüştürür.
* Dosyaları B18 klasörünü SPSS çalışma klasörü yaparak çalıştırın veya /FILE yollarını uyarlayın.

SET DECIMAL DOT.

* ================================================================.
* 1. SLEEP: GERÇEK VERİYİ İÇE AKTARMA VE ID ÜZERİNDEN EŞLEŞTİRME.
* ================================================================.

GET DATA
  /TYPE=TXT
  /FILE='sleep.csv'
  /ENCODING='UTF8'
  /DELCASE=LINE
  /DELIMITERS=","
  /ARRANGEMENT=DELIMITED
  /FIRSTCASE=2
  /IMPORTCASE=ALL
  /VARIABLES=
    kaynak_satir F3.0
    extra F8.2
    group F1.0
    ID F3.0.
CACHE.
EXECUTE.
DATASET NAME SleepLong WINDOW=FRONT.

FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.

FREQUENCIES VARIABLES=group ID.
DESCRIPTIVES VARIABLES=extra.

* Uzun veri 20 satırdır; eşli analiz birimi 10 ID'dir.
SORT CASES BY ID group.
CASESTOVARS
  /ID=ID
  /INDEX=group
  /GROUPBY=VARIABLE.

* CASESTOVARS sonrasında extra.1 ve extra.2 oluşur.
* Fark yönü group2 - group1 olsun diye extra.2 ilk değişkendir.
T-TEST PAIRS=extra.2 WITH extra.1 (PAIRED)
  /CRITERIA=CI(.95)
  /MISSING=ANALYSIS.

* Kontrol: n=10 çift; ortalama fark~1.58; t~4.062; df=9; p~.00283.

* ================================================================.
* 2. TOOTHGROWTH: DOSE=1 İÇİN BAĞIMSIZ T-TESTİ.
* ================================================================.

GET DATA
  /TYPE=TXT
  /FILE='ToothGrowth.csv'
  /ENCODING='UTF8'
  /DELCASE=LINE
  /DELIMITERS=","
  /ARRANGEMENT=DELIMITED
  /FIRSTCASE=2
  /IMPORTCASE=ALL
  /VARIABLES=
    kaynak_satir F3.0
    len F8.2
    supp A2
    dose F3.1.
CACHE.
EXECUTE.
DATASET NAME ToothGrowth WINDOW=FRONT.

FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.

* Tam veri N=60.
FREQUENCIES VARIABLES=supp dose.

* Ana öğretim karşılaştırması: yalnız dose=1.
USE ALL.
COMPUTE filter_dose1=(dose=1).
FILTER BY filter_dose1.
EXECUTE.

* Aktif analiz N=20; OJ=10, VC=10.
FREQUENCIES VARIABLES=supp.
MEANS TABLES=len BY supp
  /CELLS=COUNT MEAN STDDEV.

* SPSS iki satır verir: equal variances assumed / not assumed.
* Bu bölümde Welch (not assumed) satırı ana sonuç olarak okunur.
T-TEST GROUPS=supp('OJ' 'VC')
  /MISSING=ANALYSIS
  /VARIABLES=len
  /CRITERIA=CI(.95).

* Kontrol: OJ ort=22.70; VC ort=16.77; OJ-VC=5.93.
* Welch t~4.033; df~15.358; p~.00104.

* Filtreyi açık bırakmayın.
FILTER OFF.
EXECUTE.

* ================================================================.
* 3. DURUM DENEYİ: AĞIRLIK VE SPLIT FILE.
* ================================================================.

* Birim ağırlık sonuçları değiştirmez; bu yalnız oturum durumunu görünür kılma örneğidir.
COMPUTE birim_agirlik=1.
WEIGHT BY birim_agirlik.
DESCRIPTIVES VARIABLES=len.
WEIGHT OFF.
DELETE VARIABLES birim_agirlik.

* Split File açıkken aynı komut her supp düzeyi için ayrı çalışır.
SORT CASES BY supp.
SPLIT FILE LAYERED BY supp.
DESCRIPTIVES VARIABLES=len.
SPLIT FILE OFF.

* Ağırlık gözlenmemiş yeni bağımsız kişiler yaratmaz.
* Split File yeni bir araştırma tasarımı yaratmaz.

* ================================================================.
* 4. EKSİK EŞ: AYNI 20 SATIR, 9 GEÇERLİ ÇİFT.
* ================================================================.

GET DATA
  /TYPE=TXT
  /FILE='sleep_eksik.csv'
  /ENCODING='UTF8'
  /DELCASE=LINE
  /DELIMITERS=","
  /ARRANGEMENT=DELIMITED
  /FIRSTCASE=2
  /IMPORTCASE=ALL
  /VARIABLES=
    kaynak_satir F3.0
    extra F8.2
    group F1.0
    ID F3.0.
CACHE.
EXECUTE.
DATASET NAME SleepEksik WINDOW=FRONT.

FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.

SORT CASES BY ID group.
CASESTOVARS
  /ID=ID
  /INDEX=group
  /GROUPBY=VARIABLE.

T-TEST PAIRS=extra.2 WITH extra.1 (PAIRED)
  /CRITERIA=CI(.95)
  /MISSING=ANALYSIS.

* Kontrol: 9 geçerli çift; fark~1.60; t~3.684; df=8; p~.00618.

* ================================================================.
* 5. OTURUMU TEMİZ BIRAK.
* ================================================================.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
EXECUTE.
