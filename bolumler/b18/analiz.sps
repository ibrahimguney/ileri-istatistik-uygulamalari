* B18 — Ana IBM SPSS oturumu.
* Bu dosyanın bulunması yürütme kanıtı değildir.

SET DECIMAL=DOT.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.

* 1) Eşli uyku çalışma dosyasını içe aktar.
GET DATA /TYPE=TXT
 /FILE='bolumler/b18/uyku_esli.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS="," /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=ID F8.0 kosul1 F16.3 kosul2 F16.3 fark F16.3.
DATASET NAME UykuEsli WINDOW=FRONT.
MISSING VALUES ID kosul1 kosul2 fark ().
FORMATS kosul1 kosul2 fark (F10.3).
FREQUENCIES VARIABLES=ID.
DESCRIPTIVES VARIABLES=kosul1 kosul2 fark /STATISTICS=MEAN STDDEV MIN MAX.

* Paired Samples Statistics / Correlations / Test.
T-TEST PAIRS=kosul2 WITH kosul1 (PAIRED)
 /MISSING=ANALYSIS /CRITERIA=CI(.95).

* Aynı fark hipotezinin kontrol çağrısı; yeni araştırma sonucu değildir.
T-TEST TESTVAL=0 /VARIABLES=fark
 /MISSING=ANALYSIS /CRITERIA=CI(.95).

* 2) ToothGrowth çalışma dosyasını içe aktar.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
GET DATA /TYPE=TXT
 /FILE='bolumler/b18/dis_veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS="," /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=kaynak_satir F8.0 len F16.3 supp A2 dose F8.1 supp_kod F8.0.
DATASET NAME DisVeri WINDOW=FRONT.
MISSING VALUES kaynak_satir len dose supp_kod ().

* Ana öğretim karşılaştırması: yalnız 1 mg/gün.
COMPUTE doz1=(dose=1).
FILTER BY doz1.
T-TEST GROUPS=supp_kod(1 2) /VARIABLES=len
 /MISSING=ANALYSIS /CRITERIA=CI(.95).

* Filtreyi kapat ve bütün 60 kaydın geri döndüğünü kontrol et.
FILTER OFF.
FREQUENCIES VARIABLES=dose.

* Gerçek SPSS yürütmesinde Viewer/SPV çıktısını sürümlü adla ayrıca kaydedin.
