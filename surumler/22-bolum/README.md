# İleri İstatistik — 22 bölümlük öğrenci sürümü

Bu klasör güncel 22 bölümlük kitaba eşlik eder. Depo kökündeki `bolumler/`
klasörü eski 18 bölümlük sürümdür; aynı numaralar farklı konulara karşılık gelebilir.
Eski dosyalar ve doğrulama kayıtları korunmuştur. Tam kitap metni/PDF'si ve
ECLS-K SAV/DAT dosyaları bu öğrenci paketine dahil değildir.

## Kurulum ve doğrulama

```sh
cd surumler/22-bolum
python -m pip install -r requirements.txt
python tools/dogrula_22.py
python tools/dogrula_22.py --analyses --report dogrulama/latest.json
```

Analiz doğrulayıcısı geçici çalışma kopyasında yürütür; referans sonuçları
sonuca uydurarak değiştirmez. R ve SPSS/Amos bu teslimde ayrıca çalıştırılmadı.

## Bölümler

| Bölüm | Konu | Paket |
|---|---|---|
| 1 | İstatistiksel Düşünme: Sorudan Kanıta | [B01](bolumler/b01/) |
| 2 | Betimsel İstatistik | [B02](bolumler/b02/) |
| 3 | Veri Hazırlama ve Analize Hazırlık | [B03](bolumler/b03/) |
| 4 | Hipotez Testi | [B04](bolumler/b04/) |
| 5 | Güç Analizi ve Örneklem Büyüklüğü Planlama | [B05](bolumler/b05/) |
| 6 | Parametrik Testler | [B06](bolumler/b06/) |
| 7 | Varyans Analizi (ANOVA) | [B07](bolumler/b07/) |
| 8 | Tekrarlı Ölçümler ve Karma Desenler | [B08](bolumler/b08/) |
| 9 | Çok Değişkenli Varyans Analizi (MANOVA) | [B09](bolumler/b09/) |
| 10 | Parametrik Olmayan Testler | [B10](bolumler/b10/) |
| 11 | Korelasyon Analizi | [B11](bolumler/b11/) |
| 12 | Regresyon Analizi | [B12](bolumler/b12/) |
| 13 | Çoklu ve Lojistik Regresyon | [B13](bolumler/b13/) |
| 14 | Kovaryans Analizi (ANCOVA) | [B14](bolumler/b14/) |
| 15 | Aracılık ve Düzenleyicilik Analizleri | [B15](bolumler/b15/) |
| 16 | Çok Düzeyli Modeller | [B16](bolumler/b16/) |
| 17 | Ölçek Uyarlama ve Güvenirlik | [B17](bolumler/b17/) |
| 18 | Faktör Analizi | [B18](bolumler/b18/) |
| 19 | Doğrulayıcı Faktör Analizi | [B19](bolumler/b19/) |
| 20 | Ölçme Değişmezliği | [B20](bolumler/b20/) |
| 21 | Yapısal Eşitlik Modeli | [B21](bolumler/b21/) |
| 22 | IBM SPSS Uygulamaları | [B22](bolumler/b22/) |

Kod lisansı: `uygulamalar/LICENSE`. Veri koşulları: `uygulamalar/VERI-LISANSLARI.md`.

## Güncel yürütme kaydı

22 Python analizi geçici çalışma kopyasında yürütüldü; sayısal referanslarla
karşılaştırma ve ek çoklu atama kontrolleri başarılı. R/SPSS/Amos bu teslimde
çalıştırılmadı. Sınanan paket sürümleri `requirements-tested.txt`,
karşılaştırma kapsamı ve teknik metadata istisnaları `DOGRULAMA.json` içindedir.
Bir optimizasyonun durdurma bayrağı, gradyan/amaç/kovaryans denetimlerinin
yerine kullanılmaz; kitap uygulamalarının bu iç denetimleri korunmuştur.

Bu paket kod ve materyal bütünlüğü açısından sınandı; kitabın tamamının bağımsız
bilimsel hakemliği veya R/SPSS/Amos yürütme onayı anlamına gelmez.

## Revizyon 5: Bölüm 1

Hedef parametre/tasarım görevleri ve Python'da tam tasarım varyansı ile 20.000
tekrarlı seçim eklendi. Diğer bölüm ana analizleri korunmuştur. Yeni ek modülün
R/SPSS eşdeğeri yoktur. Küçük anakütlede tam sayım testleri geçmiştir.

## Revizyon 6: Bölüm 2

Özet hedefleri, ampirik dağılım/eşik eşitsizlikleri, eşleşmiş fark grafiği ve
raporlama hassasiyeti geliştirildi. Yeni Python ek modülü ve T1–T3 görevleri
eklendi. Diğer bölüm ana analizleri korundu; yeni R/SPSS modülü yok.

## Revizyon 7: Bölüm 3

Veri sözleşmesi, atama/analiz uyumu ve gerçek A/C puanlarında birleştirme
paydaları geliştirildi. Yeni Python ek modülü, merkezleme sızıntısı kurgusu
ve T1–T3 görevleri eklendi. Mevcut çoklu atama uygulaması korundu; yeni
R/SPSS/MICE/FIML veya tahmin başarımı uygulaması yok.

## Revizyon 8: Bölüm 4

TOST eşdeğerliği, %90 aralık terslemesi, belirsiz sonuç ayrımı ve Holm aile
düzeltmesi eklendi. Sınırlar ve p ailesi öğretim içindir; klinik standart değildir.
Yeni Python ek modülü ve T1–T3 görevleri eklendi; ana test/simülasyon korundu.
Yeni R/SPSS eşdeğeri veya düzeltilmiş güven aralığı hesaplanmadı.
