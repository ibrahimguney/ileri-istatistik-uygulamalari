# Bölüm 3 — Birleştirme denetimi ve bilgi sınırı

Gerçek ilk 100 BFI kaydında A/C 5/5 puanları ve ayrı bir merkezleme kurgusu.
Ana BFI arşivi, ana hazırlama kodu ve önceki çoklu atama uygulaması değiştirilmez.

Kitap kökünden; öğrenci deposunda `surumler/22-bolum/` klasöründen:

```sh
python uygulamalar/b03-veri-hazirlama/birlesim-denetimi/dogrula.py
python uygulamalar/b03-veri-hazirlama/birlesim-denetimi/analiz.py
```

Ek betik üst klasörün mevcut `validate` ve `score` işlevlerini kullanır; ana
betiğin `main` yordamını çağırmaz. Ortak NumPy/pandas bağımlılıkları kullanılır.
Yeni modül yalnız Python'da doğrulandı; R/SPSS karşılığı yoktur.

## Gerçek kayıtlar

A geçerli n=99, C n=98, ortak n=97. A solda:

| Birleştirme | Satır | A geçerli | C geçerli | Yalnız A/C |
|---|---:|---:|---:|---|
| inner | 97 | 97 | 97 | 0/0 |
| left | 99 | 99 | 97 | 2/0 |
| outer | 100 | 99 | 98 | 2/1 |

Ortak A/C ortalamaları 4.554639 ve 4.179381; bütün geçerli puanlarda ise
4.563636 ve 4.187755'tir. Birleştirme kapsamı puan paydasını değiştirebilir.
Bu, eksiklik mekanizmasını veya dış anakütlede yanlılığı saptamaz.

`checked_join` yalnız bu örneğin bire bir ilişki sözleşmesi içindir. Eksik/boş,
tekrarlı, türü farklı anahtarları ve anahtar dışı çakışan sütun adlarını reddeder.
Örneğin `01` ile sayısal 1'in aynı kimlik olduğunu varsaymaz. Genel bir veri tabanı
anahtar temizleyicisi değildir. pandas boş anahtarları eşleştirebildiği için boşlar
birleştirmeden önce reddedilir. Hatalı girdiler gerçek arşivde değil test kopyasındadır.

Çıktılar `sonuclar/inner-birlesim.csv`, `left-birlesim.csv`, `outer-birlesim.csv`,
`birlesim-denetimi.csv`, `ozet.json`. Ham dosyanın SHA-256 özeti ana README'deki
tanımla kontrol edilir. Yeni kişisel tanımlayıcı eklenmez; kaynak sıra etiketleri korunur.

## Ayrı kurgu: sızıntı

Eğitim [0,2], test [100,102]. Eğitim ortalaması 1, havuzlanmış ortalama 51;
eğitim merkezlemeleri [-1,1] ve [-51,-49]. Bu yalnız öğrenilen dönüşüme test
dağılımının taşınmasını gösterir. Gerçek BFI puanı, tahmin modeli veya başarım
sonucu değildir. Gelecekte bilinmeyen test sonucu kullanılamaz. Çıkarım amaçlı
MI'da gözlenen sonuç değişkeninin kullanımı bununla aynı problem değildir.

Beş test; çokluk/eşleşme, boş/tekrarlı anahtar reddi, türlerin sessiz dönüşmemesi,
eğitim merkezi ve geçersiz eğitim girdilerini denetler. Kaynak/lisans sınırları
üst uygulama README'sinde korunur. Yeni MI/MICE, FIML veya mekanizma testi yapılmaz.
