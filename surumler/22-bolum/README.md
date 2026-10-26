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

## Revizyon 9: Bölüm 5

TOST için örneklem planı ve rastgele güven aralığı genişliği olasılığı eklendi.
Normal/eşit varyanslı varsayımsal modelin sayısal sonuçları 100.000 çekilişle
denetlendi; yeni kişi/pilot verisi yok. Ana güç analizi korundu. Ek yalnız Python;
R/SPSS/G*Power, belirsiz sigma üzerinden veya kayıpla ortak güç hesabı yok.

## Revizyon 10: Bölüm 6

Welch/Student normal model kalibrasyonu ve gerçek doz1'de Yuen kırpılmış konum
duyarlılığı eklendi. Her kurguda200.000 çekiliş; bu bir Tip I hata denetimidir.
Yuen farklı hedefi sınar; küçük p seçilmez. Ana analizler/ham veriler korunur.
Yeni ek yalnız Python'da sınandı; R/SPSS karşılığı veya klinik genelleme yoktur.

## Revizyon 11: Bölüm 8

Eksik izlemde aynı karma modelin karşılaştırılması, normal Wald sınırları ve yaş ailesinde Holm/Bonferroni eklendi. Ham veriler ve eski ana sonuçlar korunur. Tek maske yanlılığı kanıtlamaz; MNAR duyarlılığı ve küçük örneklem sd düzeltmesi uygulanmadı.

## Revizyon 12: Bölüm 9

Ortak tersinir dönüşüm, iki puanlık Bonferroni/Hotelling aralıkları ve iki grup için asimptotik heterojen Wald duyarlılığı eklendi. Pillai/Box M, seçilmiş ayırma yönü ve çokluk sınırları netleştirildi. Ana veriler/sonuçlar korundu; yeni ek yalnız Python, altı eğitim grubu için sağlam çözüm değildir.

## Revizyon 13: Bölüm 10

Üstünlük A için grup-içi hayvan bootstrap ve yaklaşık BM, eşli fark için koşullu işaret testi/medyan sıra aralığı eklendi. Eski ana sonuçlar korundu. Yeni ek yalnız Python; küçük örneklem kapsaması, BCa ve öğrencilendirilmiş permütasyon yapılmadı.

## Revizyon 14: Bölüm 11

Aynı öğrenci satırlarını koruyan Pearson/Spearman bootstrap aralıkları, katsayı farkı ve ilk kayıt etkisi eklendi. Sıfır korelasyon/bağımsızlık, dönüşüm ve uyum ayrımı netleştirildi. Eski ana sonuçlar korunur; yeni ek yalnız Python. Küme-bootstrap, BCa ve kapsama simülasyonu yapılmadı.

## Revizyon 15: Bölüm 12

OLS/klasik t-F/HC3 koşulları ayrıldı. Ayrı eğitim40/kalibrasyon20/kontrol20 split conformal öğretimi eklendi; model ve kontrol yanıtları karıştırılmaz. Yeni ek yalnız Python, tek okulun sıralı verisi değiştirilebilirlik ve garantili kapsama kanıtı değildir. Ana60 kayıtlık sonuçlar korunur.

## Revizyon 16: Bölüm 13

Profil olasılığı GA ve tam kovaryansla olasılık farkı eklendi. Aynı AUC/.50 sınıflarda farklı Brier/log-kayıp, toplu ortalama/kalibrasyon ve kontrol etiketleriyle seçim sınırları açıklandı. Yeni ek yalnız Python; kalibrasyon eğrisi, performans aralıkları ve dış doğrulama yok. Eski ana sonuçlar korunur.

## Revizyon 17: Bölüm 14

Aynı doz desteğinde sabit hedef dağılımları, model grup ortalamaları ve kontrast aralıkları eklendi. Ortak modelde aynı kontrast/aile1; ayrı ve hücrede üç hedef/aile3. Yeni ek yalnız Python; ağırlık belirsizliği ve nedensel taşıma yok. Ön-test/değişim tartışması ayrı teorik modeldir; dozdan değişim üretilmez.

## Revizyon 18: Bölüm 15

Aynı simülasyonda yapısal hata korelasyonu duyarlılığı, ayrı düzenleyicilik yanıtında noktasal JN ve iki-parametre eşzamanlı bant eklendi. Yol çarpımı/özdeşlik/bootstrap nedensel tanımlama testi değildir. Yeni ek yalnız Python; rho eğrisi aralıkları ve HC3/küme bandı yok. Eski üretim/5000 bootstrap korunur.

## Revizyon 19: Bölüm 16

HSB verisinde hedef ortalamalar, eşit olmayan okul büyüklükleri ve bilinen/yeni okul tahmini eklendi. Koşullu aralıklar parametre belirsizliğini içermez; okul sıralaması veya ulusal temsil iddiası yok. Yeni ek yalnız Python; eski veriler ve ana analizler korunur.

## Revizyon 20: Bölüm 17

Ortak97 IPIP kaydında eşleşmiş alfa farkı ve ayrı bilinen parametreli model örnekleri eklendi. Gerçek veriye omega modeli uydurulmadı; SEM öğretim sınırı klinik karar eşiği değildir. Yeni ek yalnız Python; önceki99/98 kişi ana analizleri ve kaynak veriler korunur.

## Revizyon 21: Bölüm 18

Keşif yarısında dört faktörlü PAF doğrudan denendi; bu yordam/başlangıçta Heywood ile yakınsamadı. İki faktörlü modelde regresyon/Bartlett puanları ve sabit model altında koşullu belirsizlik eklendi. Yarım B yanıtları okunmadı; bireysel tanı/kapsama doğrulanmadı. Yeni ek yalnız Python; eski veri/bölme ve ana analizler korunur.

## Revizyon 22: Bölüm 19

Aynı incelenmiş B yarısında ham/standart toplam payları ve tam beklenen parametre kovaryansıyla CR/AVE delta aralıkları eklendi. Her sabit modelin iki AVE−phi² farkı ayrı Bonferroni ailesidir; bütün rapor için ortak kapsama iddiası yok. Normal kuramlı; sağlam/ordinal veya yeni doğrulama değil. Yeni ek yalnız Python; eski ana analizler korunur.

## Revizyon 23: Bölüm 20

Aynı B yarısında sabit çıpa kümeleri için gizil fark aralıkları, A1+A2 duyarlılık senaryosu, referans birimi dönüşümü ve model ortalama farkının bileşenleri eklendi. Seçim sonrası koşullu normal kuramlı çıkarımdır; tüm arama belirsizliği veya yeni doğrulama değildir. Ana veri/model/arama korunur; yeni ek yalnız Python.

## Revizyon 24: Bölüm 21

Aynı B yarısında K→A1/A2 MIMIC senaryoları ve aynı kovaryansı veren yapısal artık-rho ailesi eklendi. Ana dolaylı çarpım .190 iken rho=.3 varsayımında aynı uyumla .030 olur; bu varsayım veriden seçilemez. Yeni senaryolara bootstrap/aralık raporlanmaz; eski ana veri/kod/2000 bootstrap korunur. Yeni ek yalnız Python; nedensel etki veya yeni doğrulama iddiası yok.
