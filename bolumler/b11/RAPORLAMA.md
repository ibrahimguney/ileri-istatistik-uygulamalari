# Bölüm 11 — ANOVA Sonuçlarını Akademik Raporlama

Bu rehber, Bölüm 11'deki tek yönlü ANOVA, Welch ANOVA, Tukey/Games–Howell çoklu karşılaştırmaları, iki faktörlü ANOVA ve etkileşim sonuçlarının bilimsel bir raporda doğru biçimde sunulmasına yardımcı olur.

Temel ilke:

**Genel test → etki büyüklüğü → planlı/çoklu karşılaştırmalar → etkileşim → tanılar → sınırlılıklar**

şeklinde bütüncül bir raporlama yapılmalıdır.

## 1. Önce veri yapısını ve analiz birimini yazın

Bu uygulamada iki faktör vardır:

- uygulama: OJ ve VC,
- doz: 0.5, 1 ve 2.

Toplam 2×3 = 6 hücre vardır ve her hücrede 10 ayrı hayvan kaydı bulunmaktadır. Toplam `N=60`'tır.

Bu veri 20 hayvanın üç tekrarlı ölçümü değildir.

Örnek yöntem ifadesi:

> Tarihsel ToothGrowth verisinin yerel kopyasında uygulama (OJ, VC) ve doz (0.5, 1, 2) faktörleri incelenmiştir. Altı hücrenin her birinde 10 ayrı kayıt bulunmakta ve toplam örneklem 60 gözlemden oluşmaktadır.

Kısa kaynak kopyasından kafes, ortak çevre ve özgün atama ayrıntılarının tamamı doğrulanamadığından bağımsızlık varsayımını veri tablosunun kendisinden kanıtlanmış kabul etmeyin.

## 2. OJ tek yönlü ANOVA'yı raporlayın

OJ grubunda üç doz ortalaması:

- 0.5: `13.23`,
- 1: `22.70`,
- 2: `26.06`.

Her grupta `n=10` vardır.

Klasik ANOVA sonucu:

- `F(2,27) = 31.442`,
- `p < .001`,
- `η² = .700`,
- `ω² = .670`.

Örnek raporlama:

> OJ uygulamasındaki üç kategorik doz düzeyinin ortalamaları tek yönlü ANOVA ile karşılaştırılmıştır. Doz düzeyleri arasında genel ortalama farkına ilişkin kanıt elde edilmiştir, `F(2,27)=31.44`, `p<.001`. Klasik tek yönlü model altında etki büyüklüğü `η²=.700` ve `ω²=.670` olarak hesaplanmıştır.

Eta-kare ve omega-kareyi Welch ANOVA'nın etki büyüklükleriymiş gibi sunmayın; bu değerler burada klasik tek yönlü modelin kareler toplamlarına dayanmaktadır.

## 3. Genel F testini bütün çiftlerin farklılığı olarak yorumlamayın

OJ için genel F testi anlamlıdır. Buna rağmen doz 2−1 karşılaştırmasında:

- ham fark = `3.36`,
- Tukey `p = .131`,
- %95 eşzamanlı Tukey GA `[-0.800, 7.520]`.

Aralık sıfırı içermektedir.

Bu bir çelişki değildir.

Uygun ifade:

> Genel ANOVA testi üç doz ortalamasının tamamının eşit olduğu ortak hipoteze karşı kanıt sağlamıştır. Bununla birlikte Tukey çoklu karşılaştırmasında doz 2 ile doz 1 arasındaki 3.36 birimlik farkın eşzamanlı %95 güven aralığı sıfırı içermiştir (`[-0.80, 7.52]`). Dolayısıyla anlamlı genel F testi bütün ikili karşılaştırmaların ayrı ayrı anlamlı olmasını gerektirmemektedir.

## 4. Tukey ailesini açıkça tanımlayın

OJ grubunda üç ikili karşılaştırma aynı Tukey ailesindedir:

- doz 1 − doz 0.5 = `9.47`,
- doz 2 − doz 0.5 = `12.83`,
- doz 2 − doz 1 = `3.36`.

İlk iki karşılaştırmanın aralıkları sıfırı dışlarken 2−1 karşılaştırmasının aralığı sıfırı içerir.

Raporunuzda yalnız anlamlı çiftleri seçmeyin; tanımlanan ailenin bütün karşılaştırmalarını görünür tutun.

## 5. Welch ve Games–Howell sonuçlarını ayrı varyans modeli olarak raporlayın

OJ için Welch sonucu:

`F(2,17.069) = 29.404`, `p < .001`.

Doz 2−1 için Games–Howell sonucu:

- `p = .0935`,
- yaklaşık aile GA `[-0.501, 7.221]`.

Örnek raporlama:

> Eş varyans varsayımına daha az bağımlı alternatif analiz olarak Welch ANOVA ve Games–Howell ikili karşılaştırmaları da incelenmiştir. Welch genel testi `F(2,17.07)=29.40`, `p<.001` vermiştir. Games–Howell yaklaşımında doz 2−1 farkının yaklaşık aile güven aralığı `[-0.50, 7.22]` olup sıfırı içermektedir.

Welch/Games–Howell analizini yalnız Levene testinin sonucuna göre sonradan seçilmiş otomatik yöntem gibi sunmayın.

## 6. VC analizini ayrı aile olarak raporlayın

VC grubunda doz ortalamaları:

- 0.5: `7.98`,
- 1: `16.77`,
- 2: `26.14`.

Klasik ANOVA:

- `F(2,27)=67.072`,
- `p<.001`,
- `η²=.832`,
- `ω²=.815`.

Welch sonucu:

`F(2,17.165)=59.372`, `p<.001`.

Örnek raporlama:

> VC uygulamasındaki üç doz düzeyi ayrı bir tek yönlü analiz ailesi olarak değerlendirilmiştir. Klasik ANOVA doz ortalamaları arasında genel farklılık göstermiştir, `F(2,27)=67.07`, `p<.001`, `η²=.832`, `ω²=.815`. Welch alternatifinde de genel test anlamlıdır, `F(2,17.16)=59.37`, `p<.001`.

OJ'nin hata varyansını VC analizine taşımayın.

## 7. İki faktörlü modeli doğru tanımlayın

Tüm 60 kayıt için tam 2×3 faktöriyel modelde kareler toplamları:

- uygulama: `SS = 205.350`,
- doz: `SS = 2426.434`,
- uygulama × doz: `SS = 108.319`,
- hata: `SSE = 712.106`.

Altı hücre ortalaması tahmin edildiği için hata serbestlik derecesi:

`60 − 6 = 54`

olur.

Toplam `df=59` hata serbestlik derecesi değildir.

## 8. Etkileşimi doğrudan ortak modelden raporlayın

Klasik etkileşim sonucu:

- `F(2,54)=4.107`,
- `p=.0219`,
- kısmi `η²=.132`.

Örnek raporlama:

> Uygulama ile kategorik doz arasındaki etkileşim ortak 2×3 faktöriyel modelde incelenmiştir. Uygulama × doz etkileşimi için `F(2,54)=4.11`, `p=.022` ve kısmi `η²=.132` elde edilmiştir. Bu sonuç, OJ−VC farkının üç doz düzeyinde sabit olduğu hipotezine karşı model-temelli kanıt sağlamaktadır.

OJ ve VC için ayrı ayrı elde edilen p değerlerini karşılaştırmak etkileşim testi değildir.

## 9. Kısmi eta-kareyi doğru yorumlayın

Etkileşim için:

`partial η² = SS_etkileşim / (SS_etkileşim + SSE) = .132`

olarak hesaplanmaktadır.

Kısmi eta-karelerin her birinin paydası farklı olabileceğinden ana etki ve etkileşim için hesaplanan kısmi eta-kareleri toplayarak “toplam açıklanan oran” elde etmeyin.

Ayrıca tek yönlü ANOVA'daki `η²` ile faktöriyel modeldeki kısmi `η²` aynı payda tanımına sahip değildir.

## 10. HC3 duyarlılık sonucunu doğru adlandırın

Klasik etkileşim:

`F(2,54)=4.107`, `p=.0219`.

HC3 ortak Wald duyarlılığı:

`F(2,54)=3.523`, `p=.0365`.

Örnek raporlama:

> Etkileşim sonucunun heteroskedastisiteye duyarlılığı HC3 kovaryans tahminiyle ayrıca incelenmiş ve yaklaşık ortak Wald testi `F(2,54)=3.52`, `p=.036` vermiştir. Bu hesap klasik ANOVA kareler toplamlarının robust bir yeniden ayrıştırması değil, kovaryans temelli bir duyarlılık analizidir.

HC3 kümelenmeyi, yanlış ortalama modelini veya tasarım sorunlarını otomatik olarak çözmez.

## 11. Üç OJ−VC basit etkisini aynı aile içinde raporlayın

Ortak faktöriyel modelin `MSE=13.187` ve `df=54` değerleri kullanılarak üç OJ−VC karşılaştırması tek Bonferroni ailesi olarak değerlendirilmiştir.

| Doz | OJ−VC | Bonferroni p | En az %95 aile GA |
|---|---:|---:|---:|
| 0.5 | 5.25 | .0063 | `[1.237, 9.263]` |
| 1 | 5.93 | .0018 | `[1.917, 9.943]` |
| 2 | -0.08 | 1.000 | `[-4.093, 3.933]` |

Örnek raporlama:

> Etkileşimin yorumunu desteklemek amacıyla üç doz düzeyindeki OJ−VC farkları ortak faktöriyel modelin hata varyansı kullanılarak ve üç karşılaştırmalık Bonferroni ailesi içinde incelenmiştir. OJ−VC farkları doz 0.5'te 5.25, doz 1'de 5.93 ve doz 2'de -0.08 olarak tahmin edilmiştir. Bonferroni aile aralıkları ilk iki dozda sıfırı dışlarken doz 2'de sıfırı içermiştir.

Bu Bonferroni düzeltmesi bölümdeki bütün analizler için tek bir aile hata kontrolü sağlamaz; yalnız tanımlanan üç OJ−VC karşılaştırmasını kapsar.

## 12. Doz 2 sonucunu eşdeğerlik olarak yorumlamayın

Doz 2'de OJ−VC farkı yaklaşık `-0.08` ve Bonferroni aile aralığı `[-4.093,3.933]`'tür.

Bu sonuç:

> OJ ve VC'nin doz 2'de eşdeğer olduğunu kanıtlamaz.

Eşdeğerlik iddiası için bilimsel olarak anlamlı tolerans sınırlarının önceden belirlenmesi ve uygun eşdeğerlik analizi gerekir.

## 13. Kategorik doz ile sayısal eğimi karıştırmayın

Doz düzeylerini 0.5, 1 ve 2 olarak tek sayısal yordayıcıyla modellemek bir doğrusal eğim kısıtı getirir.

Üç düzeyli kategorik faktör ise doz etkisi için iki serbestlik derecesi kullanır ve ortalamaların tek bir doğrusal çizgi üzerinde bulunmasını zorunlu kılmaz.

Özellikle 0.5, 1 ve 2 dozları eşit aralıklı olmadığından bu ayrımın raporda açık olması önemlidir.

## 14. Tanıları kanıt gibi sunmayın

Bu bölümde faktöriyel model artıkları için Shapiro sonucu yaklaşık:

`p=.669`

ve altı hücre için medyan merkezli Brown–Forsythe sonucu yaklaşık:

`p=.148`

olarak bulunmuştur.

Bu büyük p değerleri varsayımların kesin olarak sağlandığını kanıtlamaz.

Uygun ifade:

> Artık dağılımı ve hücreler arası yayılım grafiksel ve sayısal tanılarla incelenmiştir. Shapiro–Wilk ve Brown–Forsythe testlerinde .05 düzeyinde belirgin aykırılık kanıtı elde edilmemiş olmakla birlikte, bu sonuçlar model varsayımlarının kanıtı olarak değerlendirilmemiştir.

## 15. Örnek bütünleşik rapor paragrafı

> Tarihsel ToothGrowth verisinin yerel kopyasında uygulama (OJ, VC) ve kategorik doz (0.5, 1, 2) faktörleri incelenmiştir. OJ grubunda üç doz ortalaması arasında genel farklılık bulunmuştur, `F(2,27)=31.44`, `p<.001`, `η²=.700`, `ω²=.670`. Bununla birlikte üç karşılaştırmalık Tukey ailesinde doz 2−1 farkı 3.36 birim olup eşzamanlı %95 güven aralığı sıfırı içermiştir (`[-0.80,7.52]`); dolayısıyla anlamlı genel F testi bütün doz çiftlerinin ayrı ayrı farklı olduğu şeklinde yorumlanmamıştır. Tüm 60 kayıtla kurulan 2×3 faktöriyel modelde uygulama × doz etkileşimi `F(2,54)=4.11`, `p=.022`, kısmi `η²=.132` olarak bulunmuştur. HC3 kovaryansıyla yapılan duyarlılık analizinde yaklaşık ortak Wald testi `F(2,54)=3.52`, `p=.036` vermiştir. Üç doz düzeyindeki OJ−VC karşılaştırmaları ortak modelin hata varyansı altında Bonferroni ailesi olarak değerlendirilmiş; aile aralıkları doz 0.5 ve 1'de sıfırı dışlarken doz 2'de sıfırı içermiştir. Bulgular tarihsel öğretim verisinin yeniden analizine ait olup nedensel tasarım doğrulaması, insanlara genelleme veya tedavi önerisi olarak yorumlanmamıştır.

## 16. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce şunları kontrol edin:

- Faktörler, düzeyler, altı hücre ve analiz birimi doğru belirtilmiş mi?
- Bunun tekrarlı ölçüm tasarımı olmadığı açıklanmış mı?
- Genel ANOVA sonucu F, df ve p ile verilmiş mi?
- Eta-kare/omega-kare doğru modele bağlanmış mı?
- Anlamlı genel F bütün çiftlerin farklılığı şeklinde yorumlanmamış mı?
- Tukey ve Games–Howell aileleri açıkça adlandırılmış mı?
- Ham farklar ve eşzamanlı/aile güven aralıkları raporlanmış mı?
- VC analizi OJ'nin hata varyansını kullanmadan yapılmış mı?
- Faktöriyel modelde hata `df=54` doğru kullanılmış mı?
- Etkileşim ayrı p değerleri karşılaştırılarak değil ortak modelden sınanmış mı?
- Kısmi eta-kareler toplanmamış mı?
- HC3 sonucu robust kareler toplamı olarak adlandırılmamış mı?
- Bonferroni ailesinin yalnız üç OJ−VC karşılaştırmasını kapsadığı belirtilmiş mi?
- Doz 2 sonucu eşdeğerlik kanıtı olarak sunulmamış mı?
- Kategorik doz ile sayısal eğim modeli ayrılmış mı?
- Tanı testlerinin büyük p değerleri varsayım kanıtı olarak sunulmamış mı?
- Nedensellik ve genellenebilirlik sınırları belirtilmiş mi?
- R/SPSS çalıştırılmadıysa çalıştırılmış gibi raporlanmamış mı?

## Son mesaj

ANOVA çalışmalarında temel düşünce zinciri şöyledir:

**Araştırma sorusu → Faktörler ve analiz birimi → Genel model → F testi → Etki büyüklüğü → Karşılaştırma ailesi → Etkileşim → Basit etkiler → Tanı/duyarlılık → Yorum → Sınırlılık → Akademik raporlama**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.