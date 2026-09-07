# Bölüm 3 — Veri Hazırlamayı Akademik Raporlama

Bu rehber, veri hazırlama sürecini belirsiz bir “veriler temizlendi” cümlesi yerine **yeniden üretilebilir, denetlenebilir ve bilimsel olarak gerekçelendirilmiş kararlar dizisi** olarak raporlamaya yardımcı olur.

Temel zincir:

**Kaynak → Gözlem birimi → Şema → Geçerli kodlar → Eksiklik → Dönüşüm → Puanlama → Reshape → Standardizasyon → Duyarlılık → Karar günlüğü → Analize hazır veri → Akademik raporlama**

## 1. Veri kaynağını ve kapsamı belirtin

Bu bölümde `psych::bfi` gösterim verisinin ilk 100 kaydındaki A1–A5 ve C1–C5 maddeleri kullanılmaktadır.

Örnek ifade:

> Veri hazırlama uygulaması, `psych` paketindeki `bfi` gösterim verisinin yerel ilk 100 kayıtlık alıntısında bulunan A1–A5 ve C1–C5 maddeleri üzerinde yürütülmüştür. Demografik değişkenler analize aktarılmamıştır.

Bu veri John ve arkadaşlarının Big Five Inventory testi veya Türkçe uyarlama olarak adlandırılmamalıdır.

## 2. Ham verinin korunduğunu açıkça yazın

Bilimsel veri hazırlamada ham veri ile türetilmiş veri ayrılmalıdır.

Örnek ifade:

> Kaynak CSV değişmeden korunmuş; ters puanlama, puan üretimi, uzun biçim dönüşümü ve duyarlılık işlemleri yeni sütun veya türetilmiş dosyalarda gerçekleştirilmiştir.

“Veriler düzeltildi” gibi belirsiz ifadelerden kaçının.

## 3. Geçerli kodları tanımlayın

Madde yanıtları `1–6` tamsayıdır.

- boş hücre = eksik,
- `0` = geçersiz,
- `99` = geçersiz,
- `2.5` = geçersiz,
- metin = geçersiz.

Örnek ifade:

> Madde düzeyinde yalnız 1–6 arasındaki tamsayılar geçerli yanıt olarak kabul edilmiş, boş hücreler eksik değer olarak korunmuştur.

## 4. Anahtar denetimini raporlayın

`kaynak_satir` ve `kaynak_kayit` alanlarının boş olmaması ve benzersizliği kontrol edilir.

Bu kontrol özellikle:

- birleşme,
- reshape,
- satır çoğalması,
- yanlış eşleşme

risklerini azaltır.

Örnek ifade:

> Kayıt anahtarlarının boş olmaması ve benzersizliği analiz öncesinde doğrulanmıştır.

## 5. Eksikliği iki paydayla raporlayın

100 kayıt × 10 madde = `1000` hücre vardır.

Üç hücre eksiktir:

- A2 / satır 66,
- C1 / satır 63,
- C3 / satır 90.

Buna göre:

- hücre düzeyinde eksiklik = `%0.3`,
- en az bir eksiği olan kayıt = `%3`,
- on maddede ortak tam kayıt = `97`.

Örnek ifade:

> Toplam 1000 madde hücresinin üçü eksikti (%0.3); 100 kaydın üçünde en az bir eksik yanıt bulundu (%3). On maddenin tamamında gözlenen ortak kayıt sayısı 97 idi.

Bu iki yüzdeyi tek bir “eksik oranı” gibi sunmayın.

## 6. Eksik oranından mekanizma sonucu çıkarmayın

Düşük eksik oranı:

- MCAR,
- MAR,
- MNAR

mekanizmalarından hangisinin geçerli olduğunu belirlemez.

Bu bölümde MCAR testi yapılmamıştır.

Uygun ifade:

> Eksiklik oranı düşük olmakla birlikte eksik veri mekanizmasına ilişkin bir test yapılmadığından MCAR varsayımı doğrulanmış kabul edilmemiştir.

## 7. Ters puanlamayı formülüyle raporlayın

A1, C4 ve C5 için:

`x_t = 7 − x`

kullanılır.

Ham maddeler korunur.

Örnek ifade:

> A1, C4 ve C5 maddeleri 1–6 ölçeğinin uçları dikkate alınarak `7−x` dönüşümüyle yeni sütunlarda ters puanlanmış; özgün madde sütunları değiştirilmemiştir.

Eksik değerler ters puanlama sırasında eksik kalır.

## 8. Yeniden terslemeyi önleyin

`7−(7−x)=x` olduğundan önceden terslenmiş veriye aynı işlemi yeniden uygulamak ilk dönüşümü geri alır.

Bu nedenle raporda işlem zinciri açık olmalıdır.

Uygun ifade:

> Yeniden üretim her seferinde ham CSV'den başlatılmış; daha önce terslenmiş türetilmiş dosyalar yeni analiz girdisi olarak kullanılmamıştır.

## 9. Puanlama kuralını açıkça tanımlayın

### Ana analiz

5/5 puan yalnız beş maddenin tamamı gözlenmişse üretilir.

### Duyarlılık

4/5 puan en az dört gözlenen maddeyle mevcut yanıtların ortalamasıdır.

Örnek ifade:

> Ana puanlama kuralında beş maddenin tamamı gerekli tutulmuş; ayrıca öğretim amaçlı duyarlılık analizinde en az dört gözlenen maddeyle ortalama puan hesaplanmıştır.

4/5 kuralının onaylanmış ölçek kılavuzu olmadığı belirtilmelidir.

## 10. Puanların geçerli n değerlerini raporlayın

| Puan | Geçerli n | Ortalama |
|---|---:|---:|
| A 5/5 | 99 | 4.563636 |
| A 4/5 | 100 | 4.565500 |
| C 5/5 | 98 | 4.187755 |
| C 4/5 | 100 | 4.191500 |

Örnek ifade:

> Tam-madde kuralında A puanı 99, C puanı 98 kayıt için hesaplanabilirken, en az dört madde kuralında her iki puan 100 kayıt için üretilebilmiştir.

Bu fark, eksik veri kuralının analiz örneklemini değiştirdiğini görünür kılar.

## 11. Toplam ve ortalamayı ayırın

Beş tam madde için toplam ve ortalama deterministik olarak ilişkilidir:

`toplam = 5 × ortalama`.

Ancak dört madde üzerinden ortalama alınmışsa bunu beş maddelik toplam diye sunmak doğru değildir.

Örnek:

`[6,4,5,3,NA]`

için 4/5 ortalama `4.5`, fakat 5/5 puanı eksiktir.

## 12. Puan üretilemeyen kaydı silmeyin

Bir puanın eksik olması bütün kaydın veri setinden çıkarılması gerektiği anlamına gelmez.

Örneğin satır 66'da A için yalnız dört yanıt varken C için beş yanıt vardır.

Dolayısıyla farklı analizler farklı geçerli n değerlerine sahip olabilir.

## 13. Geniş–uzun dönüşümünü doğrulayın

Uzun tabloda:

- 1000 kişi–madde satırı,
- 997 gözlenen yanıt

vardır.

Eksik yanıtlar da satır yapısında korunur.

Örnek ifade:

> Veri geniş biçimden uzun biçime dönüştürüldüğünde 1000 kişi–madde satırı elde edilmiş, üç eksik yanıt eksik olarak korunmuştur. Kişi–madde anahtarının benzersizliği doğrulanmış ve tekrar geniş biçime dönüşümde özgün değerlerle eşitlik kontrol edilmiştir.

## 14. Sessiz birleştirme hatalarından kaçının

Bire bir olması gereken birleşmede yinelenen anahtar varsa satır sayısı fark edilmeden artabilir.

Bu nedenle birleştirme kardinalitesi açıkça denetlenmelidir.

Örnek ifade:

> Bire bir eşleşmesi gereken veri birleştirmelerinde anahtar kardinalitesi doğrulanmış; yinelenen anahtarların sessiz satır çoğaltmasına izin verilmemiştir.

## 15. Yinelenen pivot kayıtlarını ortalamayın

Aynı kişi–madde anahtarı iki kez varsa `pivot_table` ile otomatik ortalama almak veri problemini çözmez.

Önce yinelenmenin nedeni belirlenmelidir.

Bu, veri hazırlamanın “yazılım çalıştıysa doğrudur” anlayışından farklı olduğunu gösterir.

## 16. Standardizasyonu doğru raporlayın

A 5/5 puanı 99 kullanılabilir kayıt üzerinde örneklem standart sapmasıyla z-standardize edilmiştir.

Sonuçta:

- ortalama yaklaşık `0`,
- örneklem s `1`

olur.

Örnek ifade:

> A ana puanı kullanılabilir 99 kayıt üzerinde örneklem ortalaması ve standart sapması kullanılarak z-standardize edilmiş; standartlaştırılmış puanların ortalamasının yaklaşık 0 ve örneklem standart sapmasının 1 olduğu cebirsel olarak doğrulanmıştır.

## 17. z puanını normallik kanıtı saymayın

Standardizasyon yalnız:

`z=(x−ortalama)/s`

dönüşümüdür.

Dağılımın şeklini normal yapmak zorunda değildir.

Bu nedenle:

> “z puanları normal dağıldı çünkü ortalama 0 ve s=1 oldu.”

ifadesi yanlıştır.

## 18. Ortalama atamasının varyans etkisini gösterin

C1 için gözlenen:

- `n=99`,
- ortalama `4.454545`,
- örneklem varyansı `1.515770`.

Tek eksik değer gözlenen ortalamayla doldurulduğunda varyans:

`1.500459`

olur.

Ortalama değişmese de varyans azalır.

Örnek ifade:

> Öğretim amaçlı geçici kopyada tek eksik C1 değeri gözlenen ortalamayla doldurulduğunda ortalama korunurken örneklem varyansı 1.516'dan 1.500'e düşmüştür. Bu nedenle ortalama ataması nötr bir işlem olarak değerlendirilmemiş ve ana veriye uygulanmamıştır.

## 19. Kurgusal hata testlerini doğru etiketleyin

`99`, `2.5`, metin, boş anahtar ve yinelenen anahtar eklenen dosyalar yalnız doğrulama sistemini sınamak için oluşturulan geçici kopyalardır.

Bunlar:

> “Kaynak veride 99 kodları bulundu.”

gibi raporlanamaz.

Uygun ifade:

> Veri doğrulama kurallarının davranışı, yalnız geçici kopyalarda oluşturulan sentetik hata senaryolarıyla sınanmıştır; bu hatalar özgün verinin özelliği değildir.

## 20. Karar günlüğü kullanın

İyi bir veri hazırlama raporu yalnız son veri setini değil, kararları da belgelemelidir.

Karar günlüğünde en az:

- işlem,
- gerekçe,
- etkilenen değişken,
- ana analiz mi duyarlılık mı olduğu,
- kayıt sayısına etkisi,
- geri döndürülebilirlik,
- çıktı dosyası

bulunmalıdır.

Bu yaklaşım “hangi veri üzerinde hangi analiz yapıldı?” sorusunun sonradan yanıtlanabilmesini sağlar.

## 21. Yapılmamış analizleri eklemeyin

Bu bölümde yapılmamıştır:

- MCAR testi,
- çoklu atama,
- FIML,
- güvenirlik analizi,
- faktör analizi,
- normallik testi,
- ölçek geçerliği analizi.

Veri hazırlama işlemi bu analizlerin yerine geçmez.

## 22. Yazılım durumunu doğru belirtin

Python uygulaması bölümün referans hesaplarını üretir.

R betiği hazırlanmıştır ancak bu dağıtım hazırlanırken çalıştırılarak doğrulanmamıştır ve Python ile aynı çıktı dosyalarının tamamını üretme iddiası yoktur.

SPSS syntax veya çalıştırılmış SPSS çıktısı yoktur.

Örnek ifade:

> Referans veri hazırlama çıktıları Python uygulamasından elde edilmiştir; R uygulaması hazırlanmış ancak paket hazırlanırken çalıştırılarak doğrulanmamış, SPSS analizi yürütülmemiştir.

## 23. Kaynak ve genelleme sınırını raporlayın

Bu veri yalnız ilk 100 kayıtlık yerel bir alıntıdır.

Uzak CSV ile bu paket hazırlanırken otomatik hücre karşılaştırması yapılmamıştır.

Örnek sınırlılık ifadesi:

> Bulgular yerel ilk 100 kayıtlık öğretim alıntısının veri hazırlama özelliklerini göstermektedir; alıntı temsili örneklem veya uzak kaynakla yeniden doğrulanmış veri olarak değerlendirilmemiştir.

## 24. Örnek bütünleşik yöntem paragrafı

> Veri hazırlama işlemleri `psych::bfi` gösterim verisinin yerel ilk 100 kayıtlık A1–A5 ve C1–C5 alıntısı üzerinde yürütüldü. Ham CSV değişmeden korundu. Madde düzeyinde yalnız 1–6 tamsayılar geçerli kabul edildi ve boş hücreler eksik olarak bırakıldı. Toplam 1000 madde hücresinin üçü eksikti (%0.3); üç kayıtta en az bir eksik yanıt vardı (%3). A1, C4 ve C5 maddeleri yeni sütunlarda `7−x` ile ters puanlandı. Ana analizde yapı puanının hesaplanması için beş maddenin tamamı gerekli tutuldu; öğretim amaçlı duyarlılık analizinde en az dört maddeyle ortalama puan ayrıca hesaplandı. Bu kurallarla A ve C ana puanları sırasıyla 99 ve 98 kayıt için üretilebildi. Geniş–uzun dönüşümünde kişi–madde anahtarlarının benzersizliği ve geri dönüşümde özgün veriyle eşitlik doğrulandı. Eksik değer ataması ana veriye uygulanmadı; ortalama atamasının varyansı azaltabileceği yalnız geçici bir karşı örnekle gösterildi. MCAR, güvenirlik, faktör analizi ve normallik testleri bu veri hazırlama aşamasının parçası değildi.

## 25. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Veri kaynağı ve ilk 100 kayıt kapsamı belirtilmiş mi?
- Veri BFI/Türkçe uyarlama diye yanlış adlandırılmamış mı?
- Ham CSV'nin korunması açıklanmış mı?
- Geçerli 1–6 kodları tanımlanmış mı?
- Boş değer sıfır yapılmamış mı?
- Anahtar benzersizliği denetlenmiş mi?
- Eksik hücre ve eksik kayıt paydaları ayrı mı?
- Düşük eksik oranı MCAR kanıtı sayılmamış mı?
- Ters puanlanan maddeler ve `7−x` kuralı belirtilmiş mi?
- Ham sütunların üzerine yazılmamış mı?
- Yeniden tersleme yapılmamış mı?
- 5/5 ana ve 4/5 duyarlılık puanları ayrılmış mı?
- 4/5 kuralı onaylanmış ölçek kılavuzu diye sunulmamış mı?
- Her puanın geçerli n değeri verilmiş mi?
- Ortalama ile toplam karıştırılmamış mı?
- Puanı eksik kayıt otomatik silinmemiş mi?
- Geniş–uzun dönüşümde eksikler korunmuş mu?
- Kişi–madde anahtarı benzersiz mi?
- Birleşme kardinalitesi denetlenmiş mi?
- Yinelenen pivot kayıtları sessizce ortalanmamış mı?
- z-standardizasyon normallik kanıtı sayılmamış mı?
- Ortalama ataması ana veriye uygulanmamış mı?
- Kurgusal hata testleri gerçek veri hatası diye sunulmamış mı?
- Ana analiz ile duyarlılık işlemleri ayrılmış mı?
- Karar günlüğü tutulmuş mu?
- Yapılmamış MCAR/güvenirlik/faktör analizleri eklenmemiş mi?
- R/SPSS çalıştırma durumu doğru belirtilmiş mi?
- Yerel hash uzak kaynak doğrulaması veya temsiliyet kanıtı sayılmamış mı?

## Son mesaj

Veri hazırlamanın temel bilimsel ilkesi şudur:

**Ham veriyi koru → kuralları açıkla → hatayı sessizce düzeltme → eksikliği görünür tut → dönüşümü doğrula → puan paydasını belirt → duyarlılığı ana analizden ayır → her kararı kaydet → yapılmayan işlemleri uydurma → analize hazır verinin nasıl üretildiğini yeniden üretilebilir biçimde raporla.**

İyi veri hazırlama, veriyi “daha güzel” hale getirmek değil; **ham veriden analitik veriye giden yolu denetlenebilir hale getirmektir.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.