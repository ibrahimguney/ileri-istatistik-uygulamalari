# Bölüm 9 — Çok değişkenli varyans analizi (MANOVA)

## Kaynak
`kaynak/sat_act.csv`: `psych::sat.act` (psych 2.4.1), SAPA çevrimiçi
projesinden 700 kişinin öz bildirim ACT, SATV, SATQ puanları, cinsiyet
(1 erkek, 2 kadın), eğitim (0–5; belgede 1 = lise, 5 = lisansüstü) ve yaş.
Belge: https://www.personality-project.org/r/html/sat.act.html
R'den `write.csv` ile değiştirilmeden aktarılmıştır; `kayit` satır adıdır.
Tek son LF ile normalize SHA-256:
`1eebcf05961dd2f569b545e5456c0fd2e5c8b5a79cd82770f3b0a06c31230fce`.
SATQ 13 kişide eksiktir; analiz 687 tam kayıtla yapılır.

## Çalıştırma
```sh
python uygulamalar/b09-manova/analiz.py
Rscript uygulamalar/b09-manova/analiz.R
```
`analiz.sps` IBM SPSS Statistics içindir. GNU PSPP çok bağımlı değişkenli
GLM, DISCRIMINANT ve REGRESSION /SAVE=MAHAL komutlarını desteklemez; bu
bölümler SPSS çıktısıyla ayrıca doğrulanmamıştır.

## Hesaplar
- H ve E SSCP matrisleri; E⁻¹H özdeğerleri, kanonik korelasyonlar.
- Wilks (Rao F), Pillai, Hotelling–Lawley (Pillai–Samson; R/SPSS ile aynı),
  Roy (üst sınır F). statsmodels ile değer ve Wilks/Pillai/Roy F denetlenir;
  statsmodels HL için McKeon yaklaşımı kullanır (F 2.024).
- İki grup Hotelling T², Mahalanobis D, ayırma katsayıları, SATQ−SATV farkı.
- Box M (ki-kare yaklaşımı), grup standart sapmaları.
- Mahalanobis uç değer taraması (χ²(3) .999 = 16.27) ve duyarlılık analizi.
- Ayırma fonksiyonu standart ve yapı katsayıları; Bonferroni düzeltmeli ANOVA'lar.
- İki faktörlü Tip II MANOVA (toplam-sıfır kodlama, model karşılaştırması).

## Kontrol noktaları
Cinsiyet (SATV, SATQ): T²=28.65, F(2,684)=14.31, D=.426.
Eğitim: Pillai .0435 F(15,2043)=2.00 p=.012; Wilks .9568; HL .0448;
Roy .0356. Box M χ²(30)=84.53. Tip II: cinsiyet Pillai .042 F(3,673)=9.84;
eğitim .044 F(15,2025)=2.02; etkileşim .026 F(15,2025)=1.16.
R (stats::manova, car::Manova 3.1-2) aynı sonuçları verir.

## Dosyalar
- `sonuclar/ozet.json`, `sonuclar/analiz_verisi.csv` (687 kayıt; SPSS girdisi).
- `assets_figures/mv-sat-gruplar.pdf`.
