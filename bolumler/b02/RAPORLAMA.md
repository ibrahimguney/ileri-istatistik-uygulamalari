# Bölüm 2 — Betimsel İstatistikleri Akademik Raporlama

Bu rehber, Bölüm 2'de hesaplanan betimsel istatistiklerin bilimsel bir raporda doğru ve ölçülü biçimde sunulmasına yardımcı olur.

Temel raporlama zinciri:

**Veri kaynağı → Gözlem birimi → Değişkenler → Hesap tanımları → Dağılım → Eşleşmiş ölçümler → Grafik → Duyarlılık → Yorum sınırı → Akademik raporlama**

## 1. Veri kaynağı ve kapsamı başta belirtin

Analiz UCI Student Performance arşivinden alınmış yerel 80 kayıtlık bir alıntıya dayanmaktadır.

Örnek ifade:

> Betimsel analizler, UCI Student Performance veri setinin Portekizce dersi kaynağından alınmış yerel 80 kayıtlık alıntı üzerinde yürütülmüştür. Analizde birinci dönem notu (`G1`) ve yıl sonu notu (`G3`) kullanılmıştır.

Bu 80 kayıt rastgele veya temsili örneklem olarak sunulmamalıdır.

## 2. Gözlem birimini doğru raporlayın

Her satır aynı kaydın G1 ve G3 ölçümlerini birlikte içerir.

Dolayısıyla:

- 80 bağımsız kayıt vardır,
- 160 bağımsız kişi yoktur.

Örnek ifade:

> G1 ve G3 aynı 80 kayda ait eşleşmiş ölçümlerdir; iki not sütunu ayrı bireyler olarak değerlendirilmemiştir.

## 3. Geçerli sıfırı eksik değer olarak sunmayın

İlk kayıtta:

- `G1=0`,
- `G3=11`.

Kaynakta sıfır geçerli not olduğundan ana analizde korunur.

Uygun ifade:

> Veri setinde eksik hücre bulunmamaktadır; ilk kayıttaki G1=0 değeri geçerli kaynak değeri olarak korunmuştur.

## 4. Hesap sözleşmesini belirtin

Betimsel sonuçların yeniden üretilebilmesi için kullanılan tanımlar raporda gerektiği kadar açıklanmalıdır.

Bu bölümde:

- varyans ve kovaryans için `n−1`,
- çeyrekler için NumPy `linear` / R `type=7`,
- kutu grafiği için `1.5×IQR`,
- MAD için ölçeklenmemiş medyan mutlak sapma

kullanılmıştır.

`n−1` kullanmak veri setini temsili örnekleme dönüştürmez.

## 5. G3'ün temel özetini raporlayın

G3 için:

- `n=80`,
- toplam `1011`,
- ortalama `12.6375`,
- örneklem varyansı `4.107437`,
- standart sapma `2.026681`.

Örnek akademik ifade:

> Seksen kaydın yıl sonu notu ortalaması `12.64`, standart sapması `2.03` olarak bulunmuştur (`n=80`).

Genellikle toplam ve kareli sapmalar toplamı ana metinde zorunlu değildir; yeniden üretim veya öğretim amacı varsa tablo/ek bölümde verilebilir.

## 6. n−1 ve n varyanslarını birbirine karıştırmayın

G3 için:

- `n−1` varyansı = `4.107437`,
- `n` bölenli kapalı-çerçeve varyansı = `4.056094`.

İki değerin farklı olması hesap hatası değildir.

Uygun açıklama:

> Ana betimsel raporda örneklem varyansı `n−1` böleniyle hesaplanmış; aynı 80 kayıt kapalı bir çerçeve olarak ele alındığında `n` bölenli varyans ayrıca gösterilmiştir.

## 7. Çeyrek yöntemini gerektiğinde belirtin

G1 için ana type-7 sonuçları:

- `Q1=11`,
- `Q3=13.25`,
- `IQR=2.25`.

Örnek ifade:

> G1 dağılımında type-7 tanımıyla birinci ve üçüncü çeyrekler sırasıyla `11.00` ve `13.25`, IQR ise `2.25` olarak hesaplandı.

Çeyrek tanımı özellikle farklı yazılımlarla yeniden üretim yapılacaksa önemlidir.

## 8. Tarama sınırı ile bıyığı ayırın

G1 için:

- alt tarama sınırı `7.625`,
- üst tarama sınırı `16.625`,
- alt bıyık `8`,
- üst bıyık `16`.

Tarama sınırları teorik eşiklerdir. Bıyıklar ise bu sınırlar içinde kalan gözlenen uç değerlerdir.

Bunları aynı sayı gibi raporlamayın.

## 9. İşaretlenen gözlemleri “hatalı veri” diye adlandırmayın

Type-7 kutu grafiği kuralıyla kaynak sıraları:

`1, 16, 48, 61`

işaretlenir.

Uygun ifade:

> Kutu grafiği kuralı dört kaydı inceleme için işaretlemiştir; bu işaretler veri hatası veya otomatik dışlama ölçütü olarak yorumlanmamıştır.

## 10. Çeyrek yöntemi duyarlılığını açıklayın

Yarı-medyan yaklaşımında:

- `Q3=13.5`,
- `IQR=2.5`,
- üst sınır `17.25`

olur ve yalnız sıfır not işaretlenir.

Bu sonuç, farklı tanımların uç-gözlem işaretlerini değiştirebildiğini gösterir.

Uygun ifade:

> İşaretlenen kayıtların çeyrek hesaplama yöntemine duyarlı olduğu görüldüğünden kutu grafiği işaretleri mutlak veri-silme kuralı olarak kullanılmamıştır.

## 11. Alt grup ortalamalarını doğru birleştirin

G3 ortalamaları:

- ilk 60 kayıt: `12.783333`,
- son 20 kayıt: `12.200000`.

Kayıt sayılarıyla ağırlıklı birleşim:

`12.6375`.

Basit iki-ortalama ortalaması:

`12.491667`.

Alt grupların büyüklükleri eşit olmadığı için bütün veri ortalaması basit ortalamayla bulunmaz.

Buradaki ağırlıklar örnekleme ağırlığı değildir.

## 12. Korelasyonu bağlamıyla raporlayın

G1 ve G3 için:

- kovaryans `3.456646`,
- korelasyon `r=.702586`.

Örnek ifade:

> Birinci dönem ve yıl sonu notları arasında pozitif bir doğrusal ilişki gözlendi (`r=.703`, `n=80`).

Bu bölümde hipotez testi yapılmadığı için korelasyona p değeri eklemeyin.

Ayrıca:

> “G1, G3'ün yükselmesine neden oldu.”

biçiminde nedensel ifade kullanmayın.

## 13. Fark puanlarını eşleşmiş yapı içinde raporlayın

`D=G3−G1` için:

- ortalama `.4625`,
- varyans `3.087184`,
- standart sapma `1.757038`.

Örnek ifade:

> Eşleşmiş kayıtlar için G3−G1 farkının ortalaması `.46` puan, standart sapması `1.76` puan olarak bulundu.

Bu betimsel özet bir hipotez testi değildir.

## 14. Ortalama değişimi bireysel değişimle karıştırmayın

80 kaydın:

- 32'sinde artış,
- 31'inde eşitlik,
- 17'sinde azalış

vardır.

Dolayısıyla:

> “Ortalama arttığı için herkesin notu arttı.”

yanlıştır.

Daha doğru ifade:

> Ortalama fark pozitif olmakla birlikte bireysel değişim yönleri heterojendir; 17 kayıtta G3, G1'den düşüktür.

## 15. Fark varyansı özdeşliğini yeniden üretim kontrolü olarak kullanın

Eşleşmiş iki değişken için:

`Var(G3−G1)=Var(G3)+Var(G1)−2Cov(G1,G3)`.

Bu özdeşlik aynı kayıtlar ve aynı bölen kullanıldığında hesapların iç tutarlılığını denetlemek için kullanılabilir.

Bu bir nedensellik testi değildir.

## 16. Konum ve ölçek dönüşümlerini doğru yorumlayın

G3'e `10` eklenirse:

- ortalama 10 artar,
- standart sapma değişmez.

G3 `5` ile çarpılırsa:

- ortalama 5 katına,
- standart sapma 5 katına çıkar.

Bu özellikler öğrencinin konum ve ölçek ölçülerini ayırmasına yardımcı olur.

## 17. CV konusunda ölçülü olun

CV sabit eklemeye karşı değişir, pozitif ölçeklemeye karşı değişmez.

Not puanlarında sıfırın mutlak oran ölçeği anlamı tartışmalı olduğundan CV'yi:

> “öğrencilerin göreli yetenek değişkenliği”

şeklinde yorumlamak uygun değildir.

## 18. Duyarlılık analizini ana analizden ayırın

İlk kayıt yalnız ayrı bir duyarlılık kopyasında dışlandığında:

- `n=79`,
- G1 ortalaması `12.329114`,
- G1 s `2.011005`,
- G1/G3 korelasyonu `.793762`.

Ana korelasyon `.702586`'dır.

Örnek ifade:

> İlk kaydın dışlandığı duyarlılık analizinde korelasyon `.794`'e yükselmiştir; bu değişim kaydın özeti etkilediğini göstermekle birlikte kaydın hatalı olduğu veya ana analizden silinmesi gerektiği biçiminde yorumlanmamıştır.

## 19. Yapılmamış çıkarımsal analizleri eklemeyin

Bu bölümde:

- güven aralığı,
- normallik testi,
- bootstrap,
- hipotez testi

uygulanmamıştır.

Dolayısıyla rapora uydurma p değerleri veya güven aralıkları eklenmemelidir.

## 20. Veri kaynağı sınırlılığını belirtin

Bu yerel dosya UCI kaynağının bütün 649 kaydını içermez; ilk 80 kayıtlık bir alıntıdır ve bu paketin hazırlanması sırasında uzak dosyayla yeniden hücre eşleştirmesi yapılmamıştır.

Uygun sınırlılık ifadesi:

> Bulgular yerel 80 kayıtlık öğretim alıntısının betimsel özetleridir; rastgele/temsili örnekleme veya uzak kaynakla yeniden doğrulama iddiası taşımamaktadır.

## 21. Örnek bütünleşik rapor

> UCI Student Performance veri setinin Portekizce dersi kaynağından alınmış yerel 80 kayıtlık alıntı betimsel olarak incelendi. G1 ve G3 aynı kayıtlara ait eşleşmiş notlar olarak değerlendirildi ve ilk kayıttaki G1=0 geçerli kaynak değeri olarak korundu. G3 ortalaması `12.64` ve standart sapması `2.03` idi (`n=80`). G1 için type-7 çeyrek tanımıyla `Q1=11.00`, `Q3=13.25` ve `IQR=2.25` bulundu; kutu grafiği dört kaydı inceleme için işaretledi, ancak bu kayıtlar otomatik olarak silinmedi. G1 ile G3 arasında pozitif ilişki vardı (`r=.703`); bu ilişki nedensel olarak yorumlanmadı ve bölüm kapsamında hipotez testi yapılmadı. G3−G1 farkının ortalaması `.46` puan ve standart sapması `1.76` puan olmakla birlikte 32 kayıtta artış, 31 kayıtta eşitlik ve 17 kayıtta azalış gözlendi. İlk kaydın dışlandığı ayrı duyarlılık analizinde korelasyon `.794` oldu; bu değişim veri-silme gerekçesi olarak kullanılmadı. Bulgular yalnız yerel 80 kayıtlık öğretim alıntısının betimsel özetleridir.

## 22. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Veri kaynağı belirtilmiş mi?
- Analiz kapsamının 80 kayıt olduğu yazılmış mı?
- 80 kayıt 160 bağımsız kişi gibi sayılmamış mı?
- G1=0 geçerli değer olarak korunmuş mu?
- Eksik hücre olmadığı doğru belirtilmiş mi?
- Varyans böleni gerektiğinde açıklanmış mı?
- `n−1` temsiliyet kanıtı sayılmamış mı?
- Çeyrek yöntemi belirtilmiş mi?
- IQR sınırı ile bıyık ucu ayrılmış mı?
- Kutu grafiği işaretleri otomatik silme nedeni sayılmamış mı?
- Farklı çeyrek tanımının duyarlılığı görünür mü?
- Alt grup ortalamaları doğru ağırlıklandırılmış mı?
- Kayıt sayısı ağırlıkları örnekleme ağırlığı diye sunulmamış mı?
- Korelasyon nedensel yorumlanmamış mı?
- Yapılmamış korelasyon p değeri eklenmemiş mi?
- Fark puanı eşleşmiş yapı içinde hesaplanmış mı?
- Ortalama artış herkesin artışı diye yorumlanmamış mı?
- CV aşırı yorumlanmamış mı?
- Ana analiz ve duyarlılık analizi ayrılmış mı?
- Duyarlılık sonucu otomatik silme kararı üretmemiş mi?
- Yapılmamış güven aralığı/bootstrap/hipotez testi raporlanmamış mı?
- Yerel hash uzak kaynak doğrulaması veya temsiliyet kanıtı sayılmamış mı?
- R çalıştırılmadıysa R sonucu varmış gibi yazılmamış mı?

## Son mesaj

Betimsel istatistiğin amacı veriyi birkaç sayıya indirgemek değildir. Güçlü bir betimsel analiz:

**Veriyi tanır → gözlem birimini belirler → özetleri tanımlar → dağılımı görselleştirir → eşleşmiş yapıyı korur → uç gözlemleri sorgular → duyarlılığı inceler → yorum sınırını açıklar → akademik olarak raporlar.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.