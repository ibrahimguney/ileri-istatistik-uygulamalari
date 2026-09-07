# Bölüm 13 — Ölçek Uyarlama ve Güvenirliği Akademik Raporlama

Bu rehber, Bölüm 13'teki iç tutarlılık ve madde analizlerinin bilimsel bir raporda doğru biçimde sunulmasına yardımcı olur. Aynı zamanda **güvenirlik analizi ile gerçek bir dilsel/kültürel ölçek uyarlama çalışmasının birbirine karıştırılmasını önlemeyi** amaçlar.

Temel düşünce zinciri:

**Kaynak → hedef puan → puanlama anahtarı → eksik veri kuralı → analiz örneklemi → güvenirlik katsayısı → madde analizi → belirsizlik → içerik kararı → uyarlama kanıtı → kullanım sınırı**

şeklindedir.

## 1. Önce çalışmanın ne olmadığını belirtin

Bu bölümde `psych::bfi` kaynağından alınan ilk 100 kaydın A1–A5 ve C1–C5 maddeleri yeniden analiz edilmektedir.

Bu çalışma:

- yeni Türkçe ölçek geliştirme,
- doğrulanmış Türkçe uyarlama,
- hedef grupta pilot çalışma,
- yapı geçerliği çalışması,
- ölçme değişmezliği analizi

değildir.

Örnek yöntem ifadesi:

> İç tutarlılık hesapları `psych::bfi` kaynağından alınmış yerel ilk 100 kayıt alıntısında yürütülmüştür. Analiz öğretim amaçlı bir yeniden analizdir; örneklem rastgele veya temsili kabul edilmemiş ve sonuçlar Türkçe uyarlama kanıtı olarak yorumlanmamıştır.

## 2. Puanlama anahtarını açıkça raporlayın

Yanıt aralığı `1–6`'dır. Belgelenmiş anahtara göre:

- A1,
- C4,
- C5

maddeleri bir kez `7−x` ile ters puanlanmıştır.

Örnek ifade:

> Maddeler 1–6 aralığında puanlanmış, belgelenmiş anahtar doğrultusunda A1, C4 ve C5 maddeleri `7−x` dönüşümüyle bir kez ters puanlanmıştır. Anahtar analiz sonucuna göre değiştirilmemiştir.

Daha yüksek alfa elde etmek amacıyla veriye bakarak ters anahtar seçmek uygun değildir.

## 3. Eksik veri kuralını ve n'yi raporlayın

Yerel ilk 100 kayıtta:

- A2'de bir eksik → A analizi `n=99`,
- C1 ve C3'te iki farklı eksik → C analizi `n=98`,
- ortak on madde → `n=97`.

Eksik değerler sıfır veya ortalama ile doldurulmamıştır.

Örnek ifade:

> A maddeleri için tam kayıt kuralıyla 99, C maddeleri için 98 gözlem kullanılmıştır. Eksik yanıtlar geçerli bir ölçek puanı olarak değerlendirilmemiş ve sıfır ya da ortalama ile doldurulmamıştır.

Madde silme analizinde aynı kişileri koruyun; aksi durumda alfa değişiminin ne kadarının maddeye, ne kadarının örneklem değişimine ait olduğu belirsizleşir.

## 4. A maddeleri için ham ve standart alfayı ayırın

A kümesinde:

- `k=5`,
- madde varyansları toplamı = `9.130076`,
- toplam puan varyansı = `18.395176`,
- ham alfa = `.629588`,
- ortalama maddeler arası `r=.272051`,
- standart alfa = `.651399`.

Örnek raporlama:

> Beş A maddesi için 99 tam kayıt üzerinden ham Cronbach alfa `.630`, standartlaştırılmış alfa `.651` ve ortalama maddeler arası korelasyon `.272` olarak hesaplanmıştır.

Ham ve standart alfa aynı katsayı değildir. Ham alfa maddelerin ölçek ve varyanslarından etkilenirken standart alfa korelasyon matrisi üzerinden hesaplanır.

## 5. Ters anahtar duyarlılığını doğru yorumlayın

A1 ters çevrilmeden ham alfa:

`.437554`

olmaktadır.

Bu sonuç belgelenmiş anahtarın puanlama açısından önemli olduğunu gösterir. Ancak:

> “Alfayı yükselttiği için A1 ters çevrildi”

şeklinde raporlamayın.

Doğru sıra **önce madde anlamı ve belgelenmiş anahtar, sonra analiz** olmalıdır.

## 6. Madde–kalan ile madde–toplam korelasyonunu ayırın

A1 için:

- madde–kalan `r=.198701`,
- düzeltilmemiş madde–toplam `r=.513648`.

Düzeltilmemiş toplam puan A1'in kendisini içerdiği için bu iki katsayı doğrudan aynı kavram değildir.

Örnek raporlama:

> A1'in madde–kalan korelasyonu `.199` iken maddenin kendisini de içeren düzeltilmemiş toplam puanla korelasyonu `.514`'tür. Bu nedenle ikinci katsayı madde–kalan korelasyonu olarak yorumlanmamıştır.

## 7. “Silinirse alfa”yı otomatik madde eleme kuralı yapmayın

A4 aynı 99 kişi korunarak çıkarıldığında alfa:

`.675706`

olmaktadır. Beş maddelik alfa `.629588` olduğundan artış yaklaşık:

`.046118`

kadardır.

Örnek raporlama:

> A4 çıkarıldığında, aynı 99 gözlem korunarak hesaplanan alfa `.676`'ya yükselmiştir. Beş maddelik katsayıya göre yaklaşık `.046`'lık bu sayısal artış otomatik madde silme ölçütü olarak değerlendirilmemiş; madde içeriği ve hedef yapının kapsamı ayrıca dikkate alınmıştır.

Bu iki bağımlı alfa tahmininin farkı için bu pakette istatistiksel test yapılmamıştır.

## 8. A bootstrap aralığını doğru raporlayın

A için:

- 20000 tekrar,
- katılımcı satırlarının birlikte iadeli örneklenmesi,
- tohum `202613`,
- %95 persentil GA `[.464423,.736637]`.

Örnek raporlama:

> A maddelerinin ham alfa katsayısındaki örneklem içi belirsizlik, katılımcıların beş maddelik satırlarının birlikte iadeli örneklendiği 20000 tekrarlı bootstrap ile incelenmiştir. Tohum 202613 kullanılarak elde edilen %95 persentil güven aralığı `[.464,.737]`'dir.

Bu aralık BCa değildir. Ayrıca bootstrap:

- rastgele olmayan ilk-100 seçimini düzeltmez,
- temsiliyet sağlamaz,
- kültürel eşdeğerlik kanıtlamaz,
- eksik veri mekanizmasını çözmez.

## 9. C maddelerini ayrı puan olarak raporlayın

C4 ve C5 bir kez ters puanlandıktan sonra C kümesinde:

- `n=98`,
- ham alfa `.722610`,
- standart alfa `.731783`,
- ortalama maddeler arası `r=.353029`.

Örnek raporlama:

> Beş C maddesi için C4 ve C5 belgelenmiş anahtar doğrultusunda ters puanlanmış ve 98 tam kayıt analiz edilmiştir. Ham Cronbach alfa `.723`, standartlaştırılmış alfa `.732` ve ortalama maddeler arası korelasyon `.353` olarak bulunmuştur.

## 10. Negatif alfayı gizlemeyin

C4 ve C5 ters anahtarlanmadan önce ham alfa:

`−.082651`

olmaktadır.

Bu sonuç sıfıra kırpılmamalı veya rapordan çıkarılmamalıdır.

Uygun ifade:

> Belgelenmiş ters anahtar uygulanmadan önce C maddelerinde negatif alfa elde edilmiştir (`α=−.083`). Bu örnekte sonuç puan yönünün kontrol edilmesi gerektiğini göstermiştir; ancak genel olarak her negatif alfa otomatik olarak ters kodlama hatası anlamına gelmez.

## 11. C madde analizini içerikle birlikte değerlendirin

| Madde | Madde–kalan r | Aynı kişilerde silinirse alfa |
|---|---:|---:|
| C1 | .545 | .654 |
| C2 | .502 | .668 |
| C3 | .513 | .664 |
| C4 | .494 | .671 |
| C5 | .388 | .723 |

C5 silindiğinde alfa yaklaşık `.000837` artmaktadır.

Bu kadar küçük bir sayısal kazanç:

- maddenin içerik değerini,
- yapı kapsamını,
- dilsel anlamını

otomatik olarak geçersiz kılmaz.

Madde kararı yalnız alfa optimizasyonu değildir.

## 12. C bootstrap aralığını raporlayın

C için:

- 20000 tekrar,
- tohum `202614`,
- %95 persentil GA `[.579608,.811465]`.

Örnek raporlama:

> C maddelerinde 20000 katılımcı-satırı bootstrap tekrarıyla elde edilen ham alfa için %95 persentil güven aralığı `[.580,.811]` olmuştur.

Aralığın `.70` değerini kapsaması veya katsayının `.70` civarında olması otomatik kabul/ret kuralı olarak kullanılmamalıdır.

## 13. Alfa eşiğini uyarlama kanıtı olarak sunmayın

Şu ifade yanlıştır:

> “Alfa .70'i geçtiği için ölçek Türkçeye uyarlanmıştır.”

Cronbach alfa belirli bir puanın belirli verideki iç tutarlılığına ilişkin bir özettir. Tek başına:

- içerik geçerliği,
- yapı geçerliği,
- dilsel eşdeğerlik,
- kültürel eşdeğerlik,
- ölçme değişmezliği,
- test–tekrar test güvenirliği,
- kullanım uygunluğu

kanıtı değildir.

## 14. Madde çoğaltma karşı örneğini doğru kullanın

A maddelerinin birebir iki kez eklenmesi alfayı yaklaşık:

`.835372`

düzeyine çıkarabilmektedir.

Fakat bağımsız yeni bilgi veya yeni madde içeriği eklenmemiştir.

Bu örnek, alfa katsayısının yalnızca yüksek olmasının ölçme kalitesini garanti etmediğini öğretmek içindir.

## 15. Ham ve standart alfa farkını karşı örnekle açıklayın

A'nın ilk maddesini 10 ile çarpmak ham alfayı yaklaşık:

`.145256`

düzeyine değiştirirken korelasyon matrisi ve standart alfa değişmez.

Bu yapay işlem ham arşive uygulanacak bir veri dönüşümü değildir; ham ve standart alfa arasındaki ölçek duyarlılığı farkını öğretmek için kullanılan karşı örnektir.

## 16. A+C toplamını geçerli yeni ölçek olarak sunmayın

Ortak 97 kayıtta A+C on maddesi için alfa:

`.727369`

hesaplanabilmektedir.

Ancak bir katsayının hesaplanabilir olması, maddelerin tek boyutlu ve geçerli bir toplam puan oluşturduğu anlamına gelmez.

Uygun ifade:

> A ve C maddelerinin ortak 97 kayıtta tek bir alfa katsayısının hesaplanabilmesi, bu on maddenin kuramsal veya ampirik olarak geçerli tek bir ölçek oluşturduğunu göstermemektedir.

## 17. Omega hakkında yapılmamış analiz üretmeyin

Bu pakette omega hesaplanmamıştır.

Omega için uygun ölçüm modelinin ve varsayımların değerlendirilmesi gerekir. Bu nedenle rapora tahmini omega değeri eklemeyin ve “alfa düşükse omega kullanılır” gibi otomatik bir yöntem değiştirme kuralı oluşturmayın.

## 18. Dilsel uyarlama taslağını araştırma sonucu gibi sunmayın

A4 anlamı için öğretim amacıyla iki olası Türkçe ifade taslağı düşünülebilir:

- “Çocukları severim.”
- “Çocuklara karşı sevgi duyarım.”

Bunlar **onaylanmış çeviriler değildir**.

Gerçek bir uyarlamada uzman incelemesi ve hedef grupta yanıt sürecinin araştırılması gerekir. Örneğin bilişsel görüşmelerde katılımcıya ifadenin kendi sözcükleriyle anlamı, hangi durumları düşündüğü ve 1–6 yanıtını nasıl seçtiği sorulabilir.

Gerçekte yapılmamış görüşme alıntısı, uzman adı veya pilot sonucu rapora eklenmemelidir.

## 19. Uyarlama kanıt zincirini raporlayın

Gerçek bir ölçek uyarlama projesinde araştırma amacına bağlı olarak şu kanıt alanları birbirinden ayrılmalıdır:

1. kaynak ve kullanım koşulları,
2. dilsel taslaklar,
3. uzman incelemesi,
4. bilişsel görüşmeler,
5. hedef grupta pilot,
6. faktör yapısı,
7. hedef puan için güvenirlik,
8. gerektiğinde değişmezlik/eşdeğerlik,
9. kullanım ve raporlama sınırları.

Bu bölüm yalnız bu zincirin bazı **puanlama ve iç tutarlılık** bileşenlerini sayısal olarak göstermektedir.

## 20. Örnek bütünleşik rapor paragrafı

> `psych::bfi` kaynağından alınmış yerel ilk 100 kayıt alıntısında beş C maddesinin iç tutarlılığı incelenmiştir. Belgelenmiş anahtara göre C4 ve C5 maddeleri bir kez `7−x` ile ters puanlanmış, eksik yanıtlar doldurulmadan tam kayıt kuralıyla `n=98` kullanılmıştır. Ham Cronbach alfa `.723`, standartlaştırılmış alfa `.732` ve ortalama maddeler arası korelasyon `.353` olarak bulunmuştur. Katılımcıların bütün madde satırlarının birlikte örneklendiği 20000 tekrarlı bootstrap sonucunda ham alfa için %95 persentil güven aralığı `[.580,.811]` elde edilmiştir. C5 çıkarıldığında alfa yalnız yaklaşık `.001` artmış olduğundan madde silme kararı yalnız katsayı optimizasyonuna dayandırılmamıştır. Bulgular seçilmiş yerel kayıtlardaki iç tutarlılık analizine aittir; Türkçe uyarlama, yapı geçerliği, ölçme değişmezliği veya klinik kullanım kanıtı olarak yorumlanmamıştır.

## 21. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce şunları kontrol edin:

- Veri kaynağı ve ilk-100 seçim sınırı belirtilmiş mi?
- Örneklemin rastgele/temsili olmadığı açıklanmış mı?
- Yanıt aralığı ve ters anahtar açık mı?
- Ters kodlama yalnız belgelenmiş anahtara göre yapılmış mı?
- Eksik veri kuralı ve analiz n'si belirtilmiş mi?
- Madde silme karşılaştırmalarında aynı kişiler korunmuş mu?
- Ham alfa ile standart alfa ayrılmış mı?
- Madde–kalan ile düzeltilmemiş madde–toplam ayrılmış mı?
- “Silinirse alfa” otomatik madde eleme kuralı yapılmamış mı?
- Bootstrap'ın satır düzeyinde yapıldığı belirtilmiş mi?
- Tekrar sayısı, tohum ve persentil aralık türü raporlanmış mı?
- Bootstrap temsiliyet veya kültürel eşdeğerlik çözümü olarak sunulmamış mı?
- Negatif alfa gizlenmemiş mi?
- `.70` eşiği geçerlik veya uyarlama kanıtı olarak sunulmamış mı?
- Madde çoğaltmanın yükselttiği alfa yeni kanıt sayılmamış mı?
- A+C katsayısı yeni tek ölçek kanıtı olarak yorumlanmamış mı?
- Bu pakette hesaplanmayan omega, test–tekrar test, faktör yapısı veya değişmezlik sonuçları uydurulmamış mı?
- Türkçe madde taslakları onaylanmış çeviri olarak sunulmamış mı?
- Yapılmış analiz ile gelecekte yapılması planlanan uyarlama kanıtı açıkça ayrılmış mı?
- R/SPSS çalıştırılmadıysa çalıştırılmış gibi raporlanmamış mı?

## Son mesaj

Ölçek çalışmalarında temel düşünce zinciri şöyledir:

**Yapı ve kullanım amacı → Madde içeriği → Dilsel anlam → Puanlama → Eksik veri → Güvenirlik → Madde analizi → Belirsizlik → Yapı kanıtı → Değişmezlik → Kullanım sınırı → Akademik raporlama**

Yüksek bir alfa katsayısı bu zincirin tamamının yerine geçmez.

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.