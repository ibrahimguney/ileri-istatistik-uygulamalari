# Bölüm 7 — görevler

## D1–D3: Analizden Önce

1.  İki faktör, düzeyleri, hücre sayısı ve analiz birimi nedir? Bu veri neden tekrarlı ölçümler ANOVA’sı değildir?

2.  OJ içindeki doz sorusu ile bütün kayıtlardaki uygulama–doz etkileşimi hangi farklı hipotezleri sınar?

3.  Dozu sayısal bir eğim yerine üç düzeyli faktör olarak yazmak hangi kısıtı kaldırır? 0.5, 1 ve 2’nin eşit aralıklı olmadığını dikkate alın.

Etkinlik yanıtları Ek F’de, Bölüm 7 başlığı altındadır (s. kitaptaki ilgili sayfa).

# Rehberli ve Bağımsız Etkinlikler

## G1–G3: Rehberli Hesaplar

1.  OJ ortalamaları ve standart sapmalarından $SSG$, $SSW$, $SST$, F, $\eta^2$ ve $\omega^2$ değerlerini yeniden hesaplayın. Neden hata serbestlik derecesi 29 değil 27’dir?

2.  OJ grubunda 2$-$<!-- -->1 farkının Tukey aralığını kurun. Genel F anlamlıyken bu aralığın sıfırı içermesi çelişki midir? Games–Howell ile yön ve belirsizliği karşılaştırın.

3.  Tam modelde dört KT bileşenini toplayın, etkileşim F’sini ve kısmi eta-kareyi bulun. 1 mg/gün OJ$-$VC aralığını $MS_E=13.18715$, $sd=54$ ve üçlü Bonferroni düzeltmesiyle üretin.

## B1–B3: VC Grubunda Bağımsız Çözüm

Yalnız VC alan 30 kaydı seçin; OJ hata terimini veya katsayılarını taşımayın.

1.  Üç dozun özetlerini, klasik ANOVA tablosunu, eta-kare ve omega-kareyi hesaplayın.

2.  Üç çiftlik Tukey ailesini kurun; ardından Welch/Games–Howell ile sonuçları karşılaştırın. Hangi çiftlerin aralıkları sıfırı içerir?

3.  En fazla 100 sözcüklük bir raporda örneklem kapsamını, fark yönünü, karşılaştırma ailesini ve eş varyans varsayımını belirtin. OJ ile VC’nin ayrı testlerinden etkileşim sonucuna atlamayın.

## H1: Altı Hatalı İddiayı Düzeltin

Her iddiayı bu bölümdeki bir formül veya sayısal sonuçla düzeltin.

## P1: Ortak Model ve Çoklu Karşılaştırma Denetimi

60 kayıt ve altı eşit hücreyi doğrulayın. OJ klasik/Welch sonuçlarını, Tukey/Games–Howell ailelerini, faktöriyel KT ayrıştırmasını ve üç basit etkinin Bonferroni aralıklarını yeniden üretin. Klasik etkileşimle HC3 sonucunu karşılaştırın. Teslim: çalışan kod, üç grafik, kaynak/analiz sözlüğü ve bir sayfalık eleştirel rapor.

<div class="center">

| Ölçüt                                              | Puan |
|:---------------------------------------------------|-----:|
| Kaynak, hücreler ve faktör kodlaması               |   20 |
| Kareler toplamları ve etki büyüklükleri            |   25 |
| Karşılaştırma ailesi ve aralıkların eşleştirilmesi |   25 |
| Etkileşim, tanılar ve HC3 duyarlılığı              |   20 |
| Yeniden üretim ve sınırlılık raporu                |   10 |

</div>

## T1–T3: Hedef ve Etkileşim Denetimi

1.  Öğretim alt kümesindeki 4.376111, 4.220660 ve 5.654783 farklarının ağırlıklarını açıklayın. Hangisi grupların ayrı doz bileşimini de taşır?

2.  Bir dozda p küçük, diğerinde büyük bulunması neden etkileşim testi değildir? İki planlı farkların farkının ailesini ve HC3 t yaklaşımının sınırını belirtin.

3.  Kaynak sırasıyla 48 kayıt seçiminin ana 60 kaydı veya rastgele kayıp varsayımını neden değiştirmediğini açıklayın. Tip III etiketi hedef kontrastı açıklamaya tek başına yeter mi?

- Üç veya daha fazla grupta karşılaştırma ailesini tanımlamadan düzeltmesiz t-testleri taramak.

- Genel F testini bütün ikili testleri düzeltmesiz yapma izni saymak veya her karşıtlık için zorunlu anlamlılık kapısı sanmak.

- Varyans homojenliği varsayımını kontrol etmemek.

- ANOVA’nın hangi grupların farklı olduğunu doğrudan söylediğini sanmak.

- Etki büyüklüğünü raporlamadan yalnızca $p$-değerine odaklanmak.

- Etkileşim anlamlıyken yalnızca ana etkileri yorumlamak.

Bu hataları önlemek için ANOVA sonuçları her zaman varsayımlar, genel test, etki büyüklüğü ve post-hoc aşamalarıyla birlikte ele alınmalıdır.

# Alıştırmalar

## Kolay Düzey

1.  Tek yönlü ANOVA’nın sıfır hipotezi nedir?

2.  ANOVA’da gruplar içi değişkenliği hangi kareler toplamı gösterir?

3.  Genel ANOVA sonucu anlamlıysa sonraki adım genellikle nedir?

4.  Parametrik koşullar zayıfsa tek yönlü ANOVA’ya alternatif ne olabilir?

5.  $\eta^2$ değeri neyi gösterir?

## Orta Düzey

1.  Dört öğretim yönteminin başarı puanları karşılaştırılacaktır. ANOVA neden çoklu t-testlerine tercih edilmelidir?

2.  ANOVA sonucunda $p<.05$ bulunmuştur. Bu sonuç neyi gösterir, neyi göstermez?

3.  İki yönlü ANOVA’da etkileşim etkisi anlamlı bulunmuştur. Nasıl yorumlanır?

4.  Tek yönlü ANOVA’da $F(3,76)=4.92$, $p=.004$ raporlanmıştır. Kaç grup vardır ve genel sonuç nedir?

5.  Varyans homojenliği ihlal edilmiş görünmektedir. Araştırmacı rapordan önce neyi değerlendirmelidir?

## İleri Düzey

1.  ANOVA anlamlı, Tukey karşılaştırmalarında yalnızca bir çift anlamlıdır. Nasıl raporlanır?

2.  İki yönlü ANOVA’da ana etkiler ve etkileşim anlamlıdır. Ana etkileri tek başına yorumlamak neden sakıncalıdır?

3.  Çok büyük örneklemde $p<.001$, $\eta^2=0.02$ bulunmuştur. İstatistiksel ve pratik önem nasıl dengelenir?

4.  Araştırmacı doğal üç grubu ANOVA ile karşılaştırıp grup üyeliğinin sonucu “nedenlediğini” yazmıştır. Bu neden sorunludur?

5.  Dengesiz faktöriyel ANOVA’da hücre büyüklükleri çok farklıdır. Hangi ek konular dikkate alınmalıdır?

## Çekirdek öğrenme rotası

1. Omnibus ANOVA ile tekil karşıtlıkları ayırır.
2. Etkileşimi koşullu grup farklarıyla yorumlar.
3. Karşılaştırma ailesini ve belirsizliği açık raporlar.

**İleri rota:** Dengesiz hedefler ve HC3 karşıtlıkları; çoklu doğrusal model fikri için Bölüm 13 doğrusal kısmına başvurulabilir.

**Ç1:** Üç gruplu ANOVA anlamlıysa bütün grup çiftleri farklı mıdır?

**Karar görevi:** Eşit doz ağırlığı veya ortak gözlenen doz ağırlığı hedefini seçin; tahminin değişmesini hedef farkıyla açıklayın.

[Rubrik ve teslim rehberi](RUBRIK.md).
