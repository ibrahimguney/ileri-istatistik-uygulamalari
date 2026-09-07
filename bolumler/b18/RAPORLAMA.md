# Bölüm 18 — SPSS Çıktısını Akademik Raporlamaya Dönüştürme

Bu bölümde amaç SPSS tablosunu kopyalamak değil, **hangi analizin hangi aktif veri durumu altında çalıştırıldığını ve doğru tablodan alınan sonuçların bilimsel olarak ne söylediğini** açık biçimde raporlamaktır.

## 1. Raporun yöntem cümlesi

Bir SPSS analizini raporlarken en az şu dört unsur görünmelidir:

1. kullanılan veri ve analiz örneklemi,
2. test türü ve fark/grup yönü,
3. varsa filtre veya eşleştirme kuralı,
4. temel sonuç ve belirsizlik ölçüsü.

### Eşli test için yöntem örüntüsü

`sleep` verisinde aynı 10 ID'nin iki koşuldaki ölçümleri ID üzerinden eşleştirilmiş ve fark `group2-group1` yönünde tanımlanmıştır. İki koşul arasındaki ortalama fark iki yönlü eşli örneklemler t-testiyle incelenmiştir.

### Bağımsız test için yöntem örüntüsü

`ToothGrowth` verisinde analiz öncesinde `dose=1` filtresi uygulanmış; OJ ve VC grupları arasındaki ortalama fark, varyans eşitliğini zorunlu kılmayan Welch bağımsız örneklemler t-testiyle incelenmiştir.

## 2. Eşli t-testinde üç tabloyu karıştırmayın

SPSS'in eşli t-testi tipik olarak üç farklı bilgi kümesi sunar:

- **Paired Samples Statistics:** iki koşulun ayrı ortalama ve SS'leri,
- **Paired Samples Correlations:** aynı bireylerin iki ölçümü arasındaki korelasyon,
- **Paired Samples Test:** farkın ortalaması, standart hatası, güven aralığı, t, df ve p.

Araştırma sorusu “iki koşul arasında ortalama fark var mı?” ise ana çıkarım **Paired Samples Test** tablosundadır. Korelasyon tablosundaki p değeri bu sorunun p değeri değildir.

## 3. `sleep` ana sonuç için kontrol sayıları

- n=10 eşleşmiş çift,
- group1: M=0.75, SS=1.789,
- group2: M=2.33, SS=2.002,
- eşler arası r≈0.795,
- fark `group2-group1`: M=1.58, SS=1.230,
- t(9)=4.062,
- p=.00283,
- %95 GA [0.700, 2.460].

### Akademik rapor örneği

> Aynı 10 katılımcının iki koşuldaki ölçümleri karşılaştırıldığında, ikinci koşuldaki değerler (M=2.33, SS=2.00) birinci koşula göre (M=0.75, SS=1.79) ortalama 1.58 birim daha yüksekti. Bu fark istatistiksel olarak anlamlıydı, t(9)=4.06, p=.003, %95 GA [0.70, 2.46].

Son cümle bağlama uygun sınırlılıkla tamamlanmalıdır; tarihsel `sleep` verisi klinik tedavi önerisi değildir.

## 4. Bağımsız t-testinde iki satırı okuyun

SPSS bağımsız örneklemler t-testinde genellikle:

- `Equal variances assumed`,
- `Equal variances not assumed`

satırlarını birlikte verir.

Levene testi varyans yapısına ilişkin tanısal bilgi sunar. Bu pakette Welch yaklaşımı önceden ana yöntem olarak belirlenmiştir; bu nedenle `Equal variances not assumed` satırı raporlanır. Levene p>.05 sonucu, eşit varyans satırını bilimsel olarak zorunlu hale getiren otomatik bir anahtar olarak ele alınmaz.

## 5. `ToothGrowth`, dose=1 kontrol sayıları

Filtre sonrası:

- toplam n=20,
- OJ: n=10, M=22.70, SS=3.911,
- VC: n=10, M=16.77, SS=2.515,
- fark `OJ-VC`=5.93,
- Levene F≈2.271, p≈.149,
- Welch t≈4.033,
- df≈15.358,
- p≈.00104,
- %95 GA [2.802, 9.058].

### Akademik rapor örneği

> Yalnız `dose=1` gözlemleri incelendiğinde OJ grubunun ortalaması (M=22.70, SS=3.91, n=10) VC grubundan (M=16.77, SS=2.52, n=10) 5.93 birim daha yüksekti. Welch bağımsız örneklemler t-testi bu fark için t(15.36)=4.03, p=.001 ve %95 GA [2.80, 9.06] verdi.

Bu hayvan verisi insanlara yönelik doz veya tedavi önerisine dönüştürülmemelidir.

## 6. Filtre raporlamada görünür olmalıdır

“Bağımsız t-testi yapıldı” demek yeterli değildir. Eğer 60 satırlık dosyanın yalnız 20 satırı analiz edildiyse şu bilgi görünür olmalıdır:

- hangi değişkenle filtre yapıldığı,
- filtre koşulu (`dose=1`),
- filtre sonrası analiz n'si.

Filtrenin raporda görünmemesi, başka bir araştırmacının aynı sonucu yeniden üretmesini zorlaştırır.

## 7. Eksik eş olduğunda eski sonucu taşımayın

`sleep_eksik.csv` 20 satır içerir fakat yalnız 9 tam eş vardır. Bu kopyada:

- n=9 çift,
- fark M=1.60,
- t(8)=3.684,
- p=.00618,
- %95 GA [0.599, 2.601].

Ana veri setinin 10-çift sonucu bu dosyaya kopyalanamaz. Her analizde geçerli n yeniden okunmalıdır.

## 8. Ağırlık ve Split File nasıl raporlanır?

Ağırlık veya Split File gerçekten kullanılmışsa:

- değişken adı,
- kullanım amacı,
- analiz üzerindeki etkisi

belirtilmelidir. Bunlar yanlışlıkla açık kaldıysa sonuç yeniden üretilmelidir; yalnızca rapora “açıktı” yazmak hatayı düzeltmez.

## 9. Kaçınılması gereken raporlama hataları

- SPSS çıktısındaki tüm tabloları yorumsuz kopyalamak,
- Paired Samples Correlations p değerini eşli fark testinin p değeri sanmak,
- Levene p>.05 ise Welch sonucunu görmezden gelmek gerektiğini düşünmek,
- filtre sonrası n'yi yazmamak,
- dosya satır sayısını bağımsız gözlem sayısı sanmak,
- eksik eş olduğunda eski n ve eski farkı kullanmak,
- ağırlığı yeni katılımcı yaratma aracı gibi yorumlamak,
- p değerini etki büyüklüğü veya bilimsel önem ile eşitlemek.

## 10. Minimum teslim paragrafı kontrolü

Son metniniz şu sorulara cevap veriyor mu?

- Kim/hangi kayıtlar analiz edildi?
- Hangi aktif filtre veya eşleştirme kuralı vardı?
- Hangi test kullanıldı?
- Farkın yönü nedir?
- n, ortalamalar, fark, güven aralığı, t/df/p nedir?
- Sonuç hangi sınırın ötesine genellenemez?
