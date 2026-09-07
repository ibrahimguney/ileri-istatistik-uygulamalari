# Bölüm 7 — Regresyon Sonuçlarını Akademik Raporlama

Bu dosyanın amacı analiz çıktısını yalnızca sayı listesi olarak vermek yerine, regresyon bulgularını bilimsel bir raporda açık, doğru ve ölçülü biçimde sunmanıza yardımcı olmaktır.

> **Temel ilke:** Bir regresyon raporu yalnızca `p < .05` ifadesinden oluşmaz. Model, katsayı, belirsizlik, uyum, tahmin ve sınırlılıklar birlikte değerlendirilmelidir.

## 1. Önce araştırma sorusunu yazın

Bu uygulamada temel soru şudur:

**Birinci dönem notu (G1), aynı öğrencilerin yıl sonu notunu (G3) ne ölçüde yordamaktadır?**

Burada özellikle **yordama** sözcüğü kullanılır. Gözlemsel veride regresyon katsayısı tek başına nedensel etkiyi göstermez.

Yanlış ifade:

> G1 notunu bir puan artırmak öğrencinin G3 notunu 0.582 puan artırır.

Daha uygun ifade:

> G1 ile G3 arasında pozitif doğrusal bir ilişki gözlenmiş; G1'deki bir puanlık fark modelde G3'te yaklaşık 0.582 puanlık ortalama farkla ilişkili bulunmuştur.

## 2. Modeli tanımlayın

Ana analiz ilk 60 kayıt üzerinde sabit terimli basit doğrusal regresyon modeliyle yürütülmektedir:

`G3 = β₀ + β₁ G1 + ε`

Modelde:

- bağımlı değişken: `G3`,
- yordayıcı: `G1`,
- ana analiz örneklem büyüklüğü: `n = 60`.

Veri kaynağı, seçim biçimi ve kullanım sınırları için [VERI.md](VERI.md) dosyasına bakın.

## 3. Model uyumunu raporlayın

Ana model için:

- `R² = .557`
- eğitim `RMSE = 1.314`
- artık standart sapması `s = 1.337`

Örnek raporlama:

> Basit doğrusal regresyon modeli, ana analiz örnekleminde G3 puanlarındaki değişkenliğin yaklaşık %55.7'sini açıklamıştır (`R² = .557`). Modelin eğitim verisindeki kök ortalama kare hatası yaklaşık 1.31 puandır.

### Dikkat

`R² = .557`, öğrencilerin %55.7'sinin başarılı olduğu anlamına gelmez. `R²`, modelin bağımlı değişkendeki örneklem değişkenliğinin ne kadarını açıkladığını ifade eden bir uyum ölçüsüdür.

## 4. Regresyon katsayısını raporlayın

Ana OLS sonuçları:

- sabit: `b₀ = 5.741`
- eğim: `b₁ = 0.582`
- klasik standart hata: `SE = 0.068`
- `t(58) = 8.55`
- `p < .001`
- klasik %95 güven aralığı: `[0.446, 0.718]`

Örnek raporlama:

> G1, G3'ün pozitif bir yordayıcısıdır (`b = 0.582`, `SE = 0.068`, `t(58) = 8.55`, `p < .001`, %95 GA `[0.446, 0.718]`). Model kapsamında G1'deki bir puanlık fark, G3'te ortalama yaklaşık 0.58 puanlık farkla ilişkilidir.

Bu ifade nedensel bir müdahale sonucu olarak okunmamalıdır.

## 5. Güven aralığı ile tahmin aralığını ayırın

`G1 = 12` için:

- nokta tahmini: `12.725`,
- koşullu ortalama için klasik %95 güven aralığı: `[12.379, 13.071]`,
- yeni birey için klasik %95 tahmin aralığı: `[10.027, 15.423]`.

Örnek raporlama:

> G1 puanı 12 olan öğrenciler için modelin tahmin ettiği ortalama G3 puanı 12.73'tür. Bu koşullu ortalama için klasik %95 güven aralığı 12.38–13.07'dir. Buna karşılık G1 puanı 12 olan yeni bir bireyin G3 puanı için klasik %95 tahmin aralığı daha geniş olup 10.03–15.42'dir.

Tek bir öğrenci için ortalama güven aralığını kullanmayın. Yeni birey tahmininde bireysel hata değişkenliği de bulunduğundan tahmin aralığı daha geniştir.

## 6. Etkili gözlemleri raporlayın

İlk kayıt için:

- kaldıraç: `h = .397`,
- Cook uzaklığı: `D = 8.427`.

İlk kayıt çıkarıldığında eğim yaklaşık `0.856` olmaktadır.

Örnek raporlama:

> Etki tanıları ilk kaydın model üzerinde belirgin etkisi bulunduğunu göstermiştir (`h = .397`, Cook's `D = 8.427`). Bu kayıt çıkarıldığında eğimin 0.582'den yaklaşık 0.856'ya yükselmesi, katsayı tahmininin bu gözleme duyarlı olduğunu göstermektedir. Bununla birlikte yüksek etki, gözlemin veri hatası olduğunu tek başına kanıtlamadığından kayıt ana analizden otomatik olarak çıkarılmamıştır.

Bu ayrım önemlidir:

**etkili gözlem ≠ hatalı gözlem**

## 7. HC3 sonucunu klasik sonuçtan ayrı verin

HC3 ile:

- eğim değişmez: `b = 0.582`,
- HC3 standart hata: `SE = 0.281`,
- t(58) referanslı %95 aralık: `[0.020, 1.144]`,
- `p ≈ .043`.

Örnek raporlama:

> Heteroskedastisiteye karşı HC3 kovaryans tahmini kullanıldığında OLS eğim tahmini değişmemiş (`b = 0.582`), ancak standart hata 0.281'e yükselmiştir. HC3 tabanlı t(58) referanslı %95 güven aralığı `[0.020, 1.144]` olarak elde edilmiştir. Klasik ve HC3 sonuçları arasındaki fark, katsayı belirsizliğinin kullanılan kovaryans tahminine duyarlı olduğunu göstermektedir.

HC3:

- OLS nokta tahminini değiştirmez,
- bütün model sorunlarını çözmez,
- nedensellik sağlamaz,
- klasik bireysel tahmin aralığını otomatik olarak sağlamlaştırmaz.

## 8. LOOCV sonucunu raporlayın

Ana 60 kayıtta:

- eğitim RMSE: `1.314`,
- LOOCV RMSE: `1.620`.

Örnek raporlama:

> Modelin eğitim RMSE'si 1.31 iken birini-dışarıda-bırakma çapraz doğrulama (LOOCV) RMSE'si 1.62'dir. LOOCV hatasının daha yüksek olması, aynı verideki model uyumunun dışarıda bırakılan gözlemleri yordama performansıyla aynı olmadığını göstermektedir.

LOOCV sonucu bağımsız bir okulda veya farklı yılda dış doğrulama yapılmış olduğu anlamına gelmez.

## 9. Son 20 kaydı doğru yorumlayın

Son 20 kayıtta yeniden kurulan modelde:

- sabit yaklaşık `4.112`,
- eğim yaklaşık `0.652`,
- `R² ≈ .394`.

Bu analiz ana modelin dondurularak son 20 kayıtta test edilmesi değildir. Bu nedenle **dış doğrulama** olarak adlandırılmamalıdır.

Uygun ifade:

> Son 20 kayıt üzerinde ayrı bir regresyon modeli kurulmuş ve katsayıların alt kümeler arasında nasıl değişebildiği incelenmiştir. Bu etkinlik bağımsız dış doğrulama olarak yorumlanmamıştır.

## 10. Ekstrapolasyonu belirtin

Ana analizde gözlenen `G1` aralığı 0–17'dir. Dolayısıyla `G1 = 20` için modelden sonuç üretmek matematiksel olarak mümkün olsa da bu değer gözlenen ana veri aralığının dışındadır.

Raporunuzda bunu açıkça belirtin:

> G1=20 için model tahmini gözlenen yordayıcı aralığının dışında kaldığından ekstrapolasyon niteliğindedir ve temkinli yorumlanmalıdır.

## 11. Örnek bütünleşik sonuç paragrafı

Aşağıdaki paragraf bir raporlama örneğidir; doğrudan kopyalamak yerine kendi analiziniz ve yorumunuzla uyarlayın.

> İlk 60 kayıt üzerinde G1'in G3'ü yordama düzeyini incelemek amacıyla basit doğrusal regresyon analizi uygulanmıştır. Model, G3 puanlarındaki örneklem değişkenliğinin yaklaşık %55.7'sini açıklamıştır (`R² = .557`). G1 pozitif bir yordayıcı olarak bulunmuştur (`b = 0.582`, `SE = 0.068`, `t(58) = 8.55`, `p < .001`, %95 GA `[0.446, 0.718]`). G1=12 için tahmin edilen ortalama G3 puanı 12.73 olup koşullu ortalama için klasik %95 güven aralığı 12.38–13.07, yeni birey için klasik %95 tahmin aralığı ise 10.03–15.42'dir. Etki tanıları ilk kaydın sonuçlar üzerinde belirgin etkisi bulunduğunu göstermiştir; bu nedenle sonuçların gözlem etkisine duyarlılığı ayrıca incelenmiştir. HC3 standart hatasının klasik standart hatadan belirgin biçimde büyük olması katsayı belirsizliğinin kovaryans tahminine duyarlı olduğunu göstermektedir. Eğitim RMSE'si 1.31, LOOCV RMSE'si 1.62 olarak bulunmuştur. Bulgular aynı okuldan seçilmiş gözlemsel kayıtlarla sınırlı olduğundan sonuçlar nedensel etki veya yeni okul ve yıllara doğrudan genellenebilirlik kanıtı olarak yorumlanmamıştır.

## 12. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce şunları kontrol edin:

- Araştırma sorusu açık mı?
- Bağımlı değişken ve yordayıcı belirtilmiş mi?
- Örneklem büyüklüğü verilmiş mi?
- Regresyon katsayısı ve belirsizliği raporlanmış mı?
- `R²` doğru yorumlanmış mı?
- Güven aralığı ile bireysel tahmin aralığı ayrılmış mı?
- Etkili gözlemler veri hatasıymış gibi sunulmamış mı?
- Klasik ve HC3 sonuçları birbirine karıştırılmamış mı?
- Eğitim ve LOOCV hatası ayrılmış mı?
- Ekstrapolasyon belirtilmiş mi?
- Yordama ile nedensellik ayrılmış mı?
- Genellenebilirlik sınırları açıklanmış mı?
- Yapılmamış analizler yapılmış gibi raporlanmamış mı?

## Son mesaj

İyi bir regresyon analizi, yalnızca bir doğru çizmek veya anlamlı bir p değeri bulmak değildir. İyi bir analiz şu zinciri birlikte kurar:

**Araştırma sorusu → Veri → Model → Katsayı → Belirsizlik → Tanı → Tahmin → Yorum → Sınırlılık → Akademik raporlama**

Bu bölümdeki çalışmalarınızı [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte kullanın.