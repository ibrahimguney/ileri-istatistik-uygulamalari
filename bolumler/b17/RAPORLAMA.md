# Bölüm 17 — Kovaryans Analizini Akademik Raporlama

Bu rehber, Bölüm 17'deki ANCOVA uygulamasını yalnız F ve p değerlerinden oluşan bir sonuç tablosu olmaktan çıkarıp **tasarım, model biçimi, koşullu karşılaştırma, belirsizlik ve sınırlılıkları birlikte içeren bilimsel bir rapora** dönüştürmek için hazırlanmıştır.

Temel düşünce zinciri:

**Araştırma sorusu → Tasarım → Kovaryatın rolü → Ortak destek → Model → Eğim → İşlevsel biçim → Koşullu kontrast → Belirsizlik → Çoklu karşılaştırma → Duyarlılık → Yorum sınırı → Akademik raporlama**

## 1. Önce tasarımı doğru adlandırın

Bu bölümde:

- yanıt: `len`,
- grup: `supp` (`OJ`, `VC`),
- sayısal değişken: `dose`

olarak kullanılır.

Ancak `dose` bir işlem öncesi başlangıç ölçümü değildir; uygulanan doz düzeyidir.

Bu nedenle raporda:

> “Başlangıç farklılıkları ANCOVA ile kontrol edildi.”

ifadesi kullanılmamalıdır.

Daha doğru ifade:

> ToothGrowth verisinde uygulama biçimleri arasındaki uzunluk farkı, gözlenen doz düzeyiyle birlikte modellenmiştir.

## 2. Veri yapısını belirtin

Analizde 60 ayrı kayıt vardır. Her `supp × dose` hücresinde 10 kayıt bulunur ve tekrarlı ölçüm varsayılmaz.

Doz düzeyleri:

`.5, 1 ve 2 mg/gün`.

Her iki uygulama grubunda da aynı üç doz bulunduğundan gözlenen düzeylerde ortak destek vardır.

## 3. Kovaryat seçimini p değerine indirgemeyin

Gerçek bir ANCOVA'da kovaryatın uygunluğu yalnız istatistiksel anlamlılığına göre belirlenmez.

Değerlendirilmesi gerekenler:

- ölçüm zamanı,
- konu alanı gerekçesi,
- ölçüm güvenirliği,
- grup örtüşmesi,
- tedavi/işlem tarafından etkilenip etkilenmediği,
- nedensel yapıda hangi rolde olduğu.

Küçük p, bir değişkenin uygun “kontrol değişkeni” olduğunu kanıtlamaz.

## 4. Referans değerini açıkça yazın

Analizde:

`x = dose − 1`

kullanıldığı için `x=0`, 1 mg/günü temsil eder.

Bu nedenle etkileşimli modelde grup ana etkisi 1 mg/gündeki OJ−VC farkını ifade eder.

Referans değerini raporlamak, katsayıların yorumlanabilirliği için gereklidir.

## 5. Kontrast yönünü belirtin

Bütün grup farkları:

`OJ − VC`

yönünde tanımlanmıştır.

Pozitif fark OJ ortalamasının VC'den yüksek olduğunu, negatif fark ise tersini gösterir.

Yön raporda belirtilmezse katsayı işaretinin anlamı belirsiz kalabilir.

## 6. Ortak eğim modelini tanımlayın

Ortak eğim modeli:

`len = beta0 + beta1 grup + beta2 x + epsilon`

şeklindedir.

Bu model grup farkını bütün dozlarda aynı olmaya zorlar.

1 mg/günde model ortalamaları:

- VC = `15.336`,
- OJ = `19.036`,
- OJ−VC = `3.700`.

Grupların ortalama dozları eşit olduğu için düzeltme iki grup ortalamasını aynı miktarda taşımış ve fark değişmemiştir.

Bu, ANCOVA işleminin yapılmadığı anlamına gelmez.

## 7. Eğim homojenliğini ayrı sınayın

Ortak eğim modeline grup×doz etkileşimi eklenerek ayrı eğimler modeli kurulur.

Model karşılaştırması:

`F(1,56)=5.333, p=.0246`.

Örnek raporlama:

> Ortak eğim modeli ile grup×doz etkileşimini içeren ayrı eğimler modeli karşılaştırıldığında etkileşim eklenmesinin model uyumunu artırdığı görüldü, `F(1,56)=5.33, p=.025`. Bu nedenle sabit grup farkına dayalı ortak-eğim yorumu tek başına yeterli kabul edilmedi.

## 8. Etkileşim bulunması model biçimini doğrulamaz

Ayrı eğimler modeli her grup için doğrusal bir doz ilişkisi varsayar.

Dolayısıyla grup×doz etkileşimi eklenmiş olsa bile:

> “Artık bütün ANCOVA varsayımları sağlandı.”

demek doğru değildir.

Doğrusal biçim ayrıca değerlendirilmelidir.

## 9. Hücre modelini işlevsel biçim denetimi olarak kullanın

Altı hücre ortalaması modeli, üç doz × iki grup ortalamasını ayrı ayrı tahmin eder.

Ayrı doğrular modeline göre karşılaştırma:

`F(2,54)=8.399, p=.000667`.

Örnek raporlama:

> Ayrı doğrusal eğimler modeli altı hücre ortalaması modeliyle karşılaştırıldığında iki ek serbestlik derecesinin anlamlı iyileşme sağladığı görüldü, `F(2,54)=8.40, p<.001`. Bu nedenle doz bazındaki grup karşılaştırmaları hücre modeli üzerinden raporlandı.

Bu sonuç etkileşimin varlığından farklı bir soruyu yanıtlar: doğrusal biçimin yeterliliği.

## 10. Model seçimini bilimsel gerekçeyle açıklayın

Bu bölümde yorum zinciri şöyledir:

1. ortak eğim modeli kuruldu,
2. ortak eğim kısıtı sorgulandı,
3. ayrı doğrular modeli kuruldu,
4. doğrusal biçim hücre modeliyle sınandı,
5. koşullu sonuçlar hücre modeline dayandırıldı.

Bu zincir yalnız “en küçük p değerine sahip model seçildi” biçiminde sunulmamalıdır.

## 11. Koşullu grup farklarını raporlayın

Hücre modeli sonuçları:

| Doz | OJ−VC | Bonferroni %95 aile aralığı | Düzeltilmiş p |
|---:|---:|---|---:|
| .5 | 5.25 | [1.24, 9.26] | .0063 |
| 1 | 5.93 | [1.92, 9.94] | .0018 |
| 2 | −.08 | [−4.09, 3.93] | 1.000 |

Örnek raporlama:

> Hücre modeli altında OJ−VC farkı .5 mg/günde `5.25` (%95 Bonferroni aile aralığı `[1.24,9.26]`), 1 mg/günde `5.93` (`[1.92,9.94]`) ve 2 mg/günde `−.08` (`[−4.09,3.93]`) olarak tahmin edildi.

## 12. “Anlamlı değil” ile “eşdeğer”i ayırın

2 mg/günde:

- fark `−.08`,
- Bonferroni aralığı `[−4.09,3.93]`.

Bu aralığın sıfırı içermesi eşdeğerlik kanıtı değildir.

Eşdeğerlik iddiası için:

- önceden belirlenmiş bilimsel eşdeğerlik sınırı,
- uygun eşdeğerlik hipotezi,
- buna göre tasarlanmış analiz

gerekir.

## 13. Çoklu karşılaştırma ailesini açıkça tanımlayın

Bu bölümde .5, 1 ve 2 mg/gündeki üç OJ−VC farkı **tek aile** olarak tanımlanmıştır.

Bonferroni düzeltmesi bu üç kontrast için uygulanır.

Bu düzeltme:

- bütün olası modelleri,
- sonradan denenmiş bütün analizleri,
- araştırma boyunca yapılmış bütün testleri

otomatik olarak kapsamaz.

## 14. Tekil aralık ve aile aralığını karıştırmayın

Model ortalamaları için verilen tekil %95 güven aralıkları ile üç OJ−VC kontrastı için verilen Bonferroni aile aralıkları farklı belirsizlik hedefleridir.

Raporunuzda aralığın hangi hedefe ait olduğunu belirtin.

## 15. Kısmi eta-kareyi doğru bağlamda verin

Ortak modelde grup testi için:

`partial eta²=.167236`.

Örnek ifade:

> Ortak-eğim modelinde grup terimi için kısmi eta-kare `.167` olarak hesaplandı.

Ancak bu değer:

- toplam ham varyansın `.167`'si,
- nedensel etkinin `.167`'si,
- bireysel yararın `.167`'si

değildir.

Kısmi eta-kare, ilgili etki kareler toplamını o etki ile model hata kareler toplamına göre ölçekleyen model-içi bir etki büyüklüğüdür.

## 16. Referans değerini değiştirmenin ne yaptığını açıklayın

Referans 2 mg/güne taşındığında ayrı-eğim modelindeki grup katsayısı:

`.446429`

olur.

Ancak:

- tahminler,
- SSE,
- global model,
- grup×doz etkileşim testi

değişmez.

Yalnız grup katsayısının hangi dozda yorumlandığı değişir.

Bu, merkezlemenin modelin bilimsel sonucunu otomatik değiştirmediğini gösterir.

## 17. Ortak destek dışına genelleme yapmayın

Her iki grup için gözlenen dozlar `.5`, `1` ve `2` mg/gündür.

`3 mg/gün` gözlenmemiştir.

Dolayısıyla:

- hücre modeli 3 mg/günde tanımlı değildir,
- doğrusal modelin 3 mg/gün tahmini ekstrapolasyondur,
- gözlenen destek içindeki sonuçlarla aynı kanıt gücünde sunulmamalıdır.

## 18. Levene sonucunu varsayım kanıtına dönüştürmeyin

Altı hücre için medyan-merkezli Levene sonucu:

`p=.148361`.

Uygun ifade:

> Levene sınaması varyans farklılığına karşı güçlü kanıt vermedi (`p=.148`); bununla birlikte büyük p değeri eşit varyans varsayımının doğru olduğunu kanıtlayan bir test olarak yorumlanmadı.

## 19. HC3 duyarlılığını doğru tanımlayın

2 mg/gün hücre farkı için:

- klasik OLS Bonferroni aralığı `[−4.093,3.933]`,
- HC3 duyarlılık aralığı `[−4.596,4.436]`.

HC3 katsayı kovaryans tahminini değiştirir.

HC3:

- modeli yeniden seçmez,
- bağımlı gözlemleri bağımsız hale getirmez,
- yanlış işlevsel biçimi düzeltmez,
- tasarım sorunlarını çözmez.

## 20. Tek-kayıt dışlama ile HC3'ü ayırın

Tek-kayıt dışlama analizinde 60 kez model yeniden kurulur ve her seferinde bir gözlem dışarıda bırakılır.

Amaç tek bir kaydın katsayıları ne kadar etkilediğini incelemektir.

HC3 ise aynı örneklemde standart hata/kovaryans duyarlılığıdır.

Bu nedenle iki yöntem farklı sorulara yanıt verir.

Tek-kayıt dışlama değerlerinin minimum–maksimum aralığı **güven aralığı değildir**.

## 21. Duyarlılık analizi otomatik silme kuralı değildir

Bir gözlemin çıkarılması sonucu değiştirse bile:

> “Bu kayıt aykırıdır, silinmelidir.”

sonucu otomatik olarak çıkmaz.

Kayıt hatası, tasarım, ölçüm ve bilimsel bağlam ayrıca değerlendirilmelidir. Ana analizde 60 kayıt korunmuştur.

## 22. Hash kontrolünün sınırını belirtin

Yerel hash ve kitap kopyasıyla bayt eşitliği dosya bütünlüğünü denetlemeye yardımcı olur.

Bunlar:

- uzak kaynaktaki hücrelerin yeniden doğrulandığını,
- özgün deneyin randomize olduğunu,
- körleme yapıldığını,
- nedensel tasarımın doğrulandığını

göstermez.

## 23. Yazılım durumunu doğru raporlayın

Referans sayısal sonuçlar Python hesabıdır.

R betiği `emmeans` ile çalışmak üzere hazırlanmıştır ancak bu dağıtım hazırlanırken çalıştırılarak doğrulanmamıştır.

SPSS kontrol listesi uygulama planıdır; çalıştırılmış çıktı veya `.sps` dosyası değildir.

Örnek ifade:

> Sayısal referans sonuçlar Python uygulamasından elde edilmiştir; R ve SPSS uygulamaları bu paket hazırlanırken çalıştırılarak doğrulanmamıştır.

## 24. Hayvan verisini insan tedavi önerisine dönüştürmeyin

`ToothGrowth` bir öğretim veri setidir ve kobay kayıtlarına dayanır.

Sonuçlardan insanlara yönelik klinik tedavi, doz veya sağlık önerisi çıkarılmamalıdır.

## 25. Gerçek ön-test kontrollü ANCOVA'da ek olarak ne raporlanır?

Yeni bir eğitim veya klinik çalışmada gerçek işlem öncesi kovaryat kullanılıyorsa ayrıca şunlar belirtilmelidir:

- ön-testin işlemden önce ölçüldüğü,
- ölçüm güvenirliği,
- gruplar arası başlangıç dağılımları,
- ortak destek,
- atama mekanizması,
- kümelenme/bağımsızlık,
- eksik veri yaklaşımı,
- kovaryatın işlemden etkilenmediğine ilişkin tasarım gerekçesi,
- önceden tanımlanmış referans değeri,
- eğim ve işlevsel biçim kontrolleri,
- planlanmış kontrast ailesi.

## 26. Örnek bütünleşik rapor

> ToothGrowth arşivindeki 60 bağımsız kayıtta `len` yanıtı, `supp` grubu ve uygulanan `dose` düzeyi birlikte modellenmiştir. Doz bir işlem öncesi ön-test olarak yorumlanmamıştır. Önce ortak-eğim modeli, ardından grup×doz etkileşimini içeren ayrı-eğim modeli değerlendirilmiştir. Ortak eğim kısıtının gevşetilmesi model uyumunu artırmıştır, `F(1,56)=5.33, p=.025`. Bununla birlikte ayrı doğrular modeli altı hücre ortalaması modeline göre de yetersiz kalmıştır, `F(2,54)=8.40, p<.001`; bu nedenle koşullu grup karşılaştırmaları hücre modeli üzerinden raporlanmıştır. OJ−VC farkları .5, 1 ve 2 mg/günde sırasıyla `5.25`, `5.93` ve `−.08` olmuş; üç kontrastlık aile için Bonferroni %95 aralıkları `[1.24,9.26]`, `[1.92,9.94]` ve `[−4.09,3.93]` bulunmuştur. Son dozda sıfırı içeren aralık eşdeğerlik kanıtı olarak yorumlanmamıştır. HC3 ve tek-kayıt dışlama analizleri farklı duyarlılık incelemeleri olarak sunulmuş, hiçbir kayıt ana analizden otomatik olarak çıkarılmamıştır. Sonuçlar gözlenen üç doz düzeyiyle sınırlandırılmış ve hayvan verisinden insanlara yönelik tedavi önerisi çıkarılmamıştır.

## 27. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Yanıt, grup ve kovaryat açıkça tanımlanmış mı?
- `dose` ön-test olarak yanlış adlandırılmamış mı?
- Kovaryat seçimi yalnız p değerine dayandırılmamış mı?
- Bağımsız gözlem birimi doğru belirtilmiş mi?
- Ortak destek değerlendirilmiş mi?
- 3 mg/gün ekstrapolasyon sınırı belirtilmiş mi?
- Referans doz yazılmış mı?
- Kontrast yönü OJ−VC olarak belirtilmiş mi?
- Ortak-eğim modeli tanımlanmış mı?
- Eğim homojenliği ayrı sınanmış mı?
- Etkileşim bulunması doğrusal biçim kanıtı sayılmamış mı?
- Hücre modeli karşılaştırması raporlanmış mı?
- Model seçiminin gerekçesi açıklanmış mı?
- Üç koşullu OJ−VC farkı doğru raporlanmış mı?
- Bonferroni ailesi açıkça tanımlanmış mı?
- Tekil ve aile-düzeyi aralıklar ayrılmış mı?
- 2 mg/gündeki anlamsız sonuç eşdeğerlik diye sunulmamış mı?
- Kısmi eta-kare nedensel/toplam varyans oranı diye yorumlanmamış mı?
- Levene `p>.05` varsayım kanıtı sayılmamış mı?
- HC3'ün neyi değiştirip neyi değiştirmediği belirtilmiş mi?
- Tek-kayıt dışlama HC3 ile karıştırılmamış mı?
- Tek-kayıt dışlama aralığı güven aralığı diye adlandırılmamış mı?
- Etkili gözlem otomatik silinmemiş mi?
- Bonferroni bütün model aramasının düzeltmesi sayılmamış mı?
- Python/R/SPSS çalıştırma durumu doğru belirtilmiş mi?
- Hash kontrolü kaynak/tasarım doğrulaması olarak sunulmamış mı?
- İnsanlara tedavi önerisinden kaçınılmış mı?

## Son mesaj

ANCOVA'da güçlü analiz yalnız bir “düzeltilmiş grup farkı” üretmek değildir.

Bilimsel düşünce zinciri:

**Tasarım → Kovaryatın bilimsel rolü → Ortak destek → Referans → Ortak eğim → Etkileşim → İşlevsel biçim → Koşullu fark → Güven aralığı → Çoklu karşılaştırma → Duyarlılık → Genelleme sınırı → Akademik raporlama**

şeklinde ilerlemelidir.

Bu bölümün temel dersi şudur: **Bir kovaryat eklemek tasarım sorunlarını otomatik olarak temizlemez; etkileşim eklemek de model biçimi sorunlarını otomatik çözmez. Koşullu sonuçlar, yalnız gözlenen destek ve savunulabilir model yapısı içinde yorumlanmalıdır.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.