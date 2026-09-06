# Bölüm 10 — Veri, kaynak ve analiz sözleşmesi

## Kaynak ve aktarım
R datasets paketinin `sleep` ve `ToothGrowth` verileri kullanılır. Sayısal kayıtlar
5 Eylül 2026'da R kaynak deposunun tarayıcıda görünen metninden CSV'ye aktarıldı.
Değerler değiştirilmedi; kaynak_satir mevcut sırayı gösteren ek dizindir.
CSV biçimi, sayıların ondalık yazımı ve başlıklar bu paket için düzenlenmiştir;
dosyalar özgün R kaynak dosyalarının bayt kopyası değildir.

- sleep kaynak: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/sleep.R
- ToothGrowth kaynak: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/ToothGrowth.R
- Sözlükler: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/sleep.html ve https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html
- sleep kaynak çalışmaları: Cushny ve Peebles (1905), DOI 10.1113/jphysiol.1905.sp001097; Student (1908), DOI 10.2307/2331554.
- ToothGrowth: R sözlüğünde veri kaynağı Bliss (1952), The Statistics of Bioassay;
  ilişkili özgün çalışma Crampton (1947), DOI 10.1093/jn/33.5.491.

Uzak URL'ler değişebilir; bu yerel CSV'ler ve aşağıdaki hash'ler sabit öğretim
kopyasını tanımlar. Terminalde uzak erişim 403 ile engellendiğinden otomatik
kaynak karşılaştırması çalıştırılmadı. Özgün makalelerin bireysel ham kayıtları da
denetlenmedi. Tarayıcıdan aktarım, otomatik karşılaştırma ve arşiv doğrulaması
aynı şey değildir. Bu öğrenci sürümü çevrimdışı çalışır; uzak kaynak karşılaştırması içermez.
Yeni doğrulama yapılırsa sonuçları ayrıca kaydedin; eski kopyayı sessizce değiştirmeyin.

SHA-256 (CRLF → LF ve dosya sonunda tek LF ile normalleştirilmiş):
- sleep.csv: adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e
- ToothGrowth.csv: 654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3

R kaynak dağıtımının GNU GPL v2 bildirimi GPL-2.txt içinde sağlanır;
R COPYING kaydı: https://raw.githubusercontent.com/wch/r-source/trunk/COPYING .
Bu veri kopyalarına UCI'nin veya başka bir kaynağın CC BY lisansı atfedilmez.
Makalelerin şekilleri veya metinleri kopyalanmadı; grafik ve analizler bu kitapta üretildi.

## Tasarım ve değişken sözlüğü
`sleep.csv`: 20 ölçüm satırı, 10 kişi, her ID için iki group değeri.
- extra: kontrole göre uyku artışı, saat; mutlak uyku süresi değildir.
- group: ilaç koşulu 1/2; iki bağımsız hasta grubu değildir.
- ID: kaynakta eşleşmeyi sağlayan kişi kodu; yeni kimlik çıkarımı yapılmaz.
- Tek örneklem: group=1 extra değerleri, mu0=0 saat.
- Eşleştirilmiş: her ID için group2−group1, sıfıra karşı sınama.
Bunlar eski araştırmanın öğretim verileridir; uygulama sırası, körleme ve taşıma
etkileri bu kısa kopyadan denetlenmez. Sonuçlar tedavi önerisi değildir.

`ToothGrowth.csv`: 60 ayrı hayvan kaydı, 6 hücrenin her birinde 10 kayıt.
- len: odontoblast uzunluğu ölçüsü; R sözlüğü birimi açık belirtmediği için
  mikrometre varsayılmadan “kaynak ölçüm birimi” denir.
- supp: OJ portakal suyu; VC askorbik asit.
- dose: 0.5, 1, 2 mg/gün.
- Ana karşılaştırma: dose=1 içinde OJ−VC (iki ayrı grup).
- Bağımsız etkinlik: dose=2 içinde OJ−VC, yeni t-testi.
- dose=0.5 pakette tutulur ve hesaplanır; sonuç avcılığı için kullanılmaz.
Kısa sözlük randomizasyon/kafes bilgisini belgelemiyor; ayrı satır tek başına
bağımsızlığı kanıtlamaz. Tasarım sınırları raporlanır. Doz seçimi öğretim amaçlıdır,
yeni bir önkayıt iddiası değildir. Dozların tümünü sınamak çoklu test veya ortak
faktöriyel model planı gerektirir. Verilerde hiçbir satır silinmedi veya doldurulmadı.

## Yöntem ve denetimler
Bütün testler iki yönlü, alfa .05; aralıklar fark için %95 t aralıklarıdır.
Welch ana yöntemdir; Student yalnız eş varyanslı modelle karşılaştırma içindir.
Levene p-değeri yöntemler arasında otomatik anahtar değildir. Ortalama merkezli
Levene ve medyan merkezli Brown–Forsythe ayrı kaydedilir.
Etki ölçüleri: tek örneklem d=(ortalama−referans)/SS; eşli dz=ortalama fark/fark SS;
bağımsız gruplar d_pooled=fark/birleştirilmiş SS. Bunlar farklı standartlaştırıcılardır.
Bağımsız d_pooled, eş varyans varsayımının doğrulandığı iddiası değildir; ana sonuç
ham fark ve Welch aralığıdır. Burada d için güven aralığı üretilmez.

Elle formüller SciPy'nin t, serbestlik derecesi, p ve aralıklarıyla karşılaştırılır.
Eşli test ayrıca farkların tek örneklem testiyle; fark varyansı kovaryans özdeşliğiyle
kontrol edilir. Satırların karıştırılması ID tabanlı eşleşmeyi değiştirmez. İşaret
ve saat→dakika dönüşümleri kontrol edilir. Tek çifti dışarıda bırakma sonuçları
her ID için raporlanır; bu bir silme kuralı veya seçilerek raporlanacak yeni analiz değildir.
Shapiro sonuçları tanı amaçlıdır; farklarda p=.0333 sorunu metinde gizlenmez.

## Bu öğrenci kopyasında yapılan işlem
Kitabın uygulama klasöründeki iki CSV ve GPL-2.txt baytları değiştirilmeden
kopyalanır. Bu aktarımda uzaktaki kaynak yeniden doğrulanmaz. Analizlerin yönü,
örneklem seçimi ve yöntemleri korunur; yalnız dosya yolları ve çıktı dizinleri
bölümün tek başına çalışabilmesi için uyarlanır. R kaynak dağıtımının mevcut
bildirimi korunur; kitap veya bütün öğrenci deposu için yeni lisans atanmaz.

Yerel hash eşleşmesi arşivin değişmediğini gösterir; kaynak verinin hatasızlığını,
araştırma tasarımını veya temsiliyeti doğrulamaz. sleep verisinin Bölüm 4 ve 5'te
de kullanılması bağımsız tekrar çalışması değildir. Eksik doldurma, ana analizden
silme, bootstrap, permütasyon ve eşdeğerlik testi bu pakette yapılmaz.