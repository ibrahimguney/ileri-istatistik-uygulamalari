# Hedef, birim ve eşzamanlı aralıklar

Kaynak üst dizindeki `kaynak/sat_act.csv`; SHA-256 kodda denetlenir. Orijinal
üç puanın tamamı olan 687 kişi korunur; yalnız SATV/SATQ analizi için örneklem
yeniden büyütülmez. Erkek245/kadın442, fark erkek eksi kadın. Gözlemsel öz bildirim
verisi; nedensellik ve ulusal temsil iddiası yok.

```sh
python uygulamalar/b09-manova/hedef-aralik/dogrula.py
python uygulamalar/b09-manova/hedef-aralik/analiz.py
```

- Ortak tersinir dönüşüm/kaydırma Hotelling T² ve Wald W'yi değiştirmez.
  Yeni koordinatların tekil hipotezleri değişir; boyut azaltma aynı değildir.
- Klasik ortak kovaryans/bağımsız çok değişkenli normal modelde marjinal %95,
  iki koordinat için Bonferroni en az %95 aile ve bütün doğrultulara Hotelling
  izdüşümleri. Her iki grup için ortak kovaryans varsayılır.
- Havuzlanmamış W yalnız büyük örneklem chi-kare duyarlılığıdır; küçük örneklem
  Welch–James düzeltmesi veya altı eğitim grubuna sağlam analiz değildir.
  Klasik aralıkları heteroskedastisiteye dayanıklı yapmaz.
- Basit etiket permütasyonu yapılmadı; ortalama eşitliği değiştirilebilirliği
  garanti etmez. En küçük p seçimi yok.

Altı denetim: tek değişkende Student karesi, affine değişmezlik, grup tersleme,
tekil/eksik kayıt reddi, aile aralığının marjinali içermesi, havuzlanmamış Wald'ın
tek değişkende Welch istatistiği karesine dönüşü. Sonuncunun p'si Welch t dağılımı
değil asimptotik chi-karedir. Yeni ek yalnız Python'dur; R/SPSS sınanmadı.

Çıktı: `sonuclar/ozet.json`, `sonuclar/araliklar.csv`. Kaynak: kitapta kullanılan
Rencher & Christensen (2012), *Methods of Multivariate Analysis*, 3. baskı.
