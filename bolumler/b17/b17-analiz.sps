* B17 - ANCOVA: SPSS 29 icin calistirma dosyasi.
* SPSS gercek yurutmesi henuz dogrulanmadi.
* Veri: R datasets::ToothGrowth; depodaki ToothGrowth.csv ile ayni 60 kayit.
* Kaynak ve lisans: ayni bolumde VERI.md ve GPL-2.txt dosyalarina bakiniz.
* https://github.com/ibrahimguney/ileri-istatistik-uygulamalari/tree/main/bolumler/b17 .
* Veri bu dosyaya dahil; CSV yolu veya PROCESS gerekmez.
* Ilk calistirmadan once acik calismanizi kaydedin; B17 adli ayri veri kumesi kullanilir.

SET DECIMAL=DOT.
DATASET DECLARE B17 WINDOW=FRONT.
DATASET ACTIVATE B17.
DATA LIST FREE /kaynak_satir (F8.0) len (F8.1) supp (A2) dose (F8.1).
BEGIN DATA
1 4.2 VC 0.5
2 11.5 VC 0.5
3 7.3 VC 0.5
4 5.8 VC 0.5
5 6.4 VC 0.5
6 10.0 VC 0.5
7 11.2 VC 0.5
8 11.2 VC 0.5
9 5.2 VC 0.5
10 7.0 VC 0.5
11 16.5 VC 1.0
12 16.5 VC 1.0
13 15.2 VC 1.0
14 17.3 VC 1.0
15 22.5 VC 1.0
16 17.3 VC 1.0
17 13.6 VC 1.0
18 14.5 VC 1.0
19 18.8 VC 1.0
20 15.5 VC 1.0
21 23.6 VC 2.0
22 18.5 VC 2.0
23 33.9 VC 2.0
24 25.5 VC 2.0
25 26.4 VC 2.0
26 32.5 VC 2.0
27 26.7 VC 2.0
28 21.5 VC 2.0
29 23.3 VC 2.0
30 29.5 VC 2.0
31 15.2 OJ 0.5
32 21.5 OJ 0.5
33 17.6 OJ 0.5
34 9.7 OJ 0.5
35 14.5 OJ 0.5
36 10.0 OJ 0.5
37 8.2 OJ 0.5
38 9.4 OJ 0.5
39 16.5 OJ 0.5
40 9.7 OJ 0.5
41 19.7 OJ 1.0
42 23.3 OJ 1.0
43 23.6 OJ 1.0
44 26.4 OJ 1.0
45 20.0 OJ 1.0
46 25.2 OJ 1.0
47 25.8 OJ 1.0
48 21.2 OJ 1.0
49 14.5 OJ 1.0
50 27.3 OJ 1.0
51 25.5 OJ 2.0
52 26.4 OJ 2.0
53 22.4 OJ 2.0
54 24.5 OJ 2.0
55 24.8 OJ 2.0
56 30.9 OJ 2.0
57 26.4 OJ 2.0
58 27.3 OJ 2.0
59 29.4 OJ 2.0
60 23.0 OJ 2.0
END DATA.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
MISSING VALUES kaynak_satir len dose ().
COMPUTE oj=(supp='OJ').
COMPUTE dose_c=dose-1.
COMPUTE oj_dose=oj*dose_c.
COMPUTE dose_q=dose_c**2.
COMPUTE oj_q=oj*dose_q.
VARIABLE LABELS oj 'Grup: 0=VC, 1=OJ' dose_c 'Doz eksi 1 mg/gun'.
VALUE LABELS oj 0 'VC' 1 'OJ'.
EXECUTE.

* 1 - Veri kontrolu: 60 kayit; her supp x dose hucresinde 10.
FREQUENCIES VARIABLES=supp dose.
CROSSTABS /TABLES=supp BY dose /CELLS=COUNT.
DESCRIPTIVES VARIABLES=len dose /STATISTICS=MEAN STDDEV MIN MAX.
MEANS TABLES=len BY supp BY dose /CELLS=COUNT MEAN STDDEV.

* 2 - Ortak egim ANCOVA: grup testi ve 1 mg/gun duzeltilmis ortalamalar.
* Pairwise Comparisons tablosunda I=OJ, J=VC satirini okuyun.
UNIANOVA len BY oj WITH dose_c
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /PRINT=ETASQ
 /EMMEANS=TABLES(oj) WITH(dose_c=0) COMPARE(oj) ADJ(LSD)
 /CRITERIA=ALPHA(.05)
 /DESIGN=oj dose_c.

* 3 - Ic ice modeller: Method ENTER bloklari, adimsal secim degildir.
* Model 1 ortak egim; Model 2 ayri egimler.
* Model 3: uc dozda hucre modeliyle ayni tahminleri veren hesaplama modeli.
* dose_q/oj_q sadece 2 sd dogrusal bicim testini hesaplamak icindir.
* Bu, gozlenmeyen dozlara ikinci derece egriyle genelleme talimati degildir.
* Model Summary: model 2 F Change=5.333483; model 3 F Change=8.399425.
REGRESSION /MISSING LISTWISE
 /STATISTICS=COEFF R ANOVA CHANGE CI(95)
 /DEPENDENT=len
 /METHOD=ENTER oj dose_c
 /METHOD=ENTER oj_dose
 /METHOD=ENTER dose_q oj_q.

* 4 - Ayri egim modelinde ortalama tahminleri: tekil yuzde 95 araliklar.
UNIANOVA len BY oj WITH dose_c
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /EMMEANS=TABLES(oj) WITH(dose_c=-.5)
 /EMMEANS=TABLES(oj) WITH(dose_c=0)
 /EMMEANS=TABLES(oj) WITH(dose_c=1)
 /CRITERIA=ALPHA(.05)
 /DESIGN=oj dose_c oj*dose_c.

* 5 - Ayri egim: uc dozdaki OJ-VC farklari tek ailedir.
* Aralik duzeyi 98.333333; uc fark icin en az yuzde 95 aile kapsami.
* Pairwise Comparisons Sig. ham p'dir; raporda min(3*p,1) uygulanir.
* Bu cagrinin ortalama araliklari da 98.333333'tur; bolum 4 ile karistirmayin.
UNIANOVA len BY oj WITH dose_c
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /EMMEANS=TABLES(oj) WITH(dose_c=-.5) COMPARE(oj) ADJ(LSD)
 /EMMEANS=TABLES(oj) WITH(dose_c=0) COMPARE(oj) ADJ(LSD)
 /EMMEANS=TABLES(oj) WITH(dose_c=1) COMPARE(oj) ADJ(LSD)
 /CRITERIA=ALPHA(.0166666666667)
 /DESIGN=oj dose_c oj*dose_c.

* 6 - Alti hucre modeli: dose artik kategorik faktordur.
* Ortalama tahminlerinin tekil yuzde 95 araliklari.
UNIANOVA len BY oj dose
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /PRINT=DESCRIPTIVE
 /EMMEANS=TABLES(oj*dose)
 /CRITERIA=ALPHA(.05)
 /DESIGN=oj dose oj*dose.

* 7 - Hucre modeli: uc dozda OJ-VC farklari, aile araliklari.
* I=OJ, J=VC yonunu secin. Sig. ham p; duzeltilmis p=min(3*p,1).
* Tekil araliklar 98.333333; uc fark icin en az yuzde 95 aile kapsami.
UNIANOVA len BY oj dose
 /METHOD=SSTYPE(3)
 /INTERCEPT=INCLUDE
 /EMMEANS=TABLES(oj*dose) COMPARE(oj) ADJ(LSD)
 /CRITERIA=ALPHA(.0166666666667)
 /DESIGN=oj dose oj*dose.

* Ciktilari B17_SPSS_YYYY-AA-GG.spv olarak ayri kaydedin.
* HC3, medyan merkezli Levene ve 60 dislama bu dosyada hesaplanmaz.
* Bunlar icin mevcut Python/R analizleri ve bolum kontrol listesi gecerlidir.


