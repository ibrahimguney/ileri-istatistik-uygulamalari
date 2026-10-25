# Bölüm 13 — Çoklu ve lojistik regresyon

## Kaynak ve aktarım
Cortez, P. (2008). Student Performance [Veri seti]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T. CC BY 4.0.
Özgün araştırma: Cortez, P., & Silva, A. (2008). Using data mining to predict
secondary school student performance. FUBUTEC 2008, EUROSIS.

- Veri sayfası: https://archive.ics.uci.edu/dataset/320/student+performance
- Resmî CSV: https://archive.ics.uci.edu/static/public/320/data.csv
- Lisans: https://creativecommons.org/licenses/by/4.0/
- Aktarım tarihi: 5 Eylül 2026.

Resmî CSV'nin 1–80. veri satırlarından school, age, G1 ve G3 sütunları
kaynak dosyasına aktarıldı.
Bu dosya 649 satırlı Portekizce dersi verisinin tamamı değil, bir sütun/satır
alıntısıdır. Kaynak satır numarası tarafımızdan eklendi; öğrenci kimliği değildir.
Yaşlar uydurulmadı; G1/G3 ve okul değerlerinin Bölüm 12 dosyasıyla eşleşmesi
betikte ayrıca denetlenir. Bölüm 11–12 kaynak dosyaları değiştirilmez.

İlk aktarım SHA-256 (sonunda LF dahil):
`3ad427ac4ce8da8f4fc8d12fcb271d6f0a2699a0e086dc18d9ae4400636462b5`.
Güncel ham dosya hash'i her çalıştırmada JSON'a kaydedilir. Bu hash, özgün
kaynakla otomatik karşılaştırmanın yerine geçmez. Varsayılan çevrimdışı koşuda
`official_csv_automatically_verified=false` yazılır.

## Sözlük ve önceden belirlenen analiz
| Sütun | Anlam |
|---|---|
| school | Seçili kayıtların tümünde GP; modele alınmaz |
| age | Kaynakta kayıtlı yaş, yıl; seçili 80 kayıtta 15–18 |
| G1 | Birinci dönem notu, 0–20 |
| G3 | Yıl sonu (üçüncü dönem) notu, 0–20 |
| age_c | age - 16; yaşın merkezlenmiş hali |
| hedef14 | G3 >= 14 için 1, diğerlerinde 0 |

İlk 60 kayıt model kurma, sonraki 20 kayıt sabit modeli uygulama etkinliğidir.
Bu ayrım kaynak sırasına dayanır; rastgele örneklem veya bağımsız dış doğrulama
değildir. Her iki grup GP okulundandır. G1=0 dahil hiçbir kayıt silinmez.

Doğrusal model: G3 ~ G1 + age_c. Lojistik model: hedef14 ~ G1 + age_c.
14, bu bölümün öğretim amaçlı not hedefidir; resmî geçme sınırı değildir.
60 kayıtta 19, sonraki 20 kayıtta 5 olay vardır. İkili kodlama ham not bilgisini
azaltır. Bu nedenle sürekli sonuç analizi korunur ve iki model aynı soruyu
cevaplıyormuş gibi karşılaştırılmaz. Olay tanımı 14 ile olasılık karar eşikleri
0.3/0.5/0.7 birbirinden farklıdır. Eşikler aktarım sonuçlarına göre seçilmez.

G2 veya G3'ten türetilen bir yordayıcı kullanılmaz. G3 sadece yanıt/olay tanımıdır.
Bununla birlikte age kaydının zamanı ve gerçek kullanım anında erişilebilirliği
ayrıca doğrulanmadığından uygulama doğrulanmış bir erken uyarı sistemi değildir.
Buradaki sonuçlar kitap için yeniden hesaplanmıştır; özgün makalenin bulguları değildir.

## Çalıştırma
Kitap kök dizininden:

```sh
python uygulamalar/b13-coklu-lojistik/analiz.py
Rscript uygulamalar/b13-coklu-lojistik/analiz.R
```

Ağ erişimi varsa kaynak karşılaştırması:

```sh
python uygulamalar/b13-coklu-lojistik/analiz.py --kaynak-dogrula
```

R temel paketleri kullanır ve Python ile aynı katsayıları verir.
SPSS betiği ilk 60 kaydı kullanarak iki modeli kurar; HC3 ve sonraki 20 kaydı
puanlama adımları Python/R paketindedir. SPSS çıktısında modellenen olayın 1
olduğunu kontrol edin. R'de üstel aralıklar profil olabilirlik değil, Python
ve SPSS ile karşılaştırılabilir normal yaklaşımına dayalı Wald aralıklarıdır.

## Çıktılar ve kontroller
- veri.csv: 80 gözlem ve açıkça türetilmiş age_c/hedef14 sütunları.
- sonuclar/ozet.json: katsayılar, klasik/HC3 aralıklar, Wald OR aralıkları,
  VIF, değişim F testi, model karşılaştırmaları, eşik tabloları, sürümler.
- sonuclar/tani.csv: ilk 60 kayıt için artık, kaldıraç, Cook ve olasılık.
- sonuclar/aktarim.csv: 61–80. kayıtlara ilk 60'ın sabit modellerinden tahminler.
- sonuclar/profiller.csv: örnek G1/yaş profilleri için ortalama ve olasılık.
- assets_figures/b08-uci-modeller.pdf ve b08-uci-tani.pdf: kitap kökündeki şekiller.

OLS katsayıları NumPy en küçük kareleriyle; kısmi G1 eğimi FWL artıklaştırmasıyla;
HC3 kovaryansı elle matris formülüyle; tek ek değişkenin F testi t² eşitliğiyle
kontrol edilir. Logit katsayıları Binomial GLM ve SciPy bağımsız olabilirlik
optimizasyonuyla, standart hataları bilgi matrisinin tersiyle denetlenir.
AUC hem pozitif/negatif çift karşılaştırması hem ortalama sıralarla hesaplanır.
Kaynak dosyasının değişmeden kaldığı ayrıca doğrulanır.

## Sayısal kontrol noktaları
- OLS: G3_hat = 5.295723 + 0.639696 G1 + 0.505431 age_c.
- R²=0.581404, düzeltilmiş R²=0.566716, ΔR²=0.023973; ek yaş testi p=0.076076.
- G1 klasik SE=0.074043; HC3 SE=0.227043; VIF=1.228577.
- Logit: eta = -22.191778 + 1.652342 G1 - 0.319966 age_c.
- G1 OR=5.219187; yaklaşık %95 Wald GA=[2.048683, 13.296304].
- Eğitim, eşik0.5: TP14 FN5 TN39 FP2; AUC0.937099, Brier0.089672.
- Aktarım, eşik0.5: TP3 FN2 TN14 FP1; AUC0.760000, Brier0.131860.

Eğitim performansı iyimser olabilir. Sonraki 20 kayıtta yalnız 5 olay vardır;
sonuçlar bir kullanım onayı veya doğrulanmış genellenebilirlik değildir.
Brier skoru yalnızca kalibrasyon ölçüsü değildir; AUC de kalibrasyonu ölçmez.
Model-temelli güven aralıkları seçim/kümelenme yanlılığını ortadan kaldırmaz.