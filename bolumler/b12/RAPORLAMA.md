# Bölüm 12 — Parametrik Olmayan Testleri Akademik Raporlama

Bu rehber, Bölüm 12'deki Mann–Whitney U, Wilcoxon işaretli sıralar, Kruskal–Wallis/Dunn–Holm, Friedman ve kategorik sayım analizlerinin bilimsel bir raporda doğru biçimde sunulmasına yardımcı olur.

Temel ilke:

**Tasarım → analiz birimi → sıra/fark yönü → test istatistiği → p hesap yöntemi → etki büyüklüğü → çoklu karşılaştırma ailesi → sınırlılık**

zincirinin görünür olmasıdır.

## 1. “Parametrik olmayan” ifadesini “varsayımsız” olarak kullanmayın

Parametrik olmayan yöntemlerin de:

- bağımsızlık veya eşleşme yapısı,
- değişkenin ölçüm düzeyi,
- sıralanabilirlik,
- bağların ve sıfırların ele alınışı,
- bazı yorumlarda dağılım şekli veya fark simetrisi

gibi koşulları vardır.

Bu nedenle yöntem seçimini yalnızca “Shapiro anlamlı çıktı” gerekçesine dayandırmayın.

## 2. Mann–Whitney U analizini raporlayın

Doz 1 düzeyinde OJ ve VC farklı hayvan kayıtlarıdır ve karşılaştırma bağımsız iki grup yapısındadır.

Sıra toplamları:

- OJ: `143.5`,
- VC: `66.5`.

U değerleri:

- `U_OJ = 88.5`,
- `U_VC = 11.5`.

Bunlar aynı karşılaştırmanın iki yönlü U gösterimidir ve toplamları `n1×n2=100`'dür.

100 çapraz çiftte:

- OJ kazanımı = 88,
- bağ = 1,
- üstünlük ölçüsü `A=.885`,
- sıra-biserial = `.770`.

P değerleri:

- 184756 etiket atamasının tam sayımı: `p=.002230`,
- süreklilik düzeltmeli normal yaklaşım: `p=.004030`.

Örnek raporlama:

> Doz 1 düzeyinde OJ ve VC kayıtları Mann–Whitney U yaklaşımıyla karşılaştırılmıştır. OJ için sıra toplamı 143.5 ve karşılık gelen U değeri 88.5'tir. Tüm 184756 grup etiketi atamasının sayıldığı iki yönlü hesapta `p=.00223`, süreklilik düzeltmeli normal yaklaşımda ise `p=.00403` bulunmuştur. Çapraz çift üstünlük ölçüsü `A=.885` ve sıra-biserial etki büyüklüğü `.77`'dir.

`A=.885` değerini “OJ tedavisinin başarı olasılığı %88.5'tir” şeklinde yorumlamayın. Bu değer bu örneklemdeki çapraz çiftlerin sıralı üstünlüğünü özetler.

## 3. U testini yalnız medyan testi olarak sunmayın

Mann–Whitney U sıralı dağılımlar arasındaki üstünlük yapısına duyarlıdır. Yalnız belirli konum-kayması ve dağılım şekli koşulları altında sonucu basit bir medyan farkı yorumuna indirgemek uygundur.

Bu nedenle daha güvenli ifade:

> OJ gözlemleri VC gözlemlerine göre daha yüksek sıralarda bulunma eğilimi göstermiştir.

şeklindedir.

## 4. Wilcoxon analizinde fark yönünü yazın

Sleep verisinde aynı 10 kişinin iki ölçümü bulunmaktadır. Fark yönü:

`koşul 2 − koşul 1`

olarak tanımlanmıştır.

Farklar:

`1.2, 2.4, 1.3, 1.3, 0, 1.0, 1.8, 0.8, 4.6, 1.4`

saat şeklindedir.

Bir sıfır fark `wilcox` kuralında sıralama hesabına girmez ancak ham veri ve 10 çiftlik arşivde kalır. İki adet 1.3 fark bağlı olduğundan ortalama sıra kullanılır.

Sonuçlar:

- `W+ = 45`,
- `W− = 0`,
- `T = 0`,
- sıfır olmayan fark sayısı = 9,
- `2^9 = 512` işaret örüntüsü,
- tam işaret sayımı `p=.003906`,
- süreklilik düzeltmeli yaklaşık `p=.009091`,
- sıra-biserial = `1.00` (sıfır olmayan sıraların paydasında).

Örnek raporlama:

> Aynı 10 kişinin koşul 2−koşul 1 farkları Wilcoxon işaretli sıralar yaklaşımıyla incelenmiştir. Bir sıfır fark `wilcox` sıralama kuralında dışarıda bırakılmış, iki bağlı 1.3 saatlik fark için ortalama sıra kullanılmıştır. Dokuz sıfır olmayan farkın 512 olası işaret örüntüsünün tam sayımında `T=0` ve iki yönlü `p=.00391` elde edilmiştir; süreklilik düzeltmeli normal yaklaşım `p=.00909` vermiştir.

Sıra-biserial değerinin 1 olması bütün kişilerin “yarar gördüğü” anlamına gelmez; bir kişinin farkı sıfırdır ve sonuç yalnız tanımlanan koşul karşılaştırmasına aittir.

## 5. Kesin p ile yaklaşık p'yi açıkça ayırın

Raporunuzda yalnız `p=.004` yazmak yerine mümkünse p değerinin nasıl elde edildiğini belirtin:

- tam etiket sayımı,
- tam işaret sayımı,
- normal yaklaşım,
- ki-kare yaklaşımı,
- Monte Carlo permütasyonu.

“Kesin” ifadesi, kullanılan null model altında ilgili sonlu örnek uzayının sayılması anlamındadır; “varsayımsız” anlamına gelmez.

## 6. OJ Kruskal–Wallis sonucunu raporlayın

OJ grubunda üç doz için ortalama sıralar:

- 0.5: `6.25`,
- 1: `17.40`,
- 2: `22.85`.

Bağ düzeltmeli sonuç:

- `H=18.506`,
- `df=2`,
- ki-kare yaklaşımı `p=.0000958`.

Örnek raporlama:

> OJ uygulamasındaki üç doz düzeyi Kruskal–Wallis testiyle karşılaştırılmıştır. Bağ düzeltmeli test istatistiği `H(2)=18.51` olup ki-kare yaklaşımıyla `p<.001` bulunmuştur.

Genel test hangi çiftlerin ayrıştığını tek başına göstermez.

## 7. Dunn–Holm ailesini bütünüyle raporlayın

OJ için aynı 30 kaydın ortak sıraları kullanılarak üç Dunn karşılaştırması yapılmıştır:

| Doz çifti | Ham p | Holm p |
|---|---:|---:|
| 1−0.5 | .004592 | .009185 |
| 2−0.5 | .0000245 | .0000734 |
| 2−1 | .165936 | .165936 |

Örnek raporlama:

> Genel Kruskal–Wallis testini izleyen üç Dunn karşılaştırması tek Holm ailesi olarak değerlendirilmiştir. Düzeltilmiş p değerleri doz 1−0.5 için `.0092`, doz 2−0.5 için `<.001` ve doz 2−1 için `.166` olmuştur. Son karşılaştırmada null hipotezin reddedilememesi doz 1 ve doz 2'nin eşdeğer olduğunu göstermez.

Holm yöntemi her ham p değerini doğrudan üçle çarpmak değildir. Bu işlem Bonferroni yaklaşımına karşılık gelir; Holm sıralı çarpanlar ve kümülatif maksimum kullanır.

## 8. VC ailesini OJ ailesinden ayırın

VC için:

- bağ düzeltmeli `H=25.072`,
- `df=2`,
- `p=.00000359`.

Dunn–Holm düzeltilmiş p değerleri:

- 1−0.5: `.01774`,
- 2−0.5: `.00000167`,
- 2−1: `.01774`.

Bu üç karşılaştırma VC'ye ait ayrı bir öğretim ailesidir. OJ ve VC p değerlerinin farklı olması doğrudan uygulama × doz etkileşimi kanıtı değildir.

## 9. Friedman analizinde blok birimini doğru yazın

RoundingTimes örneğinde:

- 22 satır = 22 blok,
- 3 sütun = 3 koşul,
- 66 hücre = 66 bağımsız kişi değildir.

Blok içi sıra toplamları:

- Round Out: `53`,
- Narrow Angle: `47`,
- Wide Angle: `32`.

Sonuçlar:

- bağ düzeltmeli `Q=11.143`,
- `df=2`,
- ki-kare yaklaşımı `p=.003805`,
- Kendall `W=.253`.

Örnek raporlama:

> RoundingTimes kod matrisindeki 22 blok üç koşul açısından Friedman testiyle karşılaştırılmıştır. Bağ düzeltmeli test sonucu `Q(2)=11.14`, ki-kare yaklaşımıyla `p=.0038` bulunmuş ve Kendall uyum katsayısı `W=.253` olarak hesaplanmıştır.

## 10. Friedman Monte Carlo p değerini tam sayım diye yazmayın

Tohum `202612` kullanılarak 99999 rastgele blok içi permütasyonda 311 aşım elde edilmiştir:

`p_MC=(311+1)/(99999+1)=.003120`.

Monte Carlo standart hatası yaklaşık:

`.000176`

olarak hesaplanmıştır.

Örnek raporlama:

> Friedman istatistiği ayrıca 99999 rastgele blok içi permütasyonla değerlendirilmiş ve `p_MC=.00312` elde edilmiştir. Monte Carlo hesap belirsizliğinin standart hatası yaklaşık `.00018`'dir. Bütün `6^22` olası blok içi düzen sayılmadığından bu sonuç tam enumerasyon p değeri değildir.

Monte Carlo standart hatasını etki büyüklüğünün güven aralığı olarak yorumlamayın.

## 11. Friedman sonrası karşılaştırmaları ayrı Holm ailesi olarak raporlayın

İkinci koşul eksi ilk koşul yönünde sonuçlar:

- Narrow−Round: medyan fark `−0.05`, Holm `p=.449`,
- Wide−Round: medyan fark `−0.125`, Holm `p=.0374`,
- Wide−Narrow: medyan fark `−0.10`, Holm `p=.00512`.

Bu p değerleri süreklilik düzeltmeli normal yaklaşım kullanan eşli Wilcoxon analizlerinden gelir; Friedman'ın Monte Carlo p değeri değildir.

Medyan farklar betimsel özetlerdir ve Wilcoxon'un sınadığı parametreyle koşulsuz biçimde özdeşleştirilmemelidir.

## 12. 18/22 kaynak uyuşmazlığını gizlemeyin

Yerel kaynak notunda RoundingTimes açıklamasının 18 oyuncudan, yayımlanan kod matrisinin ise 22 satırdan söz ettiği kayıtlıdır.

Bu nedenle raporda örneğin şöyle belirtilebilir:

> Analiz yayımlanmış kod matrisindeki 22 satır üzerinden yürütülmüştür. Yerel kaynak notunda açıklama metninin 18 oyuncudan söz ettiği bir kaynak uyuşmazlığı bulunduğundan özgün deneydeki katılımcı sayısı bu yeniden analizle doğrulanmış kabul edilmemiştir.

## 13. Kategorik tabloyu raporlayın

Tüm 60 ToothGrowth kaydında öğretim amacıyla `len≥20` eşiği kullanıldığında gözlenen tablo:

`[[11,19],[20,10]]`

ve beklenen tablo:

`[[15.5,14.5],[15.5,14.5]]`

şeklindedir.

Sonuçlar:

- düzeltmesiz Pearson `χ²(1)=5.406`,
- `p=.0201`,
- Cramér `V=.300`,
- iki yönlü Fisher `p=.0379`.

Örnek raporlama:

> OJ/VC uygulaması ile öğretim amacıyla tanımlanan `len≥20` kategorisi arasındaki ilişki düzeltmesiz Pearson ki-kare testiyle incelenmiştir, `χ²(1,N=60)=5.41`, `p=.020`, `V=.300`. İki yönlü Fisher testi `p=.0379` vermiştir. Yöntemlerin farklı p değerleri üretmesi nedeniyle sonuç seçimi istenen p değerine göre yapılmamıştır.

`len≥20` eşiği resmî veya biyolojik başarı eşiği değildir. Ayrıca doz düzeyleri bu tabloda birleştirilmiştir; sonuç doza göre düzeltilmiş uygulama etkisi değildir.

## 14. Etki büyüklüklerinin sınırını belirtin

Bu bölümde örneğin:

- üstünlük `A`,
- sıra-biserial,
- Kendall W,
- Cramér V

nokta tahminleri hesaplanmaktadır.

Paket bu etki büyüklükleri için güven aralıkları üretmemektedir. Önceki bölümlerdeki ortalama fark güven aralıklarını sıra temelli etki büyüklüklerine taşımayın.

## 15. Örnek bütünleşik rapor paragrafı

> Parametrik olmayan analizlerde yöntem seçimi yalnız normallik testine dayandırılmamış; bağımsızlık/eşleşme yapısı, bağlar, sıfırlar ve hedef parametreler ayrıca dikkate alınmıştır. Doz 1 düzeyindeki bağımsız OJ ve VC kayıtlarının Mann–Whitney karşılaştırmasında OJ için `U=88.5` elde edilmiş; 184756 etiket atamasının tam sayımında `p=.00223`, süreklilik düzeltmeli normal yaklaşımda `p=.00403` bulunmuştur (`A=.885`, sıra-biserial=.77). Aynı 10 kişinin sleep koşullarındaki 2−1 farklarında bir sıfır `wilcox` sıralama kuralında dışarıda bırakılmış ve dokuz sıfır olmayan farkın tam işaret sayımında `T=0`, `p=.00391` elde edilmiştir. RoundingTimes kod matrisindeki 22 blok için Friedman sonucu `Q(2)=11.14`, `W=.253` olup 99999 rastgele blok içi permütasyonla `p_MC=.00312` bulunmuştur. Kaynak açıklamasındaki 18 oyuncu ile 22 kod satırı uyuşmazlığı korunarak bildirilmiş ve sonuçlar özgün deneyin bağımsız doğrulaması veya tedavi önerisi olarak yorumlanmamıştır.

## 16. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce şunları kontrol edin:

- Bağımsız ve eşli veri yapıları doğru ayrılmış mı?
- Analiz birimi her örnekte açık mı?
- Fark ve karşılaştırma yönü belirtilmiş mi?
- Bağ ve sıfır kuralları yazılmış mı?
- U testi yalnız medyan testi olarak sunulmamış mı?
- Kesin, yaklaşık ve Monte Carlo p değerleri açıkça ayrılmış mı?
- Kullanılan p hesap yöntemi belirtilmiş mi?
- Etki büyüklükleri doğru yorumlanmış mı?
- Dunn için ortak sıralar kullanılmış mı?
- Holm ve Bonferroni birbirine karıştırılmamış mı?
- OJ Dunn, VC Dunn ve Friedman sonrası aileler ayrı tutulmuş mu?
- Genel Kruskal–Wallis/Friedman sonucu bütün çiftleri otomatik olarak anlamlı saymak için kullanılmamış mı?
- Friedman'da 22 blok bağımsız analiz birimi olarak korunmuş mu?
- 18/22 kaynak uyuşmazlığı raporlanmış mı?
- Monte Carlo standart hatası güven aralığı olarak yorumlanmamış mı?
- `len≥20` eşiğinin öğretim amaçlı olduğu belirtilmiş mi?
- Dozların birleştirildiği kategorik tablo doza göre düzeltilmiş etki olarak sunulmamış mı?
- Üretilmeyen etki büyüklüğü güven aralıkları rapora eklenmemiş mi?
- R/SPSS çalıştırılmadıysa çalıştırılmış gibi yazılmamış mı?

## Son mesaj

Parametrik olmayan analizlerde temel düşünce zinciri şöyledir:

**Araştırma sorusu → Tasarım → Analiz birimi → Bağımlılık → Sıralar/farklar → Bağlar ve sıfırlar → Test istatistiği → p hesap yöntemi → Etki büyüklüğü → Çoklu karşılaştırma ailesi → Yorum → Sınırlılık → Akademik raporlama**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.