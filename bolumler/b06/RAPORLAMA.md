# Bölüm 6 — Korelasyonu Akademik Raporlama

Bu rehber, korelasyon analizini yalnız bir katsayı ve p değeriyle değil; **veri kaynağı, analiz örneklemi, ilişkinin biçimi, belirsizlik, duyarlılık ve nedensellik sınırıyla birlikte** raporlamak için hazırlanmıştır.

Temel zincir:

**Araştırma sorusu → Veri ve eşleşme → Grafik → Katsayı türü → Tahmin → Belirsizlik → Duyarlılık → Permütasyon → Yorum → Sınırlılık → Akademik raporlama**

## 1. Araştırma sorusunu birliktelik diliyle yazın

Bu bölümün ana sorusu:

> İlk 60 kayıtta birinci dönem notu (G1) ile yıl sonu notu (G3) arasındaki doğrusal ve sıralı birliktelik ne düzeydedir?

“G1, G3'ü etkiler mi?” aynı soru değildir. Korelasyon analizi tek başına nedensel etkiyi tanımlamaz.

## 2. Veri kaynağını ve yerel kapsamı belirtin

Veri, UCI Student Performance veri setinin Portekizce dersi bölümünden alınmış yerel bir alıntıdır.

Tam kaynak 649 kayıt içerirken bu öğrenci paketinde ilk 80 kaydın `school`, `G1`, `G3` ve aktarım sırasını gösteren `kaynak_satir` alanları bulunur.

Bütün yerel kayıtlar GP okulundandır.

Örnek ifade:

> Analizde UCI Student Performance veri setinin Portekizce dersi bölümünden alınmış yerel bir alıntı kullanıldı. Ana analiz kaynak sırasındaki ilk 60 kayıtla sınırlandırıldı.

Bu örneklem rastgele veya temsili örnek olarak sunulmamalıdır.

## 3. Ana n'yi açıkça yazın

Ana analiz:

`n=60`.

Son 20 kayıt ana analize eklenmemiştir.

Örnek ifade:

> Önceden belirlenmiş ana analiz kümesi kaynak sırasındaki ilk 60 kayıttan oluşmuştur (`n=60`); kaynak 61–80 ayrı bir öğrenci etkinliği olarak değerlendirilmiştir.

## 4. Değişkenleri tanımlayın

- `G1`: birinci dönem notu,
- `G3`: yıl sonu notu,
- ölçek: 0–20.

Sıfır not geçerli değerdir ve otomatik olarak eksik/hatalı kabul edilmemiştir.

## 5. Grafiği katsayıdan önce inceleyin

Korelasyon raporunda saçılım grafiği ilişkinin:

- yönünü,
- yaklaşık biçimini,
- olası etkili gözlemleri,
- üst üste gelen kayıtları

değerlendirmek için kullanılır.

Örnek ifade:

> Korelasyon katsayıları yorumlanmadan önce G1 ve G3 saçılım grafiği incelenmiş ve pozitif birliktelik görsel olarak değerlendirilmiştir.

Grafik tek başına çıkarımsal test değildir.

## 6. Pearson katsayısını raporlayın

Ana sonuç:

`r=.746612792`.

Akademik metinde uygun yuvarlama:

`r=.747`.

Örnek ifade:

> G1 ile G3 arasında güçlü pozitif doğrusal ilişki gözlendi (`r=.747`).

“Güçlü” gibi sözel sınıflandırmalar bağlama bağlıdır; katsayının kendisini mutlaka verin.

## 7. Pearson testini doğru yazın

Ana klasik test:

`t(58)=8.547100`, `p≈7.47×10⁻¹²`.

Raporlama için:

> `t(58)=8.55, p<.001`.

Örnek ifade:

> Pearson korelasyonu klasik iki yönlü testte sıfırdan farklıydı, `t(58)=8.55, p<.001`.

Küçük p değeri ilişkinin nedensel veya örneklemin temsili olduğunu göstermez.

## 8. Güven aralığını ekleyin

Yaklaşık Fisher %95 güven aralığı:

`[.607944246, .841082238]`.

Raporlama için:

`%95 GA [.608, .841]`.

Örnek ifade:

> Pearson korelasyonu `.747` olup yaklaşık Fisher %95 güven aralığı `[.608, .841]` idi.

Bu aralık klasik model koşullarına bağlıdır.

## 9. Pearson r²'yi dikkatle yorumlayın

`r²=.557430662`.

Aynı 60 kayıt ve sabit terimli tek yordayıcılı OLS regresyonda bu değer `R²`ye eşittir.

Uygun ifade:

> Aynı iki değişken ve aynı 60 kayıt için Pearson `r²=.557`, sabit terimli basit OLS modelinin `R²` değeriyle özdeştir.

Uygun olmayan ifade:

> “G1, G3'ün %55.7'sine neden olmaktadır.”

`r²` nedensel açıklama oranı değildir.

## 10. Spearman katsayısını raporlayın

Ana sonuç:

`r_s=.831085662`.

Raporlama için:

`r_s=.831`.

Örnek ifade:

> Bağlı değerlere ortalama sıra verilerek hesaplanan Spearman sıra korelasyonu `.831` idi.

## 11. Bağları belirtin

Veride aynı not değerleri tekrarlandığından bağlar vardır.

Spearman hesabı, her değişkende bağlı değerlere ortalama sıra verilip sıraların Pearson korelasyonunun hesaplanmasıyla doğrulanmıştır.

Örnek ifade:

> Notlarda bağlı değerler bulunduğundan sıra dönüşümünde ortalama sıralar kullanıldı; bağ düzeltmesi içermeyen kısa sıra-farkı formülü kullanılmadı.

Bu yöntem bilgisi raporun yeniden üretilebilirliğini artırır.

## 12. Pearson ve Spearman'ı rakip sonuçlar gibi sunmayın

Ana sonuçlar:

- Pearson `.747`,
- Spearman `.831`.

Uygun yorum:

> Hem ham değerlerde doğrusal hem de sıralarda monoton pozitif birliktelik gözlendi; Spearman katsayısı Pearson katsayısından daha yüksekti.

Uygun olmayan yorum:

> “Spearman daha yüksek olduğu için doğru katsayı Spearman'dır.”

Katsayı seçimi yalnız büyüklüğe göre yapılmaz.

## 13. Spearman karesini açıklanan ham varyans diye yazmayın

`r_s²` ham G3 notlarındaki açıklanan varyans oranı değildir.

Spearman sıraların korelasyonudur.

Bu nedenle Pearson'ın basit OLS özdeşliğini Spearman'a mekanik olarak taşımayın.

## 14. İlk kayıt duyarlılığını doğru raporlayın

Ana Pearson:

`.746612792`.

Kaynak 1 yalnız duyarlılık kopyasında dışlandığında:

`.865833531`.

Spearman:

`.831085662 → .826699998`.

Örnek ifade:

> Kaynak 1'in yalnız duyarlılık amacıyla dışlanması Pearson katsayısını `.747`den `.866`ya yükseltirken Spearman katsayısını `.831`den `.827`ye değiştirdi. Bu kayıt ana analizden çıkarılmadı.

## 15. Etkili kayıt ile hatalı kayıt aynı değildir

İlk kaydın Pearson üzerinde güçlü etkisi olması onun yanlış kaydedildiğini kanıtlamaz.

Uygun ifade:

> Kaynak 1 Pearson korelasyonu açısından etkili bir gözlem olarak belirlendi; bağımsız veri-hatası kanıtı bulunmadığından ana analizde korundu.

Bu ayrım özellikle öğrenci raporlarında önemlidir.

## 16. Birini-dışarıda-bırakma aralığını güven aralığı diye sunmayın

Pearson duyarlılık aralığı:

`[.727846069, .865833531]`.

Spearman duyarlılık aralığı:

`[.822255639, .849831028]`.

Bunlar 60 farklı yeniden hesaplamanın aralığıdır.

Örnek ifade:

> Birini-dışarıda-bırakma analizlerinde Pearson katsayısı `.728–.866`, Spearman katsayısı `.822–.850` arasında değişti. Bu değerler örnekleme güven aralığı değil, gözlem etkisine yönelik duyarlılık aralığıdır.

## 17. En etkili kayıtları yöntem bazında belirtin

Ana katsayıdan mutlak değişim ölçütüne göre:

- Pearson için kaynak 1,
- Spearman için kaynak 40

en etkili kayıttır.

Bu farklılık, Pearson ve Spearman'ın gözlemlerin ham değer ve sıra özelliklerine farklı duyarlılık gösterebildiğini öğretir.

## 18. Son 20 kaydı doğru etiketleyin

Kaynak 61–80:

- n=20,
- Pearson `.627307114`,
- Spearman `.570535504`.

Örnek ifade:

> Kaynak sırasındaki son 20 kayıt ayrı etkinlik olarak incelendi; Pearson `.627`, Spearman `.571` bulundu.

Ardından sınırı ekleyin:

> Bu kayıtlar aynı yerel alıntının devamı olduğundan bağımsız dış doğrulama örneklemi olarak değerlendirilmedi.

## 19. İki alt kümedeki katsayıları yalnız karşılaştırmayın

Ana Pearson `.747`, son 20 Pearson `.627` diye yalnız sayısal fark görmek, anakütle korelasyonlarının farklı olduğunu kanıtlamaz.

Korelasyon farkına ilişkin bilimsel soru ayrıca uygun test/tasarım gerektirir.

Bu bölümde böyle bir anakütle korelasyon farkı testi yapılmamıştır.

## 20. Monte Carlo permütasyonunu yöntem adıyla raporlayın

Python hesabında:

- seed `202606`,
- B `19999`,
- iki yönlü mutlak uçluk,
- uç sayısı `0`.

Monte Carlo p:

`(0+1)/(19999+1)=.00005`.

Örnek ifade:

> Spearman ilişkisi için 19,999 rastgele permütasyonlu Monte Carlo testi (seed 202606) yürütüldü. Gözlenen mutlak katsayı kadar veya daha uç permütasyon görülmedi ve +1 düzeltmeli Monte Carlo p değeri `.00005` olarak hesaplandı.

## 21. p=0 yazmayın

Sıfır uç permütasyon görülmesi:

`p=0`

demek değildir.

Bu uygulamada minimum raporlanabilir +1 düzeltmeli değer:

`.00005`.

Uygun ifade:

> Hiçbir örneklenmiş permütasyon gözlenen istatistik kadar uç değildi; ancak sonlu Monte Carlo örneklemesi nedeniyle sonuç sıfır olasılık olarak yorumlanmadı.

## 22. Monte Carlo testi “tam kesin test” değildir

19,999 rastgele permütasyon bütün olası permütasyonların taranması değildir.

Bu nedenle:

> “exact p=...”

ifadesi kullanılmamalıdır.

Ayrıca permütasyon yaklaşımı değiştirilebilirlik varsayımına dayanır.

## 23. Asimptotik ve permütasyon p değerlerini karıştırmayın

Spearman için yazılımın asimptotik/yaklaşık p değeri ile Monte Carlo permütasyon p değeri farklı yöntemlerden gelir.

Raporlarken yöntem adını p değerinin yanında belirtin.

## 24. Seed tek başına yeniden üretilebilirlik değildir

Aynı `seed=202606`, R ve NumPy'da aynı permütasyon dizisini garanti etmez.

Raporlama için yazılım, sürüm, algoritma ve B sayısı da önemlidir.

## 25. Ölçek dönüşümünü doğru yorumlayın

Pozitif doğrusal ölçekleme Pearson ve Spearman katsayılarını korur; negatif ölçekleme işareti tersine çevirir.

Bu deney korelasyonun ölçü birimine bağlı olmayan yönünü gösterir.

Ancak doğrusal olmayan dönüşümler Pearson ve Spearman'ı farklı biçimde etkileyebilir; bu bölümde genel dönüşüm değişmezliği iddiası yapılmaz.

## 26. Korelasyonu bireysel gelişme olarak raporlamayın

Uygun olmayan ifade:

> “r yüksek olduğu için öğrencilerin notları yükselmiştir.”

Uygun ifade:

> “G1'i daha yüksek olan öğrencilerin G3 değerleri de genel olarak daha yüksek olma eğilimindedir.”

Bireysel değişim için `G3−G1` ayrı analiz edilmelidir.

## 27. Korelasyonu nedensellik olarak raporlamayın

Uygun olmayan ifade:

> “G1'in yüksek olması G3'ün yükselmesine neden olur.”

Uygun ifade:

> “G1 ve G3 arasında pozitif birliktelik gözlenmiştir; gözlemsel korelasyon nedensel etki olarak yorumlanmamıştır.”

Zamansal sıra tek başına nedensellik için yeterli değildir.

## 28. Temsil sınırını ekleyin

Yerel alıntı:

- ilk sıralardaki kayıtları içerir,
- tek okul kodundadır,
- rastgele örnek değildir.

Bu nedenle:

> “Portekiz'deki bütün öğrencilerde korelasyon .747'dir.”

şeklinde genelleme yapılmamalıdır.

## 29. Yazılım doğrulamasını doğru raporlayın

Python sonuçları üretilmiştir. R kodu hazırlanmış ancak çalıştırılmamıştır. SPSS syntax/çıktısı yoktur.

Uygun ifade:

> Ana hesaplar Python ile yürütülmüş; R betiği karşılaştırma amacıyla hazırlanmış ancak bu paket hazırlanırken çalıştırılmamıştır. SPSS analizi yapılmamıştır.

Yapılmamış yazılım analizlerini doğrulama olarak sunmayın.

## 30. Örnek bütünleşik Pearson paragrafı

> UCI Student Performance veri setinden alınmış yerel alıntının önceden belirlenen ilk 60 kaydında birinci dönem notu (G1) ile yıl sonu notu (G3) arasındaki ilişki incelendi. Saçılım grafiği pozitif birlikteliğe işaret etti. Pearson korelasyonu `r=.747` olup klasik iki yönlü testte `t(58)=8.55, p<.001` ve yaklaşık Fisher %95 güven aralığı `[.608, .841]` olarak elde edildi. Aynı kayıtlarla sabit terimli basit OLS modelinde `R²=r²=.557` özdeşliği doğrulandı. Bununla birlikte örneklem tek okuldan sıralı bir alıntı olduğundan sonuç temsili anakütle tahmini veya nedensel etki olarak yorumlanmadı.

## 31. Örnek bütünleşik Pearson–Spearman ve duyarlılık paragrafı

> Ana örneklemde Pearson korelasyonu `.747`, bağlı değerlere ortalama sıra verilerek hesaplanan Spearman korelasyonu `.831` idi. Birini-dışarıda-bırakma analizlerinde Pearson `.728–.866`, Spearman `.822–.850` aralığında değişti; bu aralıklar güven aralığı değil kayıt etkisine yönelik duyarlılık sonuçlarıdır. Kaynak 1'in dışlanması Pearson'ı `.866`ya yükseltmesine rağmen bu gözlem veri hatası olarak değerlendirilmedi ve ana analizde korundu.

## 32. Örnek bütünleşik permütasyon paragrafı

> Spearman ilişkisi için seed 202606 ile 19,999 rastgele permütasyonlu iki yönlü Monte Carlo analizi yapıldı. Örneklenen permütasyonların hiçbirinde gözlenen mutlak katsayı kadar uç değer oluşmadı; +1 düzeltmesiyle `p_MC=.00005` elde edildi. Bu sonuç p=0 veya bütün olası permütasyonların tarandığı tam kesin test olarak yorumlanmadı.

## 33. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Araştırma sorusu birliktelik diliyle yazılmış mı?
- G1 ve G3 tanımlanmış mı?
- Ana analiz n=60 olarak belirtilmiş mi?
- Son 20 kayıt ayrı etkinlik olarak etiketlenmiş mi?
- Son 20 dış doğrulama diye sunulmamış mı?
- `kaynak_satir` kişi kimliği sayılmamış mı?
- Sıfır not veri hatası diye silinmemiş mi?
- Saçılım grafiği incelenmiş mi?
- Pearson katsayısı verilmiş mi?
- t, sd ve p doğru raporlanmış mı?
- Yaklaşık Fisher güven aralığı verilmiş mi?
- `r²` nedensel açıklama oranı diye sunulmamış mı?
- Spearman bağlı değerlerde ortalama sıralarla hesaplanmış mı?
- Bağsız kısa sıra-farkı formülünden kaçınılmış mı?
- Spearman karesi ham varyans açıklaması diye yorumlanmamış mı?
- Pearson/Spearman yalnız büyüklüğe göre seçilmemiş mi?
- İlk kayıt etkili ama otomatik hatalı sayılmamış mı?
- Ana 60 kayıt korunmuş mu?
- Birini-dışarıda-bırakma aralığı güven aralığı diye sunulmamış mı?
- En yüksek korelasyonlu alt küme seçilmemiş mi?
- Son 20 farkı doğrudan korelasyon farkı testi sayılmamış mı?
- Permütasyon B ve seed belirtilmiş mi?
- `p_MC=.00005` doğru yazılmış mı?
- Sıfır uç gözlemi p=0 diye yazılmamış mı?
- Monte Carlo sonucu tam kesin test diye sunulmamış mı?
- Asimptotik ve permütasyon p değerleri ayrılmış mı?
- Korelasyon bireysel gelişme diye yorumlanmamış mı?
- Korelasyon nedensellik diye yorumlanmamış mı?
- Tek okul/sıralı alıntı sınırı belirtilmiş mi?
- R/SPSS yapılmış gibi raporlanmamış mı?

## Son mesaj

İyi bir korelasyon analizi yalnız:

> `r=.75, p<.001`

demek değildir.

Bilimsel olarak daha güçlü zincir:

**Veri kaynağı → Analiz örneklemi → Grafik → Pearson/Spearman seçimi → Katsayı → Güven aralığı/test → Kayıt etkisi → Permütasyon → Genelleme sınırı → Nedensellik sınırı → Akademik raporlama**

şeklindedir.

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.