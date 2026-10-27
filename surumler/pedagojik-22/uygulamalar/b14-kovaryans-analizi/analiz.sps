* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 14: Kovaryans analizi.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b14-kovaryans-analizi/doz_uzunluk.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   len F12.4
   supp A2
   dose F12.4
   oj F8.0
   dose_c F12.4.
EXECUTE.

VALUE LABELS oj 0 'VC' 1 'OJ'.
* dose_c = dose - 1; 1 mg/gün için kovaryat değeri 0'dır.

* M_A: ortak eğimli ANCOVA. Tek OJ-VC farkı, %95 aralık.
UNIANOVA len BY oj WITH dose_c
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /PRINT=PARAMETER DESCRIPTIVE HOMOGENEITY
 /EMMEANS=TABLES(oj) WITH(dose_c=0) COMPARE ADJ(LSD)
 /CRITERIA=ALPHA(.05)
 /DESIGN=oj dose_c.

* M_I: ayrı eğimler. Üç doz tek aile: tekil %98.3333 aralıklar.
* Sig. değerleri ham p'dir; raporda min(3p, 1) kullanılır.
UNIANOVA len BY oj WITH dose_c
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /PRINT=PARAMETER
 /EMMEANS=TABLES(oj) WITH(dose_c=-0.5) COMPARE ADJ(LSD)
 /EMMEANS=TABLES(oj) WITH(dose_c=0) COMPARE ADJ(LSD)
 /EMMEANS=TABLES(oj) WITH(dose_c=1) COMPARE ADJ(LSD)
 /CRITERIA=ALPHA(.0166667)
 /DESIGN=oj dose_c oj*dose_c.

* M_H: hücre modeli (doz kategorik). Aynı aile düzeltmesi.
UNIANOVA len BY oj dose
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /PRINT=DESCRIPTIVE
 /EMMEANS=TABLES(oj*dose) COMPARE(oj) ADJ(LSD)
 /CRITERIA=ALPHA(.0166667)
 /DESIGN=oj dose oj*dose.
