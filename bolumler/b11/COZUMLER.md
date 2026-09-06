# Bölüm 11 — Çözüm rehberi

Yerel arşiv yeniden analiz edilir; özgün çalışmanın sonuç tablosu olduğu iddia
edilmez. Tam hassasiyet beklenen.json içindedir. Önce kendi çözümünüzü tamamlayın.

## D1–D3
1. Uygulama OJ/VC, doz 0.5/1/2 mg/gün; 2×3=6 hücre, her hücrede 10 ayrı hayvan.
   Aynı hayvanın üç ölçümü değildir. Kafes/ortak çevre ve atama bilgisi kısa
   tabloda bulunmadığından bağımsızlık ayrıca savunulmalıdır.
2. OJ tek yönlü H0 üç doz ortalamasını eşitler. Ortak etkileşim H0, OJ−VC
   farkının üç dozda aynı olmasıdır; iki ayrı genel F testinin p farkı değildir.
3. Kategorik doz tek doğrusal eğim zorunluluğunu kaldırır. İki serbestlik derecesi
   vardır; sayısal eğim tek dereceli ve mg/gün ölçeğinde doğrusal bir kısıttır.

## G1: OJ tek yönlü
Doz sırasıyla ortalamalar 13.23, 22.70, 26.06; her grupta n=10.
SSG=885.264667, SSW=380.105000, SST=1265.369667.
SSG+SSW=SST; df_grup=3−1=2, df_hata=30−3=27.
MSE=14.077963; F(2,27)=31.441504, p≈8.88716×10⁻⁸.
Eta²=SSG/SST=.699610; omega²=(SSG−2MSE)/(SST+MSE)=.669905.
Bu katsayılar klasik tek yönlü modele aittir; Welch etki büyüklüğü diye sunulmaz.
Welch F(2,17.069264)=29.404475, p≈2.95388×10⁻⁶.

## G2: Genel test bütün çiftleri belirlemez
OJ 2−1 farkı=3.36. Üç çiftlik aile için Tukey p=.130926,
%95 eşzamanlı GA=[−.800395,7.520395]. Games–Howell p=.093518,
yaklaşık aile GA=[−.500938,7.220938]. Her ikisi sıfırı içerir;
ortalamaların eşitliği veya eşdeğerlik kanıtlanmaz. Genel F, en az bir
ortalama farkı için kanıt sağlar; bütün çiftlerin ayrışmasını gerektirmez.
Diğer OJ farkları 1−0.5=9.47 ve 2−0.5=12.83'tür; iki yöntemde de
aralıkları sıfırı dışlar. Aynı üç çift ailesi ve yüksek doz−düşük doz yönü korunur.

## G3: Dengeli tam 2×3 model
SS_uygulama=205.350000; SS_doz=2426.434333; SS_etkileşim=108.319000;
SSE=712.106000. Toplam SST=3452.209333.
Altı hücre ortalaması tahmin edildiğinden df_hata=60−6=54; MSE=13.187148.
Etkileşim F=(108.319/2)/MSE=4.106991; p=.021860;
kısmi eta²=108.319/(108.319+712.106)=.132028.
HC3 ortak Wald F(2,54)=3.522846, p=.036471: yaklaşık duyarlılık hesabıdır,
klasik SS oranı veya robust ANOVA kareler toplamı değildir.

Üç OJ−VC karşıtlığının ortak SH=√(MSE×(1/10+1/10))=1.624017.
Bonferroni kritik t, 1−.05/(2×3) kantilinden ve df=54'ten gelir.

| Doz | OJ−VC | Bonferroni p | En az %95 aile aralığı |
|---|---:|---:|---|
| 0.5 | 5.25 | .006277 | [1.237302,9.262698] |
| 1 | 5.93 | .001769 | [1.917302,9.942698] |
| 2 | −.08 | 1.000000 | [−4.092698,3.932698] |

Doz 2'de eşdeğerlik kanıtlanmaz. Bunlar tüm modelin ortak hata varyansını
kullanır; Bölüm 10'daki ayrı Welch aralıkları değildir. Bonferroni ailesi
üç OJ−VC karşılaştırmasıdır, bölümdeki tüm testler değildir.

## B1–B3: VC
Ortalamalar 7.98,16.77,26.14; df=(2,27). Klasik F=67.072379,
p≈3.35732×10⁻¹¹, eta²=.832449, omega²=.814980.
Welch F(2,17.164506)=59.372204, p≈1.94019×10⁻⁸.
VC'nin kendi hata varyansı kullanılır (MSE=12.296333).
Tukey fark ve aralıkları: 1−0.5=8.79 [4.901765,12.678235];
2−0.5=18.16 [14.271765,22.048235]; 2−1=9.37 [5.481765,13.258235].
Games–Howell aralıkları sırasıyla [5.782182,11.797818],
[13.596364,22.723636], [4.871395,13.868605]. Hiçbiri sıfırı içermez.

Örnek kısa rapor: “Tarihsel ToothGrowth verisinde yalnız VC uygulanan 30 ayrı
hayvanın üç kategorik dozu incelendi. Klasik ANOVA F(2,27)=67.072 verdi.
Üç çiftlik Tukey ailesinde tüm yüksek doz−düşük doz aralıkları sıfırı dışladı.
Welch/Games–Howell alternatif varyans modeli de raporlandı. Bulgular eş varyans
ve bağımsızlık gibi model koşullarıyla sınırlıdır; tek başına nedensel etkileşim
veya insanlara genelleme değildir.”

## H1
1. Genel test bütün çiftleri belirlemez; OJ 2−1 örneği karşı kanıttır.
2. Levene/Brown–Forsythe büyük p'si eş varyansı kanıtlamaz.
3. Sayısal eğim kategorik dozla aynı kısıtları kullanmaz.
4. Tam modelde hata df=54; 59 yalnız toplam df'dir.
5. Kısmi eta-karelerin paydaları farklıdır; toplanmaz. Tek yönlü eta² ile karıştırılmaz.
6. P değerlerini karşılaştırmak yerine ortak modelin etkileşim karşıtlığı sınanır.

## P1: Raporun sınırları
Dengeli ve tam bu tasarımda Sum kodlamalı Tip II/III etki SS'leri eşleşir;
dengesiz veya boş hücreli tasarıma otomatik taşınmaz. HC3 heteroskedastisite
bakımından duyarlılık sağlar, kümelenmeyi veya yanlış ortalama modelini düzeltmez.
Artık Shapiro p≈.669424 ve altı hücre medyan merkezli Brown–Forsythe p≈.148361
sonuçları varsayımların kanıtı değildir; grafik ve tasarım bilgisiyle yorumlanır.
Bütün aileler, ham farklar, eşzamanlı aralıklar ve sınırlılıklar görünür olmalıdır.
Yerel hash kaynak bütünlüğüdür; uzak veri doğrulaması değildir. Rubrik GOREVLER.md'dedir.