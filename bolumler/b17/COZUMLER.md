# Çözüm ve yorum denetimi

## D yanıtları
D1: Yanıt len, grup supp, kovaryat dose'dur. Doz uygulanan koşulun düzeyidir;
önceden ölçülen başlangıç başarısı değildir.
D2: Her iki grupta .5, 1, 2 mg/gün vardır. 3 mg/gün gözlenen destek dışıdır;
hücre modeli burada tanımlı değildir ve doğrusal uzatma ayrıca savunulmalıdır.
D3: Ölçüm zamanı, konu bilgisi, güvenirlik, ortak destek ve tasarım önemlidir;
küçük p kovaryatın nedensel kontrol için uygunluğunu kanıtlamaz.

## Rehberli sonuçlar
G1: VC=15.336071, OJ=19.036071; fark=3.700000.
Grupların doz ortalaması eşittir (7/6 mg/gün); ortak eğim düzeltmesi iki ortalamayı
aynı miktarda taşır. Farkın değişmemesi düzeltme yapılmadığı anlamına gelmez.
G2: F=((SSE_ortak−SSE_ayrı)/1)/(SSE_ayrı/56)=5.333483;
p=.024631. Hata sd'leri 57 ve 56'dır. Ortak eğim kısıtı için kanıt değerlendirilir.
G3: x=0, L=[0,1,0,0]; fark=4.350714, SH=1.091266;
üçlü Bonferroni aralığı [1.657445,7.043983].
Kritik değer t_(1−.05/6,56)'dır; üç ortalama değil üç OJ−VC farkı ailedir.
G4: kısmi eta-kare=0.167236; ek grup KT/(ek grup KT+tam model hata KT).
Bu ham toplam varyansın tamamının açıklanan oranı veya nedensel etki değildir.

## Bağımsız sonuçlar
B1: 2 mg/gündeki grup katsayısı b_G+b_Gx=0.446429.
Merkezleme modelin sütun uzayını değiştirmez; tahminler, SSE ve etkileşim testi
aynıdır. Grup katsayısının hangi doza ait olduğu değişir.
B2: F=((SSE_ayrı−SSE_hücre)/2)/(SSE_hücre/54)=8.399425; p=.000667.
İki ayrı doğrunun 4 parametresinden 6 hücre ortalamasına geçilir. Etkileşim
bulmak, her grubun doz ilişkisini doğru biçiminde yeterince temsil etmeyi sağlamaz.
B3: 2 mg/günde fark −.080000; OLS Bonferroni aralığı [−4.092698,3.932698].
Bu eşdeğerlik değildir. HC3 aralığı [−4.596207,4.436207]; HC3 kovaryansı değiştirir,
60 tek-kayıt dışlama ise her seferinde modeli yeniden kurarak katsayı kararlılığını
inceler. Dışlama aralığı bir güven aralığı değildir; ana modelde 60 kayıt korunur.

## Hücre modeli: üç dozun tek ailesi
| Doz | OJ−VC | Bonferroni %95 aile aralığı | Düzeltilmiş p |
|---|---:|---|---:|
| .5 | 5.25 | [1.237302,9.262698] | .006277 |
| 1 | 5.93 | [1.917302,9.942698] | .001769 |
| 2 | −.08 | [−4.092698,3.932698] | 1 |

## H1 onarımı
1. Doz ön-test değildir; ANCOVA gözlemsel farkları otomatik nedensel etkiye dönüştürmez.
2. Medyan merkezli altı hücre Levene p=.148361; büyük p varsayım kanıtı değildir.
3. Ortak eğimde fark sabittir ama bu kısıt sorgulanmıştır; koşullu sonuçlar gerekir.
4. Ayrı doğrular da hücre modeline göre yetersizdir; etkileşim biçim sorununu bitirmez.
5. Anlamsızlık eşdeğerlik değildir; eşdeğerlik için önceden gerekçeli sınırlar gerekir.
6. Üç doz birlikte tek aile olmalıdır; bu düzeltme bütün model aramasını kapsamaz.

## P1 ve kısa rapor
P1'in tek sayısal cevabı yoktur. İşlem öncesi ölçüm, atama/kümelenme, örtüşme,
referans, model şekli ve aile kararları sonuç görülmeden gerekçelendirilmelidir.
Gerçekte yapılmayan veri toplama veya rastgeleleştirme “planlandı” olarak yazılır.

“ToothGrowth arşivindeki 60 kayıtta ortak eğim ve doğrusal biçim ayrı sınandı.
F(1,56)=5.333, p=.025 ve F(2,54)=8.399, p<.001 bulunduğundan doz bazındaki
karşılaştırma altı hücre modeline dayandırıldı. Üç OJ−VC farkı 5.25, 5.93 ve −.08;
Bonferroni aralıkları sırasıyla [1.24,9.26], [1.92,9.94], [−4.09,3.93] idi.
Son dozda eşdeğerlik iddia edilmedi; doz ön-test, sonuç insan tedavisi olarak sunulmadı.”

Referans `beklenen.json`; bütün basamaklar kodda korunur. Bu tablolar Python
hesabıdır; R/SPSS çıktısı veya yeni bir deney değildir.