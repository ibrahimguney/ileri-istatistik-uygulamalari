# Bölüm 11 — Görevler

Kitaptaki D1–D3, G1–G3, B1–B3, H1 ve P1 sırasını izleyin. Önce VERI.md'yi
okuyun. Kaynak değerlerini değiştirmeyin; fark yönü ve aileyi her sonuçta yazın.

## D1–D3: Analizden önce
1. İki faktörü, düzeylerini, altı hücreyi ve analiz birimini belirleyin. Bu veri
   neden 20 hayvanın üç tekrarlı ölçümü değildir?
2. OJ grubunda üç doz ortalamasının eşitliği ile tüm kayıtlardaki uygulama–doz
   etkileşimi hangi farklı hipotezleri sınar?
3. Dozu üç düzeyli faktör yerine tek sayısal eğimle modellemek neyi kısıtlar?
   0.5, 1 ve 2'nin eşit aralıklı olmadığını dikkate alın.

## G1–G3: Rehberli hesaplar
1. OJ'nin 30 kaydından SSG, SSW, SST, MSE, F, eta² ve omega² hesaplayın.
   Hata serbestlik derecesi neden 29 değil 27'dir?
2. OJ'de 2−1 farkının Tukey aralığını kurun. Genel F anlamlıyken aralığın sıfırı
   içermesi çelişki midir? Games–Howell ile aynı çift ve aileyi karşılaştırın.
3. Tam modelin dört KT bileşenini toplayın; etkileşim F ve kısmi eta² değerlerini
   bulun. MSE=13.187148, df=54 ve üçlü Bonferroni ile doz 1 OJ−VC aralığını kurun.

## B1–B3: VC grubunda bağımsız çözüm
Yalnız VC'nin 30 kaydını kullanın. OJ'nin MSE'sini taşımayın; bu yeni dış doğrulama değildir.
1. Üç dozun özetleri, klasik ANOVA tablosu, eta² ve omega² değerlerini hesaplayın.
2. Üç çiftlik Tukey ailesini ve Welch/Games–Howell alternatifini kurun. Hangi
   aralıklar sıfırı içerir? Hangi varyans modeli ve aileyi kullandığınızı yazın.
3. En fazla 100 kelimeyle kapsam, yön, aile ve varsayımları raporlayın.
   OJ ve VC'nin ayrı p değerlerinin karşılaştırılması neden etkileşim testi değildir?

## H1: Altı hatalı iddia
“Genel F anlamlıysa bütün doz çiftleri farklıdır. Levene p>.05 ile eş varyans
kanıtlandı. Sayısal doz ile üç düzeyli faktör aynı modeldir. Tam modelde hata
df=59'dur. Üç kısmi eta-kare toplanarak toplam açıklanan oran bulunur. Ayrı
doz p değerlerini karşılaştırmak etkileşim testidir.” Her iddiayı düzeltin.

## P1: Ortak model ve çoklu karşılaştırma denetimi
60 kayıt ve her hücrede 10 gözlemi doğrulayın. OJ klasik/Welch, Tukey/Games–Howell,
faktöriyel KT ayrıştırması ve üç OJ−VC farkının Bonferroni aralıklarını yeniden
üretin. Klasik etkileşim ile HC3 ortak testi karşılaştırın. Satırları karıştırın;
hücreler ve model sonuçlarının değişmediğini gösterin. Üç grafiği yorumlayın.
Yerel hash denetimini uzak kaynak doğrulaması olarak sunmayın.
Teslim: kod/notebook, kaynak sözlüğü, ozet.json, üç grafik ve bir sayfalık eleştirel rapor.

| Ölçüt | Puan |
|---|---:|
| Kaynak, hücreler ve faktör kodlaması | 20 |
| Kareler toplamları ve etki büyüklükleri | 25 |
| Karşılaştırma ailesi ve aralıkların eşleştirilmesi | 25 |
| Etkileşim, tanılar ve HC3 duyarlılığı | 20 |
| Yeniden üretim ve sınırlılık raporu | 10 |

Kısmen doğru fakat eksik gerekçe kısmi puan alır. Yapılmamış R/SPSS çalıştırması,
uzak veri doğrulaması veya yeni araştırma önkaydı yapılmış gibi yazılmaz.