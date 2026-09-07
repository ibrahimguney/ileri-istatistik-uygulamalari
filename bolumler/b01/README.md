# B01 — İstatistiksel Düşünme: Sorudan Kanıta

Bu bölüm, *İleri İstatistik Uygulamaları* kitabının ilk bölümüne eşlik eden öğrenci çalışma ortamıdır. Amaç, istatistiğe bir formül listesi olarak değil; **araştırma sorusundan veriye, veriden kanıta ve kanıttan dengeli yoruma uzanan bir karar süreci** olarak yaklaşmaktır.

## Öğrenme hedefleri

Bu çalışmayı tamamladığınızda:

- araştırma sorusu, hedef anakütle, örnekleme çerçevesi ve eldeki kayıtları birbirinden ayırabilecek,
- gözlem birimi, değişken, ölçüm ve satır sayısını doğru tanımlayabilecek,
- sayısal kod ile sayısal ölçümü; nominal, ordinal, aralık ve oran düzeylerini ayırt edebilecek,
- basit rastgele, sistematik, tabakalı ve küme örneklemenin seçim mantığını açıklayabilecek,
- frekans ve yüzdeyi doğru payda üzerinden hesaplayabilecek,
- veri türüne uygun grafik seçebilecek ve kaynak sınırlarını belirten kısa bir rapor yazabileceksiniz.

## 1.2 İstatistiksel Düşünme Süreci

Bu bölümde temel zincir şöyledir:

**Araştırma sorusu → hedef anakütle → örnekleme çerçevesi → gözlem/analiz birimi → veri üretim veya seçim mekanizması → değişkenler → özetleme/görselleştirme → istatistiksel kanıt → sınırlılıklar → raporlama**

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

## Kitaptaki sistematik örnekleme örneği

Kitapta yalnız örnekleme öğretimi için eldeki 80 kayıt kapalı bir öğretim anakütlesi olarak ele alınır. Burada:

- `N = 80`,
- `n = 10`,
- sistematik aralık `j = N/n = 8`,
- gösterim için sabit başlangıç `r = 3`.

Bu nedenle seçilen kayıt sıraları:

`3, 11, 19, 27, 35, 43, 51, 59, 67, 75`

ve bu 10 kaydın `G3` ortalaması **12.2**'dir.

> Başlangıç 3 burada öğretim amacıyla sabitlenmiştir; rastgele çekildiği iddia edilmez. Gerçek bir sistematik örnekleme uygulamasında başlangıcın nasıl rastgele seçildiği kaydedilmelidir.

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

Veri tablosundaki satır sayısı otomatik olarak bağımsız gözlem sayısını tanımlamaz. Bu dosya uzun biçime çevrilirse 160 satır oluşabilir; fakat aynı 80 öğrenci kaydı korunur. Aynı öğrencinin G1 ve G3 notlarını 160 bağımsız öğrenci gibi analiz etmek doğru değildir.

### Aynı sayı bağlama göre parametre veya istatistik olabilir

Eldeki 80 kayıt yalnız öğretim alıştırması için kapalı bir anakütle olarak tanımlandığında `G3` toplamı 1011 ve bu çerçevenin ortalaması `1011/80 = 12.6375` bir parametre rolündedir. Bu 80 kayıttan seçilen 10 kaydın ortalaması ise bu çerçeveye yönelik bir örneklem istatistiğidir. Ancak 12.6375, bütün Portekiz öğrencilerinin ya da kaynak dosyadaki 649 kaydın bilinen parametresi değildir.

### Rastgelelik yanlılığı otomatik olarak yok etmez

Rastgele örnekleme örnekleme hatasını yönetmeye yardımcı olur; kötü tanımlanmış çerçeve, yanıtlamama veya ölçüm hatası gibi sistematik sorunları tek başına çözmez.

### Grafik, araştırma sorusunun parçasıdır

Kategorik bir değişken için çubuk grafik, tek nicel değişken için histogram veya nokta grafiği, iki nicel değişken için saçılım grafiği gibi seçimler veri yapısına göre yapılmalıdır. Eksen kesmeleri ve ölçek seçimleri görsel yorumu yanıltmamalıdır.

## Teknik referans

`analiz.py` şu kontrolleri üretmelidir:

- satır ve eksik hücre sayısı,
- okul kodu düzeyleri,
- G1 ve G3 için temel aralık ve merkez özetleri,
- G3 frekans ve yüzde tablosu,
- kitapla uyumlu olarak başlangıç 3 ve aralık 8 ile sistematik seçim,
- seçilen 10 kaydın G3 ortalaması 12.2,
- G3 için basit dağılım grafiği.

Bu sistematik seçim yalnız **öğretim örneğidir**; mevcut 80 kaydı temsili örnekleme dönüştürmez.

## Akademik yorum sınırı

Bu bölümün verisinden yapılabilecek güvenli ifade, incelenen **80 kayda** ilişkindir. Kaynak dosyanın tüm öğrencilerine, başka okullara, ülkelere veya hedef popülasyonlara doğrudan genelleme yapılmamalıdır.

## Çıktı politikası

- `sonuclar/` içindeki dosyalar teknik referans/doğrulama çıktılarıdır.
- `grafikler/` yeniden üretilebilir çalışma çıktısıdır ve varsayılan olarak Git tarafından izlenmez.
- Kendi ödev, tablo, grafik ve raporlarınızı kişisel çalışma alanınızda tutun.

Depo genelindeki kurallar için kök dizindeki `CIKTI_POLITIKASI.md` dosyasına bakın.
