* B09 - SPSS 29 icin OLS kontrol oturumu; gercek SPSS yurutmesi bekliyor.
* SIMULASYON verisi, gercek katilimci yoktur.
* Yeni bir SPSS oturumunda calistirin.
* Asagidaki CD yolunu bilgisayarinizdaki B09 klasoruyle degistirin.
CD 'C:/B09'.

SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='veri.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS="," /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=kayit F8.0 x F20.10 araci F20.10 w F20.10
 ymed F20.10 ymod F20.10.
DATASET NAME B09 WINDOW=FRONT.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
MISSING VALUES kayit x araci w ymed ymod ().
VARIABLE LABELS ymed 'y_aracilik: aracilik yaniti'
 ymod 'y_duzenleyicilik: duzenleyicilik yaniti'.
DESCRIPTIVES VARIABLES=kayit x araci w ymed ymod
 /STATISTICS=MEAN STDDEV MIN MAX.

* Aracilik: a, c-prime ve b, toplam c; standart olmayan B okunur.
REGRESSION /MISSING LISTWISE
 /STATISTICS COEFF OUTS R ANOVA CI(95)
 /DEPENDENT araci /METHOD=ENTER x.
REGRESSION /MISSING LISTWISE
 /STATISTICS COEFF OUTS R ANOVA CI(95)
 /DEPENDENT ymed /METHOD=ENTER x araci.
REGRESSION /MISSING LISTWISE
 /STATISTICS COEFF OUTS R ANOVA CI(95)
 /DEPENDENT ymed /METHOD=ENTER x.

* Duzenleyicilik: tam orneklem ortalamasi ve orneklem standart sapmasi.
AGGREGATE /OUTFILE=* MODE=ADDVARIABLES
 /BREAK=
 /xmean=MEAN(x) /wmean=MEAN(w) /wsd=SD(w).
COMPUTE xc=x-xmean.
COMPUTE wc=w-wmean.
COMPUTE xw=xc*wc.
EXECUTE.
REGRESSION /MISSING LISTWISE
 /STATISTICS COEFF OUTS R ANOVA CI(95)
 /DEPENDENT ymod /METHOD=ENTER xc wc xw.

* W ortalama-1SS: xc katsayisi alt duzeydeki basit egimdir.
COMPUTE wlow=wc+wsd.
COMPUTE xwlow=xc*wlow.
EXECUTE.
REGRESSION /MISSING LISTWISE
 /STATISTICS COEFF OUTS R ANOVA CI(95)
 /DEPENDENT ymod /METHOD=ENTER xc wlow xwlow.

* W ortalama+1SS: xc katsayisi ust duzeydeki basit egimdir.
COMPUTE whigh=wc-wsd.
COMPUTE xwhigh=xc*whigh.
EXECUTE.
REGRESSION /MISSING LISTWISE
 /STATISTICS COEFF OUTS R ANOVA CI(95)
 /DEPENDENT ymod /METHOD=ENTER xc whigh xwhigh.

* Ortalama duzeyindeki basit egim ilk merkezlenmis modeldeki xc katsayisidir.
* Bu dosya bootstrap GA uretmez; bunun icin process-modeller.sps kullanilir.
* Viewer ciktisini tarih ve surumle ayri SPV olarak kaydedin.
