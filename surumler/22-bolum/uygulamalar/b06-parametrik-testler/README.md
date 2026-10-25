# Bölüm 6 — Gerçek veride üç t-testi

## Kaynak ve aktarım
R datasets paketinin `sleep` ve `ToothGrowth` verileri kullanılır. Sayısal kayıtlar
5 Eylül 2026'da R kaynak deposundaki metinden CSV'ye aktarıldı ve kurulu R
`datasets` tablolarıyla birebir aynı olduğu doğrulandı.
Değerler değiştirilmedi; kaynak_satir mevcut sırayı gösteren ek dizindir.
CSV biçimi, sayıların ondalık yazımı ve başlıklar bu paket için düzenlenmiştir;
dosyalar özgün R kaynak dosyalarının bayt kopyası değildir.

- sleep kaynak: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/sleep.R
- ToothGrowth kaynak: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/ToothGrowth.R
- Sözlükler: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/sleep.html ve https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html
- sleep kaynak çalışmaları: Cushny ve Peebles (1905), DOI 10.1113/jphysiol.1905.sp001097; Student (1908), DOI 10.2307/2331554.
- ToothGrowth: R sözlüğünde veri kaynağı Bliss (1952), The Statistics of Bioassay;
  ilişkili özgün çalışma Crampton (1947), DOI 10.1093/jn/33.5.491.

Uzak URL'ler değişebilir; bu CSV'ler ve aşağıdaki SHA-256 özetleri sabit öğretim
kopyasını tanımlar. Özgün makalelerin bireysel ham kayıtları bu paketin kapsamı
dışındadır. `--kaynak-dogrula` ağ erişimi varsa R metnindeki sayıları ve
kodlamayı ayrıştırıp karşılaştırır; dosyaları üzerine yazmaz. Kaynak biçimi değişirse
durur. Güncel değerler farklıysa eski kopyayı sessizce değiştirmeyin.

SHA-256:
- sleep.csv: adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e
- ToothGrowth.csv: 654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3

R kaynak dağıtımının GNU GPL v2 bildirimi kaynak/GPL-2.txt içinde sağlanır;
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

## Çalıştırma
Kitap kökünden:

```sh
python uygulamalar/b06-parametrik-testler/analiz.py
python uygulamalar/b06-parametrik-testler/analiz.py --kaynak-dogrula
Rscript uygulamalar/b06-parametrik-testler/analiz.R
```

İkinci komut internet gerektirir. R betiği hem yerel CSV'yi kullanır hem kurulu
R datasets tablolarıyla bütün sütunları karşılaştırır ve Python ile aynı test
sonuçlarını verir. SPSS betiği önce Python ile
üretilen uyku_esli.csv ve dis_veri.csv'yi okur; fark yönünü korur.

Çıktılar: sonuclar/ozet.json, sonuclar/cift_duyarlilik.csv, uyku_esli.csv,
dis_veri.csv; kitap assets_figures dizininde b10-uyku-eslestirme.pdf ve
b10-welch-farklar.pdf. Kaynak dosyalarının hash'leri analiz sonunda tekrar kontrol edilir.

Beklenen sonuçlar:
- Tek örneklem: t(9)=1.325710, p=.217598; GA [-.529780,2.029780], d=.419226.
- Eşli: fark=1.58, t(9)=4.062128, p=.002833; GA [.700114,2.459886], dz=1.284558.
- Yanlış bağımsız sleep analizi: p=.079394; yöntem seçimi bu p'ye göre yapılmaz.
- Doz 1 Welch: fark=5.93, t(15.357672)=4.032770, p=.001038;
  GA [2.802148,9.057852], d_pooled=1.803509.
- Doz 2 Welch: fark=−.08, p=.963852; GA [−3.798070,3.638070].

Grafik geri yükleme denetimi (6 Eylül 2026): Beklenen kaynak hash'leri LF satır
sonları ve tek son LF ile karşılaştırılır. Böylece CSV aktarımında yalnız son
satır sonunun kaybolması yanlış veri-değişikliği uyarısı üretmez. Ham bayt
hash'leri ayrıca `source_csv_sha256`, normalleştirilmiş hash'ler
`source_normalized_sha256` alanında tutulur; çalışma sonunda ham dosyaların
değişmediği tekrar sınanır. Sayısal/kategorik hücre farkları normalleştirilmez.

## Revizyon 10 — Kalibrasyon ve sağlam duyarlılık

`welch-saglamlik/` eki; n10/n30 normal sıfır modelinde Student/Welch hata
oranlarını ve gerçek doz1 verisinde %20 kırpılmış ortalama için Yuen testini
gösterir. Yuen farklı hedefi sınar; küçük p seçilmez. Ana veri ve ana analiz
korunur. Beş yeni Python testi geçti; yeni R/SPSS eşdeğeri hazırlanmadı.
