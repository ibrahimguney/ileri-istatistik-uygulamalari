# Bölüm 4 — Hipotez Testini Akademik Raporlama

Bu rehber, hipotez testini yalnız “anlamlı/anlamsız” kararı olarak değil; **tasarım, tahmin, belirsizlik, etki büyüklüğü ve yorum sınırlarıyla birlikte** raporlamaya yardımcı olur.

Temel zincir:

**Araştırma sorusu → Tasarım → Analiz birimi → Fark yönü → H₀/H₁ → α → Tahmin → Test istatistiği → p → Güven aralığı → Etki büyüklüğü → Duyarlılık/simülasyon → Yorum → Sınırlılık → Akademik raporlama**

## 1. Önce veri türünü belirtin

Bu bölüm üç farklı bilgi türü içerir:

1. gerçek eşleşmiş `sleep` verisi,
2. yalnız özet istatistiklerle verilen kurgusal örnekler,
3. ideal normal model altında oluşturulan simülasyonlar.

Bunlar raporda ayrı başlıklarla sunulmalıdır.

Örnek ifade:

> Ana uygulama R `datasets` paketindeki `sleep` verisinin yerel aktarımında bulunan 10 eşleşmiş kişinin iki koşuldaki ölçümlerine dayanmaktadır. Bölümdeki diğer özet örnekler kurgusal, Monte Carlo sonuçları ise ideal normal model altında simüle edilmiştir.

## 2. Analiz birimini doğru tanımlayın

Dosyada 20 satır vardır ancak aynı 10 kişi iki koşulda ölçülmüştür.

Bu nedenle:

- ölçüm sayısı = 20,
- bağımsız kişi sayısı = 10,
- eşleştirme anahtarı = `ID`.

Örnek ifade:

> Yirmi ölçüm satırı 10 kişiye ait iki eşleşmiş koşulu temsil ettiğinden analiz birimi kişi olarak alınmış ve `n=10` kullanılmıştır.

## 3. Fark yönünü analizden önce yazın

Ana fark:

`D = koşul2 − koşul1`.

Hipotezler:

`H₀: μ_D = 0`

`H₁: μ_D ≠ 0`

ve:

`α=.05`.

Bu yön ve alternatif sonuç görüldükten sonra değiştirilmemelidir.

## 4. Betimsel farkı raporlayın

Fark puanları için:

- `n=10`,
- ortalama = `1.58` saat,
- s = `1.229995`,
- SH = `.388959`.

Örnek ifade:

> Koşul 2−Koşul 1 farkının ortalaması `1.58` saat (s=`1.23`, SH=`.39`) olarak bulundu (`n=10`).

Bu ifade test sonucundan önce etkinin yönünü ve büyüklüğünü görünür hale getirir.

## 5. Eşleşmiş t testini tam raporlayın

Ana sonuç:

- `t(9)=4.062128`,
- iki yönlü `p=.002832890`,
- %95 GA `[.700114, 2.459886]`.

Yuvarlatılmış akademik ifade:

> Koşullar arasındaki ortalama fark istatistiksel olarak sıfırdan farklıydı, `t(9)=4.06`, `p=.0028`, %95 GA `[0.70, 2.46]` saat.

Yalnız:

> “Sonuç anlamlıdır (p<.05).”

demek bilgi kaybına yol açar.

## 6. p değerini doğru yorumlayın

`p=.0028`:

- H₀'ın doğru olma olasılığı değildir,
- etkinin büyük olma olasılığı değildir,
- sonucun tekrarlanma olasılığı değildir,
- nedensellik olasılığı değildir.

Uygun ifade:

> Belirlenen sıfır hipotezi ve klasik t modeli altında gözlenen kadar veya daha uç bir test istatistiğinin iki yönlü olasılığı yaklaşık `.0028` idi.

Genellikle raporda bu uzun tanımın her seferinde yazılması gerekmez; fakat yorum bu anlamla uyumlu olmalıdır.

## 7. Güven aralığını tahmin olarak kullanın

%95 güven aralığı:

`[0.700114, 2.459886]` saattir.

Örnek ifade:

> Ortalama fark `1.58` saat olarak tahmin edilmiş ve %95 güven aralığı `0.70–2.46` saat bulunmuştur.

Aralık etki büyüklüğünün makul değerleri hakkında p değerinden daha doğrudan bilgi verir.

Ancak güven aralığı kullanılan model ve varsayımlara bağlıdır.

## 8. d_z etki büyüklüğünü raporlayın

Eşleşmiş tasarım için:

`d_z = ortalama fark / farkların s'si`.

Sonuç:

`d_z=1.284558`.

Örnek ifade:

> Fark puanlarının standart sapmasıyla standartlaştırılan eşleşmiş etki büyüklüğü `d_z=1.28` idi.

Bu bölümde `d_z` için güven aralığı hesaplanmadığından uydurma aralık eklemeyin.

## 9. t ve d_z ilişkisini denetim olarak kullanın

Bu tanımla:

`t = d_z√n`.

Burada:

`1.284558 × √10 ≈ 4.062128`.

Bu eşitlik yeniden üretim kontrolüdür; ayrı bir bilimsel bulgu değildir.

## 10. Fark yönü terslenirse ne olur?

Fark `koşul1−koşul2` olarak tanımlansaydı:

- t işaret değiştirirdi,
- iki yönlü p aynı kalırdı,
- güven aralığı `[−2.459886, −.700114]` olurdu.

Bu nedenle işaretin yorumu fark tanımına bağlıdır.

Raporda fark yönü mutlaka görünür olmalıdır.

## 11. Tek yönlü p değerini sonradan seçmeyin

Ana veri için:

- iki yönlü p = `.002832890`,
- sağ kuyruk = `.001416445`,
- sol kuyruk = `.998583555`.

Sağ ve sol kuyruk farklı alternatif hipotezlerdir.

Uygun yöntem ifadesi:

> Test yönü sonuçlar incelenmeden önce araştırma sorusuna göre belirlenmelidir; analiz sonrası en küçük tek yönlü p değerinin seçilmesi kullanılmamıştır.

## 12. Reddetmemeyi eşdeğerlik olarak sunmayın

Kurgusal dolum örneğinde:

- `t(24)=−2`,
- iki yönlü `p=.056940`,
- %95 GA `[491.872203, 500.127797]`.

Bu sonuç:

> “Ortalama 500'dür.”

veya

> “İki değer eşdeğerdir.”

anlamına gelmez.

Eşdeğerlik farklı hipotezler ve önceden belirlenmiş eşdeğerlik sınırları gerektirir.

## 13. Sonuca bakıp test yönünü değiştirmeyin

Aynı dolum örneğinde sol kuyruk p değeri `.028470`'tir.

İki yönlü sonuç `.056940` görüldükten sonra:

> “Tek yönlü test yapalım, artık anlamlı.”

demek uygun değildir.

Araştırma hipotezi ve test yönü veri sonucundan önce belirlenmelidir.

## 14. Kurgusal özetleri ham veri gibi sunmayın

Ders özeti:

- `n=16`, ortalama `74.5`, s `8`, referans `70`,
- `t(15)=2.25`,
- iki yönlü `p=.039888`,
- %95 GA `[70.237101,78.762899]`.

İleri özet:

- `n=36`, ortalama `52`, s `12`, referans `50`,
- `t(35)=1`,
- iki yönlü `p=.324174`.

Bu örnekler verilen özetlerden hesaplanmıştır; yeni bireysel gözlemler üretilmemiştir.

## 15. 2×2 tablo testini doğru adlandırın

Kurgusal `[[20,30],[30,20]]` tablosunda:

- beklenen hücrelerin her biri `25`,
- düzeltmesiz Pearson `χ²=4`,
- `sd=1`,
- `p=.045500`,
- Cramer `V=.2`.

Örnek ifade:

> Kurgusal 2×2 tabloda düzeltmesiz Pearson ki-kare testi `χ²(1)=4.00`, `p=.0455` ve Cramer `V=.20` verdi.

Bu sonuç Yates düzeltmeli veya Fisher kesin testi olarak etiketlenmemelidir.

## 16. Simülasyon tasarımını raporlayın

Simülasyon koşulları:

- her koşulda 20,000 tekrar,
- `n=25`,
- `σ=1`,
- normal model,
- Python tohumu `20260906`.

Örnek ifade:

> Tip I hata ve güç davranışını göstermek amacıyla normal model altında her koşul için 20,000 Monte Carlo tekrarı (`n=25`, `σ=1`, seed=20260906) yürütülmüştür.

Bu simülasyon gerçek `sleep` veri setinin özelliklerini yeniden üretmek amacıyla yapılmamıştır.

## 17. Tip I hata sonucunu raporlayın

Gerçek standartlaştırılmış etki `d=0` iken:

- gözlenen iki yönlü red oranı = `.0502`,
- kuramsal hedef = `.0500`,
- Monte Carlo SH = `.001544`,
- gerçek ortalama kapsaması = `.9498`.

Örnek ifade:

> Sıfır etki koşulunda iki yönlü testin Monte Carlo red oranı `.0502` olup nominal `.05` düzeyiyle uyumluydu (MC SH=`.00154`).

Bu, belirli ideal modelin simülasyon sonucudur.

## 18. Gücü doğru bağlamda raporlayın

`d=.5` koşulunda:

- simülasyon red oranı = `.6667`,
- kuramsal güç = `.669708`,
- MC SH = `.003333`,
- gerçek ortalama kapsaması = `.9474`.

Örnek ifade:

> `d=.5` ideal model koşulunda ampirik red oranı `.6667`, kuramsal güç `.6697` idi (MC SH=`.00333`).

Şunu yazmayın:

> “Sleep çalışmasının gücü %66.7'dir.”

Çünkü bu simülasyon gerçek çalışmanın örnekleme, tasarım ve etki belirsizliğini modellememektedir.

## 19. Monte Carlo belirsizliğini görünür tutun

20,000 tekrar büyük görünse de simülasyon oranları hâlâ örnekleme hatasına sahiptir.

Bu nedenle MC standart hatası raporlanır.

Ayrıca aynı seed'in R ve Python'da aynı örnekleri üretmesi beklenmemelidir; farklı rastgele sayı üreticileri kullanılabilir.

## 20. Veriden yön seçmenin sonuçlarını raporlayın

`d=0` altında veriye bakarak tek yön seçen yanlış kuralın red oranı:

`.1016`.

Örnek ifade:

> Sıfır etki altında veri sonucuna göre tek kuyruk seçen hatalı kural yaklaşık `.102` red oranı üretmiş, böylece nominal `.05` hata düzeyini belirgin biçimde aşmıştır.

Bu simülasyon test yönünün önceden belirlenmesi gereğini gösterir.

## 21. Test ve güven aralığı ilişkisini doğru açıklayın

İki yönlü α=.05 t testinde H₀ değeri olan sıfırın %95 güven aralığı dışında kalması red kararıyla eşleşir.

Ancak `d=.5` simülasyonunda:

- gerçek `.5` değerinin aralık içinde olması = kapsama,
- sıfırın aralık dışında olması = H₀ red kararı

olup aynı olay değildir.

## 22. Çoklu testlerde aile hata oranını raporlayın

20 **bağımsız** doğru H₀ testi için:

`FWER = 1 − (1−.05)^20 = .641514`.

Örnek ifade:

> Birbirinden bağımsız 20 doğru sıfır hipotezinin her biri α=.05 ile sınandığında en az bir yanlış red olasılığı yaklaşık `.642`'dir.

Bağımlı testlerde bu formül doğrudan kullanılmaz.

## 23. Varsayımları “kanıtlandı” diye yazmayın

Klasik eşleşmiş t testi bu bölümde bağımsız kişiler ve normal fark modeli altında öğretilir.

Ancak:

- n yalnız 10'dur,
- normallik testi yapılmamıştır,
- en büyük fark 4.6 saattir,
- sıra/taşıma etkileri, randomizasyon ve temsil ayrıntıları kısa veri kopyasından doğrulanmamaktadır.

Dolayısıyla:

> “Tüm varsayımlar sağlanmıştır.”

ifadesi desteklenmez.

## 24. Büyük farkı otomatik silmeyin

4.6 saatlik fark ana analizde korunur.

Büyük veya dikkat çekici bir değer:

- veri hatası,
- aykırı gözlem,
- silme gerekçesi

ile eş anlamlı değildir.

Silme ancak veri kaynağı ve önceden tanımlanmış bilimsel gerekçeyle yapılmalıdır.

## 25. Nedensellik sınırını koruyun

Tarihsel `sleep` verisinin kısa yerel kopyası:

- randomizasyon ayrıntılarını,
- sıra etkilerini,
- taşıma etkilerini,
- temsil özelliklerini

tam olarak doğrulamaz.

Bu nedenle bölüm sonuçları yeni tedavi önerisi veya güçlü nedensel etki kanıtı olarak sunulmamalıdır.

## 26. Yapılmayan analizleri rapora eklemeyin

Bu pakette yapılmamıştır:

- normallik testi,
- bootstrap,
- permütasyon testi,
- `d_z` güven aralığı,
- eşdeğerlik testi,
- gerçek `sleep` verisi için güç analizi.

## 27. Örnek bütünleşik gerçek-veri paragrafı

> R `datasets` paketindeki `sleep` verisinin yerel aktarımında aynı 10 kişinin iki koşuldaki ölçümleri ID üzerinden eşleştirildi. Ana fark Koşul 2−Koşul 1 olarak önceden tanımlandı. Ortalama fark `1.58` saat (s=`1.23`, SH=`.39`) idi. İki yönlü eşleşmiş t testi ortalama farkın sıfırdan farklı olduğunu gösterdi, `t(9)=4.06`, `p=.0028`, %95 GA `[0.70, 2.46]`. Fark puanlarının standart sapmasına göre eşleşmiş etki büyüklüğü `d_z=1.28` idi. Sonuç küçük örneklem, klasik t modeli varsayımları ve kısa kaynak kopyasından randomizasyon, sıra/taşıma etkileri ile temsiliyetin doğrulanamaması dikkate alınarak yorumlanmalıdır; küçük p değeri tek başına pratik önem veya nedensellik kanıtı olarak değerlendirilmemiştir.

## 28. Örnek bütünleşik simülasyon paragrafı

> Test davranışını ideal koşullarda incelemek amacıyla normal model altında her koşul için 20,000 Monte Carlo tekrarı (`n=25`, `σ=1`, seed=20260906) yürütüldü. `d=0` koşulunda iki yönlü red oranı `.0502` (MC SH=`.00154`), %95 güven aralığının gerçek ortalamayı kapsama oranı `.9498` idi. `d=.5` koşulunda ampirik güç `.6667` (MC SH=`.00333`) ve kuramsal güç `.6697` olarak bulundu. Veriye bakarak tek yön seçen hatalı kural sıfır etki altında `.1016` red oranı üretti. Bu sonuçlar ideal simülasyon modeline aittir ve gerçek sleep verisinin güç veya varsayım doğrulaması olarak yorumlanmamıştır.

## 29. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Gerçek veri, kurgu ve simülasyon ayrılmış mı?
- 20 satır yerine doğru analiz birimi `n=10` kullanılmış mı?
- ID eşleştirme anahtarı belirtilmiş mi?
- Fark yönü açık mı?
- H₀, H₁ ve α belirtilmiş mi?
- Ortalama fark, s ve SH raporlanmış mı?
- `t(sd)` doğru verilmiş mi?
- İki yönlü p doğru raporlanmış mı?
- Güven aralığı verilmiş mi?
- `d_z` doğru standartlaştırıcıyla hesaplanmış mı?
- `d_z` için yapılmamış güven aralığı eklenmemiş mi?
- p değeri H₀'ın doğru olma olasılığı diye yorumlanmamış mı?
- Test yönü sonuçtan sonra değiştirilmemiş mi?
- `p>.05` eşdeğerlik kanıtı sayılmamış mı?
- Küçük p pratik önem veya nedensellik kanıtı sayılmamış mı?
- Kurgusal özetler gerçek ham veri diye sunulmamış mı?
- Pearson ki-kare doğru adıyla raporlanmış mı?
- Simülasyon koşulları ve tekrar sayısı verilmiş mi?
- Monte Carlo SH belirtilmiş mi?
- Simülasyon gücü gerçek veri gücü diye sunulmamış mı?
- Çoklu test aile hata formülünün bağımsızlık koşulu belirtilmiş mi?
- Varsayımlar kanıtlanmış gibi yazılmamış mı?
- 4.6 saatlik fark otomatik silinmemiş mi?
- Yapılmayan normallik/bootstrap/permütasyon/eşdeğerlik analizleri eklenmemiş mi?
- R çalıştırılmadıysa R sonucu varmış gibi sunulmamış mı?
- SPSS analizi yapılmış gibi yazılmamış mı?

## Son mesaj

Hipotez testinde güçlü raporlama şu soruya yalnız “anlamlı mı?” diye bakmaz:

**Ne karşılaştırıldı? → Bağımsız birim neydi? → Fark nasıl tanımlandı? → Etki ne büyüklükteydi? → Belirsizlik neydi? → Test hangi hipoteze yanıt verdi? → Sonuç neyi destekliyor? → Neyi desteklemiyor?**

Bu nedenle bilimsel raporlamanın hedefi:

**p değerini merkeze almak değil; tahmin, belirsizlik, etki büyüklüğü, tasarım ve yorum sınırını birlikte görünür kılmaktır.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.