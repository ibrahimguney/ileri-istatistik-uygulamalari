# Üstünlük olasılığı ve belirsizlik

Kaynaklar Bölüm6 sleep/ToothGrowth CSV'leri; normalleştirilmiş SHA-256 kodda
denetlenir. Yeni ölçüm yok. Doz1: OJ10/VC10 bağımsız hayvan; sleep10 ID-eşli çift.

```sh
python uygulamalar/b10-parametrik-olmayan/ustunluk-belirsizlik/dogrula.py
python uygulamalar/b10-parametrik-olmayan/ustunluk-belirsizlik/analiz.py
```

A=P(X>Y)+.5P(X=Y)=.885; BM t=4.302937, sd11.835244, yaklaşık p=.001059.
Kodda üstünlük pozitif; SciPy istatistik işareti ters, iki yönlü p aynı.
Dağılım eşitliği, A=.5 ve medyan eşitliği farklı hipotezlerdir.

Seed20261025, 20000 bağımsız grup-içi hayvan resampling'i; percentile yaklaşık
%95 aralık [.690,1.000], 2415 tekrar1. Sıra-biserial dönüşümü [.380,1.000].
100 ikili kazanım bağımsız değildir; binom aralığı kurulmaz. Üst sınır1 evrende
kusursuz ayrım değildir. BCa/öğrencilendirilmiş bootstrap, küçük örneklem kapsama
simülasyonu ve öğrencilendirilmiş BM permütasyonu yapılmadı.

Sleep işaret testi sıfırı çıkarınca9/9 pozitif, koşullu p=.00390625. Wilcoxon
ile aynı sayı olması simetri varsayımlarını eşitlemez. Medyan aralığı sıfır dahil
10 farkla [.8,2.4] saat, medyan1.3. Sürekli modelde kapsama .978515625; kaydedilmiş
kesikli veride eşitlik otomatik değil, daha tutucu olabilir. Bu, eşli fark medyanıdır;
iki marjinal medyanın farkı değildir. Eşleme, iid çiftler ve örneklem seçimi önemlidir.

Yedi test: U/A, grup tersleme, artan dönüşüm, sıra değişmezliği, SciPy BM,
işaret-sıfır/medyan kapsamı, dejenere/eksik veri reddi. Yeni ek yalnız Python;
R/SPSS tekrar çalıştırılmadı. Eski ana kod/veri/sayısal sonuçlar korunur.
Çıktılar: `sonuclar/ozet.json`, `sonuclar/araliklar.csv`. Kaynak:
Fay & Proschan (2010), https://doi.org/10.1214/09-SS051 .
