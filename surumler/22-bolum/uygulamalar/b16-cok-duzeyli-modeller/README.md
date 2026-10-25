# Bölüm 16 — Çok düzeyli modeller

## Kaynak
`nlme::MathAchieve` ve `nlme::MathAchSchool` (nlme 3.1-164): 1982 High School
and Beyond araştırmasından 160 okulda 7185 öğrenci (Raudenbush ve Bryk, 2002).
Belge: https://search.r-project.org/CRAN/refmans/nlme/html/MathAchieve.html
R'den `write.csv` ile değiştirilmeden aktarılmıştır. Normalize SHA-256:
- MathAchieve.csv `087beeed36585553ec1b69dd5b29266a99e8189c565d51a301b99e53a2a0be72`
- MathAchSchool.csv `f4b5327f022a2433b536bbde8cd6f7273d89b72c69bef8cd6de6bc1cd6a0cf19`
Okul ortalama SES'i örneklemden hesaplanır (kaynak MEANSES ile en büyük fark .006).

## Çalıştırma
```sh
python uygulamalar/b16-cok-duzeyli-modeller/analiz.py   # ~20 sn
Rscript uygulamalar/b16-cok-duzeyli-modeller/analiz.R
```
`analiz.sps` IBM SPSS Statistics içindir (MIXED); GNU PSPP desteklemez.

## Hesaplar
- Boş model, ICC, tasarım etkisi, etkili n, okul ortalaması güvenirliği.
- Naif OLS, okul kümeli sağlam SH (HC1 benzeri, statsmodels cluster) ve
  rastgele kesişimli model.
- Grup ortalamasına merkezleme: okul içi, okullar arası ve bağlamsal etki
  (genel ortalamaya merkezlenmiş modelle doğrulanır).
- Rastgele eğim; REML olabilirlik oranı ve sınırda karışım p değeri.
- Düzeyler arası etkileşim (okul içi SES × okul ortalama SES, × Katolik);
  sabit etkiler için ML olabilirlik oranı.
- statsmodels MixedLM'de L-BFGS bir modelde sahte (varyans = 0) çözümde
  "yakınsadı" bildirdi; betik BFGS, Powell ve BFGS'ten başlayan Powell
  çözümlerini karşılaştırıp en yüksek olabilirliği seçer.

## Kontrol noktaları (R lme4 1.1-35.1 ile aynı)
Boş model: γ00=12.637, τ00=8.614, σ²=39.148, ICC=.180, DE=8.92.
Grup içi 2.191, gruplar arası 5.866, bağlamsal 3.675.
Rastgele eğim: τ11=.701, LR=10.497, karışım p=.0032.
Düzeyler arası: 12.128, ses_m 2.945, ses_ort 5.333, katolik 1.227,
ses_m×ses_ort 1.039, ses_m×katolik −1.643; τ00=2.380, τ11=.101, σ²=36.721;
ML LR χ²(2)=41.71.
Rastgele kesişimli SES modelinde eğim SH'si statsmodels'ta .108, lme4'te .106'dır
(varyans bileşeni belirsizliğinin bilgi matrisine katılış biçimi farklıdır).

## Dosyalar
- `sonuclar/ozet.json`, `sonuclar/analiz_verisi.csv`.
- `assets_figures/cd-okul-dogrulari.pdf`.

## Yorum sınırı

Grup içi merkezleme okul içi ve gruplar arası ilişkileri ayırır; tek başına
nedensel karıştırıcılığı gidermez. Yaklaşık DE=8.92 ve etkili n≈806 bir
ortalama için kaba hesaptır; her katsayının belirsizliğine uygulanmaz.
Okul türü katsayıları bu gözlemsel örneklemde ilişki olarak yorumlanır.

## Revizyon 19: hedef ve tahmin

[Ek uygulama](okul-tahmini/README.md): bağımsız toplulaştırılmış REML,
eşit/eşitsiz okul büyüklüklerinde tasarım etkisi, hedef ortalamalar ve bilinen/yeni
okul tahmini. Yedi test; yalnız Python. Eski veriler ve ana analizler korunur.
Koşullu aralıklar parametre kestirim belirsizliğini içermez.
