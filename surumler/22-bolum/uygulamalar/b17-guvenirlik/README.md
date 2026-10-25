# Bölüm 17 — Ölçek uyarlama ve güvenirlik

## Veri kaynağı ve kapsam

Bu paket, **psych::bfi** veri kümesinin Rdatasets CSV aktarımındaki ilk 100 veri
satırının yalnızca A1–A5 ve C1–C5 sütunlarını içerir. Dokümantasyondaki tam veri
2800 kişinin 25 IPIP kişilik maddesine yanıtlarını içerir; SAPA projesinin 2010
ilkbaharındaki verileridir. Bu, John ve arkadaşlarının Big Five Inventory ölçeği
veya Türkçeye uyarlanmış bir test değildir. Buradaki sonuçlar tam 2800 kaydın
sonuçları olarak gösterilmemelidir.

- Veri tanımı ve puan anahtarı: https://www.personality-project.org/r/html/bfi.html
- Kullanılan CSV aktarımı: https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/psych/bfi.csv
- Alfa belgesi: https://www.personality-project.org/r/psych/help/alpha.html
- IPIP kullanım açıklaması: https://ipip.ori.org/newPermission.htm
- ITC uyarlama kılavuzu: https://www.intestcom.org/files/guideline_test_adaptation_2ed.pdf
- Revelle ve Condon (2019): https://doi.org/10.1037/pas0000754
- IBM RELIABILITY: https://www.ibm.com/docs/en/spss-statistics/31.0.0?topic=reference-reliability

Erişim: 5 Eylül 2026. İlk 100 satırın seçili sütunları yukarıdaki CSV'den
aktarılmıştır; değerler **kurulu `psych` paketindeki `bfi` verisiyle birebir aynıdır**.
SHA-256 özeti dosyanın sonradan değişmediğini denetler. Hiçbir yanıt üretilmemiş veya doldurulmamıştır.

`kaynak_satir` CSV başlığı hariç 1–100 sıra konumudur; `kaynak_kayit` yayımlanmış
CSV'nin satır etiketidir (ilk 61617, son 61831). Bu etiket kişi kimliği olarak
kullanılmaz. Diğer demografik sütunlar alınmamıştır. İlk 100 kayıt rastgele
örneklem değildir; Türkiye'yi, tüm SAPA katılımcılarını veya klinik grupları
temsil ettiği ileri sürülmez.

IPIP kendi maddelerinin kamu malı olduğunu açıklar. Bu açıklama başka ölçeklerin
veya her veri aktarımının lisansının aynı olduğu anlamına gelmez. Maddelerin
Türkçe karşılıkları yalnızca öğretim taslaklarıdır; uzman onayı, bilişsel görüşme,
pilot, faktör yapısı veya kültürler arası değişmezlik çalışması yapılmış değildir.

## Dosyalar ve çalıştırma

Kitap kökünde (`03-AdvancedStaticalAppTR`):

```sh
python uygulamalar/b17-guvenirlik/analiz.py
```

Mevcut numpy, pandas, scipy ve matplotlib kullanılır; sürümler `sonuclar/ozet.json`
içindedir. Ağ gerekmez. Kaynak dosyası değiştirilmez. Başka bir çalışma dizininden
betiğin yoluyla çalıştırmak da mümkündür; Python yolları betik konumuna göredir.

- `kaynak/bfi-ilk100-AC.csv`: anahtarlanmamış yanıtlar, boş hücreler NA.
- `puanlanmis_A.csv`, `puanlanmis_C.csv`: anahtarlanmış tam kayıtlar ve kaynak etiketleri.
- `sonuclar/ozet.json`: katsayılar, eksik kayıtlar, bootstrap, yöntem ve sürümler.
- `sonuclar/madde_A.csv`, `madde_C.csv`: madde–kalan, madde–toplam ve silinirse alfa.
- `sonuclar/kovaryans_*.csv`, `korelasyon_*.csv`: aynı kayıtların matrisleri.
- `../../assets_figures/b13-madde-analizi.pdf`, `b13-bootstrap.pdf`: bölüm grafikleri.
- `analiz.R`: temel R hesabı; psych zaten kuruluysa alfa karşılaştırması.
- `analiz.sps`: Python'un ürettiği tam ve anahtarlanmış kayıtlarla SPSS RELIABILITY.

R/SPSS dosyalarında çalışma dizini kitap kökü olmalıdır. R ve `psych` Python ile
aynı alfa ve madde istatistiklerini verir. R betiği paket kurmaz. SPSS betiği ikinci kez ters kodlama veya bootstrap yapmaz. R'nin aynı
tohumu Python ile aynı örnekleri üretmez; nokta hesapları karşılaştırılabilir,
bootstrap aralıklarının son basamaklarının eşit olması beklenmez.

## Sabit analiz kararları

Yanıtlar 1–6 arasındadır. A1, C4 ve C5 **belgelenmiş anahtarla** `7 - yanıt`
işleminden geçer. Korelasyon işaretine göre otomatik anahtar seçilmez.
Eksikler: A2/satır66, C1/satır63, C3/satır90. A için 99, C için 98 tam kayıt
kullanılır; on maddeyi birlikte isteyen karşı örnekte n=97'dir. Silinirse alfa
hesaplarında beş maddelik ölçeğin aynı tam kayıtları korunur. Eksikler sıfıra
çevrilmez, kişi ortalamasıyla doldurulmaz, ikili kovaryans silmesi uygulanmaz.

Alfa hem varyans hem ortalama kovaryans özdeşliğiyle; standart alfa z-puanlı
matrisle; düzeltilmiş korelasyonlar ayrı kovaryans hesabıyla doğrulanır.
Bootstrap katılımcı satırlarını bütün olarak iadeli çeker: 20000 tekrar,
A tohumu 202613, C tohumu 202614; yüzde 2.5/97.5 doğrusal nicelikleriyle percentile
aralık. BCa değildir. Sıfır toplam varyanslı tekrar olursa kod hata verir,
sessizce elemez; mevcut çalıştırmada sıfır geçersiz tekrar vardır. Bağımsız ve
aynı dağılımlı katılımcı varsayımı ile örneklem içi belirsizlik gösterilir;
seçim yanlılığı, eksiklik mekanizması veya kültürel eşdeğerlik düzeltilmez.

A: ham alfa .629588, standart alfa .651399, GA [.464423, .736637].
C: ham alfa .722610, standart alfa .731783, GA [.579608, .811465].
Anahtarlanmamış C alfası -.082651'dir; sıfıra kırpılmaz.
Maddeyi 10 ile çarpma ve sütunları aynen çoğaltma yalnızca hesap karşı
örnekleridir, yeni veri değildir. A+C toplamı geçerli tek ölçek olarak önerilmez.
Omega, test–tekrar test, değerlendiriciler arası güvenirlik ve değişmezlik için
sayısal sonuç üretilmez. Alfa eşikleri otomatik kabul/silme veya klinik karar
kuralı olarak kullanılmaz.

Kaynağın tek son LF ile normalize SHA-256 değeri:
`8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557`.
Betik son satır sonu farklılıklarını normalize eder; ayrıca gerçek dosya
baytlarının hash'ini JSON'a kaydeder. Hücre değişimi normalizasyonla gizlenmez.