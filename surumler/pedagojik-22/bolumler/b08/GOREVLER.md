# Bölüm 8 — görevler

Güncel kitap bölümünün etkinlik ve alıştırmalarıdır. Önce kendi çözümünüzü
üretin; ardından çözümleri kontrol edin. Kitap sayfa numaraları PDF sürümüne
göre değişebilir.

## D1–D3: Analizden Önce

1.  Neden 0. ve 1. günler ana analize alınmaz? Bu karar veriye bakmadan hangi belgeye dayanarak verilebilir?

2.  144 satırı bağımsız sayan tek yönlü ANOVA’nın hata serbestlik derecesi kaç olur? Tekrarlı ölçümler ANOVA’sında kaçtır? Fark neden önemlidir?

3.  Kontrol grubu olmadığında “yoksunluk tepki süresini uzatır” cümlesi hangi alternatif açıklamaları dışlayamaz?

Yanıtlar Ek F, Bölüm 8’dedir (s. kitaptaki ilgili sayfa).

<figure>
<embed src="assets_figures/tk-uyku-profilleri.pdf" />
<figcaption>Solda 18 kişinin temel günden (0) itibaren tepki süresi profilleri ve gün ortalamaları; sağda her kişi için ayrı doğrusal regresyonla bulunan eğimler ile karma etkiler modelinin kişiye özgü eğimleri (BLUP). Kesikli çizgi ortak (sabit) eğimdir. Kaynak: <code>lme4::sleepstudy</code>, 2.–9. günler; uygulama paketindeki <code>analiz.py</code>.</figcaption>
</figure>

Gün ortalamaları temel günde 265.4 ms’den 9. günde 350.9 ms’ye çıkar; standart sapmalar da 29.5 ms’den 67.0 ms’ye büyür. Şekil (kitaptaki ilgili başvuru) bu yayılmanın nedenini gösterir: kişilerin başlangıç düzeyleri farklıdır ve bazıları hızla kötüleşirken bazılarının profili neredeyse düzdür.

# Rehberli ve Bağımsız Etkinlikler

## G1–G4: Rehberli Çözüm

1.  Uyku verisinin kaynak tablosundaki SS ve sd değerlerinden MS ve F’yi yeniden hesaplayın. Toplam değişkenliğin yüzde kaçı kişi farklarıdır?

2.  $\hat\varepsilon_{GG}=.445$ ile düzeltilmiş sd’leri bulun. F değeri neden değişmez?

3.  $\eta^2_p$ ve $\eta^2_G$’yi hesaplayın. Neden bu kadar farklıdır?

4.  Doğrusal karşıtlık puanlarının ortalaması ve standart sapmasından $t$’yi hesaplayın. Bu test neden küresellik gerektirmez?

## B1–B3: Bağımsız Çözüm

1.  Orthodont kaynak tablosundan cinsiyet ve yaş için F’yi ve iki farklı hata terimini açıklayın.

2.  $\hat\varepsilon_{GG}=.867$ ile etkileşimin düzeltilmiş sd’lerini bulun. Özgün HF’nin neden 1’e kırpıldığını açıklayın.

3.  Genel etkileşim $p=.078$ iken büyüme hızı karşıtlığı $p=.019$ veriyor. İki sonucu nasıl birlikte raporlarsınız?

## H1: Hatalı Raporu Onarma

> “144 ölçümü tek yönlü ANOVA’ya koyduk. Mauchly anlamlı çıktığı için ANOVA yapılamaz. Kısmi eta-kare .47 olduğuna göre gün, bağımsız gruplar deneyindeki kadar büyük bir etki. Etkileşim anlamsız olduğundan kızlar ve erkekler aynı hızla büyüyor. En büyük farkı veren 2. ve 7. günleri seçip eşli t yaptık.”

Beş iddiayı düzeltin.

## P1: Tekrarlı Ölçüm Çalışması Planı

Bir müdahalenin dört haftalık izlem çalışması için tasarımı yazın: kontrol grubu, ölçüm zamanları, sıra etkileri, önceden belirlenmiş karşıtlıklar (örneğin grup $\times$ doğrusal zaman), küresellik kararı, eksik veri stratejisi (ANOVA mı karma model mi), etki büyüklüğü türü ve raporlanacak tablolar. Rubrik: tasarım 25, analiz planı 30, varsayımlar 20, raporlama 15, yeniden üretim 10 puan.

# Alıştırmalar

## Kolay Düzey

1.  Denek içi desenin bağımsız gruplar desenine göre temel üstünlüğü nedir?

2.  Küresellik varsayımı neyi ifade eder? İki ölçümlü desende neden sorun olmaz?

3.  Greenhouse–Geisser düzeltmesi F testinde neyi değiştirir?

4.  Uzun ve geniş veri biçimi arasındaki fark nedir?

5.  Karma (arası–içi) desende kaç ayrı hata terimi vardır?

## Orta Düzey

1.  Beş ölçümlü bir desende $\hat\varepsilon_{GG}=.62$, $F(4,76)=3.10$ bulunmuştur. Düzeltilmiş sd’leri yazın ve kararın nasıl değişebileceğini açıklayın.

2.  Bir araştırmacı $\eta^2_p=.40$ bulmuş ve bağımsız gruplar çalışmasındaki $\eta^2=.10$ ile karşılaştırıyor. Uyarınız nedir?

3.  Üç koşullu bir deneyde koşul sırası tüm katılımcılarda aynıdır. Hangi sorun doğar, nasıl önlenir?

4.  Dört ölçümlü bir çalışmada 40 katılımcının 9’unun bir ölçümü eksiktir. Tekrarlı ölçümler ANOVA’sı ile karma model arasında nasıl seçim yaparsınız?

5.  Karma desende etkileşim anlamlıdır. Ana etkileri nasıl yorumlarsınız?

## İleri Düzey

1.  Çok değişkenli yaklaşım ile GG düzeltmeli tek değişkenli test hangi koşullarda farklı sonuç verir? Hangisini ne zaman seçersiniz?

2.  Karma modelde rastgele eğim varyansı sıfıra yakın bulunursa ne sonuç çıkarırsınız?

3.  Genel etkileşim testi yerine önceden belirlenmiş tek sd’li karşıtlık kullanmanın gerekçesini ve riskini tartışın.

4.  Kişiler arası kovaryans matrisleri gruplar arasında belirgin biçimde farklıysa karma desen ANOVA’sı yerine ne yapılabilir?

5.  Güçlü bir tekrarlı ölçüm raporunda bulunması gereken en az beş unsuru yazın.


## Revizyon 11: eksik izlem ve aynı hedef

## T1–T3: Eksik İzlem ve Hedef Denetimi

1.  Özgün veride 144 tam ölçüm varken maskede 104 ölçüm/18 kişi, tam kişilerde 56 ölçüm/7 kişi kalmasını açıklayın. Üç satırda neden aynı doğrusal model kullanıldı? Tam-veri eğimi bilinen anakütle gerçeği midir?

2.  Maskenin MAR türü olduğu hangi tasarım bilgisinden gelir? Karma modelin yakınsaması, MAR veya doğru kovaryans kanıtı mıdır? 18 kişiyle normal Wald aralığı ve kişi eğim dağılımı aralığını ayırın.

3.  Dört yaş için Holm ve Bonferroni sonuçlarını hesaplayın. Bu kararlar genel etkileşim ve doğrusal eğim karşıtlığı hakkında neden aynı iddiayı üretmez? Karşılaştırma ailesinin ne zaman tanımlanması gerekir?

## Çekirdek öğrenme rotası

1. Kişi içi bağımlılığı analiz biriminden ayırır.
2. Zaman ve grup etkileşimini profil grafiğiyle yorumlar.
3. Tekrarlı ANOVA ile karma modelin koşullarını karşılaştırır.

**İleri rota:** Eksik izlem, kovaryans yapısı ve küçük örneklem çıkarımı; Bölüm 16 ile birlikte derinleştirilebilir.

**Ç1:** 18 kişinin sekizer ölçümü 144 bağımsız kişi midir?

**Karar görevi:** Mevcut ölçümler veya yalnız tam kişiler yaklaşımını seçin; eğim, kişi sayısı ve kayıp varsayımını birlikte karşılaştırın.

[Rubrik ve teslim rehberi](RUBRIK.md).
