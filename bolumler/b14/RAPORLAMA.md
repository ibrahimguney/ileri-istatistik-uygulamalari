# Bölüm 14 — Faktör Analizini Akademik Raporlama

Bu rehber, Bölüm 14'teki açımlayıcı faktör analizinin (AFA) bilimsel bir raporda doğru, şeffaf ve yeniden üretilebilir biçimde sunulmasına yardımcı olur.

Temel düşünce zinciri:

**Veri ve amaç → analiz örneklemi → korelasyon matrisi → faktörlenebilirlik → faktör sayısı → çıkarım → rotasyon → örüntü/yapı → ortak varyans → artıklar → alternatifler → içerik → doğrulama planı**

şeklindedir.

## 1. Veri ve örneklem seçimini önce raporlayın

Analiz, `psych::bfi` kaynağının yerel ilk 100 kayıt alıntısındaki A1–A5 ve C1–C5 maddeleri üzerinde yürütülmüştür.

Üç farklı satırdaki eksikler nedeniyle on maddenin ortak tam kayıt örneklemi:

`n=97`

olarak belirlenmiştir.

A1, C4 ve C5 belgelenmiş anahtara göre bir kez `7−x` ile ters puanlanmıştır.

Örnek yöntem ifadesi:

> Açımlayıcı faktör analizi, yerel ilk 100 kayıt alıntısındaki on A/C maddesinin ortak 97 tam kaydı üzerinde yürütülmüştür. A1, C4 ve C5 maddeleri belgelenmiş anahtara göre bir kez ters puanlanmış; ikili silme veya eksik değer ataması kullanılmamıştır.

Bölüm 13'teki A=99 ve C=98 analiz örneklemlerinden hesaplanan ayrı korelasyonlar tek bir matris halinde birleştirilmemelidir.

## 2. Korelasyon türünü belirtin

Bu bölümde **Pearson korelasyon matrisi** kullanılmaktadır.

Polikorik korelasyon veya ordinal faktör modeli uygulanmamıştır.

Bu nedenle raporda:

> Faktör analizi Pearson korelasyon matrisi üzerinden yürütülmüştür; polikorik/ordinal duyarlılık analizi bu paketin kapsamında değildir.

şeklinde yöntem sınırı açıkça yazılabilir.

## 3. KMO ve Bartlett'i ön bilgi olarak raporlayın

Sonuçlar:

- KMO = `.726118`,
- yaklaşık Bartlett `χ²(45)=208.912`,
- `p≈5.81×10⁻²³`.

Örnek raporlama:

> Ortak 97 kaydın Pearson korelasyon matrisi için KMO örneklem yeterliği katsayısı `.726` olarak hesaplanmış, yaklaşık Bartlett küresellik testi anlamlı bulunmuştur, `χ²(45)=208.91, p<.001`.

Bu sonuçların ardından:

> KMO ve Bartlett sonuçları faktör analizinin incelenmesini destekleyen ön bilgiler olarak değerlendirilmiş; doğru faktör sayısı, kültürel geçerlik veya yeterli örneklem büyüklüğünün tek başına kanıtı olarak yorumlanmamıştır.

ifadesi eklenebilir.

## 4. Örneklem büyüklüğünü tek bir oranla savunmayın

“Madde başına 10 kişi yeterlidir” gibi sabit oranlar evrensel yeterlik belgesi değildir.

Örneklem gereksinimi:

- ortak varyansların düzeyine,
- faktör başına gösterge sayısına,
- yüklerin büyüklüğüne,
- faktör yapısına,
- örneklem seçimine,
- çözüm kararlılığına

bağlıdır.

Bu küçük ve sıralı ilk-100 alıntısı için genellenebilirlik onayı verilmemelidir.

## 5. Faktör sayısı kararında birden fazla kanıt kullanın

PCA'nın ilk üç özdeğeri:

`3.062119, 1.657400, 1.156765`

olduğundan Kaiser `>1` kuralı üç bileşen önerebilir.

Ancak 2000 sütun permütasyonlu paralel analizde üçüncü boyut için:

| Yaklaşım | Gözlenen | %95 referans |
|---|---:|---:|
| PCA | 1.156765 | 1.320067 |
| SMC | .356621 | .438259 |

olduğundan üçüncü gözlenen değer iki yaklaşımda da referansın altında kalmaktadır.

Örnek raporlama:

> Kaiser ölçütünde üç PCA özdeğeri 1'in üzerinde olmakla birlikte, 2000 bağımsız sütun permütasyonuna dayanan paralel analizde üçüncü gözlenen özdeğer hem PCA hem SMC referansının altında kalmıştır. İlk sıradan ardışık aşma kuralı bu örneklemde iki aday boyutu desteklemiştir.

Paralel analiz de “iki faktör kesin doğrudur” anlamına gelmez; faktör sayısı için önemli bir kanıttır.

## 6. Paralel analiz yöntemini ayrıntılandırın

Bu pakette:

- 2000 permütasyon,
- her sütunun ayrı permütasyonu,
- tohum `20261401`,
- her sıralı özdeğer için doğrusal %95 referans niceliği

kullanılmıştır.

Sütun permütasyonu marjinal dağılımları korurken satır içi ilişkileri kırar.

Bu işlem Bölüm 13'teki katılımcı-satırı bootstrap ile aynı değildir.

Ayrıca referans eğrisi gözlenen özdeğerin güven aralığı değildir.

## 7. Çıkarım yöntemini açıkça yazın

Faktör çıkarımında **SMC başlangıç ortak varyanslı temel eksenler faktörleştirmesi (PAF)** kullanılmıştır.

Örnek yöntem ifadesi:

> Faktörler, başlangıç ortak varyanslarının karesel çoklu korelasyonlarla (SMC) belirlendiği temel eksenler faktörleştirmesiyle çıkarılmıştır. Bir, iki ve üç faktörlü aday çözümler aynı 97 gözlem üzerinde incelenmiştir.

SMC başlangıç azaltılmış spektrumunu nihai PAF faktör spektrumu olarak raporlamayın.

## 8. Rotasyonu ve eğik faktör ilişkisini raporlayın

İki faktörlü çözüm Kaiser satır normalizasyonu olmadan **quartimin** ile döndürülmüştür.

Faktör korelasyonu:

`Phi_AC=.216668`

olarak bulunmuştur.

Örnek raporlama:

> İki faktörlü PAF çözümü, faktörlerin ilişkili olmasına izin veren normalizasyonsuz quartimin rotasyonuyla döndürülmüştür. Faktörler arası korelasyon `.217` olarak hesaplanmıştır.

Faktörler ilişkili olduğundan örüntü ve yapı matrislerinin birbirinden ayrılması gerekir.

## 9. Örüntü ve yapı katsayılarını karıştırmayın

A2 için örüntü katsayıları:

- A faktörü: `.478526`,
- C faktörü: `.307147`.

Faktör korelasyonu nedeniyle C yapı katsayısı:

`.410828`

olmaktadır.

Örnek raporlama:

> A2'nin örüntü katsayıları A ve C faktörlerinde sırasıyla `.479` ve `.307` iken, faktör korelasyonu dikkate alındığında C yapı katsayısı `.411`'dir. Yapı katsayısı örüntü çapraz yükü olarak yorumlanmamıştır.

Tam raporda hangi matrisin sunulduğu açıkça belirtilmelidir.

## 10. Eğik çözümde ortak varyansı doğru hesaplayın

A2 için:

`h²=.387017`

ve:

`u²=.612983`.

Eğik rotasyonda ortak varyans yalnız yük karelerinin toplamı değildir; `Phi` nedeniyle çapraz terim de hesaba girer.

Örnek ifade:

> A2 için faktör korelasyonu dikkate alınarak hesaplanan ortak varyans `.387`, özgüllük `.613` olmuştur.

## 11. A5 örneğini madde kararında ölçülü kullanın

A5 örüntüsü yaklaşık:

`(.893598, −.069620)`

şeklindedir.

Sonuçlar:

- `h²=.776406`,
- özgüllük `.223594`,
- C yapı katsayısı `.123994`.

Küçük negatif C örüntü katsayısı maddenin anahtarını değiştirmek için gerekçe değildir.

Ters puanlama içerik ve önceden belgelenmiş anahtara dayanır; istenen yük desenini üretmek için sonradan değiştirilmez.

## 12. PAF ortak varyansı ile PCA açıklanan varyansını eşitlemeyin

İki PAF faktörünün ortak varyans oranı:

`.366554`

iken ilk iki PCA özdeğerinin toplamının madde sayısına oranı:

`.471952`

olmaktadır.

Bunlar farklı matematiksel yapılara dayanır.

Örnek raporlama:

> İki PAF faktörünün ortak varyans katkısı `.367` iken ilk iki PCA bileşeninin toplam özdeğer oranı `.472`'dir. Bu iki değer aynı “açıklanan varyans” ölçüsü olarak yorumlanmamıştır.

## 13. Artık uyumunu doğru payda ile raporlayın

On madde için benzersiz köşegen dışı çift sayısı:

`10×9/2 = 45`.

İki faktörlü çözümde:

- RMSR `.056761`,
- maksimum `|artık|=.198783`,
- `.05`'i aşan 12 çift.

Örnek raporlama:

> İki faktörlü çözümün 45 benzersiz köşegen dışı korelasyon çifti üzerinden RMSR değeri `.0568` olarak hesaplanmış; 12 çiftte mutlak artık `.05`'i aşmış ve en büyük mutlak artık `.199` olmuştur.

Buradaki `.05` yalnız işaretleme eşiğidir; hipotez testi değildir.

RMSR'yi DFA'daki SRMR veya RMSEA olarak adlandırmayın.

## 14. Alternatif faktör sayılarını karşılaştırın

| Model | RMSR | Maks. |artık| | |artık|>.05 |
|---|---:|---:|---:|
| 1 faktör | .121292 | .371746 | 29 |
| 2 faktör | .056761 | .198783 | 12 |
| 3 faktör | .039941 | .111194 | 8 |

Üç faktörlü modelin aynı veride daha küçük artık üretmesi beklenebilir; model esnekliği artmıştır.

Örnek yorum:

> Üç faktörlü çözüm daha düşük RMSR ve daha az büyük artık üretmiş olsa da, paralel analiz iki aday boyutu desteklediğinden ve ek faktörün içerik/kararlılık kanıtı bulunmadığından yalnız artık küçülmesine dayanarak üç faktörlü çözüm seçilmemiştir.

## 15. Heywood yokluğunu model doğruluğu olarak sunmayın

Mevcut bir, iki ve üç faktör adaylarında Heywood durumu görülmemiştir.

Bu yararlı bir tanı bilgisidir fakat:

> “Heywood yok, dolayısıyla model doğrudur.”

sonucu çıkarılamaz.

## 16. Madde çıkarma duyarlılığını ana modelden ayırın

A1 ve A4 yalnız duyarlılık kopyasında çıkarılmıştır. Aynı 97 kişi korunmuştur.

Sekiz maddelik çözümde:

- RMSR `.049025`,
- ortak varyans oranı `.432950`,
- 28 çiftin 7'sinde `|artık|>.05`.

Örnek raporlama:

> A1 ve A4'ün çıkarıldığı sekiz maddelik çözüm yalnız duyarlılık analizi olarak incelenmiş ve ana modelde maddeler korunmuştur. Sekiz maddelik çözümde RMSR `.0490` bulunmuştur; ancak madde içeriği ve RMSR paydası değiştiğinden bu değer on maddelik modele karşı doğrudan üstünlük testi olarak yorumlanmamıştır.

## 17. Varimax hakkında yanlış uyum iddiasından kaçının

Aynı çıkarılmış ortak faktör uzayında ortogonal veya eğik rotasyon yüklerin yorumlanışını değiştirir. Rotasyon tek başına çıkarılmış ortak matrisin yeniden ürettiği korelasyonları otomatik olarak iyileştiren yeni bir model değildir.

Bu nedenle:

> “Varimax RMSR'yi iyileştirdi, dolayısıyla daha iyi modeldir.”

şeklinde yöntem ayrıntısı doğrulanmadan raporlama yapılmamalıdır.

## 18. AFA'yı doğrulama olarak sunmayın

Bu bölümde elde edilen iki faktörlü yapı **keşifsel bir aday modeldir**.

AFA sonucunun bilimsel değeri, gelecekte sınanabilir açık hipotezler üretmesidir.

Örneğin gelecekte:

- A1/A4 içerik ve ortak varyans sorunları,
- A2 çapraz örüntüsü,
- faktör korelasyonu,
- hangi maddelerin hangi faktöre yükleneceği

önceden gerekçelendirilerek yeni veride sınanabilir.

## 19. Aynı veride DFA bağımsız doğrulama değildir

AFA ile yapı keşfedildikten sonra aynı 97 kayda DFA uygulamak teknik olarak mümkündür; ancak bu **bağımsız doğrulama** değildir.

Aynı şekilde küçük sıralı veriyi yalnız ikiye bölmek hedef anakütlede bağımsız doğrulama garantisi vermez.

Uygun ifade:

> AFA bulguları gelecekteki doğrulayıcı model için hipotez oluşturmak amacıyla kullanılmıştır. Bağımsız doğrulama için yeni ve hedef kullanımı temsil eden veri gerekmektedir.

## 20. Yapılmamış analizleri raporlamayın

Bu pakette şu analizler yapılmamıştır:

- polikorik korelasyonlu AFA,
- yükler için güven aralıkları,
- bootstrap yük kararlılığı,
- yeni örneklemde AFA tekrarı,
- bağımsız veriyle DFA,
- ölçme değişmezliği.

Bu sonuçlar varmış gibi rapora eklenmemelidir.

## 21. Örnek bütünleşik AFA raporu

> `psych::bfi` kaynağından alınmış yerel ilk 100 kayıt alıntısındaki A1–A5 ve C1–C5 maddeleri incelenmiş; üç farklı satırdaki eksikler nedeniyle analiz ortak 97 tam kayıt üzerinde yürütülmüştür. A1, C4 ve C5 belgelenmiş anahtara göre bir kez ters puanlanmış ve Pearson korelasyon matrisi kullanılmıştır. KMO `.726`, yaklaşık Bartlett küresellik testi `χ²(45)=208.91, p<.001` bulunmuştur. Kaiser ölçütü üç PCA bileşeni önermekle birlikte, 2000 bağımsız sütun permütasyonuna dayanan PCA ve SMC paralel analizlerinde üçüncü gözlenen değer ilgili %95 referansın altında kaldığından iki aday boyut değerlendirilmiştir. SMC başlangıç ortak varyanslı iki faktörlü PAF çözümü normalizasyonsuz quartimin ile döndürülmüş ve faktör korelasyonu `.217` bulunmuştur. İki faktörlü çözümün 45 benzersiz köşegen dışı çift üzerinden RMSR değeri `.0568`'dir. A1/A4 çıkarılması yalnız duyarlılık analizi olarak incelenmiş, ana analizde madde silinmemiştir. Bulgular küçük ve sıralı yerel veri alıntısına aittir; Türkçe uyarlama veya bağımsız DFA doğrulaması olarak yorumlanmamıştır.

## 22. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce kontrol edin:

- Veri kaynağı ve ilk-100 seçim sınırı belirtilmiş mi?
- Ortak tam kayıt `n=97` gerekçelendirilmiş mi?
- Ters puanlama açık mı?
- İkili silme/atama yapılmadığı belirtilmiş mi?
- Pearson korelasyon kullanıldığı yazılmış mı?
- Polikorik analiz yapılmadığı belirtilmiş mi?
- KMO ve Bartlett doğru kapsamda yorumlanmış mı?
- Örneklem yeterliği tek bir kişi/madde oranına indirgenmemiş mi?
- Faktör sayısı kararı yalnız özdeğer >1 kuralına dayandırılmamış mı?
- Paralel analiz tekrar sayısı ve yöntemi belirtilmiş mi?
- Referans çizgisi güven aralığı olarak sunulmamış mı?
- PAF ve SMC başlangıç spektrumu ayrılmış mı?
- Rotasyonun quartimin ve eğik olduğu belirtilmiş mi?
- Örüntü ile yapı matrisi ayrılmış mı?
- `Phi` raporlanmış mı?
- Ortak varyans eğik çözüm için doğru hesaplanmış mı?
- PAF ortak varyansı PCA açıklanan varyansıyla eşitlenmemiş mi?
- RMSR'nin 45 benzersiz köşegen dışı çift üzerinden hesaplandığı belirtilmiş mi?
- RMSR, SRMR/RMSEA olarak adlandırılmamış mı?
- Alternatif 1/2/3 faktör çözümleri ölçülü biçimde değerlendirilmiş mi?
- Daha düşük artık otomatik faktör sayısı kararı yapılmamış mı?
- Heywood yokluğu doğru model kanıtı sayılmamış mı?
- A1/A4 çıkarılması duyarlılık analizi olarak belirtilmiş mi?
- Madde silme için kültürel neden uydurulmamış mı?
- AFA bağımsız doğrulama olarak sunulmamış mı?
- Aynı veride DFA bağımsız doğrulama olarak sunulmamış mı?
- Yapılmamış polikorik analiz, yük güven aralığı veya yeni-veri DFA sonucu eklenmemiş mi?
- R/SPSS çalıştırılmadıysa çalıştırılmış gibi raporlanmamış mı?

## Son mesaj

Açımlayıcı faktör analizinde temel düşünce zinciri şöyledir:

**Araştırma amacı → Veri ve maddeler → Korelasyon yapısı → Faktörlenebilirlik → Faktör sayısı → Çıkarım → Rotasyon → Örüntü/yapı → Faktör ilişkisi → Ortak varyans → Artıklar → İçerik → Duyarlılık → Yeni veride doğrulama → Akademik raporlama**

AFA'nın güçlü kullanımı, aynı veride “doğru modeli kanıtlamak” değil, **kuram ve içerikle birlikte gelecekte sınanabilecek bir ölçüm modeli üretmektir.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.