# Çözüm ve kontrol rehberi

Bu dosyayı görevleri denedikten sonra açın. Sayılar bu yerel alıntının özetidir.

## D — Hesaptan önce

80 eşleşmiş kayıt vardır, 160 bağımsız kişi değil. Okul kodu nominaldir.
İlk kaydın not farkı 11−0=11'dir; kaynakta sıfır geçerli olduğundan korunur.
n−1 böleni örnekleme yöntemini veya alıntının kapsamını değiştirmez.

## G — Rehberli hesap

1. G3 toplamı 1011; ortalama 12.6375; kareli sapmalar 324.4875.
   Örneklem varyansı 324.4875/79=4.107437; s=2.026681.
   Kapalı çerçeve varyansı 324.4875/80=4.056094.
2. G1'de sıralı 60. ve 61. değerler 13 ve 14'tür. Tip 7 konumu 60.25;
   Q3=13.25, Q1=11, IQR=2.25. Sınırlar 7.625 ve 16.625;
   bıyıklar 8 ve 16'dır. Kaynak sıraları 1, 16, 48, 61 işaretlenir.
3. İlk 60 ortalaması 12.783333, son 20 ortalaması 12.2.
   Ağırlıklı birleşim 12.6375, basit ortalama 12.491667'dir.
   Ağırlıklar kişi sayılarıdır; örnekleme yanlılığını düzelten ağırlıklar değildir.
4. Kovaryans 3.456646, korelasyon .702586. Fark ortalaması .4625,
   fark varyansı 3.087184 ve s=1.757038. Artış 32, eşitlik 31, azalış 17.
   Varyans özdeşliği: var(G3−G1)=var(G3)+var(G1)−2cov(G1,G3).
   Aynı kayıtlar ve aynı bölen kullanılmalıdır; nedensel dönem etkisi çıkarılmaz.

## B — Bağımsız deneme

1. Yarı-medyan Q3=13.5, IQR=2.5, üst sınır 17.25; yalnız sıfır not işaretlenir.
   Ana sonuç tip 7'dir. Yöntem değişikliği kaydın kendisini değiştirmez.
2. +10 ortalamayı 22.6375 yapar, s değişmez. ×5 ortalamayı 63.1875,
   s'yi yaklaşık 10.133406 yapar. Mekanik CV kaydırmada değişir, pozitif
   çarpmada aynı kalır; not için göreli yetenek değişkenliği iddiası kurulmaz.
3. Kalan 79 kayıtta G1 ortalaması 12.329114, s=2.011005,
   korelasyon .793762 olur. Fark görülmesi kaynak kaydın hatalı olduğunu kanıtlamaz.

## H — Yorum

Ortalama–medyan farkı tek başına dağılım tanısı değildir. Kutu grafiği işareti
inceleme nedenidir, otomatik silme gerekçesi değildir. Temsil tasarımla ilgilidir.
Ortalama artarken 17 kaydın notu azalmıştır; toplu özet her kişinin değişimini anlatmaz.