# Bölüm 6 — Çözüm rehberi

Önce görevleri çözün; ayrıntılar beklenen.json içindedir.

## Ana analiz

Sxx=385.4, Syy=234.1833333333, Sxy=224.3. Pearson r=.746612792;
ortalama sıralarla Spearman r_s=.831085662. Sıraların Pearson korelasyonu
Spearman'a eşittir; bağlı veride bağsız kısa sıra farkı formülü kullanılmaz.

Pearson t(58)=8.547100; klasik p≈7.46694e−12;
yaklaşık Fisher %95 aralık [.607944246,.841082238]. Pearson r²=.557430662,
aynı 60 kayıtta sabit terimli OLS R²'sidir. Spearman karesi ham not varyansını
açıklama oranı diye raporlanmaz. Model/temsil sınırları korunur.

| Alt küme | n | Pearson | Spearman |
|---|---:|---:|---:|
| Ana | 60 | .746612792 | .831085662 |
| Kaynak 1 hariç | 59 | .865833531 | .826699998 |
| Kaynak 61–80 | 20 | .627307114 | .570535504 |

Pearson'daki artış ilk kaydın hatalı olduğunu kanıtlamaz. Ana 60 korunur.
Duyarlılık tablosu en iyi sonucu seçmek için değil kayıt etkisini göstermek
içindir. Son 20'nin farklı katsayısı doğrudan korelasyon farkı testi değildir.

Birini-dışarıda-bırakma denetiminde Pearson aralığı
[.727846069, .865833531]; en düşük değer kaynak 48, en yüksek kaynak 1
çıkarılınca oluşur. Spearman aralığı [.822255639, .849831028]; uçlar
sırasıyla kaynak 16 ve 40 çıkarılınca oluşur. Ana katsayıdan mutlak değişim
ölçütüyle en etkili kayıt Pearson için 1, Spearman için 40 olur.
Bunlar güven aralığı değil, 60 farklı duyarlılık hesabının aralığıdır.

## Permütasyon ve yorum

Python seed202606, B19999, mutlak iki yönlü uç sayısı0;
Monte Carlo p=(0+1)/(19999+1)=.00005. Bu çözünürlük sınırıdır; sıfır olasılık
veya bütün permütasyonları tarayan tam kesin test değildir. Spearman asimptotik
p'si farklı yöntemdir. Aynı seed R/NumPy'da aynı diziyi garanti etmez.

Pozitif doğrusal ölçekleme katsayıları korur, negatif ölçekleme işareti tersler.
Not sırası ile dönem farkı farklı sorulardır. Aynı koordinattaki kayıtlar üst
üste gelir; nokta sayısı kişi sayısı değildir. Korelasyon nedensellik değildir.