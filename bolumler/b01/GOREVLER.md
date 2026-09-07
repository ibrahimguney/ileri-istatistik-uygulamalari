# B01 Görevler — İstatistiksel Düşünme: Sorudan Kanıta

Bu görevleri mümkün olduğunca `COZUMLER.md` dosyasına bakmadan tamamlayın.

## G1 — Analiz birimini belirleme

`veri.csv` dosyasını açın.

1. Bir satır neyi temsil ediyor?
2. `G1` ile `G3` neden iki bağımsız gözlem gibi sayılmamalıdır?
3. `kaynak_satir` alanı neden gerçek kişi kimliği değildir?

## G2 — Değişken ve ölçüm düzeyi

Aşağıdaki alanları sınıflandırın:

- `school`
- `G1`
- `G3`
- `fark_G3_G1`

Her biri için veri saklama türü ile ölçüm düzeyinin aynı kavram olup olmadığını açıklayın.

## G3 — Frekans, yüzde ve payda

`G3` için frekans ve yüzde tablosu oluşturun.

1. Yüzdelerin toplamını kontrol edin.
2. Eksik değer olsaydı hangi paydayı kullanacağınızı açıkça yazın.
3. `G3=12` ve `G3=13` değerlerinin frekanslarını karşılaştırın.

## G4 — Sistematik seçim örneği

80 kayıttan başlangıç satırı **3**, seçim aralığı **5** olacak biçimde sistematik bir seçim oluşturun.

1. Seçilen kaynak satır numaralarını yazın.
2. Kaç kayıt seçildiğini bulun.
3. Seçilen kayıtlarda `G1` ve `G3` ortalamalarını hesaplayın.
4. Bu seçimin ilk 80 kaydı temsili hale getirip getirmediğini tartışın.

## B1 — Anakütle, çerçeve ve örnek

Aşağıdaki üç ifadeyi birbirinden ayırın:

- Araştırmacının hakkında sonuç üretmek istediği hedef grup,
- Seçim yapılabilen erişilebilir kayıt listesi,
- Gerçekte analiz edilen 80 satır.

Bunları sırasıyla **anakütle**, **örnekleme çerçevesi** ve **örnek** kavramlarıyla eşleştirin. UCI alıntısının hangi kavramı tek başına garanti etmediğini açıklayın.

## B2 — Grafik seçimi

Aşağıdaki araştırma soruları için uygun grafik türünü seçin ve nedenini yazın:

1. `G3` notlarının dağılımı nasıl?
2. `G1` ile `G3` birlikte nasıl değişiyor?
3. Okul kodlarının frekansı nasıl?

Bu veri alıntısında üçüncü grafik neden çok az bilgi verir?

## B3 — Genelleme dili

Aşağıdaki cümleyi bilimsel olarak onarın:

> “Öğrencilerin yıl sonu not ortalaması 12.64'tür; dolayısıyla öğrenciler genel olarak başarılıdır.”

En az üç sorunu belirtin:

- hedef kitlenin belirsizliği,
- örnekleme/temsiliyet sorunu,
- “başarılı” ifadesinin tanımsız oluşu.

## H1 — Hatalı raporu onarma

Aşağıdaki kısa raporu eleştirin:

> “Araştırmada 160 bağımsız gözlem bulunmaktadır; çünkü 80 öğrencinin G1 ve G3 puanları ayrı ayrı analiz edilmiştir. Veriler rastgele seçildiği için sonuçlar bütün öğrencilere genellenebilir. G3 dağılımı 0'dan başlamayan bir sütun grafiği ile gösterilmiştir.”

En az dört hata bulun ve doğru ifadelerle değiştirin.

## P1 — Bir sayfalık veri tanıma dosyası

Bir sayfalık kısa bir belge hazırlayın. Belgede şu başlıklar bulunmalıdır:

1. Araştırma sorusu
2. Analiz birimi
3. Veri kaynağı
4. Değişkenler ve anlamları
5. Örnekleme/seçim biçimi
6. Eksik değer durumu
7. Uygun iki grafik
8. Genelleme sınırı
9. Yeniden üretim için kullanılan dosya ve yazılım bilgisi

Bu dosyanın amacı analiz yapmadan önce **veriyle yapılabilecek ve yapılamayacak çıkarımları** görünür hale getirmektir.
