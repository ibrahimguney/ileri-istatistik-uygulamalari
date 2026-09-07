# B01 — İstatistiksel Düşünme: Sorudan Kanıta

Bu bölüm, *İleri İstatistik Uygulamaları* kitabının ilk bölümüne eşlik eden öğrenci çalışma ortamıdır. Amaç, istatistiğe bir formül listesi olarak değil; **araştırma sorusundan veriye, veriden kanıta ve kanıttan dengeli yoruma uzanan bir karar süreci** olarak yaklaşmaktır.

## Öğrenme hedefleri

Bu çalışmayı tamamladığınızda:

- anakütle, örnekleme çerçevesi, örnek ve istatistik kavramlarını ayırabilecek,
- analiz birimini ve değişkenleri doğru tanımlayabilecek,
- veri türü ile ölçüm düzeyinin aynı şey olmadığını açıklayabilecek,
- basit rastgele, sistematik ve olasılıksız seçim mantıklarını birbirinden ayırabilecek,
- frekans ve yüzdelerde doğru paydayı kullanabilecek,
- değişken yapısına uygun grafik seçebilecek,
- örnekleme hatası ile yanlılığı birbirine karıştırmayacak,
- araştırma tasarımının izin verdiği sonuç dilini belirleyebilecek,
- bir veri analizini yeniden üretilebilir biçimde belgeleyebileceksiniz.

## 1.2 İstatistiksel Düşünme Süreci

Bu bölümde temel zincir şöyledir:

**Araştırma sorusu → hedef anakütle → gözlem/analiz birimi → veri üretim veya seçim mekanizması → değişkenler → özetleme/görselleştirme → istatistiksel kanıt → sınırlılıklar → raporlama**

Bir analizin teknik olarak doğru hesaplanması, bu zincirin önceki halkaları yanlış kurulmuşsa bilimsel olarak yeterli değildir.

## Kullanılan veri

Uygulamada `veri.csv` dosyasındaki 80 kayıt kullanılır. Dosya, UCI Student Performance veri setinin Portekizce dersi kaynağından seçilmiş sınırlı bir alıntıdır. Aynı 80 kayıt B02'de de betimsel istatistik uygulamalarında kullanılır; B01'de amaç hesaplamayı derinleştirmek değil, **verinin neyi temsil ettiğini ve nasıl okunması gerektiğini** öğrenmektir.

Önemli sınırlar:

- Bu 80 kayıt rastgele veya temsili bir örneklem değildir.
- Kayıtların tamamı kaynakta `GP` okul kodundadır.
- `kaynak_satir` gerçek kişi kimliği değildir.
- `G1` ve `G3` aynı kayıt içindeki iki farklı nottur; iki bağımsız kişi gibi ele alınamaz.
- Bu veri Türkiye'deki öğrencileri temsil etmez.

Ayrıntılar için önce [`VERI.md`](VERI.md) dosyasını okuyun.

## Çalışma sırası

1. [`VERI.md`](VERI.md) — veri kaynağı, birim, değişken ve kullanım sınırları.
2. [`GOREVLER.md`](GOREVLER.md) — rehberli ve bağımsız görevler.
3. [`calisma.ipynb`](calisma.ipynb) — veri tanıma, frekans, sistematik örnekleme ve grafik seçimi uygulaması.
4. [`analiz.py`](analiz.py) — yeniden üretilebilir teknik referans analizi.
5. [`RAPORLAMA.md`](RAPORLAMA.md) — sonuçları uygun bilimsel dille yazma rehberi.
6. [`COZUMLER.md`](COZUMLER.md) ve [`beklenen.json`](beklenen.json) — çalışmanız bittikten sonra kontrol için.

> Önce kendi kararınızı verin; sonra referans çözüme bakın.

## Bu bölümde özellikle dikkat edin

### Bir satır her zaman bağımsız birim değildir

Veri tablosundaki satır sayısı otomatik olarak bağımsız gözlem sayısını tanımlamaz. Tekrarlı ölçümler, kümelenmiş veriler ve eşleştirilmiş tasarımlar analiz birimini değiştirir.

### Aynı sayı bağlama göre parametre veya istatistik olabilir

Bir değer bütün hedef anakütleden hesaplanıyorsa parametre; anakütleden seçilmiş bir örnekten hesaplanıyorsa istatistiktir. Sayının matematiksel biçimi değil, **hangi veri kümesinden üretildiği** belirleyicidir.

### Rastgelelik yanlılığı otomatik olarak yok etmez

Rastgele örnekleme örnekleme hatasını yönetmeye yardımcı olur; kötü tanımlanmış çerçeve, yanıtlamama veya ölçüm hatası gibi sistematik sorunları tek başına çözmez.

### Grafik, araştırma sorusunun parçasıdır

Kategorik bir değişken için çubuk grafik, tek nicel değişken için histogram veya nokta grafiği, iki nicel değişken için saçılım grafiği gibi seçimler veri yapısına göre yapılmalıdır. Eksen kesmeleri ve ölçek seçimleri görsel yorumu yanıltmamalıdır.

## Teknik referans

`analiz.py` şu kontrolleri üretir:

- satır ve eksik hücre sayısı,
- okul kodu düzeyleri,
- G1 ve G3 için temel aralık ve merkez özetleri,
- G3 frekans ve yüzde tablosu,
- başlangıç satırı 3 ve aralık 5 olacak biçimde örnek bir sistematik seçim,
- G3 için basit dağılım grafiği.

Bu sistematik seçim yalnız **öğretim örneğidir**; mevcut 80 kaydı temsili örnekleme dönüştürmez.

## Akademik yorum sınırı

Bu bölümün verisinden yapılabilecek güvenli ifade, incelenen **80 kayda** ilişkindir. Kaynak dosyanın tüm öğrencilerine, başka okullara, ülkelere veya hedef popülasyonlara doğrudan genelleme yapılmamalıdır.

## Çıktı politikası

- `sonuclar/` içindeki dosyalar teknik referans/doğrulama çıktılarıdır.
- `grafikler/` yeniden üretilebilir çalışma çıktısıdır ve varsayılan olarak Git tarafından izlenmez.
- Kendi ödev, tablo, grafik ve raporlarınızı kişisel çalışma alanınızda tutun.

Depo genelindeki kurallar için kök dizindeki `CIKTI_POLITIKASI.md` dosyasına bakın.
