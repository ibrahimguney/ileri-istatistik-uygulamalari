# Bölüm 17 — Kovaryans Analizi (ANCOVA)

Bu bölümde **kovaryans analizi (ANCOVA)**, grup karşılaştırmasını sayısal bir değişkenle birlikte modellemenin ötesinde, model varsayımlarının ve koşullu karşılaştırmaların nasıl incelenmesi gerektiğini göstermek için kullanılır. `ToothGrowth` arşivindeki 60 kayıt üzerinden ortak eğim, ayrı eğimler ve hücre ortalamaları modelleri karşılaştırılır.

**Önemli:** Bu veri setinde `dose` bir işlem öncesi ön-test değildir; uygulanan doz düzeyidir. Dolayısıyla bu örnek, klasik “başlangıç puanına göre düzeltilmiş grup karşılaştırması” biçimindeki ANCOVA ile aynı araştırma tasarımı değildir. Hücre ortalamaları modeli de sayısal kovaryatlı ANCOVA değildir. fileciteturn50file0

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- yanıt, grup ve sayısal kovaryatı doğru tanımlayabilir,
- bir değişkenin neden yalnız p değerine göre kovaryat seçilemeyeceğini açıklayabilir,
- ortak destek/örtüşme kavramını değerlendirebilir,
- ortak eğim ANCOVA modelini kurabilir,
- grup×kovaryat etkileşimiyle eğim homojenliğini sınayabilir,
- ortak eğim ve doğrusal biçim varsayımlarını birbirinden ayırabilir,
- ayrı doğrular modelini hücre ortalamaları modeliyle karşılaştırabilir,
- belirli dozlarda koşullu grup farklarını hesaplayabilir,
- kontrast yönünü ve referans değerini açıkça belirtebilir,
- tekil güven aralığı ile aile-düzeyinde Bonferroni aralığını ayırabilir,
- kısmi eta-kareyi doğru bağlamda yorumlayabilir,
- HC3 ile tek-kayıt dışlama duyarlılığını ayırabilir,
- anlamsızlık ile eşdeğerlik arasındaki farkı açıklayabilir,
- ANCOVA sonuçlarını akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ile veri kaynağını, tasarımı ve analiz sınırlarını okuyun.
2. [GOREVLER.md](GOREVLER.md) D1–D3 ile yanıt, grup, kovaryat ve ortak destek sorularını çözün.
3. `calisma.ipynb` içinde ortak eğim modelini kurun.
4. Grup×doz etkileşimi ekleyerek eğim homojenliğini inceleyin.
5. Ayrı eğimler modelini altı hücre ortalaması modeliyle karşılaştırarak doğrusal biçimi değerlendirin.
6. Önceden tanımlı OJ−VC kontrastlarını .5, 1 ve 2 mg/gün için hesaplayın.
7. Bonferroni aile aralıklarını ve düzeltilmiş p değerlerini inceleyin.
8. HC3 ve tek-kayıt dışlama duyarlılıklarını karşılaştırın.
9. Sonuçları [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile denetleyin.
10. [RAPORLAMA.md](RAPORLAMA.md) ile sonuçları bilimsel rapor diline dönüştürün.

## Veri ve araştırma sorusu

Kaynak R `datasets::ToothGrowth` arşividir. Veri setinde 60 ayrı kobay kaydı bulunur; her `supp × dose` hücresinde 10 kayıt vardır ve tekrarlı ölçüm varsayılmaz. fileciteturn50file0

Değişkenler:

- **Yanıt:** `len`
- **Grup:** `supp` (`OJ` ve `VC`)
- **Sayısal değişken:** `dose` (`.5`, `1`, `2` mg/gün)

Analizde:

`x = dose − 1`

ile 1 mg/gün referans alınır.

Kontrast yönü her zaman:

`OJ − VC`

olarak tanımlanır.

Her iki grupta da `.5`, `1` ve `2` mg/gün gözlendiği için bu üç düzeyde ortak destek vardır. `3 mg/gün` ise gözlenen destek dışındadır; oradaki yorum doğrusal ekstrapolasyon gerektirir ve hücre modeli orada tanımlı değildir.

## Model 1 — Ortak eğim

Ortak eğim modeli kavramsal olarak:

`len = beta0 + beta1 grup + beta2 x + epsilon`

şeklindedir.

Bu modelde OJ−VC farkı bütün dozlarda sabit olmaya zorlanır.

Model:

- 3 parametre,
- hata `sd=57`

ile tahmin edilir.

1 mg/gün için düzeltilmiş/tahmin edilen ortalamalar:

- VC = `15.336071`,
- OJ = `19.036071`,
- OJ−VC = `3.700000`.

Grupların doz ortalamaları bu veri setinde eşit olduğundan ortak eğim düzeltmesi iki grup ortalamasını aynı miktarda taşır ve fark değişmez. Bu durum “düzeltme yapılmadığı” anlamına gelmez. fileciteturn49file0

## Model 2 — Ayrı eğimler

Eğim homojenliğini incelemek için grup×doz etkileşimi eklenir:

`len = beta0 + beta1 grup + beta2 x + beta3(grup×x) + epsilon`

Bu model:

- 4 parametre,
- hata `sd=56`

kullanır.

Ortak ve ayrı eğim modelleri karşılaştırıldığında:

`F(1,56)=5.333483, p=.024631`

elde edilir. fileciteturn49file0

Bu sonuç ortak eğim kısıtının sorgulanması gerektiğini gösterir. Ancak etkileşimin eklenmesi doğrusal biçimin otomatik olarak yeterli olduğu anlamına gelmez.

## Model 3 — Hücre ortalamaları

Üç doz × iki uygulama biçimi için altı hücre ortalaması ayrı tahmin edilir.

Model:

- 6 parametre,
- hata `sd=54`

kullanır.

Ayrı eğimler modeli hücre modeliyle karşılaştırıldığında:

`F(2,54)=8.399425, p=.000667`

elde edilir. fileciteturn49file0

Bu sonuç, yalnız grup×doz doğrusal etkileşimi eklemenin doz ilişkisini yeterince temsil etmediğini gösterir. Dolayısıyla bu örnekte koşullu yorumlar hücre ortalamaları modeline dayandırılır.

## Üç modelin mantığı

| Model | Temel kısıt | Parametre | Hata sd |
|---|---|---:|---:|
| Ortak eğim | Grupların eğimleri aynı | 3 | 57 |
| Ayrı eğimler | Her grup için ayrı doğrusal eğim | 4 | 56 |
| Hücre modeli | Altı hücre ortalaması serbest | 6 | 54 |

İç içe model F karşılaştırmalarında payda olarak her karşılaştırmanın kendi **tam modelinin hata karesi** kullanılır.

## Koşullu karşılaştırmalar

Hücre modelinde üç OJ−VC farkı tek bir karşılaştırma ailesi olarak ele alınır:

| Doz (mg/gün) | OJ−VC | Bonferroni %95 aile aralığı | Düzeltilmiş p |
|---:|---:|---|---:|
| .5 | 5.25 | [1.237, 9.263] | .006277 |
| 1 | 5.93 | [1.917, 9.943] | .001769 |
| 2 | −.08 | [−4.093, 3.933] | 1.000 |

Bu sonuçlar **doza koşullu** grup karşılaştırmalarıdır. fileciteturn49file0

2 mg/gündeki `−.08` farkının istatistiksel olarak anlamlı olmaması, OJ ve VC'nin eşdeğer olduğunu kanıtlamaz. Eşdeğerlik için önceden gerekçelendirilmiş eşdeğerlik sınırları ve uygun bir eşdeğerlik testi gerekir.

## Bonferroni ailesini doğru tanımlayın

Üç doz için OJ−VC farkları aynı karşılaştırma ailesidir.

Bonferroni kritik değeri üç iki-taraflı karşılaştırma için:

`t_(1−.05/6, df)`

şeklindedir.

Ortalama tahminlerinin tekil %95 aralıkları ile üç grup farkının Bonferroni aile aralıklarını birbirine karıştırmayın.

Ortak eğim modelinde aynı grup farkının üç dozda tekrar yazılması üç bağımsız karşılaştırma oluşturmaz; model farkı zaten sabit tutmaktadır.

## Referans değerinin değiştirilmesi

Ayrı eğimler modelinde referans 1 mg/günden 2 mg/güne taşındığında grup katsayısı:

`b_G + b_Gx = .446429`

olur.

Merkezleme/referans değişikliği:

- modelin sütun uzayını,
- tahminlerini,
- SSE'yi,
- etkileşim testini

değiştirmez.

Yalnız katsayıların yorumlandığı doz değişir.

## Kısmi eta-kare

Ortak modelde grup testi için:

`partial eta² = .167236`.

Bu değer ek grup kareler toplamının, ek grup kareler toplamı ile tam model hata kareler toplamı toplamına oranıdır.

Bu değer:

- ham toplam varyansın `%16.7`'si,
- nedensel etkinin `%16.7`'si,
- bireylerin `%16.7`'sinin fayda gördüğü

anlamına gelmez.

## Varsayım ve model biçimi

ANCOVA'da iki farklı soru ayrılmalıdır:

1. **Ortak eğim uygun mu?**
2. **Doz ile yanıt arasındaki doğrusal biçim uygun mu?**

Grup×doz etkileşimi yalnız ilk soruyu genişletir. Ayrı doğruların hücre modeline göre yetersiz olması, ikinci sorunun ayrıca değerlendirilmesi gerektiğini gösterir.

Bu nedenle:

**“Etkileşimi ekledik, model sorunu çözüldü.”**

sonucu doğru değildir.

## Levene testi

Altı hücre için medyan-merkezli Levene sonucu yaklaşık:

`p=.148361`.

Bu büyük p değeri eşit varyans varsayımının kanıtlandığı anlamına gelmez. Varsayım değerlendirmesi tasarım, grafikler, artıklar, örneklem büyüklüğü ve duyarlılık analizleriyle birlikte yapılmalıdır.

## HC3 duyarlılığı

Hücre modelinin 2 mg/gün OJ−VC farkı için klasik OLS Bonferroni aralığı:

`[-4.092698, 3.932698]`

iken HC3 yaklaşımı:

`[-4.596207, 4.436207]`

verir. fileciteturn49file0

HC3 katsayı kovaryans tahminini değiştirir; modeli yeniden seçmez, bağımlılığı düzeltmez ve tasarım sorunlarını çözmez.

## Tek-kayıt dışlama duyarlılığı

60 tek-kayıt dışlama analizinde her seferinde bir kayıt çıkarılarak model yeniden tahmin edilir.

Bu işlem katsayıların tek gözlemlere duyarlılığını inceler.

HC3 ile aynı şey değildir:

- **HC3:** aynı veri ve katsayılarla kovaryans/standart hata duyarlılığı,
- **tek-kayıt dışlama:** veri setini değiştirip modeli yeniden tahmin ederek gözlem etkisi duyarlılığı.

Tek-kayıt dışlama sonuç aralığı bir güven aralığı değildir ve ana analizde hiçbir kayıt otomatik olarak silinmez.

## Python ile çalıştırma

Depo kökünden:

```sh
python bolumler/b17/analiz.py
```

Bölüm klasöründen:

```sh
python analiz.py
```

kullanabilirsiniz.

Kod kaynak CSV'yi değiştirmez. Çalıştırma daha önce üretilmiş sonuç dosyalarını yeniler.

Python'u `-O` seçeneğiyle çalıştırmayın; doğrulama kontrolleri korunmalıdır.

## R ile çalıştırma

Bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

R için önceden kurulu `emmeans` paketi gerekir; betik paket kurmaz.

**Bu dağıtım hazırlanırken R analizi çalıştırılarak doğrulanmamıştır.**

## SPSS yolu

`spss-kontrol-listesi.md`, SPSS'te uygulanacak adımlar için bir çalışma/kontrol listesidir.

Bu dosya:

- çalıştırılmış SPSS çıktısı değildir,
- `.sps` syntax dosyası değildir,
- Python sonuçlarının SPSS tarafından doğrulandığını göstermez.

Bu dağıtım hazırlanırken SPSS çalıştırılmamıştır.

## Üretilen dosyalar

`sonuclar/ozet.json` içinde sürümler, model katsayıları, F testleri, tahmini ortalamalar, kontrastlar ve duyarlılık özetleri yer alır.

CSV çıktıları:

- katsayı kovaryansları,
- HC3 matrisleri,
- tahmini ortalamalar,
- karşılaştırmalar,
- altı hücre özeti,
- tanılar,
- 60 tek-kayıt dışlama sonucu

gibi denetlenebilir ara sonuçları saklar.

Türetilmiş `doz_uzunluk.csv` dosyası `sonuclar/` içine yazılır.

`grafikler/b17-egimler-karsilastirmalar.pdf` kodla yeniden üretilir.

Kaynak CSV değiştirilmez.

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- `dose` değişkenini ön-test olarak adlandırmayın.
- ANCOVA'nın bütün başlangıç farklarını otomatik “temizlediğini” söylemeyin.
- Kovaryatı yalnız p değerine göre seçmeyin.
- Ortak destek dışındaki 3 mg/gün değerine hücre modeli sonucu atfetmeyin.
- Levene `p>.05` sonucunu eşit varyansın kanıtı saymayın.
- Ortak eğim modelindeki tek farkı bütün dozlar için sorgulanamaz gerçek gibi sunmayın.
- Etkileşim eklenince doğrusal biçim sorununun çözüldüğünü varsaymayın.
- 2 mg/gündeki anlamsız farkı eşdeğerlik olarak yorumlamayın.
- Tekil ortalama aralıklarını Bonferroni kontrast aralıklarıyla karıştırmayın.
- Model başına Bonferroni düzeltmesini bütün model aramasının hata kontrolü saymayın.
- HC3 ile tek-kayıt dışlamayı aynı duyarlılık analizi olarak sunmayın.
- Tek-kayıt dışlama aralığını güven aralığı olarak yorumlamayın.
- Hash kontrolünü uzak kaynak doğrulaması veya randomizasyon kanıtı saymayın.
- Hayvan verisinden insanlara tedavi önerisi üretmeyin.

## Yeni ön-test kontrollü çalışma için protokol

Gerçek bir eğitim/klinik ANCOVA çalışmasında önceden tanımlanması gereken başlıca kararlar:

1. hedef grup karşılaştırması ve yanıt,
2. gerçekten işlem öncesi ölçülen kovaryat,
3. kovaryatın ölçüm zamanı ve güvenirliği,
4. gruplar arasında ortak destek,
5. atama, bağımsızlık ve olası kümelenme,
6. kovaryat referans değeri,
7. eğim homojenliği değerlendirmesi,
8. doğrusal/işlevsel biçim değerlendirmesi,
9. önceden tanımlı karşılaştırma ailesi,
10. eksik veri yaklaşımı,
11. aykırı/etkili gözlem politikası,
12. sağlamlık ve duyarlılık analizleri,
13. örneklem planı,
14. nedensel yorum sınırı.

Gerçekte yapılmayan randomizasyon, veri toplama veya ölçüm işlemleri sonuç bölümünde yapılmış gibi yazılmamalıdır; yeni araştırma protokolünde “planlandı” olarak belirtilmelidir.

## Akademik raporlama

ANCOVA sonuçlarının yöntem ve bulgu bölümünde nasıl raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi raporlama yalnız “F ve p” vermek değildir. **Tasarım, kovaryatın rolü, ortak destek, model biçimi, referans değeri, koşullu kontrastlar, güven aralıkları, çoklu karşılaştırma ailesi, duyarlılık ve yorum sınırları** birlikte sunulmalıdır.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Gerçekte hangi testlerin yapıldığı ve hangi yazılımların çalıştırılmadığı `DOGRULAMA.json` dosyasında belirtilmiştir.

Yerel kaynak hash'i ve kod kontrolleri yeniden üretilebilirliği destekler; uzak veri doğrulaması, özgün deneyin randomizasyonu veya nedensel geçerlik kanıtı değildir.