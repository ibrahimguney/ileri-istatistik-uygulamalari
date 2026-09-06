# Bölüm 4 — Çözüm rehberi

Önce GOREVLER.md sorularını çözün; ayrıntılı sayılar beklenen.json içindedir.

## Gerçek eşleşmiş veri

n=10 kişi; koşul2−koşul1 fark ortalaması 1.58 saat, örneklem s=1.229995,
SH=.388959. t(9)=4.062128; iki yönlü p=.002832890;
%95 güven aralığı [.700114, 2.459886] saat. d_z=1.284558;
standartlaştırıcı fark s'sidir ve d_z×sqrt(10)=t.

Sağ kuyruk p=.001416445, sol kuyruk p=.998583555 farklı alternatiflerdir.
Fark yönü terslenince t'nin işareti değişir; iki yönlü p aynı kalır,
aralık [−2.459886, −.700114] olur. ID'ye göre eşleştirme satır karıştırmadan
etkilenmez. Eksik/tekrarlı kişi–koşul kaydı reddedilmelidir.

p, H0'ın doğru olma olasılığı değildir. Test ve aralık model varsayımlarına
bağlıdır; küçük p pratik önem veya nedensel tedavi etkisi kanıtı değildir.
Küçük örneklem ve en büyük fark saklanmaz; varsayımlar kanıtlanmış sayılmaz.

## Kurgu örnekleri

Dolum: t(24)=−2, iki yönlü p=.056940; %95 aralık [491.872203,500.127797].
Sol kuyruk p=.028470'tir; sonuç görüldükten sonra yön seçilmez. Reddetmeme
sıfır etki veya eşdeğerlik kanıtı değildir.

Ders özeti: n=16, ortalama74.5, s8, referans70 → t(15)=2.25;
iki yönlü p=.039888, sağ p=.019944; aralık [70.237101,78.762899].
İleri özet: n=36, ortalama52, s12, referans50 → t(35)=1, iki yönlü p=.324174.
Bu özetlerin arkasında yeni üretilmiş ham veri yoktur.

2×2 kurgu tablosunda beklenen her hücre25; düzeltmesiz Pearson ki-kare=4,
sd=1, p=.045500, V=.2. Başka test sonuçlarıyla aynı etiket kullanılmaz.

## İdeal model simülasyonu

Python tohum20260906, her koşulda20000 tekrar, n25, sigma1, normal model:

| Gerçek d | İki yönlü red | Kuramsal red | MC SH | Gerçek ortalama kapsaması |
|---|---:|---:|---:|---:|
| 0 | .0502 | .0500 | .001544 | .9498 |
| .5 | .6667 | .669708 | .003333 | .9474 |

d=0 altında yanlış, veriden yön seçen tek kuyruk kuralı .1016 red verir.
Her tekrarda iki yönlü red, sıfırın %95 aralık dışında kalmasıyla eşleşir.
d=.5 altında gerçek .5'i kapsama ile sıfırı kapsamama aynı olay değildir.
Sayılar belirtilen Python ortamına aittir; R aynı tohumla aynı diziyi üretmek
zorunda değildir. Simülasyon uyku verisinin gücü veya varsayım doğrulaması değildir.
Yirmi bağımsız doğru H0 testi için aile hatası 1−.95^20=.641514;
bağımlı testler için bu eşitlik doğrudan kullanılmaz.