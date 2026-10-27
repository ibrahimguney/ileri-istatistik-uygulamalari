# Bölüm 7 — ToothGrowth ile tek yönlü ve faktöriyel ANOVA

## Kaynak ve kapsam
Yeni veya sentetik gözlem eklenmez. Bölüm 6'nın ortak kaynağı okunur:
`../b06-parametrik-testler/kaynak/ToothGrowth.csv`.
Kaynak, aktarım ve lisans açıklamaları o paketin README.md ve kaynak/GPL-2.txt
dosyalarındadır; ikinci bir veri kopyası oluşturulmaz.

R sözlüğü: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html
R kaynak metni: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/ToothGrowth.R
R belgesinde kaynak: Bliss (1952), The Statistics of Bioassay; ilişkili çalışma:
Crampton (1947), The Journal of Nutrition 33(5), 491–504,
DOI 10.1093/jn/33.5.491. Kaynak sözlüğü 5 Eylül 2026'da tekrar incelendi.
Veri, kurulu R `datasets::ToothGrowth` ile birebir aynıdır. Özgün makalenin ham
kayıtları bu paketin kapsamı dışındadır.

60 ayrı hayvan, OJ/VC × 0.5/1/2 mg/gün, her hücrede 10 kayıt vardır.
len odontoblast uzunluğudur; kısa kaynakta birim belirtilmediğinden mikrometre
varsayılmaz. supp: OJ portakal suyu, VC askorbik asit; dose mg/gündür.
Doz burada üç düzeyli faktördür, tek doğrusal eğim değildir. Tekrarlı ölçüm yoktur.
Kafes, randomizasyon ve ortak çevre yapısı kısa dosyada doğrulanmadığından
bağımsızlık varsayımı ayrıca tartışılır. İnsanlara veya tedaviye genellenmez.

CSV sonundaki satır sonu uygulama tarafından kaldırılmış olabilir. Betik yalnız
son LF karakterlerini tek LF olarak normalize edip eski veri kopyasının hash'iyle
karşılaştırır; kaynak baytlarını değiştirmez. Hücre veya sayı değişikliği kabul edilmez.
Normalize SHA-256: 654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3.
Gerçekte okunan baytların hash'i JSON'da ayrıca kaydedilir.

## Önceden tanımlanmış öğretim analizleri
- OJ, 30 kayıt: üç doz için klasik ANOVA + üç çiftin Tukey ailesi.
- Aynı OJ kayıtları: Welch + Games–Howell alternatif varyans modeli; yöntemler
  Levene sonucuna göre otomatik değiştirilmez. İkisi aynı verinin alternatifidir.
- VC, 30 kayıt: öğrencinin bağımsız çözeceği aynı analizler.
- Bütün 60 kayıt: iki sabit faktör, uygulama × doz etkileşimli OLS modeli.
- Üç dozun OJ−VC basit etkileri: tüm modelin ortak MSE'si ve 54 sd ile,
  tek üç-karşılaştırmalı ailede Bonferroni p ve en az %95 eşzamanlı aralıklar.
  Bunlar Bölüm 6'daki ayrı Welch testlerinin aralıkları değildir.
- Etkileşim için HC3 kovaryanslı iki kısıtlı Wald F duyarlılığı, yaklaşık F(2,54).
  Bu, klasik SS oranı değildir; yeni bir robust kareler toplamı gibi sunulmaz.

Tukey ve Games–Howell için aynı üç çift ailesi tanımlıdır; Games–Howell'in aile
kontrolü yaklaşık ve varsayımlara bağlıdır. OJ, VC ve üç basit etki ailesi ayrı
öğretim sorularıdır. Bütün bölümde yapılan testlerin toplam hata oranını .05'te
kontrol ettiğimiz iddia edilmez. Bu bir yeni deneyin önkaydı değildir.

## Hesaplar ve doğrulamalar
SSG+SSW=SST; klasik F elle/SciPy; Welch elle/SciPy/Statsmodels ile doğrulanır.
Tukey ve Games–Howell için öğrencilendirilmiş açıklık q, farklar, aralıklar ve
p değerleri elle/SciPy ile karşılaştırılır; Tukey ayrıca Statsmodels ile denetlenir.
Faktöriyel kareler toplamları hücre ortalamalarından ayrıca hesaplanır. Dengeli ve
tam 2×3 tasarımda Sum kodlamalı Tip II/III sonuçları karşılaştırılır; bu eşitlik
boş hücrelere veya dengesiz tasarımlara genellenmez. HC3 matris hesabı ve ortak
etkileşim karşıtlığı iki ayrı yoldan doğrulanır. Satır sırasının sonuçları
etkilemediği ve kaynak baytlarının değişmediği denetlenir.

Eta-kare OJ tek yönlü modelinin SSG/SST oranıdır. Omega-kare aynı klasik modele
ait düzeltmeli tahmindir. Faktöriyel tabloda kısmi eta-kare SS_etki/(SS_etki+SSE)
kullanılır; üç kısmi eta-kare toplanmaz. Etki büyüklükleri için GA üretilmez.

## Çalıştırma
Kitap kökünden:
```sh
python uygulamalar/b07-varyans-analizi/analiz.py
Rscript uygulamalar/b07-varyans-analizi/analiz.R
```
Python için numpy, pandas, scipy, statsmodels ve matplotlib gerekir. Bu ortamda
SciPy 1.17.0 / Statsmodels 0.14.6 kullanıldı. Daha eski SciPy'de tukey_hsd'nin
equal_var=False seçeneği bulunmayabilir; sürümler sonuç dosyasına yazılır.
R betiği base R ile çalışacak biçimde yazıldı; Games–Howell ayrıca formülle hesaplanır.
R betiği Python ile aynı sonuçları verir. SPSS temel ANOVA, Tukey/GH ve hücre
ortalamalarını üretir; üç dozu tek aile olarak düzelten basit etki aralıkları ve
HC3 ortak testi için Python kullanılır. R betiği Bonferroni ailesini hesaplar,
HC3 kontrolünü içermez. SPSS EMMEANS içindeki tek tek düzeltmelerin üç dozun
tamamını kapsadığını varsaymayın.

## Çıktılar
- analiz_veri.csv: kaynak sütunları + supp_kod (OJ=1, VC=2), dose_kod (0.5=1, 1=2, 2=3).
- sonuclar/ozet.json: bütün testler, aralıklar, kaynak ve sürümler.
- sonuclar/hucreler.csv, faktoriyel_anova.csv, basit_etkiler.csv, ikili_OJ.csv, ikili_VC.csv.
- assets_figures/b11-oj-tukey.pdf, b11-etkilesim.pdf, b11-tanilar.pdf.

Ana kontrol sonuçları: OJ F(2,27)=31.441504, eta²=.699610, omega²=.669905;
Welch F(2,17.069264)=29.404475. OJ'de 2−1 Tukey p=.130926, GA[-.800395,7.520395].
Tam model etkileşim F(2,54)=4.106991, p=.021860, kısmi eta²=.132028;
HC3 F(2,54)=3.522846, p=.036471. Basit etkiler 5.25,5.93,−.08;
üçlü Bonferroni p değerleri .006277,.001769,1.000000.
## Revizyon 25

[Yeni geliştirme](dengesiz-hedef/README.md). Ana veri ve sayısal referanslar korunur; yeni ek yalnız Python ile denetlendi.
