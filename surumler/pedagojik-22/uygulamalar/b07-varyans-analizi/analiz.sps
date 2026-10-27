* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 7: Varyans analizi.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b07-varyans-analizi/analiz_veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   len F12.4
   supp A2
   dose F12.4
   supp_kod F8.0
   dose_kod F8.0.
EXECUTE.

VALUE LABELS supp_kod 1 'OJ' 2 'VC' /dose_kod 1 '0.5' 2 '1' 3 '2'.

* Tek yönlü ANOVA: her uygulama biçimi ayrı bir öğretim ailesidir.
SORT CASES BY supp_kod.
SPLIT FILE SEPARATE BY supp_kod.
ONEWAY len BY dose_kod
 /STATISTICS=DESCRIPTIVES HOMOGENEITY WELCH
 /MISSING=ANALYSIS
 /POSTHOC=TUKEY GH ALPHA(0.05).
SPLIT FILE OFF.

* İki faktörlü ANOVA (Tip III KT; dengeli desende Tip I ile aynı).
UNIANOVA len BY supp_kod dose_kod
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /PRINT=DESCRIPTIVE ETASQ HOMOGENEITY
 /EMMEANS=TABLES(supp_kod*dose_kod) COMPARE(supp_kod) ADJ(LSD)
 /CRITERIA=ALPHA(.05)
 /DESIGN=supp_kod dose_kod supp_kod*dose_kod.

* Not: EMMEANS karşılaştırmaları her doz içinde ayrı düzeltilir.
* Üç dozu tek aile saymak için ham p değerleri 3 ile çarpılır (en çok 1).
