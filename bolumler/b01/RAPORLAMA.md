# B01 Akademik Raporlama Rehberi

Bu bölümde amaç bir hipotez testini raporlamak değil; **verinin ne olduğunu, nasıl seçildiğini, neyi temsil ettiğini ve hangi sınırlar içinde yorumlanabileceğini** açık biçimde yazabilmektir.

## 1. Veri kaynağını tanımlayın

Uygun bir rapor, verinin yalnız dosya adını değil kaynağını ve kapsamını belirtmelidir.

Örnek yapı:

> Uygulamada UCI Student Performance veri setinin Portekizce dersi kaynağından alınmış 80 kayıtlık sınırlı bir alıntı kullanılmıştır. Analizde okul kodu (`school`), birinci dönem notu (`G1`) ve yıl sonu notu (`G3`) alanları incelenmiştir.

## 2. Analiz birimini yazın

Bir satırın neyi temsil ettiğini belirtin. Aynı kayda ait tekrarlı ölçümlerin bağımsız birimler olmadığını gerekiyorsa özellikle vurgulayın.

> Her satır bir öğrenci kaydını temsil etmektedir. Aynı satırdaki G1 ve G3 değerleri aynı kayda ait iki not olduğundan bağımsız iki gözlem olarak değerlendirilmemiştir.

## 3. Örnekleme/seçim sınırını belirtin

Bu veri, olasılıklı örnekleme ile seçilmiş temsili bir örneklem gibi sunulmamalıdır.

Uygun ifade:

> İncelenen 80 kayıt, kaynak verinin sınırlı ve sıralı bir alıntısıdır; bu nedenle bulgular hedef bir öğrenci anakütlesine doğrudan genellenmemiştir.

Kaçınılması gereken ifade:

> “Örneklem öğrencileri temsil etmektedir.”

Bu iddia ancak örnekleme tasarımı ve hedef anakütle açıkça bunu destekliyorsa kullanılabilir.

## 4. Betimsel sonuç ile değer yargısını ayırın

Örneğin G3 ortalamasının yaklaşık 12.64 olması betimsel bir sonuçtur. “Başarılı”, “iyi”, “yeterli” gibi ifadeler ise ek bir ölçüt gerektirir.

Daha güvenli ifade:

> İncelenen 80 kayıtta G3 ortalaması yaklaşık 12.64'tür.

Daha güçlü bir başarı yorumu yapılacaksa başarı eşiğinin önceden tanımlanmış olması gerekir.

## 5. Frekans ve yüzdeyi birlikte raporlayın

Kategoriler veya ayrık puanlar için hem sayı hem yüzde yararlıdır. Paydanın ne olduğu açık olmalıdır.

Örnek:

> G3=12 değeri 16 kayıtta, G3=13 değeri ise 15 kayıtta gözlenmiştir. Bu veri dosyasında eksik G3 değeri bulunmadığından yüzdelerin paydası 80'dir.

Eksik değer varsa toplam satır sayısı ile geçerli gözlem sayısını birbirine karıştırmayın.

## 6. Grafik seçimini gerekçelendirin

Grafik adı vermek yeterli değildir; neden uygun olduğunu da açıklayın.

- Tek nicel değişkenin dağılımı: histogram veya nokta grafiği.
- İki nicel değişkenin ilişkisi: saçılım grafiği.
- Kategorik değişken frekansı: çubuk grafik.

Bu alıntıda `school` yalnız tek düzey içerdiği için okul dağılımını gösteren grafik bilimsel açıdan sınırlı bilgi taşır.

## 7. Sistematik örnekleme uygulamasını doğru çerçeveleyin

Başlangıç 3 ve aralık 5 ile yapılan seçim, **sistematik seçim algoritmasını göstermek için bir öğretim uygulamasıdır**. Bu işlem ilk 80 kaydın kaynağa göre temsili olmadığını değiştirmez.

Uygun ifade:

> Sistematik seçim örneğinde 3. kayıttan başlanarak her beşinci kayıt alınmış ve 16 kayıt seçilmiştir. Bu uygulama seçim mekanizmasını göstermek amacıyla yapılmış, temsili örnekleme iddiasında bulunulmamıştır.

## 8. Nedensellikten kaçının

B01 verisi gözlemsel bir alıntıdır. G1 ve G3 arasında görülen desenler nedensel etki olarak yazılmamalıdır.

Kaçınılması gereken:

> “G1 puanı G3 puanını artırmaktadır.”

Daha güvenli:

> “Bu kayıtlar içinde G1 ve G3 birlikte değişmektedir.”

Nedensel yorum için yalnız ilişki değil, uygun araştırma tasarımı gerekir.

## 9. Yeniden üretilebilirlik notu

Raporun sonunda veri dosyası ve analiz dosyasını belirtmek yararlıdır.

> Teknik kontroller `veri.csv` ve `analiz.py` kullanılarak yeniden üretilebilir. Referans değerler `beklenen.json` dosyasında tutulmaktadır.

## Önerilen kısa rapor şablonu

> Bu uygulamada UCI Student Performance veri setinden alınmış 80 kayıtlık sınırlı bir alıntı incelenmiştir. Her satır bir öğrenci kaydını temsil etmekte; G1 ve G3 aynı kayda ait iki farklı not olarak ele alınmaktadır. Veri dosyasında eksik hücre bulunmamaktadır. İncelenen kayıtlarda G1 ortalaması 12.18, G3 ortalaması 12.64'tür. Bulgular yalnız bu 80 kayıt için betimsel olarak yorumlanmış; sıralı alıntının olasılıklı ve temsili bir örneklem olmaması nedeniyle daha geniş öğrenci anakütlelerine genelleme yapılmamıştır.

## Teslim öncesi kontrol listesi

- [ ] Hedef anakütleyi veya genelleme sınırını açıkça yazdım.
- [ ] Analiz birimini tanımladım.
- [ ] Veri kaynağını belirttim.
- [ ] Örnek ile örnekleme çerçevesini karıştırmadım.
- [ ] Frekans/yüzdede doğru paydayı kullandım.
- [ ] Grafik türünü değişken yapısına göre seçtim.
- [ ] Betimsel sonuçtan nedensellik çıkarmadım.
- [ ] “Başarı” gibi normatif ifadeleri ölçütsüz kullanmadım.
- [ ] Yeniden üretim dosyalarını belirttim.
