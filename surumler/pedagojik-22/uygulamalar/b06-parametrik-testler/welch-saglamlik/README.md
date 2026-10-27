# Bölüm 6 — Welch kalibrasyonu ve sağlam duyarlılık

Ana t-testleri, sleep/ToothGrowth kaynakları ve önceki sonuçlar korunur.
Ek yalnız Python'da doğrulandı; R/SPSS eşdeğeri hazırlanmadı.

Kitap kökünden; öğrenci deposunda `surumler/22-bolum/` klasöründen:

```sh
python uygulamalar/b06-parametrik-testler/welch-saglamlik/dogrula.py
python uygulamalar/b06-parametrik-testler/welch-saglamlik/analiz.py
```

## Kalibrasyon kurgusu

Bağımsız normal model, gerçek ortalama farkı0, n1=10/n2=30, iki yönlü alfa.05.
Her senaryoda 200.000 normal ortalama ve bağımsız ki-kare varyans çekilişi;
NumPy default_rng seed20261025. Yeni ham kişi/hayvan tablosu üretilmez.

| Sigma1/Sigma2 | Student red oranı | Welch red oranı |
|---|---:|---:|
| 3/1 | .210145 | .051055 |
| 1/3 | .004045 | .049930 |
| 1/1 | .049160 | .050320 |

H0 doğru olduğundan bunlar güç değil Tip I hata simülasyon tahminidir.
Welch MC SH yaklaşık .00049; ilk Student satırında .00091. Welch-Satterthwaite
yaklaşımı ve sonlu simülasyon nedeniyle oranların tam .05 olması beklenmez.
Bu, her dağılım/n veya bağımlılık yapısında kusursuz hata kontrolü iddiası değildir.

Gerçek fark varyansı sigma1²/n1+sigma2²/n2 ile E(SE_pooled²) ayrıca hesaplanır.
Oranlar .413534 / 2.368421 / 1'dir. Küçük grupta büyük varyans belirsizliği
küçümsetirken ters eşleşme tutuculuğa yol açar. Levene/Shapiro ile otomatik
iki aşamalı yöntem seçimi bu simülasyonda uygulanmaz.

## Gerçek veri: Yuen

ToothGrowth doz1'de OJ/VC n10+10, sıradan Welch farkı5.93,
GA[2.80215,9.05785], p=.001038. Her kuyruktan %20 kırpılmış konumlar
23.183333/16.383333, fark6.80; Yuen SE1.498243, df6.386005,
p=.003369, GA[3.18698,10.41302]. Ana dosyadan hayvan silinmez.

Her grupta g2/h6. Varyans hesabında winsorize SS59.001/8.341,
q=SS/[h(h−1)] kullanılır. Elle hesap SciPy `ttest_ind(equal_var=False,trim=.2)`
istatistiği, p, df ve aralığıyla denetlenir. Yuen sıradan ortalama değil kırpılmış
anakütle ortalaması farkını hedefler. Küçük katkı sayısı ve dağılım/bağımsızlık
koşulları önemlidir; en küçük p seçilmez. Welch ve Yuen aralıkları aynı hedefe
aitmiş gibi birleştirilmez. Sıra/permütasyon/bootstrap uygulanmadı.

Beş test: elle küçük kırpma/winsor hesabı, sıfır kırpmanın Welch'e dönüşmesi,
birim/yön dönüşümleri, eşit n standart hata özdeşliği ve geçersiz girdi reddi.
`sonuclar/kalibrasyon.csv` ve `sonuclar/ozet.json` üretilir. Ham kaynak hash'i
ve dosya değişmezliği kontrol edilir. Kaynak/GPL notları üst README'de korunur.

Kaynak: Yuen (1974), https://doi.org/10.1093/biomet/61.1.165 ;
mevcut bölümdeki Delacre ve arkadaşları kaynakları.
