# Veri ve yöntem kaydı

## Kaynak

R `datasets::ToothGrowth`: 60 kobayda odontoblast uzunluğu, iki uygulama biçimi
ve üç doz. Her uygulama×doz hücresinde 10 ayrı kayıt vardır; tekrarlı ölçüm
varsayılmaz. Kaynak sözlüğü Bliss (1952), *The Statistics of Bioassay* ve
ilişkili Crampton (1947) çalışmasına yönlendirir. Kısa sözlük `len` için
fiziksel birimi belirtmediğinden burada kaynak ölçüm birimi kullanılır.

- R sözlüğü: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html
- Arşiv aktarım kaynağı: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/ToothGrowth.R
- Kitap arşivi: `03-AdvancedStaticalAppTR/uygulamalar/b10-parametrik-testler/kaynak/ToothGrowth.csv`

5 Eylül 2026'da tarayıcıdan yapılan aktarımın yerel kopyası aynen korunmuştur.
Bu pakette yeni gözlem, eksik değer tamamlama veya uzak kaynakla otomatik hücre
karşılaştırması yoktur. Özgün makalenin ham kayıtları, kafes, rastgele atama ve
körleme denetlenmemiştir. Kaynak sıra numarası yeni hayvan kimliği değildir.

CRLF→LF ve tek son LF normalizasyonuyla SHA-256:
`654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3`.
Ham dosya hash'i çalıştırmada `sonuclar/ozet.json` içine yazılır.
Kaynak CSV'nin kitap kopyasıyla bayt eşitliği ayrıca denetlenir.
Bölüm 10 arşivindeki `GPL-2.txt` bildirimi korunmuştur; bu veri için yeni
CC BY/UCI lisansı atanmaz. Kaynak bildirimleri yeniden dağıtımda saklanmalıdır.

## Analiz kararları

Yanıt `len`; grup `supp`; sayısal kovaryat `dose` (mg/gün).
Doz işlem öncesi ölçüm değildir. OJ=1, VC=0 ve x=dose−1 kullanılır.
Bütün modellerde aynı 60 kayıt vardır. Hücre modeli yalnız .5, 1 ve 2 dozlarında
tanımlıdır; ayrı eğrilerin biçim sınamasında karşılaştırma modelidir.
Ortalamaların aralıkları bireysel hayvan tahmin aralığı değildir.
HC3 modeli yeniden seçmez ve bağımlılığı düzeltmez.

## Yöntem belgeleri

6 Eylül 2026'da aşağıdaki resmi belgeler incelendi; bu, R çalıştırması değildir.
- https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html
- https://rvlenth.github.io/emmeans/articles/confidence-intervals.html

R'de `by=NULL` üç doz kontrastını tek ailede toplar; model çiftleri ayrı ayrı
karşılaştırılır. Paket sürümleri çalışma sırasında ayrıca kaydedilir.