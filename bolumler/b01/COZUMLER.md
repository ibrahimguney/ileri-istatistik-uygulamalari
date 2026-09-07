# B01 Referans Çözümler

Bu dosyayı görevleri tamamladıktan sonra kontrol amacıyla kullanın.

## G1 — Analiz birimi

1. Her satır, veri alıntısındaki bir öğrenci kaydını temsil eder.
2. `G1` ve `G3` aynı kayda ait iki farklı nottur; iki bağımsız öğrenci değildir.
3. `kaynak_satir` yalnız alıntı içindeki kaynak sıra numarasıdır; gerçek kişi kimliği olarak yorumlanmaz.

## G2 — Değişkenler

- `school`: kategorik / nominal.
- `G1`: nicel not değişkeni.
- `G3`: nicel not değişkeni.
- `fark_G3_G1`: iki notun farkından türetilen nicel değişken.

Bilgisayarda bir değişkenin tamsayı, metin veya ondalık olarak saklanması ile bilimsel ölçüm düzeyi aynı kavram değildir.

## G3 — G3 frekansları

80 kayıt içinde G3 frekansları:

| G3 | Frekans | Yüzde |
|---:|---:|---:|
| 7 | 1 | 1.25 |
| 9 | 1 | 1.25 |
| 10 | 8 | 10.00 |
| 11 | 15 | 18.75 |
| 12 | 16 | 20.00 |
| 13 | 15 | 18.75 |
| 14 | 9 | 11.25 |
| 15 | 6 | 7.50 |
| 16 | 6 | 7.50 |
| 17 | 3 | 3.75 |

Toplam yüzde 100'dür. Bu dosyada eksik G3 olmadığı için payda 80'dir. G3=12 en sık görülen değerdir (16 kayıt); G3=13 ise 15 kayıtta görülür.

## G4 — Sistematik seçim

Başlangıç 3 ve aralık 5 kullanıldığında seçilen kaynak satırları:

`3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78`

- Seçilen kayıt sayısı: **16**
- Seçilen kayıtlarda G1 ortalaması: **12.5625**
- Seçilen kayıtlarda G3 ortalaması: **12.8125**

Bu seçim, sistematik örnekleme algoritmasını gösterir. İlk 80 kaydın sıralı ve temsili olmayan bir alıntı olması gerçeğini değiştirmez.

## B1 — Anakütle, çerçeve ve örnek

- **Anakütle:** araştırmacının sonuç üretmek istediği hedef grup.
- **Örnekleme çerçevesi:** seçim yapılabilen erişilebilir birim listesi.
- **Örnek:** gerçekte analize alınan birimler.

Bu depodaki 80 kayıt bir analiz örneğidir; ancak hedef anakütleyi temsil eden olasılıklı bir örnekleme çerçevesinden seçildiği iddia edilemez.

## B2 — Grafik seçimi

1. G3 dağılımı: histogram veya nokta grafiği.
2. G1–G3 ilişkisi: saçılım grafiği.
3. `school` frekansı: kategorik yapı için çubuk grafik uygundur; fakat bu alıntıda yalnız `GP` olduğu için grafik karşılaştırma bilgisi taşımaz.

## B3 — Düzeltilmiş genelleme dili

Daha uygun ifade:

> İncelenen 80 kayıtta yıl sonu notu G3'ün ortalaması 12.64'tür. Kayıtlar temsili bir olasılık örneklemi olmadığından bu sonuç daha geniş öğrenci gruplarına doğrudan genellenmemelidir. Ayrıca “başarı” yorumu yapılabilmesi için önceden tanımlanmış bir başarı ölçütüne ihtiyaç vardır.

## H1 — Hatalar

Örnek hatalar:

1. 80 öğrencinin G1 ve G3 değerleri 160 bağımsız gözlem değildir; aynı kişideki ölçümlerdir.
2. Kullanılan 80 kayıt rastgele seçilmiş temsili örneklem olarak belgelenmemiştir.
3. Bu nedenle bütün öğrencilere genelleme yapılamaz.
4. G3 nicel bir değişkendir; dağılımını göstermek için histogram/nokta grafiği daha uygundur.
5. Eksenin kesilmesi görsel farkı olduğundan büyük gösterebilir ve açıkça gerekçelendirilmelidir.

## P1 — Beklenen yaklaşım

Bir sayfalık veri tanıma dosyasında şu fikirler görünür olmalıdır:

- araştırma sorusunun veriyle cevaplanabilir olması,
- birimin açık tanımı,
- kaynağın ve lisansın belirtilmesi,
- değişkenlerin anlamlarının yazılması,
- örnekleme/seçim sınırının açıklanması,
- eksik değer kontrolü,
- değişken yapısına uygun grafik seçimi,
- genelleme sınırı,
- kullanılan veri ve kod dosyalarıyla yeniden üretilebilirlik.
