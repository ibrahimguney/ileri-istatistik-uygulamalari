# Bölüm 13 — Ölçek uyarlama ve güvenirlik

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

Erişim: 5 Eylül 2026. Terminalden ağ erişimi HTTP 403 verdiği için ilk 100 satırın
seçili sütunları web üzerinden görüntülenen CSV'den yerel dosyaya aktarılmıştır.
Bu aktarım **resmî psych paketindeki değerlerle otomatik karşılaştırılmamıştır**.
Hash denetimi yalnızca arşivlenen yerel kopyanın değişmediğini gösterir; kaynakla
bağımsız doğrulama yerine geçmez. Hiçbir yanıt üretilmemiş veya doldurulmamıştır.

`kaynak_satir` CSV başlığı hariç 1–100 sıra konumudur; `kaynak_kayit` yayımlanmış
CSV'nin satır etiketidir (ilk 61617, son 61831). Bu etiket kişi kimliği olarak
kullanılmaz. Diğer demografik sütunlar alınmamıştır. İlk 100 kayıt rastgele
örneklem değildir; Türkiye'yi, tüm SAPA katılımcılarını veya klinik grupları
temsil ettiği ileri sürülmez.

IPIP kendi maddelerinin kamu malı olduğunu açıklar. Bu açıklama başka ölçeklerin
veya her veri aktarımının lisansının aynı olduğu anlamına gelmez. Maddelerin
Türkçe karşılıkları yalnızca öğretim taslaklarıdır; uzman onayı, bilişsel görüşme,
pilot, faktör yapısı veya kültürler arası değişmezlik çalışması yapılmış değildir.

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
Öğrenci betiği CRLF → LF ve tek son LF farklılıklarını normalize eder; ayrıca gerçek dosya
baytlarının hash'ini JSON'a kaydeder. Hücre değişimi normalizasyonla gizlenmez.

## Bu öğrenci kopyası
Kitabın kaynak/bfi-ilk100-AC.csv dosyası baytları değiştirilmeden kopyalanır.
Önceki kaynak erişim ve aktarım notları korunur; paketleme sırasında yeni uzak
veri veya psych paket veri karşılaştırması yapılmaz. Kaynak etiketleri ve boş
hücreler korunur; dosya özgün R nesnesinin bayt kopyası değildir.

Bölüm 3'te aynı alıntının kullanılması bağımsız bir örneklem veya tekrar çalışma
oluşturmaz. A/C iç tutarlılıkları, Türkçe ifade taslaklarının uygulanmış ve
geçerlenmiş olduğu anlamına gelmez. GOREVLER.md'deki P1 formu yalnız planlama
şablonudur. Gerçek katılımcı, uzman onayı veya görüşme yanıtı üretilmez.
Başka kaynağın GPL/CC BY lisansı bu veriye taşınmadı; depo genelinde yeni lisans atanmadı.