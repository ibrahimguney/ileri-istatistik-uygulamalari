# Bölüm 14 — Kovaryans analizi

## Gerçek veri ve sınırlar

R datasets `ToothGrowth` verisinin Bölüm 6'da arşivlenmiş 60 kaydı kullanılır:
`../b06-parametrik-testler/kaynak/ToothGrowth.csv`.
- len: kaynak uzunluk yanıtı; kısa R sözlüğü ölçüm birimini açık vermediğinden mm vb. eklenmez.
- supp: OJ (portakal suyu) ve VC (askorbik asit) uygulama biçimleri.
- dose: .5, 1, 2 mg/gün; her uygulama biçimi–doz hücresinde 10 hayvan.
- kaynak_satir: arşivdeki sıra; eklenmiş dizin, yeni bir hayvan kimliği değil.

Doz **ön-test değildir**; uygulanan koşulun sayısal düzeyidir. ANCOVA'nın doğrusal
model mantığı öğretilir. Hayvan verisi öğrenci ön-test verisi diye yeniden
etiketlenmez; kısa sözlükte yer almayan rastgeleleştirme/körleme ayrıntıları
uydurulmaz. İnsanlarda klinik kullanım önerilmez. Hiçbir kayıt dışlanmaz.

Kaynak tanımı:
https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html
R kaynak verisi:
https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/ToothGrowth.R

CSV'ye aktarım Bölüm 6'da belgelenmiştir; veri kurulu R `datasets::ToothGrowth`
ile birebir aynıdır. GPL bildirimi aynı kaynak klasöründedir; UCI lisansı bu veriye atfedilmez.
Tek terminal LF ile normalize SHA-256:
`654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3`.
Ham hash ayrıca sonuç JSON'unda tutulur. Kaynak dosyası değiştirilmez.

## Çalıştırma

Kitap kökünden:
```sh
python uygulamalar/b14-kovaryans-analizi/analiz.py
```
Kurulu NumPy/pandas/SciPy/statsmodels/matplotlib kullanılır; kurulum yapılmaz.

## Önceden açıklanan öğretim karşılaştırmaları

Kodlama: G=1 OJ, G=0 VC; x=dose−1. Fark yönü daima OJ−VC.
- Ortak model: `[1,G,x]`, q=3, hata sd 57.
- Ayrı doğrusal eğimler: `[1,G,x,G*x]`, q=4, hata sd 56.
- Hücre modeli: VC(.5,1,2), OJ(.5,1,2) altı gösterge, q=6, hata sd 54.

Doz için referans 1 mg/gündür; gerçek gözlenen destek noktasındadır. Ortak model
hesabı gösterilir ama etkileşim ve doğrusal şekil bulguları nedeniyle esas
koşullu yorum hücre modelindedir. Hücre modeli sayısal kovaryat ANCOVA'sı değil,
doza kategorik yaklaşan karşılaştırma modelidir. Daha fazla doz aralığına şekil
veya 3 mg/güne dışa kestirim yapılmaz.

İç içe F testleri **ikişer modelle**, ilgili serbest modelin SSE/sd paydasıyla
hesaplanır. Üç modeli tek `anova` çağrısına vermek en büyük model MSE'sini bütün
satırlara taşıyabilir; aynı test değildir. Ortak model grup testi (1,57),
etkileşim testi (1,56), ayrı doğruların biçim testi (2,54) sd kullanır.

Tekil düzeltilmiş ortalama aralıkları %95 OLS t aralıklarıdır; bireysel tahmin
aralığı değildir. Ortak modelde grup farkı sabittir, bu tek kontrast üç farklı
dozda gösterilse de aile büyüklüğü 1'dir. Ayrı eğim ve hücre modellerinde üç
dozdaki farklar her model için bir aile kabul edilir: p_adj=min(3p,1), kritik
t=t_(1−.05/6,df). Aralıklar Bonferroni ailesel %95 aralıklardır. Modeller arası
arama için ayrıca düzeltme yapıldığı iddia edilmez; tablolar yöntem duyarlılığıdır.

HC3 katsayı kovaryansı ayrıca hesaplanır; t referansı artık sd'sidir. Bu küçük
örneklemde yaklaşık sağlam duyarlılıktır; kesin heterojen-varyans testi veya
bootstrap değildir. HC3 yanlış ortalama biçimini ve bağımlı kayıtları düzeltmez.
Kısmi eta kare ilgili ek-SS/(ek-SS+SSE_full) oranıdır; güven aralığı hesaplanmaz.

## Hesaplanan ana bulgular

Ortak model: VC 1 mg/gün ortalaması 15.336071, OJ 19.036071; fark 3.7,
%95 GA [1.510095,5.889905]. Grup F(1,57)=11.446768,p=.001301,eta_p²=.167236.
Her iki grupta doz ortalaması 7/6 olduğundan ham fark 3.7 düzeltmeyle değişmez.

Ayrı model: intercept 15.010714, grup 4.350714, VC eğimi 11.715714,
eğim farkı −3.904286. Ortak eğime karşı F(1,56)=5.333483,p=.024631.
Hücre modeline göre doğrusal biçim F(2,54)=8.399425,p=.000667.

Hücre OJ−VC farkları 5.25,5.93,−.08; üçlü Bonferroni aralıkları
[1.237302,9.262698], [1.917302,9.942698], [−4.092698,3.932698].
Düzeltilmiş p değerleri .006277,.001769,1.000000. Son doz eşdeğerlik kanıtı değildir.
HC3 aralıkları [.936186,9.563814],[2.100200,9.759800],[−4.596207,4.436207].
Altı hücrede medyan merkezli Levene p=.148361; varsayım onayı sayılmaz.
Tek-kayıt dışlama koşulları güven aralığı değildir, ana kayıtlar korunur.

## Dosyalar ve denetimler

- `doz_uzunluk.csv`: 60 kayıt + oj ve dose_c kodları.
- `sonuclar/ozet.json`: bütün model, test, aralık, kaynak ve sürüm bilgileri.
- `sonuclar/hucre_ozetleri.csv`: n, ortalama, sd, en küçük/en büyük yanıtlar.
- `sonuclar/duzeltilmis_ortalamalar.csv`: model/doz/grup için tekil %95 OLS ortalama aralıkları.
- `sonuclar/karsilastirmalar.csv`: model/doz/kovaryans türüne göre tüm kontrastlar.
- `sonuclar/*covariance.csv`, `*HC3.csv`: katsayı kovaryans matrisleri.
- `sonuclar/tanilar.csv`: ayrı-eğim tahmin/artık/kaldıraç/Cook tablosu.
- `sonuclar/birini_disarida.csv`: 60 ayrı tek-kayıt dışlama koşusu.
- `../../assets_figures/b17-egimler-karsilastirmalar.pdf`: şekil. Nokta kaydırma
  yalnız görünürlük içindir; modelde orijinal dozlar kullanılır.

İç kontroller: statsmodels–NumPy katsayıları, manuel OLS/HC3 kovaryansları,
Geçersiz model/grup/eksik doz ve hücre modelinde destek dışı doz reddi,
satır sırası değişince aynı katsayı/SSE, F=t², SSE farkları ve compare_f_test, doğrudan hücre ortalamaları/saf hata,
merkezleme altında aynı tahminler ve kontrast SH'leri. Bunlar R/SPSS çalıştırılmış
sayılmaz. Normal hata biçimi ve model seçimi belirsizliği kontrollerle yok olmaz.

## R ve SPSS

`analiz.R` kurulu emmeans gerektirir, paket kurmaz. `by=NULL` ile üç doz kontrastı
tek Bonferroni ailesinde birleştirilir. HC3 temel R matrisleriyle hesaplanır.
R betiği Python ile aynı katsayıları, düzeltilmiş ortalamaları ve kontrastları verir.

`analiz.sps` kitap kökünden çalıştırılır; önce Python ile üretilen CSV'yi açar.
SPSS çalışma dizini kitap kökü olmalıdır; betik mutlak yol veya paket kurulumu içermez.
CSV sütun sırası `kaynak_satir,len,supp,dose,oj,dose_c` olarak tanımlanır;
`oj=0` VC, `oj=1` OJ'dir. Betik mevcut filtre/ağırlık/bölünmüş dosya durumunu kapatır;
açık verilerle çalışıyorsanız ayrı bir oturumda kullanın. EMMEANS tablosunda
I=1 (OJ), J=0 (VC) satırını okuyun; ters satır aynı karşılaştırmanın ters yönüdür.
Sonraki satırdaki `TITLE` metinleri öğretim etiketleridir, çalıştırma kanıtı değildir.
Ortak modelde tek %95 fark aralığı; diğer iki modelde alfa .05/3 ile tekil
%98.3333 aralıklar istenir. Bu üç aralığın ailesel kapsamı en az %95 hedefler;
SPSS'teki ham p değerlerini 3 ile çarpıp 1'de sınırlayın. Ortalamalar da bu
çağrılarda %98.3333 aralıkla gelir; kitaptaki tekil %95 ortalama aralıklarıyla
karıştırmayın. `ADJ(LSD)` ham kontrastı bırakır; aile düzeltmesi alfa ve raporlama
üzerinden açıkça uygulanır. Her dozda ayrı iki-grup Bonferroni seçimi dozlar
arası aileyi otomatik kontrol etmez. SPSS farklı referans kodlayabilir; OJ−VC
farkını seçin, parametre tablosunun tek bir işaretini körlemesine eşitlemeyin.

SPSS HOMOGENEITY çıktısının merkezleme sürümünü kontrol edin: Python'da hesaplanan
medyan merkezli altı-hücre Levene ile otomatik eşitlik varsaymayın. Kısmi eta kare
satırlarının hangi model/hipoteze ait olduğunu kaydedin. Gözlenen güç kullanılmaz.

## Yöntem belgeleri (6 Eylül 2026)

- https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html
- https://rvlenth.github.io/emmeans/articles/interactions.html
- https://rvlenth.github.io/emmeans/articles/confidence-intervals.html
- https://www.ibm.com/docs/en/SSLVMB_31.0.0/pdf/IBM_SPSS_Statistics_Command_Syntax_Reference.pdf
## Teslim kontrolü

1. `doz_uzunluk.csv` 60 kayıt ve altı hücrede 10'ar gözlem içermeli.
2. Model hata sd'leri ortak/ayrı/hücre için 57/56/54 olmalı.
3. `duzeltilmis_ortalamalar.csv` tekil ortalamaları; `karsilastirmalar.csv` farkları içerir.
   İki ortalama aralığının örtüşmesi fark testi yerine kullanılmaz.
4. Ayrı/hücre farklarında aile büyüklüğü 3; ortak modelde 1'dir.
5. SPSS MI/MH tablolarındaki `Sig.` ham p'dir; min(3p,1) ayrıca raporlanır.
   ALPHA(.05/3) aralıkları düzeltir; p değerini otomatik üçle çarpmaz.
6. SPSS model tablolarındaki SSE ve hata sd ile doğrusal biçim F testi ayrıca hesaplanır;
   MH tablosundaki grup×doz testi bu iki-sd şekil testiyle aynı değildir.
7. Python tekrar koşularında JSON/CSV ve şekil byte düzeyinde karşılaştırılabilir.
   R/SPSS ve uzak kaynak karşılaştırması çalıştırılmış sayılmaz.