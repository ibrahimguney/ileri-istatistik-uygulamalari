# Bölüm 12 — Birinci dönem notu ve yıl sonu başarısı

## Kaynak, atıf ve lisans
Gerçek gözlemsel veri kaynağı: Paulo Cortez (2008), **Student Performance**,
UCI Machine Learning Repository, DOI: 10.24432/C5TG7T.

- Veri sayfası: https://archive.ics.uci.edu/dataset/320/student+performance
- Resmi CSV: https://archive.ics.uci.edu/static/public/320/data.csv
- Lisans: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Lisans metni: https://creativecommons.org/licenses/by/4.0/
- Özgün araştırma: Cortez, P., & Silva, A. (2008). Using data mining to predict
  secondary school student performance. Proceedings of the 5th Future Business
  Technology Conference (FUBUTEC 2008), 5–12. EUROSIS.
- Erişim ve bu kitaptaki uyarlama tarihi: 5 Eylül 2026.

Kaynak iki Portekiz okulunda okul kayıtları ve anketlerle toplanmıştır.
Bu pakette **Portekizce dersi** verisi kullanılır; matematik verisi kullanılmaz.
G1 birinci dönem, G3 üçüncü dönemde verilen yıl sonu notudur. Ölçek 0–20'dir.
Çalışma saati veya 0–100 sınav puanı değildir. Asıl kaynaktaki studytime sıralı
kategoridir ve bu modele alınmamıştır.

## Alt küme seçimi ve veri aktarımı
Resmî CSV'nin **ilk 80 veri satırının school, G1 ve G3 sütunları** kaynak
dosyasına aktarılmıştır. Bu, orijinal CSV'nin tamamı değil,
sütunları azaltılmış bir alıntıdır. Kaynakta Portekizce dersi için 649 kayıt vardır.

| Dosya | Seçim | Amaç |
|---|---|---|
| kaynak/uci-portekizce-ilk80-notlar.csv | Kaynak sırası 1–80 | Dondurulmuş kaynak alıntısı |
| not_basari.csv | Kaynak sırası 1–60 | Ana analiz, n=60 |
| aktarim.csv | Kaynak sırası 61–80 | Bağımsız çözüm etkinliği, n=20 |

Seçim başlık satırı hariç, özgün sıra korunarak yapılmıştır; sonuçlara göre
satır seçilmemiştir. Bu **rastgele veya temsili örnekleme değildir**.
Seçilen bütün satırlar GP okuluna aittir; MS okulu bu alt kümede yoktur.
İkinci grup, yeni bir okul veya dış doğrulama örneklemi değildir. Kaynak sıra
numarası bir araştırmacı tarafından atanmış öğrenci kimliği değildir.

Notlar değiştirilmemiş, yuvarlanmamış, doldurulmamış veya üretilmemiştir.
G1=0 olan ilk kayıt da korunmuştur; sıfır otomatik olarak eksik değer sayılmaz.
Bu 80 satırda G1/G3 için eksiklik yoktur. Kimlik, aile, sağlık ve benzeri
analiz dışı alanlar aktarılmamıştır. Kodlar sonuçları **bu kitap için yeniden
hesaplar**; özgün makalenin sayısal bulguları olarak sunmaz.

## Veri sözlüğü
| Değişken | Açıklama |
|---|---|
| kaynak_satir | Resmi CSV'de başlık hariç, 1'den başlayan satır sırası |
| school | Kaynaktaki okul kodu; bu alıntıda GP |
| G1 | Birinci dönem notu, 0–20 |
| G3 | Yıl sonu notu, 0–20 |

## Çalıştırma ve kaynak doğrulama
Çalışma dizini kitabın ana dizini `03-AdvancedStaticalAppTR` olmalıdır.

```sh
python uygulamalar/b12-regresyon/analiz.py
Rscript uygulamalar/b12-regresyon/analiz.R
```

Python numpy, scipy, pandas, matplotlib ve statsmodels kullanır. R temel
paketlerle çalışır. SPSS'te aynı çalışma dizininden analiz.sps dosyasını açın.
SPSS betiği klasik sonuçları üretir; HC3 hesabı Python ve R betiklerindedir.

İnternet erişimi olan bir bilgisayarda **resmî CSV ile otomatik satır karşılaştırması**:

```sh
python uygulamalar/b12-regresyon/analiz.py --kaynak-dogrula
```

Bu seçenek resmi CSV'nin 649 satırını ve ilk 80 kayıttaki seçili sütunların
birebir eşleşmesini denetler.

Python ana ve aktarım CSV'lerini kaynak alıntıdan yeniden oluşturur; `sonuclar`
klasörüne JSON/CSV çıktıları yazar, kitaptaki `b07-ogrenme-senaryosu.pdf` şeklini
yeniler. Alıntının SHA-256 özeti ozet.json'a kaydedilir; bu özet, orijinal
UCI dosyasının değil **sütun alıntısının** özetidir. R kendi tanı PDF'sini
üretir. Betikler yalnızca bu çıktı dosyalarını yeniler; kaynak alıntısını değiştirmez.

## Beklenen sonuçlar: ana alt küme
- n=60; sabit=5.741221; eğim=0.581993; R²=0.557431.
- Klasik eğim SE=0.068092; t(58)=8.547100; p=7.46694e-12.
- Klasik eğim %95 GA=[0.445691, 0.718295].
- G1=12: ortalama tahmin=12.725134.
- Klasik ortalama %95 GA=[12.379418, 13.070850].
- Klasik yeni birey %95 TA=[10.027070, 15.423198].
- HC3 eğim SE=0.280588; t(58) referanslı %95 GA=[0.020334, 1.143651].
- İlk kaydın kaldıracı=0.396558; Cook uzaklığı=8.426852.
- Eğitim RMSE=1.314296; LOOCV RMSE=1.620230.
- Bir kayıt çıkarılınca eğim aralığı: [0.543534, 0.855597].
- Aktarım (n=20): sabit=4.111675; eğim=0.652284; R²=0.393514.

## Yorum sınırları
İlk kayıt yüksek etkilidir; çıkarılması eğimi belirgin değiştirir. HC3 ve
klasik standart hata farkı raporlanmalıdır. Klasik tahmin aralıkları öğretim
amaçlı model hesaplarıdır; koşullu hata modeline bağlıdır, geçerlilikleri
kanıtlanmış değildir. HC3, seçilim yanlılığını, kümelenmeyi veya model biçimini
düzeltmez ve kendiliğinden sağlam bireysel tahmin aralığı üretmez.

İlk 60 sıra kaydıyla bütün UCI verisine, iki okulun tüm öğrencilerine veya
Türkiye'deki öğrencilere genelleme yapılmaz. Birinci dönem notu mevcut olduktan
sonraki yordama hedeflenir; yıl başında henüz bilinmeyen bir notu kullanmak
uygun değildir. Yıl sonu notunun önceki değerlendirmelerle ilişkili olması
nedeniyle ilişkiyi bir müdahalenin nedensel etkisi olarak yorumlamayın.

Python, bağımsız scipy hesabı, elle kurulan aralıklar, doğrudan HC3 matris hesabı
ve 60 ayrı modelle LOOCV üzerinden doğrulanmıştır. R betiği aynı katsayıları,
aralıkları ve LOOCV hatasını verir. Eski sentetik çalışma süresi verisi bu paketten çıkarılmıştır.