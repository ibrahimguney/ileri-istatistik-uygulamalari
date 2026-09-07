* B18 — Karşı örnekler. Ana araştırma sonucu olarak raporlanmaz.

SET DECIMAL=DOT.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.

GET DATA /TYPE=TXT
 /FILE='bolumler/b18/uyku_esli.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS="," /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=ID F8.0 kosul1 F16.3 kosul2 F16.3 fark F16.3.
DATASET NAME DurumDeneyi WINDOW=FRONT.

* A) İlk beş ID filtresi.
COMPUTE ilk5=(ID<=5).
FILTER BY ilk5.
T-TEST TESTVAL=0 /VARIABLES=fark /MISSING=ANALYSIS /CRITERIA=CI(.95).
FILTER OFF.
FREQUENCIES VARIABLES=ID.

* B) Keyfi frekans ağırlığı 2: yeni kişi üretmez.
COMPUTE tekrar=2.
WEIGHT BY tekrar.
T-TEST TESTVAL=0 /VARIABLES=fark /MISSING=ANALYSIS /CRITERIA=CI(.95).
WEIGHT OFF.

* C) İki hücreyi yalnız çalışma kopyasında gizle ve farkı yeniden hesapla.
IF (ID=1) kosul2=$SYSMIS.
IF (ID=2) kosul1=$SYSMIS.
COMPUTE fark=kosul2-kosul1.
EXECUTE.
DESCRIPTIVES VARIABLES=kosul1 kosul2 fark /STATISTICS=MEAN STDDEV MIN MAX.
T-TEST PAIRS=kosul2 WITH kosul1 (PAIRED) /MISSING=ANALYSIS /CRITERIA=CI(.95).
T-TEST TESTVAL=0 /VARIABLES=fark /MISSING=ANALYSIS /CRITERIA=CI(.95).

* Sonunda ana çalışma dosyasını yeniden okuyarak kurgusal değişiklikleri bırakın.
