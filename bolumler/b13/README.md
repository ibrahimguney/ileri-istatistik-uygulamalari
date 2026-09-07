# Bölüm 13 — Ölçek Uyarlama ve Güvenirlik

Bu bölümde ölçek puanlaması ve iç tutarlılık analizleri **ham Cronbach alfa, standart alfa, madde–kalan korelasyonu, silinirse alfa ve satır-bootstrap güven aralıkları** üzerinden incelenir. Bunun yanında, sayısal güvenirlik analizinin gerçek bir ölçek uyarlama sürecinin yalnızca bir parçası olduğu özellikle vurgulanır.

Amaç yalnızca bir alfa katsayısı hesaplamak değildir. Öğrencinin **kaynağı, madde anahtarını, eksik veri kuralını, analiz örneklemini, belirsizliği, madde kararlarını ve dilsel/kültürel uyarlama kanıtlarını birbirinden ayırabilmesi** hedeflenir.

**Önemli:** Bu paket yeni bir Türkçe ölçek geliştirme veya uyarlama çalışması değildir. Türkçe ifade taslakları, uzman incelemesi ve bilişsel görüşme etkinlikleri yalnız öğretim ve planlama amaçlıdır; yapılmış araştırma sonucu olarak sunulmamalıdır.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- ölçek maddelerinde ters puanlamayı belgelenmiş anahtara göre uygulayabilir,
- eksik yanıt ile geçerli ölçek değerini ayırabilir,
- ham alfa ile standart alfa arasındaki farkı açıklayabilir,
- madde–kalan korelasyonunu düzeltilmemiş madde–toplam korelasyonundan ayırabilir,
- “madde silinirse alfa” sonucunu otomatik madde silme kuralına dönüştürmeden yorumlayabilir,
- aynı kişileri koruyarak madde silme duyarlılığını değerlendirebilir,
- katılımcı satırı bootstrap yaklaşımının neden hücre bootstrap'ından farklı olduğunu açıklayabilir,
- persentil bootstrap güven aralığını yorumlayabilir,
- alfa katsayısının geçerlik veya kültürel eşdeğerlik kanıtı olmadığını açıklayabilir,
- ölçek uyarlamasında dilsel inceleme, bilişsel görüşme, pilot, yapı geçerliği ve değişmezlik gibi ek kanıtları planlayabilir,
- sonuçları akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` dosyalarından kaynak, madde anahtarı, eksikler ve kullanım sınırlarını inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki D1–D3 sorularıyla analiz kararlarını açıklayın.
3. `calisma.ipynb` içindeki boş hesapları tamamlayın.
4. A maddelerinde ham/standart alfa, madde–kalan ve silinirse alfa hesaplarını inceleyin.
5. A için 20000 katılımcı-satırı bootstrap sonucunu değerlendirin.
6. Aynı işlemleri C maddelerinde bağımsız olarak uygulayın.
7. Hatalı alfa ve uyarlama yorumlarını düzeltin.
8. P1 kapsamında dilsel taslak, bilişsel görüşme soruları ve uyarlama kanıt planını hazırlayın.
9. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
10. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla analiz sonuçlarını bilimsel rapor diline dönüştürün.

## Veri ve kapsam

Yerel veri, `psych::bfi` kaynağından alınmış ilk 100 kaydın A1–A5 ve C1–C5 maddelerine ait öğretim alıntısıdır.

Bu seçim:

- rastgele örneklem değildir,
- temsili örneklem değildir,
- yeni Türkçe uygulama değildir,
- ölçek uyarlamasının doğrulanması değildir.

Kaynak satırı ve yayımlanmış kayıt etiketi kişi kimliği olarak yorumlanmamalıdır.

Kaynak `psych::bfi`, John ve arkadaşlarının Big Five Inventory ölçeğiyle aynı şeymiş gibi sunulmamalıdır.

## Sabit puanlama kuralları

Yanıt aralığı `1–6`'dır.

Belgelenmiş anahtara göre:

- A1,
- C4,
- C5

bir kez `7−x` ile ters puanlanır.

Örneğin:

- A1=6 → 1,
- C5=1 → 6.

Eksik yanıt sıfır değildir ve sıfır geçerli yanıt aralığının dışındadır. Anahtar veride daha yüksek alfa elde etmek amacıyla sonradan seçilmez.

Tam kayıt sayıları:

- A maddeleri: `n=99`,
- C maddeleri: `n=98`,
- A+C ortak on madde: `n=97`.

Madde silme karşılaştırmalarında aynı kişiler korunur; madde silindikten sonra örneklemi yeniden seçmek madde değişimi ile örneklem değişimini birbirine karıştırabilir.

## A maddeleri — temel sonuçlar

| Ölçü | Sonuç |
|---|---:|
| n | 99 |
| Ham alfa | .629588 |
| Standart alfa | .651399 |
| Ortalama maddeler arası r | .272051 |
| %95 bootstrap persentil GA | [.464423, .736637] |

A1 ters anahtarlanmadan ham alfa `.437554` olmaktadır. Bu fark, belgelenmiş ters anahtarın önemini gösterir; daha yüksek alfa elde etmek için keyfî ters kodlama izni vermez.

A1 için:

- madde–kalan `r=.198701`,
- düzeltilmemiş madde–toplam `r=.513648`.

Bu iki korelasyon aynı tanım değildir; düzeltilmemiş toplam maddenin kendisini de içerir.

A4 aynı 99 kişi korunarak çıkarıldığında alfa `.675706` olur. Yaklaşık `.0461` artış otomatik madde silme kararı değildir.

## C maddeleri — temel sonuçlar

| Ölçü | Sonuç |
|---|---:|
| n | 98 |
| Ham alfa | .722610 |
| Standart alfa | .731783 |
| Ortalama maddeler arası r | .353029 |
| %95 bootstrap persentil GA | [.579608, .811465] |

C4 ve C5 bir kez ters puanlanır. Ters anahtarlama yapılmadığında alfa `−.082651`'dir. Negatif alfa gizlenmemeli veya sıfıra kırpılmamalıdır; ancak başka bir veri setindeki her negatif alfa da otomatik olarak ters anahtar hatası anlamına gelmez.

C maddeleri için madde–kalan ve aynı kişiler korunarak silinirse alfa:

| Madde | Madde–kalan r | Silinirse alfa |
|---|---:|---:|
| C1 | .545418 | .653951 |
| C2 | .502439 | .667962 |
| C3 | .512805 | .664335 |
| C4 | .493804 | .670744 |
| C5 | .387612 | .723448 |

C5'in çıkarılması alfayı yalnız yaklaşık `.00084` artırmaktadır. Böyle küçük sayısal değişiklik içerik kaybı için tek başına gerekçe değildir.

## Bootstrap ve belirsizlik

A için:

- tekrar sayısı: `20000`,
- tohum: `202613`,
- %95 persentil aralığı: `[.464423,.736637]`.

C için:

- tekrar sayısı: `20000`,
- tohum: `202614`,
- %95 persentil aralığı: `[.579608,.811465]`.

Bootstrap'ta katılımcının bütün madde satırı birlikte iadeli çekilir. Hücrelerin bağımsız çekilmesi maddeler arası kovaryans yapısını bozabilir.

Aralıklar doğrusal niceliklerle hesaplanan **persentil bootstrap** aralıklarıdır; BCa değildir. Bootstrap örneklem içi belirsizliği değerlendirir; temsili olmayan ilk-sıra seçimini temsili hale getirmez ve kültürel eşdeğerlik sorununu çözmez.

## Python ile çalıştırma

Depo kökünden:

```sh
python bolumler/b13/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

kullanabilirsiniz.

Kod veri indirmez ve paket kurmaz. `requirements.txt` doğrulama ortamındaki paket sürümlerini kaydeder. Notebook için ayrıca Jupyter gerekir. A ve C için ayrı ayrı 20000 satır-bootstrap çalıştırıldığı için analiz kısa bir süre alabilir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b13/analiz.R
```

kullanılabilir. Etkileşimli R oturumunda bölüm klasöründen `source("analiz.R")` çağrılabilir.

Temel R yeterlidir; `psych` zaten kuruluysa ek alfa karşılaştırması yapılabilir, betik paket kurmaz.

**R betiği bu dağıtım hazırlanırken çalıştırılarak doğrulanmamıştır.** Aynı tohumun R ve Python'da aynı bootstrap örneklerini üretmesi beklenmemelidir.

Bu öğrenci paketinde SPSS komut dosyası veya doğrulanmış SPSS çıktısı yoktur. Kitaptaki menü/yöntem açıklamaları çalıştırılmış SPSS analizi olarak sunulmamalıdır.

## Analizde inceleyeceğiniz temel kavramlar

- ters puanlama,
- eksik veri ve tam kayıt seçimi,
- Cronbach alfa,
- ham alfa,
- standart alfa,
- ortalama maddeler arası korelasyon,
- madde–kalan korelasyonu,
- düzeltilmemiş madde–toplam korelasyonu,
- silinirse alfa,
- katılımcı-satırı bootstrap,
- persentil güven aralığı,
- iç tutarlılık,
- madde içeriği,
- dilsel/kültürel uyarlama,
- bilişsel görüşme,
- pilot çalışma,
- yapı geçerliği,
- ölçme değişmezliği.

## Üretilen dosyalar

`sonuclar/` klasöründe:

- `ozet.json`,
- `puanlanmis_A.csv`,
- `puanlanmis_C.csv`,
- `madde_A.csv`,
- `madde_C.csv`,
- `kovaryans_A.csv`,
- `kovaryans_C.csv`,
- `korelasyon_A.csv`,
- `korelasyon_C.csv`

üretilir.

`grafikler/` klasöründe:

- `b13-madde-analizi.pdf`,
- `b13-bootstrap.pdf`

oluşturulur.

Puanlanmış CSV dosyalarında ters anahtar zaten uygulanmıştır; ikinci kez terslemeyin. Ham CSV değiştirilmez.

## Sonuçları yorumlarken dikkat

Özellikle şu hatalardan kaçının:

- Alfa `.70`'i geçti diye ölçeğin geçerli veya Türkçeye uyarlanmış olduğunu söylemeyin.
- Alfa katsayısını tek başına kültürel eşdeğerlik veya kullanım uygunluğu kanıtı olarak sunmayın.
- Negatif madde ilişkisini veriye bakarak otomatik ters anahtar seçme gerekçesi yapmayın.
- Madde–toplam korelasyonunu madde–kalan korelasyonuyla eşitlemeyin.
- “Silinirse alfa yükseliyor” diye maddeyi otomatik çıkarmayın.
- Madde silme karşılaştırmasında örneklemi de değiştirerek iki etkiyi karıştırmayın.
- Aynı maddeleri çoğaltarak yükselen alfayı yeni güvenirlik kanıtı saymayın.
- Bootstrap'ın örneklem seçimi veya kültürel uyarlama sorunlarını çözdüğünü söylemeyin.
- A ve C maddelerinin ortak 97 kayıtta alfa hesaplanabilmesini geçerli tek bir toplam puan oluşturma gerekçesi saymayın.
- Bu pakette hesaplanmayan omega, test–tekrar test, faktör yapısı veya değişmezlik sonuçlarını varmış gibi raporlamayın.
- Öğretim amaçlı Türkçe madde taslaklarını onaylanmış çeviri olarak sunmayın.

## Ölçek uyarlama kanıtı

Gerçek bir uyarlama çalışması yalnız iç tutarlılık katsayısından oluşmaz. En azından araştırma amacına göre şu kanıt alanları planlanmalıdır:

- kaynak ve kullanım koşullarının belgelenmesi,
- dilsel taslakların karşılaştırılması,
- uzman incelemesi,
- bilişsel görüşmeler,
- hedef grupta pilot çalışma,
- faktör yapısının incelenmesi,
- hedef puan için uygun güvenirlik kanıtları,
- gerektiğinde grup/dil ölçme değişmezliği,
- kullanım ve raporlama sınırlarının tanımlanması.

[GOREVLER.md](GOREVLER.md) içindeki P1 tablosu bu süreci planlamak içindir. Gerçekte yapılmamış görüşme, uzman değerlendirmesi veya pilot sonuçları uydurulmamalıdır.

## Akademik raporlama

Ham/standart alfa, madde analizi, bootstrap belirsizliği ve uyarlama sınırlarının bilimsel bir raporda nasıl sunulabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi bir rapor yalnız `α=.72` yazmaz; **kaynağı, puanlama anahtarını, n'yi, eksik veri kuralını, alfa türünü, belirsizlik aralığını, madde kararlarını ve hangi uyarlama kanıtlarının henüz bulunmadığını** açıkça belirtir.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Gerçekte hangi denetimlerin çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir.

Bu bölümün sonuçları yerel ilk 100 kayıt alıntısının yeniden analizidir; Türkçe uyarlama, klinik kullanım, yapı geçerliği veya dış doğrulama sonucu değildir.