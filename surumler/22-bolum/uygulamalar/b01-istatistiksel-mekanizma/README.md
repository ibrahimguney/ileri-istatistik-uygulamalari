# Bölüm 1 — İstatistiksel mekanizma

## Kaynak ve sınırlar
Cortez, P. (2008). Student Performance [Veri seti]. UCI Machine Learning Repository.
DOI: 10.24432/C5TG7T. CC BY 4.0.
https://archive.ics.uci.edu/dataset/320/student+performance
Lisans: https://creativecommons.org/licenses/by/4.0/
Kaynak sözlüğü 6 Eylül 2026 tarihinde incelendi.

Bölüm 12'nin dondurulmuş `../b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv`
dosyası yeniden kullanılır: özgün kaynağın ilk 80 satırındaki school/G1/G3
sütunları. Ana dosya değiştirilmez; notlar üretilmez veya doldurulmaz.
Kaynak dosyasının sonuna tek LF gelecek biçimde normalize SHA-256:
`51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9`.
Ham hash de JSON'a yazılır. Hash, yalnız yerel değişmezlik denetimidir.

Bütün kayıtlar GP okulundandır. Portekizce kaynak dosyasının 649 kaydını, iki
okulun bütün öğrencilerini veya Türkiye'yi temsil eden rastgele örneklem değildir.
80 kayıt yalnız örnekleme alıştırmasında kapalı öğretim anakütlesi sayılır.
Bu tanım, gerçek araştırmanın hedef anakütlesiyle karıştırılmaz.

## Veri sözlüğü
- kaynak_satir: izlenebilir kaynak sıra numarası; öğrenci kimliği değil.
- school: nominal okul kodu; burada yalnız GP.
- G1: birinci dönem notu, 0–20; sıfır not eksik kodu değildir.
- G3: yıl sonu notu, 0–20; bu alıntıda 7–17.
- G3_bant: türetilmiş sıralı öğretim bandı, 0–9 / 10–14 / 15–20.
  Resmî geçme eşiği veya eşit aralıklı yetenek ölçüsü iddiası yoktur.

## Çalıştırma
Kitap kökünden, kurulu Python paketleriyle:
```sh
python uygulamalar/b01-istatistiksel-mekanizma/analiz.py
```
Yeni bağımlılık kurulmaz. `analiz.R` yalnız temel R kullanır.
`analiz.sps` önce Python ile üretilmiş CSV'leri okur. R betiği Python ile aynı
frekansları ve yüzdeleri verir.

## Gerçek kayıtlar ve öğretim dosyaları
- `notlar.csv`: 80 gerçek kaynak kaydı ve türetilmiş bant; hiçbir ana not değişmez.
- `notlar_uzun.csv`: 160 dönem satırı, hâlâ 80 öğrenci kaydı. Bağımsız n artmaz.
- `eksik_veri_ogretim.csv`: **değiştirilmiş öğretim kopyası**. Kaynak sırası
  1–4 için yalnız G3 görünmez yapılır ve bant yeniden hesaplanır. Gerçek eksiklik değildir.
- `dongusellik_kurgu.csv`: **tamamen kurgusal** 80 konumlu 1/0 listesi;
  gerçek öğrenci özelliği veya yeni saha verisi değildir.
- `sonuclar/ornek_*.csv`: seçilen 10'ar gerçek kayıt. İlk 10 seçimi olasılıklı değildir.
- `sonuclar/not_frekanslari.csv`, `bant_frekanslari.csv`: sayım ve yüzdeler.
- `sonuclar/sekiz_baslangic.csv`: sekiz sistematik seçimin tamamı; simülasyon değildir.
- `sonuclar/ozet.json`: kapsam, seçim satırları, tohum, sürümler ve hesaplar.
- `../../assets_figures/b01-veri-grafikleri.pdf`: bant sayıları ve bir puanlık histogram.

Sistematik gösterimde r=3 öğretim için sabittir; rastgele çekildiği iddia edilmez.
Tasarım beklentisi hesabında r=1,...,8 eşit olasılıklı kabul edilir. Her kayıt
sekiz olası örneğin tam birindedir. Basit rastgele örnek NumPy default_rng,
seed=20260906 ile yerine koymadan seçilir; seçilen satırlar ayrıca saklanır.
R/SPSS aynı satır listesini kullanır, aynı tohumla aynı seçimi üretmiş sayılmaz.

## Denetlenen sonuçlar
G3 toplamı 1011, ortalama 12.6375. Bant sayıları 2, 63, 15; yüzdeleri 2.5,
78.75, 18.75. G1'de bir sıfır var; gerçek notlarda eksik yok.
Basit rastgele 10 satırın ortalaması 13.2; sistematik r=3 için 12.2;
ilk 10 kayıt için 13.0. Tek bir sapma yöntem yanlılığı kanıtı değildir.
Sekiz sistematik ortalamanın ortalaması 12.6375'tir.
Öğretim kopyasında 76 geçerli G3; üst bant 15 kişi. Toplam yüzde 18.75,
geçerli yüzde 19.7368421053. Kurgu döngü listesinde anakütle oranı .125,
örnek oranları 1,0,0,0,0,0,0,0; eşit başlangıç beklentisi .125.

Frekans toplamları ham sayımlarla, histogram kutuları frekanslarla karşılaştırılır.
Uzun biçim tekrar genişe çevrilerek iki not sütunu birebir denetlenir.
Kaynak baytlarının değişmediği koşu sonunda kontrol edilir. Güven aralığı,
hipotez testi, nedensel analiz veya örneklem büyüklüğü yeterliği hesaplanmaz.

SPSS'te bant boşluğu öğretim kopyasında kullanıcı-eksik olarak tanımlanır.
Gerçek sıfır not eksik tanımlanmaz. Önceki filtre/ağırlık/split-file ayarları
kapatılır. Scale, notları operasyonel sayısal alan olarak tanımlar; eşit yetenek
aralığı veya geçerlik kanıtı değildir. Üretilen frekans sırası ve paydalar kontrol edilir.

Yöntem belgeleri:
- https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch13/prob/5214899-eng.htm
- https://www.ibm.com/docs/en/spss-statistics/31.0.0?topic=reference-frequencies