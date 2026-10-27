# Bölüm 1: Tasarım belirsizliği

Bu ileri okuma, mevcut 80 kaydı kapalı öğretim anakütlesi kabul eder. Kaynak
dosyayı değiştirmez; yeni saha verisi üretmez. Ana bölüm analizinden ayrıdır.

Kitap kökünden:

```sh
python uygulamalar/b01-istatistiksel-mekanizma/tasarim-belirsizligi/dogrula.py
python uygulamalar/b01-istatistiksel-mekanizma/tasarim-belirsizligi/analiz.py
```

Öğrenci deposunda aynı komutlar `surumler/22-bolum/` klasöründen çalıştırılır.
Bağımlılıklar ortak requirements dosyasındadır; ek paket gerekmez.

- Gerçek kayıtlarda SRSWOR ortalama varyansı tam formülle hesaplanır:
  `(1 - n/N) * S²/n`; `S²` böleni `N-1` olan sonlu anakütle varyansıdır.
- Sistematik örneklemenin sekiz olası başlangıcı tam sayılır; varyansın böleni
  8'dir. Birbirinden bağımsız sekiz yeni saha örneklemi gözlenmiş değildir.
- 20.000 basit rastgele örnek, sabit notlardan yerine koymadan seçilir.
  Tekrarlar arasında seçim yeniden başlatılır. NumPy default_rng tohumu 20261025.
- `sonuclar/ozet.json`: tam tasarım sonuçları, yaklaşık Monte Carlo sonuçları,
  kapsam ve sürümler. `sonuclar/srs_tekrarlari.csv`: 20.000 örnek ortalaması.
- Tam sonuçlar simülasyona uydurulmaz. Monte Carlo ortalamasının farkı kendi
  standart hatasıyla, deneysel varyansın farkı %5 göreli toleransla kontrol edilir.
- `dogrula.py`, küçük ayrı bir anakütlenin bütün alt kümelerini sayarak SRS
  varyans formülünü denetler; sistematik seçim ve geçersiz n kontrolünü sınar.

Gerçek notlarda SRS SE=.599500, sistematik SE=.353332'dir. Döngüsellik kurgusunda
sistematik varyans SRS varyansının yaklaşık 11.286 katıdır. Tek bir tasarımın
her listede üstün olduğu sonucu çıkmaz. Bunlar dış anakütleye güven aralığı,
nedensel etki veya 20.000 bağımsız öğrenci grubu değildir. Gerçek notların UCI
CC BY 4.0 koşulları ana uygulama README'sinde; kod lisansı ortak LICENSE'dadır.
Bu ek modül Python'da doğrulandı; R/SPSS sürümü hazırlanmadı.
