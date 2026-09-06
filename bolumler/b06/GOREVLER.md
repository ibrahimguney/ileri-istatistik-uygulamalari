# Bölüm 6 — Öğrenci görevleri

## D — Önce kapsam

1. Ana analizde neden 60 kayıt var? Bölüm 2'nin 80 kaydıyla aynı sonuç beklenir mi?
2. G1/G3 eşleşmesi, kaynak sırası ve okul kapsamını açıklayın.
3. Sıfır not neden korunur? Son 20 kayıt yeni doğrulama örneklemi midir?

## G — Rehberli hesap

1. İlk 60 kayıtta merkezlenmiş Sxx, Syy, Sxy ve Pearson r'yi hesaplayın.
2. Bağlı notlara ortalama sıra verip sıraların Pearson katsayısını bulun;
   SciPy Spearman ile karşılaştırın. Bağsız kısa formül uygun mudur?
3. Pearson için klasik t, sd, iki yönlü p ve yaklaşık Fisher %95 aralığını bulun.
4. Ham/sıra grafiklerini inceleyin; aynı kayıtlardaki sabit terimli OLS R² ile
   Pearson r² eşitliğini denetleyin. Spearman karesini aynı şekilde yorumlamayın.

## B — Bağımsız uygulama

1. İlk kaydı yalnız kopyada dışlayarak Pearson/Spearman değişimini yorumlayın.
2. Her seferinde bir kayıt dışlayan 60 hesabın aralığını ve en etkili kaydını
   bulun. En yüksek korelasyonu seçmek neden uygun değildir?
3. Son 20 kaydın iki katsayısını bulun. Fark, anakütle korelasyon farkı testi midir?
4. Seed 202606 ve 19999 permütasyonda mutlak uçluğu hesaplayın. Sıfır uç sayısı
   p=0 mıdır? `(uç+1)/(B+1)` ve çözünürlük sınırını açıklayın.
5. Pozitif çarpmanın katsayıları koruduğunu, negatif çarpmanın işareti değiştirdiğini sınayın.

## H — Hatalı raporu onarın

“r yüksek, herkesin notu arttı. Nedensellik kanıtlandı. Bağlı notlara kısa sıra
farkı formülünü uyguladık. İlk satırı silince r arttı; o kayıt hatalıymış.
Permütasyonda uç çıkmadı; p=0, test kesin.” Beş iddiayı ayrı düzeltin.

## Teslim

Kısa rapor, notebook/kod, ham/sıra grafikleri ve duyarlılık tablosu. Ana n,
katsayı, test yöntemi, yaklaşık aralık, permütasyon B/seed ve kaynak sınırını
belirtin. Rubrik: kaynak/seçim20, hesap/sıra30, grafik/duyarlılık20,
çıkarım/yorum20, yeniden üretim10. Yapılmamış R/SPSS çalıştırmasını raporlamayın.