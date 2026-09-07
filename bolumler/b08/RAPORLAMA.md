# Bölüm 8 — Çoklu ve Lojistik Regresyon Sonuçlarını Akademik Raporlama

Bu rehber, Bölüm 8'de elde edilen çoklu doğrusal ve lojistik regresyon sonuçlarını bilimsel bir raporda doğru biçimde sunmanıza yardımcı olur. İki model farklı hedefleri açıkladığı için sonuçları tek bir yorum altında birleştirmeyin.

> **Temel ayrım:** Çoklu doğrusal regresyon `G3` puanının koşullu ortalamasını; lojistik regresyon ise öğretim amacıyla tanımlanan `G3 ≥ 14` olayının olasılığını modeller.

## 1. Araştırma sorularını ayrı yazın

Bu bölümde iki soru vardır:

1. `G1` ve yaş birlikte ele alındığında `G3` puanını ne ölçüde yordamaktadır?
2. `G1` ve yaş, öğretim amacıyla tanımlanan `G3 ≥ 14` olayının olasılığıyla nasıl ilişkilidir?

İkinci sorudaki 14 puan resmî bir geçme veya başarı sınırı değildir.

## 2. Çoklu doğrusal regresyon modelini raporlayın

Ana model ilk 60 kayıt üzerinde kurulmuştur:

`G3 = 5.296 + 0.640 G1 + 0.505 age_c`

Burada `age_c = age - 16` olduğundan yaş değişkeni 16 yaşta merkezlenmiştir.

Model sonuçları:

- `R² = .581`,
- düzeltilmiş `R² = .567`,
- yaşın eklenmesine ilişkin `ΔR² = .024`,
- yaşın ek değişken testi için `p = .076`.

Örnek raporlama:

> G1 ve merkezlenmiş yaşın G3 puanını yordama düzeyi çoklu doğrusal regresyonla incelenmiştir. Model, G3 puanlarındaki örneklem değişkenliğinin yaklaşık %58.1'ini açıklamıştır (`R² = .581`; düzeltilmiş `R² = .567`). Yaşın modele eklenmesi açıklanan değişkenliği yaklaşık 2.4 yüzde puan artırmış (`ΔR² = .024`), ancak bu ek katkı klasik ek değişken testinde .05 düzeyinde istatistiksel olarak anlamlı bulunmamıştır (`p = .076`).

`p = .076` sonucunu “yaşın hiçbir ilişkisi yoktur” biçiminde yorumlamayın. Bu sonuç, bu örneklem ve model altında ek yaş katsayısına ilişkin belirsizliği gösterir.

## 3. Kısmi regresyon katsayısını doğru yorumlayın

G1 katsayısı yaklaşık:

`b = 0.640`

Bu katsayı yaş modelde sabit tutulduğunda G1 ile G3 arasındaki model-temelli ilişkiyi ifade eder.

Uygun ifade:

> Yaş istatistiksel olarak kontrol edildiğinde G1'deki bir puanlık fark, modelde G3'te ortalama yaklaşık 0.64 puanlık farkla ilişkilidir.

Kaçınılması gereken ifade:

> G1'i bir puan artırmak G3'ü kesin olarak 0.64 puan artırır.

Regresyon katsayısı bu gözlemsel uygulamada nedensel müdahale etkisi değildir.

## 4. Merkezlemeyi açıklayın

Yaş değişkeni:

`age_c = age - 16`

olarak tanımlanmıştır.

Bu nedenle `age_c = 0`, 16 yaş anlamına gelir. Merkezleme sabit terimin ve belirli profil tahminlerinin daha anlamlı yorumlanmasını kolaylaştırır.

Merkezleme tek başına:

- model uyumunu iyileştirmez,
- nedensellik sağlamaz,
- veri sorunlarını çözmez.

## 5. VIF ve HC3 sonuçlarını ölçülü raporlayın

G1 için VIF yaklaşık:

`VIF = 1.229`

G1 standart hataları:

- klasik `SE = 0.074`,
- HC3 `SE = 0.227`.

Örnek raporlama:

> G1 için VIF değerinin yaklaşık 1.23 olması bu modelde G1 açısından belirgin doğrusal bağlantı şişmesi bulunmadığını düşündürmektedir. Bununla birlikte düşük VIF bütün regresyon varsayımlarının sağlandığını göstermez. Ayrıca G1'in HC3 standart hatasının klasik standart hatadan daha büyük olması, katsayı belirsizliğinin kovaryans tahmin yöntemine duyarlı olduğunu göstermektedir.

İlk kayıt çıkarıldığında yaş katsayısının yaklaşık 0.505'ten 0.068'e değişmesi de sonuçların gözlem etkisine duyarlılığının raporlanması gerektiğini gösterir. Bu durum kaydın otomatik olarak silinmesi gerektiği anlamına gelmez.

## 6. Lojistik regresyon modelini tanımlayın

Lojistik model:

`logit[P(hedef14=1)] = -22.192 + 1.652 G1 - 0.320 age_c`

şeklindedir.

G1 için:

- logit katsayısı yaklaşık `1.652`,
- odds oranı `OR = 5.219`,
- yaklaşık %95 normal-Wald OR aralığı `[2.049, 13.296]`.

Örnek raporlama:

> Yaş modelde sabit tutulduğunda G1, `G3 ≥ 14` olayıyla pozitif ilişkili bulunmuştur. G1'deki bir puanlık fark için tahmin edilen odds oranı yaklaşık 5.22'dir (`OR = 5.219`, yaklaşık %95 Wald GA `[2.049, 13.296]`).

## 7. Odds oranını olasılık oranı gibi yazmayın

Yanlış ifade:

> G1 bir puan arttığında başarı olasılığı 5.22 kat artar.

Daha uygun ifade:

> Yaş sabitken G1'deki bir puanlık fark, `G3 ≥ 14` olayının odds'unda yaklaşık 5.22 katlık oranla ilişkilidir.

Odds ile olasılık aynı kavram değildir.

Örneğin 16 yaş için:

- `G1 = 12` olduğunda tahmin edilen olay olasılığı yaklaşık `.086`,
- `G1 = 13` olduğunda yaklaşık `.329`.

Bu örnekte olasılık farkı yaklaşık `.243`, yani **24.3 yüzde puandır**. OR ise yaklaşık 5.22'dir. Aynı odds oranı farklı başlangıç olasılıklarında farklı olasılık farkları oluşturabilir.

## 8. Sınıflandırma performansını raporlayın

Önceden belirlenmiş `0.50` karar eşiğinde:

| Küme | Duyarlılık | Özgüllük | Doğruluk |
|---|---:|---:|---:|
| Eğitim (n=60) | .737 | .951 | .883 |
| Aktarım (n=20) | .600 | .933 | .850 |

Örnek raporlama:

> `0.50` karar eşiğinde model eğitim kümesinde yaklaşık %73.7 duyarlılık, %95.1 özgüllük ve %88.3 doğruluk göstermiştir. Sabit model sonraki 20 kayda uygulandığında duyarlılık %60.0, özgüllük %93.3 ve doğruluk %85.0 olarak bulunmuştur.

Ancak yalnız doğruluğa bakmak yeterli değildir. Herkesi olay yok (`0`) olarak sınıflandıran basit kuralın doğruluğu eğitimde yaklaşık %68.3, aktarımda %75.0'dır ve duyarlılığı sıfırdır.

## 9. AUC ve Brier skorunu ayırın

Sonuçlar:

- eğitim AUC: `.937`,
- aktarım AUC: `.760`,
- eğitim Brier: `.090`,
- aktarım Brier: `.132`.

Örnek raporlama:

> Modelin AUC değeri eğitim kümesinde .937, aktarım kümesinde .760 olarak bulunmuştur. Brier skoru ise sırasıyla yaklaşık .090 ve .132'dir. AUC modelin olay ve olay olmayan kayıtları sıralama/ayırt etme yeteneğini özetlerken, Brier skoru tahmin edilen olasılıkların gözlenen ikili sonuçlara göre ortalama kare hatasını yansıtır.

AUC'yi “kalibrasyon ölçüsü” olarak adlandırmayın. Brier skorunu da yalnızca kalibrasyon ölçüsü olarak sunmayın.

## 10. Karar eşiklerini doğru yorumlayın

Bu uygulamada `0.3`, `0.5` ve `0.7` olasılık eşikleri incelenmektedir. Bunlar `G3 ≥ 14` olay tanımından farklı kavramlardır.

Karar eşiği değiştiğinde yanlış pozitif ve yanlış negatif sayıları değişebilir. Bu nedenle “0.50 her zaman en iyi eşiktir” şeklinde evrensel bir kural yoktur.

Bu veri örneğinde 0.50 ve 0.70 eşikleri aynı sınıfları üretebilir. Bu sonuç veri ve tahmin olasılıklarına özgüdür; genel bir lojistik regresyon özelliği değildir.

Aktarım kümesindeki sonuçlara bakarak en iyi eşiği seçip aynı kümeyi yeniden bağımsız test olarak sunmayın. Eşik seçimi için kullanılan veri artık dokunulmamış test verisi değildir.

## 11. Sabit-model aktarımını doğru adlandırın

İlk 60 kayıtta kurulan katsayılar son 20 kayda değiştirilmeden uygulanmaktadır. Bu, Bölüm 7'deki son 20 kayıt üzerinde yeniden model kurma etkinliğinden farklıdır.

Bununla birlikte tüm kayıtlar aynı okulun sıralı yerel alıntısından geldiği için:

> Sonraki 20 kayıttaki performans, sabit modelin ayrı bir veri alt kümesindeki aktarım davranışını göstermektedir; bağımsız yeni okul veya yeni yıl dış doğrulaması olarak yorumlanmamıştır.

şeklinde ifade edilmesi daha uygundur.

## 12. Örnek bütünleşik sonuç paragrafı

Aşağıdaki paragraf bir raporlama modelidir; kendi çalışmanızda analiz ve yorumunuzu kullanın.

> İlk 60 kayıt üzerinde G1 ve yaşın G3 puanını yordama düzeyi çoklu doğrusal regresyonla incelenmiştir. Model G3 değişkenliğinin yaklaşık %58.1'ini açıklamıştır (`R² = .581`; düzeltilmiş `R² = .567`). Yaş kontrol edildiğinde G1'in kısmi eğimi yaklaşık 0.640 olarak bulunmuştur. Yaşın modele eklenmesi `R²` değerini yaklaşık .024 artırmış, ancak klasik ek değişken testi .05 düzeyinde anlamlı bulunmamıştır (`p = .076`). Ayrı bir lojistik regresyon modelinde öğretim amacıyla tanımlanan `G3 ≥ 14` olayı incelenmiştir. Yaş sabitken G1 için odds oranı 5.219 olarak tahmin edilmiştir (yaklaşık %95 Wald GA `[2.049, 13.296]`). `0.50` karar eşiğinde eğitim doğruluğu .883, sonraki 20 kayda sabit-model aktarım doğruluğu .850 olarak bulunmuştur. AUC değerleri sırasıyla .937 ve .760, Brier skorları .090 ve .132'dir. Sonraki 20 kayıt aynı okulun sıralı alıntısından geldiği için bu performans bağımsız dış doğrulama olarak yorumlanmamıştır. Ayrıca katsayılar gözlemsel ilişkileri temsil etmekte olup nedensel müdahale etkisi olarak değerlendirilmemiştir.

## 13. Raporlama kontrol listesi

Raporunuzu teslim etmeden önce şunları kontrol edin:

- Sürekli `G3` hedefi ile `G3 ≥ 14` ikili hedefi ayrılmış mı?
- `n = 60` model kurma ve `n = 20` aktarım ayrımı belirtilmiş mi?
- Çoklu regresyon modeli ve kısmi katsayılar doğru yorumlanmış mı?
- `R²`, düzeltilmiş `R²` ve `ΔR²` birbirine karıştırılmamış mı?
- Merkezleme açıklanmış mı?
- VIF bütün varsayımların kanıtı gibi sunulmamış mı?
- Klasik ve HC3 standart hataları ayrılmış mı?
- Odds oranı olasılık oranı olarak yorumlanmamış mı?
- 14 not eşiği ile olasılık karar eşiği ayrılmış mı?
- Duyarlılık, özgüllük ve doğruluk birlikte değerlendirilmiş mi?
- AUC ve Brier skorunun farklı anlamları belirtilmiş mi?
- Eşik seçiminin performans ölçülerini değiştirebileceği açıklanmış mı?
- Aktarım kümesi bağımsız dış doğrulama olarak adlandırılmamış mı?
- Nedensellik ve genellenebilirlik sınırları belirtilmiş mi?
- Yapılmamış R/SPSS analizleri yapılmış gibi raporlanmamış mı?

## Son mesaj

Bu bölümde iki farklı model ailesini aynı veri üzerinden karşılaştırırken temel düşünce zinciri şöyledir:

**Araştırma sorusu → Hedef değişken → Model seçimi → Katsayı/OR → Belirsizlik → Tanı → Olasılık → Karar eşiği → Performans → Aktarım → Sınırlılık → Akademik raporlama**

Çalışmanızı [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md), [VERI.md](VERI.md) ve `beklenen.json` ile birlikte değerlendirin.