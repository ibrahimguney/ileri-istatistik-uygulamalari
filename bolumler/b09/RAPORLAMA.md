# Bölüm 9 — Aracılık ve Düzenleyicilik Sonuçlarını Akademik Raporlama

Bu rehber, Bölüm 9'daki simülasyon sonuçlarının bilimsel bir raporda doğru ve ölçülü biçimde sunulmasına yardımcı olur.

> **Zorunlu raporlama bilgisi:** Bu bölümdeki bütün veriler simülasyondur. Bulgular gerçek katılımcılara veya gerçek bir araştırmaya ait değildir.

Aracılık ve düzenleyicilik iki ayrı simülasyon mekanizmasıdır. Sonuçları tek bir modelin parçalarıymış gibi birleştirmeyin.

## 1. Aracılık modelini tanımlayın

Aracılık analizinde temel yollar:

- `a`: X → M,
- `b`: M → Y, X modeldeyken,
- `c'`: X → Y doğrudan yolu, M modeldeyken,
- `c`: X → Y toplam ilişkisi,
- `ab`: model-temelli dolaylı etki.

Bu simülasyonda tahminler:

- `a = 0.633`,
- `b = 0.824`,
- `c' = 0.135`,
- `ab = 0.522`,
- `c = 0.657`.

Aynı doğrusal modeller altında `c = c' + ab` eşitliği sağlanmaktadır.

Örnek raporlama:

> Simülasyon verisinde X ile M arasındaki yol `a = 0.633`, X kontrol edildiğinde M ile Y arasındaki yol `b = 0.824` olarak tahmin edilmiştir. X'in M üzerinden Y ile ilişkisini özetleyen yol çarpımı `ab = 0.522` olarak bulunmuştur. X'in M modeldeyken doğrudan yolu `c' = 0.135`, toplam X–Y ilişkisi ise `c = 0.657` olarak tahmin edilmiştir.

Bu katsayıları gerçek bir nedensel mekanizmanın kanıtı olarak sunmayın.

## 2. Dolaylı etki için bootstrap yöntemini açıkça yazın

Bu bölümde dolaylı etkinin belirsizliği:

- `B = 5000` bootstrap yeniden örneklemesi,
- satır bazlı yeniden örnekleme,
- `seed = 202610`,
- %95 **persentil** bootstrap aralığı

kullanılarak değerlendirilmiştir.

Sonuçlar:

- `ab = 0.522`,
- bootstrap `SE = 0.083`,
- %95 persentil bootstrap aralığı `[0.369, 0.698]`.

Örnek raporlama:

> Model-temelli dolaylı etkinin belirsizliği 5000 satır bazlı bootstrap yeniden örneklemesiyle değerlendirilmiştir. Dolaylı etki `ab = 0.522` olarak tahmin edilmiş, bootstrap standart hatası 0.083 ve %95 persentil bootstrap güven aralığı `[0.369, 0.698]` olarak bulunmuştur. Bu simülasyon örneğinde aralık sıfırı içermemektedir.

## 3. Bootstrap sonucunu aşırı yorumlamayın

Uygun olmayan ifade:

> Bootstrap sonucuna göre gerçek nedensel aracılık kanıtlanmıştır.

Daha uygun ifade:

> Simülasyon verisinde tanımlanan regresyon modelleri altında dolaylı yol çarpımının %95 persentil bootstrap aralığı sıfırı dışlamıştır.

Bu analiz:

- BCa aralığı kullanmaz,
- bootstrap p değeri hesaplamaz,
- gerçek nedensel mekanizma kanıtlamaz,
- tek bir simülasyon üzerinden yöntemin kapsama oranını değerlendirmez.

## 4. Yeniden örnekleme birimini doğru belirtin

Bootstrap sırasında X, M ve Y sütunları ayrı ayrı örneklenmez. Aynı gözleme ait değerler aynı satırla birlikte yeniden örneklenir.

Raporunuzda gerektiğinde şu ifade kullanılabilir:

> Bootstrap yeniden örneklemesinde analiz birimi gözlem satırı olarak korunmuş; X, M ve Y değerleri aynı satır indisleriyle birlikte yeniden örneklenmiştir.

Sütunların bağımsız örneklenmesi değişkenler arasındaki ortak yapıyı bozardı.

## 5. “Tam aracılık” ifadesinde dikkatli olun

Sadece `c'` yolunun tekil p değerine bakarak kesin biçimde “tam aracılık vardır” veya “tam aracılık yoktur” demeyin.

Bu bölümün temel odağı dolaylı etkinin tahmini ve belirsizliğidir. Aracılık sonucunu tek bir doğrudan-yol anlamlılık kararına indirgemeyin.

## 6. Düzenleyicilik modelini tanımlayın

Düzenleyicilik örneği aracılık örneğinden ayrı bir yanıt değişkeni üzerinde kurulmuştur:

`Y = β₀ + β₁X + β₂W + β₃XW + ε`

Etkileşim sonucu:

- `b_XW = 0.559`,
- `SE = 0.072`,
- `t(156) = 7.74`,
- %95 klasik güven aralığı `[0.416, 0.702]`.

Örnek raporlama:

> Ayrı düzenleyicilik simülasyonunda X × W etkileşim katsayısı pozitif bulunmuştur (`b = 0.559`, `SE = 0.072`, `t(156) = 7.74`, %95 GA `[0.416, 0.702]`). Bu sonuç, simülasyon modeli kapsamında X ile Y arasındaki eğimin W düzeyine göre değiştiğini göstermektedir.

Bu ifade simülasyon modeline ilişkindir; gerçek bir popülasyondaki nedensel düzenleyicilik sonucu değildir.

## 7. Merkezlemeyi doğru açıklayın

X ve W'nin merkezlenmesi ham ve merkezlenmiş modellerin aynı tahmin edilen Y değerlerini üretmesine engel değildir. Merkezleme özellikle alt terimlerin ve sabit terimin yorumlandığı referans noktasını değiştirir.

Uygun ifade:

> Merkezleme modelin etkileşim katsayısını veya tahmin edilen değerlerini ortadan kaldırmamış; alt terimlerin yorumlandığı referans noktalarını değiştirmiştir.

Yanlış ifade:

> Değişkenleri merkezleyince etkileşim ortadan kalktı.

## 8. Basit eğimleri raporlayın

Bu simülasyonda W'nin üç düzeyi için basit eğimler şöyledir:

| W düzeyi | X'in basit eğimi | Noktasal %95 GA |
|---|---:|---:|
| Ortalama −1 SS | -0.181 | `[-0.402, 0.039]` |
| Ortalama | 0.398 | `[0.245, 0.552]` |
| Ortalama +1 SS | 0.978 | `[0.772, 1.184]` |

Örnek raporlama:

> X'in Y ile model-temelli ilişkisi W düzeyine göre farklılaşmıştır. W ortalamanın bir standart sapma altında olduğunda basit eğim `b = -0.181` (%95 GA `[-0.402, 0.039]`), ortalama düzeyinde `b = 0.398` (%95 GA `[0.245, 0.552]`) ve ortalamanın bir standart sapma üzerinde olduğunda `b = 0.978` (%95 GA `[0.772, 1.184]`) olarak tahmin edilmiştir.

Bu aralıklar üç ayrı **noktasal** güven aralığıdır; eşzamanlı güven bandı değildir.

## 9. Basit eğimlerin p değerlerini etkileşim testiyle karıştırmayın

Düşük W düzeyindeki eğimin tekil p değeri yaklaşık `.106` iken yüksek W düzeyindeki eğimin p değeri çok küçük olabilir. Ancak:

> “Bir eğim anlamlı, diğeri anlamsız; o halde etkileşim anlamlıdır.”

şeklindeki çıkarım doğru değildir.

Etkileşim kararı doğrudan `X × W` katsayısı üzerinden değerlendirilmelidir.

## 10. Basit eğim belirsizliğinde kovaryansı unutmayın

Belirli bir merkezlenmiş W değeri (`W_c`) için basit eğim varyansı:

`Var(b_X) + W_c² Var(b_XW) + 2 W_c Cov(b_X, b_XW)`

biçimindedir.

Kovaryans terimini keyfî olarak çıkarmak genellikle yanlış standart hata üretir. `W_c = 0` özel durumunda ilgili terimler doğal olarak sadeleşir.

## 11. Bu bölümde yapılmayan analizleri raporlamayın

Bu öğrenci paketi şunları yapmaz:

- PROCESS analizi,
- BCa bootstrap,
- Johnson–Neyman analizi,
- koşullu dolaylı etki,
- düzenleyicili aracılık,
- aracılı düzenleyicilik,
- gerçek katılımcı verisinde nedensel mekanizma testi.

Aynı veri dosyasında M ve W değişkenlerinin bulunması bu analizlerin yapılmış olduğu anlamına gelmez.

## 12. Örnek bütünleşik aracılık paragrafı

> Öğretim amacıyla üretilmiş simülasyon verisinde X'in M üzerinden Y ile model-temelli dolaylı ilişkisi regresyon temelli aracılık analiziyle incelenmiştir. X–M yolu `a = 0.633`, M–Y yolu X kontrol edildiğinde `b = 0.824` ve yol çarpımı `ab = 0.522` olarak tahmin edilmiştir. Dolaylı etkinin belirsizliği 5000 satır bazlı bootstrap yeniden örneklemesiyle değerlendirilmiş ve %95 persentil bootstrap güven aralığı `[0.369, 0.698]` olarak bulunmuştur. Aralık bu simülasyon örneğinde sıfırı dışlamaktadır. Doğrudan yol `c' = 0.135`, toplam ilişki `c = 0.657` olarak tahmin edilmiştir. Bulgular simülasyon verisine ve belirtilen modellere ait olduğundan gerçek bir nedensel aracılık mekanizmasının kanıtı olarak yorumlanmamıştır.

## 13. Örnek bütünleşik düzenleyicilik paragrafı

> Ayrı bir simülasyon yanıtı üzerinde X ile W arasındaki etkileşim incelenmiştir. Etkileşim katsayısı `b = 0.559` (`SE = 0.072`, `t(156) = 7.74`, %95 GA `[0.416, 0.702]`) olarak bulunmuştur. Basit eğim analizinde X'in Y ile ilişkisi W'nin ortalamanın bir standart sapma altındaki düzeyinde `b = -0.181`, ortalama düzeyinde `b = 0.398` ve ortalamanın bir standart sapma üzerindeki düzeyinde `b = 0.978` olarak tahmin edilmiştir. Bu üç aralık noktasal güven aralıklarıdır ve Johnson–Neyman analizi veya eşzamanlı güven bandı olarak yorumlanmamıştır. Sonuçlar yalnızca öğretim amacıyla üretilmiş simülasyon mekanizmasını göstermektedir.

## 14. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce şunları kontrol edin:

- Verinin simülasyon olduğu açıkça belirtilmiş mi?
- Aracılık ve düzenleyicilik ayrı mekanizmalar olarak sunulmuş mu?
- `a`, `b`, `c`, `c'` ve `ab` doğru tanımlanmış mı?
- Bootstrap sayısı (`B=5000`) belirtilmiş mi?
- Yeniden örnekleme biriminin satır olduğu açıklanmış mı?
- Aralık doğru biçimde “persentil bootstrap” olarak adlandırılmış mı?
- BCa veya hesaplanmamış bootstrap p değeri raporlanmamış mı?
- `c'` tek başına kesin “tam aracılık” kararı için kullanılmamış mı?
- Etkileşim katsayısı doğrudan raporlanmış mı?
- Merkezlemenin rolü doğru açıklanmış mı?
- Basit eğimler ve noktasal güven aralıkları verilmiş mi?
- Basit eğim p değerleri doğrudan etkileşim testi yerine kullanılmamış mı?
- Johnson–Neyman veya koşullu dolaylı etki yapılmış gibi gösterilmemiş mi?
- Simülasyon sonucu nedensel gerçek araştırma bulgusu gibi sunulmamış mı?
- R veya PROCESS çalıştırılmadıysa çalıştırılmış gibi raporlanmamış mı?

## Son mesaj

Aracılık ve düzenleyicilik analizlerinde temel düşünce zinciri şöyledir:

**Kuramsal soru → Değişken rolleri → Model → Yol/etkileşim → Belirsizlik → Bootstrap/basit eğim → Görselleştirme → Yorum → Sınırlılık → Akademik raporlama**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.