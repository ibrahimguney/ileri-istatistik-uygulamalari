# Bölüm 8 — Çözüm rehberi

Önce görevleri tamamlayın; yuvarlanmamış hedefler beklenen.json içindedir.

## Koşullu ortalama ve model karşılaştırması

G3 tahmini = 5.295723236 + .639696333 G1 + .505431061 age_c.
R²=.581404, düzeltilmiş R²=.566716, ΔR²=.023973; ek yaş testi p=.076076.
Klasik ek değişken F testi yaşın t istatistiğinin karesidir.
G1 kısmi eğimi, G1/G3'ü sabit ve yaşa göre artıklaştırıp iki artık arasındaki
sıfır sabitli eğimi hesaplayarak da elde edilir.

VIF≈1.228577; G1 klasik SH=.074043, HC3 SH=.227043.
Düşük VIF etki duyarlılığını veya bütün varsayımları garanti etmez.
İlk kayıt çıkarılınca yaş katsayısı yaklaşık .505'ten .068'e değişir;
bu, ham kaydı silme gerekçesi değil raporlanacak duyarlılıktır.

## Logit, odds ve olasılık

eta = −22.191778 + 1.652342 G1 − .319966 age_c; p=expit(eta).
G1 OR=5.219187; yaklaşık %95 normal-Wald OR aralığı [2.048683,13.296304].
OR katsayı ve katsayı aralığının uçlarının üstelidir; olasılık oranı değildir.
16 yaş/G1=12 için G3 ortalaması 12.972079, olay olasılığı .085984729;
G1=13 için olasılık .329303733. Olasılık farkı .243319004 (yaklaşık
24.33 yüzde puan); odds oranı 5.219187'dir. Aynı OR farklı başlangıç
olasılıklarında farklı olasılık farkı verir. Merkezleme, 16 yaştaki sabitin
yorumunu belirler; tek başına modelin uyumunu iyileştirmez.

Kaynak 80: yaş=16, G1=12, gözlenen G3=11; sabit modellerle G3 tahmini
12.972079 ve olay olasılığı .085984729. 0.50 eşiğinde tahmin 0, gerçek olay
kodlaması da 0'dır. Tek bir doğru sınıflandırma modelin genel geçerliği değildir.

İlk kaydı çıkarmak OLS yaş eğimini belirgin değiştirirken logit katsayıları
bu örnekte gösterilen altı ondalıkta aynı kalır. OLS kaldıraç/etki sonucunu
lojistik modele otomatik aktarmayın; her modelin duyarlılığı ayrı incelenir.

## Sabit model performansı

| Küme | n / olay | TP | FN | TN | FP | Duyarlılık | Özgüllük | Doğruluk |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Eğitim, c=.50 | 60 / 19 | 14 | 5 | 39 | 2 | .736842 | .951220 | .883333 |
| Aktarım, c=.50 | 20 / 5 | 3 | 2 | 14 | 1 | .600000 | .933333 | .850000 |

Eğitim AUC=.937099, Brier=.089672; aktarım AUC=.760000, Brier=.131860.
AUC ayırt etmeyi, Brier olasılıkların kare hatasını özetler; AUC kalibrasyonu
ölçmez, Brier yalnızca kalibrasyon değildir. AUC'de eşit olasılıklı
pozitif/negatif çiftlere yarım puan verilir.

Herkesi 0 sayma doğruluğu eğitimde 41/60=.683333, aktarımda 15/20=.75;
duyarlılık sıfırdır. Sabit olasılık 19/60 referansının Brier değerleri
.216389 ve .191944'tür. Aktarımda referansı 5/20 olarak yeniden öğrenmeyin.
0.30 eşiğinde eğitim TP/FN/TN/FP=17/2/32/9, aktarım=4/1/9/6;
0.70 bu veride 0.50 ile aynı sınıfları üretir. Bu evrensel bir özellik değildir.

Küçük sıralı aynı-okul aktarımı dış doğrulama değildir. Aktarım sonucuyla
hedef/eşik seçmek bu grubu artık dokunulmamış test olmaktan çıkarır.
14 öğretim amaçlı not hedefi, 0.50 karar eşiğidir; ikisi zorunlu standart değil.
Hedef14'ü yordayıcı yapmak yanıt sızıntısıdır. OLS R² ve McFadden R² aynı
ölçü değildir; yaşın veya notun nedensel etkisini kanıtlamaz.