# Bölüm 10 — Parametrik Test Sonuçlarını Akademik Raporlama

Bu rehber, Bölüm 10'daki tek örneklem, eşli örneklemler ve bağımsız iki örneklem Welch t testi sonuçlarının bilimsel bir raporda doğru biçimde sunulmasına yardımcı olur.

Temel ilke şudur:

**Önce araştırma tasarımı ve karşılaştırmanın yönü tanımlanır; sonra test sonucu raporlanır.**

## 1. Her testte önce tasarımı belirtin

Bir t testi sonucunu yalnızca `t`, `p` ve “anlamlı/anlamsız” sözcükleriyle raporlamayın. En azından şu bilgiler görünür olmalıdır:

- bağımsız analiz birimi,
- örneklem büyüklüğü,
- karşılaştırmanın yönü,
- ölçüm birimi,
- kullanılan t testi türü,
- ortalama veya ortalama fark,
- %95 güven aralığı,
- t istatistiği ve serbestlik derecesi,
- p değeri,
- uygun olduğunda etki büyüklüğü,
- önemli varsayım/tanı ve tasarım sınırlılıkları.

## 2. Tek örneklem t testini raporlayın

Koşul 1 artışları 0 saatlik referans değere karşı sınanmaktadır.

Sonuçlar:

- `n = 10`,
- ortalama = `0.75` saat,
- `SD = 1.789`,
- `SE = 0.566`,
- `t(9) = 1.326`,
- `p = .218`,
- %95 GA `[-0.530, 2.030]` saat,
- `d = 0.419`.

Örnek raporlama:

> Koşul 1'deki artışın 0 saatlik referans değerden farklı olup olmadığı iki yönlü tek örneklem t testiyle incelenmiştir. On kişinin ortalama artışı 0.75 saat (`SD = 1.79`) olarak bulunmuştur. Ortalama fark istatistiksel olarak anlamlı değildir, `t(9) = 1.33`, `p = .218`, %95 GA `[-0.53, 2.03]`. Standartlaştırılmış fark yaklaşık `d = 0.42`'dir.

## 3. “Anlamlı değil” sonucunu sıfır etki olarak yazmayın

Yanlış ifade:

> `p > .05` olduğundan koşulun hiçbir etkisi yoktur.

Daha uygun ifade:

> Bu örneklem ve model altında 0 saatlik referans değerden farklılık için yeterli istatistiksel kanıt elde edilmemiştir; güven aralığı hem negatif hem pozitif ortalama farklarla uyumludur.

H0'ın reddedilememesi:

- etkinin tam sıfır olduğunu,
- iki koşulun eşdeğer olduğunu,
- pratik olarak fark bulunmadığını

tek başına kanıtlamaz.

## 4. Eşli t testini raporlayın

Aynı 10 kişinin koşul 2 ve koşul 1 ölçümleri ID üzerinden eşleştirilmiştir. Fark yönü:

`koşul 2 − koşul 1`

olarak tanımlanmıştır.

Sonuçlar:

- `n = 10` tam çift,
- ortalama fark = `1.58` saat,
- farkların `SD = 1.230`,
- `SE = 0.389`,
- `t(9) = 4.062`,
- `p = .002833`,
- %95 GA `[0.700, 2.460]` saat,
- `dz = 1.285`.

Örnek raporlama:

> Aynı 10 kişinin iki koşuldaki ölçümleri eşleştirilerek koşul 2−koşul 1 farkı analiz edilmiştir. Ortalama kişi içi fark 1.58 saat (`SD_fark = 1.23`) olarak bulunmuştur. Normal fark modeli altında bu fark 0'dan istatistiksel olarak farklıdır, `t(9) = 4.06`, `p = .0028`, %95 GA `[0.70, 2.46]`. Eşli ölçümler için standartlaştırılmış fark `dz = 1.28`'dir.

## 5. Eşli tasarımda n değerini doğru yazın

Veri dosyasında 20 ölçüm bulunmasına rağmen eşli testte:

`n = 10`

kullanılır; çünkü bağımsız analiz birimi 10 kişidir ve her kişi iki kez ölçülmüştür.

Yanlış ifade:

> 20 ölçüm bulunduğundan 20 bağımsız katılımcı analiz edilmiştir.

Doğru yaklaşım:

> Yirmi ölçüm, 10 kişiye ait 10 tam eşleşmiş çift oluşturmaktadır.

## 6. Normallik tanısını görünür tutun

Eşli t testinde ilgili normallik varsayımı iki ham koşulun ayrı ayrı normal olmasından çok **kişi içi farkların dağılımıyla** ilgilidir.

Bu örnekte farklar için Shapiro sonucu yaklaşık:

`p = .0333`

ve Q–Q grafiğinde üst kuyruk açısından kaygı bulunmaktadır.

Bu nedenle raporda ana sonucu tamamen yok saymak veya otomatik gözlem silmek yerine tanı sınırlılığını görünür biçimde belirtin:

> Örneklem küçük olduğundan farkların dağılımı ayrıca incelenmiştir. Shapiro–Wilk sonucu ve Q–Q grafiğinin üst kuyruğu normallik açısından kaygı göstermiştir; bu nedenle eşli t testi sonucu bu model sınırlılığıyla birlikte değerlendirilmiştir. Ana analizden otomatik kayıt silinmemiştir.

## 7. Welch bağımsız örneklemler testini raporlayın

Doz 1 düzeyinde karşılaştırma yönü:

`OJ − VC`

olarak tanımlanmıştır.

Her grupta 10 kayıt bulunmaktadır.

Sonuçlar:

- ortalama fark = `5.93` kaynak birimi,
- `t = 4.033`,
- Welch `df = 15.358`,
- `p = .001038`,
- %95 GA `[2.802, 9.058]`,
- `d_pooled = 1.804`.

Örnek raporlama:

> Doz 1 düzeyinde OJ ve VC grupları bağımsız iki örneklem için Welch t testiyle karşılaştırılmıştır. OJ−VC ortalama farkı 5.93 kaynak birimi olarak bulunmuş ve farkın %95 güven aralığı `[2.80, 9.06]` olmuştur, `t(15.36) = 4.03`, `p = .0010`. Pooled standart sapmayla hesaplanan standartlaştırılmış fark `d = 1.80`'dir.

Buradaki `d_pooled`, etkiyi standartlaştırmak için kullanılan bir ölçüdür; ana Welch testini Student t testine dönüştürmez.

## 8. Welch ve Student sonuçlarını ayırın

Bu örnekte her iki grupta da `n = 10` olduğu için Student ve Welch yöntemlerinin standart hata ve t değerleri aynı olabilir. Ancak serbestlik dereceleri farklı olduğundan p değerleri ve güven aralıkları farklılaşabilir.

Eşit grup büyüklüğü:

> varyansların eşit olduğunun kanıtı değildir.

Bu nedenle ana yöntem olarak Welch testi korunmuştur.

Ortalama merkezli Levene `p ≈ .149` ve medyan merkezli Brown–Forsythe `p ≈ .212` sonuçlarını “varyanslar kesin eşittir” biçiminde yorumlamayın.

## 9. Doz 2 sonucunu eşdeğerlik olarak yorumlamayın

Doz 2 için:

- OJ−VC farkı = `-0.08`,
- `p = .963852`,
- %95 GA `[-3.798, 3.638]`.

Uygun raporlama:

> Doz 2 düzeyindeki OJ−VC karşılaştırmasında ortalama fark -0.08 olarak bulunmuş ve %95 güven aralığı hem negatif hem pozitif farkları içermiştir (`p = .964`). Bu sonuç grupların eşdeğer olduğunu kanıtlamaz; eşdeğerlik için önceden tanımlanmış bağlamsal tolerans sınırları ve uygun bir eşdeğerlik testi gerekir.

Doz 2 ayrıca doz 1 modelinin “dış doğrulaması” değildir.

## 10. Birim dönüşümünü doğru yorumlayın

Koşul 2−koşul 1 ortalama farkı:

- saat cinsinden `1.58`,
- dakika cinsinden `94.8`

olur.

Saatten dakikaya geçildiğinde:

- ortalama fark ×60,
- SD ×60,
- SE ×60,
- güven aralığı uçları ×60,

olur; fakat:

- t değişmez,
- p değişmez,
- `dz` değişmez.

Bu, test istatistiğinin ölçüm biriminin keyfî ölçek değişimine karşı değişmezliğini gösterir.

## 11. Fark yönü ters çevrilirse ne olur?

`koşul 2 − koşul 1` yerine `koşul 1 − koşul 2` kullanılırsa:

- ortalama farkın işareti değişir,
- t'nin işareti değişir,
- `dz` işareti değişir,
- iki yönlü p değeri değişmez,
- güven aralığı `[-üst, -alt]` biçiminde dönüşür.

Bu nedenle raporda fark yönünü açıkça yazmak zorunludur.

## 12. Duyarlılık analizini sonuç seçmek için kullanmayın

Her bir eşleşmiş çift sırayla çıkarıldığında ortalama fark yaklaşık `1.244–1.756` saat aralığında değişmektedir.

ID=9 çıkarıldığında:

- ortalama fark ≈ `1.244`,
- `p ≈ .000477`,
- %95 GA ≈ `[0.737, 1.752]`.

Bu durum ID=9'un otomatik olarak silinmesi gerektiği anlamına gelmez.

Uygun ifade:

> Tek-çift dışarıda bırakma analizi, tahminin bireysel kayıtlara duyarlılığını değerlendirmek amacıyla kullanılmıştır. Sonuç seçmek veya en küçük p değerini elde etmek amacıyla kayıt silinmemiştir.

Daha küçük p değeri otomatik olarak daha büyük etki anlamına gelmez; hem tahmin hem standart hata değişebilir.

## 13. Güven aralığını bireysel sonuç aralığı olarak sunmayın

Örneğin eşli testteki:

`[0.700, 2.460]`

aralığı **ortalama kişi içi farkın** %95 güven aralığıdır.

Bu aralık:

- bireylerin %95'inin farkını,
- hastaların %95'inin yararını,
- yeni bir kişinin tahmin aralığını

göstermez.

## 14. Çoklu doz sonuçlarında p seçimi yapmayın

Doz 0.5, 1 ve 2 karşılaştırmaları incelendiğinde yalnızca en küçük p değerini seçerek raporlamak uygun değildir. Birden fazla dozun ortak çıkarımı ayrı bir çoklu test veya modelleme planı gerektirir.

Doz 1 ve doz 2 için ayrı testler, resmi bir doz × uygulama etkileşim testinin yerine geçmez.

## 15. Örnek bütünleşik sonuç paragrafı

> Tarihsel R `datasets` kaynaklarından hazırlanmış yerel veriler kullanılmıştır. Uyku verisinde aynı kişilere ait ölçümler ID üzerinden eşleştirilmiş ve 10 tam çift için koşul 2−koşul 1 farkı analiz edilmiştir. Ortalama kişi içi fark 1.58 saat olarak bulunmuş; normal fark modeli altında `t(9) = 4.06`, `p = .0028`, %95 GA `[0.70, 2.46]` elde edilmiştir (`dz = 1.28`). Küçük örneklemde farkların Shapiro–Wilk sonucu ve Q–Q grafiğinin üst kuyruğu normallik açısından kaygı gösterdiğinden sonuç bu sınırlılıkla birlikte değerlendirilmiş ve tanıya bakılarak kayıt silinmemiştir. Ayrı ToothGrowth uygulamasında doz 1 düzeyindeki 10 OJ ve 10 VC kaydı Welch t testiyle karşılaştırılmış; OJ−VC ortalama farkı 5.93 kaynak birimi olarak bulunmuştur, `t(15.36) = 4.03`, `p = .0010`, %95 GA `[2.80, 9.06]`. Bu öğretim analizleri özgün deney tasarımının bağımsız doğrulaması, eşdeğerlik kanıtı veya tedavi önerisi olarak yorumlanmamıştır.

## 16. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce şunları kontrol edin:

- Her araştırma sorusu ayrı kurulmuş mu?
- Bağımsız analiz birimi doğru tanımlanmış mı?
- Eşli testte `n=10` tam çift olarak verilmiş mi?
- Fark yönü açıkça belirtilmiş mi?
- Ölçüm birimi yazılmış mı?
- Uygun t testi türü belirtilmiş mi?
- Ortalama/fark, t, df, p ve %95 GA verilmiş mi?
- Uygun etki büyüklüğü ve standartlaştırıcı kullanılmış mı?
- `p>.05` sıfır etki veya eşdeğerlik kanıtı olarak sunulmamış mı?
- Shapiro/Q–Q ve varyans tanıları mekanik seçim kuralı gibi kullanılmamış mı?
- Tanı sonuçları gizlenmemiş mi?
- Duyarlılık analizi otomatik silme veya p seçme amacıyla kullanılmamış mı?
- Güven aralığı bireysel sonuç aralığı olarak yorumlanmamış mı?
- Çoklu doz incelemesinin çokluk sınırı belirtilmiş mi?
- Tarihsel öğretim verisinden tedavi önerisi çıkarılmamış mı?
- R/SPSS çalıştırılmadıysa çalıştırılmış gibi raporlanmamış mı?

## Son mesaj

Parametrik testlerde temel düşünce zinciri şöyledir:

**Araştırma sorusu → Tasarım → Bağımsız birim → Fark yönü → Test seçimi → Tahmin → Güven aralığı → Etki büyüklüğü → Tanı → Duyarlılık → Yorum → Sınırlılık → Akademik raporlama**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.