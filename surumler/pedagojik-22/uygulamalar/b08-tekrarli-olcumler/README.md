# Bölüm 8 — Tekrarlı ölçümler ve karma desenler

## Kaynaklar
- `kaynak/sleepstudy.csv`: `lme4::sleepstudy` (lme4 1.1-35.1), 18 kişi × 10 gün,
  ortalama tepki süresi (ms). Belenky vd. (2003) uyku kısıtlama çalışmasının
  gecede 3 saat yatakta kalma koşulu. Paket belgesine göre 0–1. günler uyum ve
  alıştırma, 2. gün temel; analiz 2.–9. günleri kullanır (8 ölçüm, 144 satır).
  Belge: https://search.r-project.org/CRAN/refmans/lme4/html/sleepstudy.html
- `kaynak/Orthodont.csv`: `nlme::Orthodont` (nlme 3.1-164), 27 çocuk (16 erkek,
  11 kız), 8/10/12/14 yaşlarında hipofiz–pterygomaksiller fissür uzaklığı (mm);
  Potthoff ve Roy (1964).
  Belge: https://search.r-project.org/CRAN/refmans/nlme/html/Orthodont.html

Dosyalar R'den `write.csv` ile değiştirilmeden aktarılmıştır (lme4 ve nlme
GPL lisanslıdır). Tek son LF ile normalize SHA-256:
- sleepstudy.csv `e4783c6b6ac6dcbfdf0e6731e4f0024166ca7416243873a480a64c40839a0af6`
- Orthodont.csv `2eacb310cb54353189058bd1acdfec400009bb9bd28d1afbdb012c90265284a0`

Uyku alıntısında kontrol grubu yoktur; gün etkisi yoksunluk ile zaman/öğrenme
etkilerini birlikte taşır.

## Çalıştırma
Kitap kökünden:
```sh
python uygulamalar/b08-tekrarli-olcumler/analiz.py
Rscript uygulamalar/b08-tekrarli-olcumler/analiz.R
```
`analiz.sps` IBM SPSS Statistics içindir (GLM /WSFACTOR ve MIXED). GNU PSPP bu
iki komutu desteklemez; SPSS sözdizimi PSPP ile çalıştırılamadığından SPSS
çıktısıyla ayrıca doğrulanmamıştır.

## Hesaplar
- Tek yönlü tekrarlı ölçümler ANOVA: SS kişi/zaman/hata elle; Mauchly W
  (R `mauchly.test` ile aynı ikinci dereceden p düzeltmesi), GG ve HF epsilon
  (özgün ve Lecoutre düzeltmeli), alt sınır; kısmi ve genelleştirilmiş eta-kare.
- Çok değişkenli yaklaşım: 7 ortonormal polinom karşıtlığıyla Hotelling T².
- Doğrusal eğilim karşıtlığı (kişi başına puan, tek örneklem t) ve 9.–2. gün eşli t.
- Karma etkiler modeli: `Reaction ~ DaysB + (DaysB | Subject)`, REML,
  statsmodels MixedLM; BLUP ve kişiye ayrı OLS eğimleri.
- Orthodont karma desen: cinsiyet (arası) × yaş (içi), Tip III (toplam-sıfır
  kodlama) karşıtlık puanlarının çok değişkenli doğrusal modeliyle; Mauchly,
  GG/HF; her yaşta Welch basit etkileri; kişi başına doğrusal büyüme hızlarının
  Welch karşılaştırması.

## Kontrol noktaları
Uyku: F(7,119)=15.31; W=.0025, χ²(27)=86.62; ε_GG=.445, ε_HF=.556;
η²_p=.474, η²_G=.217; Hotelling T²=81.68, F(7,11)=7.55, p=.0018;
doğrusal t(17)=6.20. Karma model: β1=11.435 (SH 1.845), τ1=6.766,
ρ=.178, σ=25.526.
Orthodont: cinsiyet F(1,25)=9.29; yaş F(3,75)=35.35; etkileşim F(3,75)=2.36,
p=.078 (GG .088); W=.735, ε_GG=.867, ε_HF(Lecoutre)=.977.
R/afex 1.3 ve lme4 1.1-35.1 aynı sonuçları verir.

## Dosyalar
- `sonuclar/ozet.json`: bütün sayılar, sürümler ve kaynak özetleri.
- `sonuclar/uyku_genis.csv`, `uyku_uzun.csv`, `orthodont_genis.csv`: SPSS girdileri.
- `assets_figures/tk-uyku-profilleri.pdf`, `assets_figures/tk-orthodont-profil.pdf`.


## Revizyon 11 — Eksik izlem ve çıkarım sınırı

`eksik-izlem/` eki sonradan maskelenmiş öğretim kopyasında aynı doğrusal karma
modeli tam/mevcut/tam kişi verilerinde karşılaştırır. Özgün arşivde eksik yoktur.
MAR/model uyumu, normal Wald ile küçük örneklem sd düzeltmesi ve kişi eğim
dağılımı ayrımı metinde açıklandı. Ana JSON'daki eski `slope_prediction_interval_95`
alanı, kestirilen parametreler sabitken normal rastgele eğim dağılımının yaklaşık
merkez aralığıdır; ortalama eğimin veya belirli bir kişinin formal tahmin aralığı
değildir. Yeni modül bu alanı kullanmaz. Dört yaşlık Holm öğretim ailesi eklenir.
Beş yeni Python testi geçti; ana veri/kod/sonuçlar korundu. Yeni R/SPSS eşdeğeri
veya MNAR/küçük-örneklem sd uygulaması yoktur.
