# Bölüm 6 — görevler

Güncel kitap bölümünün etkinlik ve alıştırmalarıdır. Önce kendi çözümünüzü
üretin; ardından çözümleri kontrol edin. Kitap sayfa numaraları PDF sürümüne
göre değişebilir.

## D1–D3: Hesaptan Önce Düşünün

1.  Uyku dosyasının 20 satırını 20 bağımsız kişi saymak hangi bilgiyi kaybettirir? Negatif `extra` ne anlama gelir?

2.  Tek örneklem örneğinde sıfır referansı neden anlamlıdır? Sıfır, ayrı bir kontrol grubunun tahmin edilen ortalaması mıdır?

3.  Diş verisinde aynı satır numarası sırasındaki OJ ve VC kayıtlarını neden eşleştiremeyiz? 1 mg/gün seçiminin kapsamını ve bağımsızlık için gereken tasarım bilgisini açıklayın.

Yanıtlar Ek F’de, Bölüm 6 gerçek veri etkinlikleri başlığı altındadır (s. kitaptaki ilgili sayfa).

# Rehberli ve Bağımsız Etkinlikler

## G1–G3: Hesabı Denetleyin

1.  İlaç 1 sütunundan toplamı, ortalamayı, örneklem SS’sini ve %95 aralığı hesaplayın. $p>.05$ sonucunu “ilaç işe yaramıyor” demeden raporlayın.

2.  ID ile 10 farkı bulun. $s_1^2+s_2^2-2s_{12}=s_D^2$ eşitliğini ve $t=d_z\sqrt n$ ilişkisini denetleyin. Saat yerine dakika kullanıldığında fark, aralık, $t$, $p$ ve $d_z$ nasıl değişir?

3.  Doz 1’de Welch serbestlik derecesini yeniden hesaplayın. $n_1=n_2$ iken Welch ve Student t değerlerinin eşit, $p$ değerlerinin farklı olabilmesini formüllerden açıklayın.

## B1–B3: Yeni Dozda Bağımsız Çözüm

Bu kez yalnız 2 mg/gün dozundaki OJ ve VC kayıtlarını seçin; doz 1’in özetlerini taşımayın.

1.  İki grubun $n$, ortalama, SS, OJ$-$VC farkı, Welch $t$, serbestlik derecesi ve %95 aralığını hesaplayın.

2.  Birleştirilmiş SS ile $d$’yi hesaplayın. Büyük $p$ değeri eşdeğerlik kanıtı mıdır? Aralığın izin verdiği değerleri kullanarak açıklayın; önceden belirlenmiş bir önem sınırının eksikliğini tartışın.

3.  En fazla 100 kelimelik bir rapor yazın. Doz 1’de anlamlı, doz 2’de anlamsız fark bulunması neden tek başına doz etkileşimi testinin yerine geçmez?

## H1: Hatalı Raporu Onarın

> “Uyku dosyasında 20 bağımsız kişi vardır. Daha küçük $p$ verdiği için eşli testi seçtik. Levene $p>.05$ olduğundan varyansların eşitliği kanıtlandı. Doz 2’de $p=.964$ olduğu için OJ ve VC kesin eşdeğerdir. %95 aralık hastaların %95’inin farklarını kapsar. ID 9’u silmek $p$’yi küçülttüğünden ana rapora silinmiş analizi koyduk.”

Altı iddiayı tasarım, standart hata, güven aralığı ve raporlama ilkeleriyle düzeltin.

## P1: Yeniden Üretim ve Duyarlılık Projesi

Yerel kaynağın 20/60 satırını ve uyku verisinin 10 ID’sini doğrulayın. Satırları karıştırıp ID ile yeniden eşleştirin; aynı sonuçları elde ettiğinizi gösterin. Her çifti sırayla dışarıda bırakan analizde ortalama fark ve aralıkları raporlayın; tek bir silme sonucunu seçmeyin. Uyku eşleştirme grafiği, fark Q–Q grafiği ve doz 1 OJ/VC dağılımını yorumlayın. Teslim: kaynak/analiz sözlüğü, çalışan kod, grafikler ve bir sayfalık sınırlılık raporu.

<div class="center">

| Ölçüt                                     | Puan |
|:------------------------------------------|-----:|
| Kaynak, analiz birimi ve ID eşleştirmesi  |   20 |
| Üç testin doğru hesaplanması ve fark yönü |   25 |
| Güven aralığı ve etki büyüklüğü paydası   |   20 |
| Tanılar ve bütün çiftler için duyarlılık  |   20 |
| Yeniden çalıştırma ve ölçülü raporlama    |   15 |

</div>

# Alıştırmalar

## Kolay Düzey

1.  Parametrik test genel olarak nedir?

2.  Eşleştirilmiş örneklemler t-testi ne zaman tercih edilir?

3.  Bağımsız örneklemler t-testinde varyans homojenliği neden önemlidir?

4.  Güven aralığının test yorumundaki pratik değeri nedir?

5.  Etki büyüklüğü neden $p$-değerine ek olarak gereklidir?

## Orta Düzey

1.  Bir sınıf ortalaması 70 ölçüt puanıyla karşılaştırılacaktır. Hangi test uygundur?

2.  Farklı yöntemlerle öğrenim gören iki ayrı öğrenci grubu karşılaştırılacaktır. Hangi test kullanılmalıdır?

3.  Aynı katılımcılar uygulama öncesi ve sonrası ölçülmüştür. Hangi test uygundur?

4.  Bağımsız örneklemler t-testinde $t(58)=2.31$, $p=.024$ bulunmuştur. $\alpha=.05$ düzeyinde sonuç ne gösterir?

5.  Levene testi anlamlı çıkmıştır. Bu ne anlama gelir ve araştırmacı neyi dikkate almalıdır?

## İleri Düzey

1.  $n=500$ olan bir çalışmada ortalama farkı anlamlı, Cohen $d=0.08$ bulunmuştur. Nasıl yorumlanır?

2.  Eşleştirilmiş tasarımda ön-test ve son-test ayrı ayrı normal değildir; fark puanları yaklaşık normaldir. Eşleştirilmiş t-testi savunulabilir mi?

3.  İki sınıf bağımsız t-testiyle karşılaştırılmış, fakat öğrenciler sınıflara rastgele atanmamıştır. Hangi sınırlılık raporlanmalıdır?

4.  Tek örneklem t-testinde ortalama farkı için %95 GA $[-1.20,4.80]$ bulunmuştur. Bu aralık karar ile nasıl ilişkilidir?

5.  Bir t-testinden sonra yalnızca “$p<.05$” raporlanmıştır. Daha güçlü rapor için en az dört ek unsur yazınız.
