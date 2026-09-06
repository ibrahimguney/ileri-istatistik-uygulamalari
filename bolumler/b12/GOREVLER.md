# Bölüm 12 — Görevler

Kitabın D1–D3, G1–G4, B1–B3, H1 ve P1 etkinliklerini izleyin. Önce VERI.md.
P değerinin hesap türünü, bağ/sıfır kurallarını ve aileyi her raporda belirtin.

## D1–D3: Analizden önce
1. ToothGrowth doz 1'de OJ/VC karşılaştırması neden bağımsız, sleep koşulları
   neden eşlidir? Ayrı hayvan kaydı bağımsızlığı tek başına kanıtlar mı?
2. Friedman örneğinde satır ve sütun neyi gösterir? İki koşunun ortalamasını
   iki ayrı gözlem gibi saymak neden yanlıştır? 18/22 kaynak uyuşmazlığını yazın.
3. “Shapiro anlamlıysa Wilcoxon seç” kuralında hangi hedef ve varsayım bilgileri eksiktir?

## G1–G4: Hesap ve yorum
1. OJ sıra toplamından U, çift kazanımlarından A hesaplayın. 88.5 ve 11.5
   nasıl aynı verinin U değerleridir? Kesin ve yaklaşık p'leri ayırın.
2. Sleep'te bir sıfır ve iki bağlı 1.3 farkını işleyin. W+, W−, T ve kesin
   p'yi bulun. 10 çift olmasına rağmen neden 512 işaret örüntüsü vardır?
3. OJ'nin H istatistiğini bağ düzeltmesiyle hesaplayın. Dunn'ın üç ham p'sine
   Holm uygulayın; her p'yi üçle çarpmaktan farkını açıklayın.
4. Friedman Q'dan Kendall W'yi, 311 aşım ve 99999 denemeden Monte Carlo p'yi
   hesaplayın. Bu sayı neden tam sayım p'si değildir? MC standart hatasını yorumlayın.

## B1–B3: Bağımsız çözüm
1. VC üç doz için ortak sıra toplamları, bağ-düzeltilmiş H ve Dunn–Holm tablosu
   üretin. OJ'nin sıralarını taşımayın; VC ayrı bir öğretim ailesidir.
2. Tüm 60 kayıtta len≥20 tablosunun beklenen frekanslarını, düzeltmesiz Pearson
   istatistiğini ve Cramér V'yi hesaplayın. Fisher p farkını, eşiğin keyfî öğretim
   tercihini ve dozların birleştirilmesini tartışın.
3. En fazla 100 kelimeyle Friedman ve üç ikili karşılaştırmayı raporlayın.
   18/22 kaynak uyuşmazlığını, yaklaşık p ve Holm ailesini gizlemeyin.

## H1: Altı hatalı iddiayı düzeltin
“Parametrik olmayan testlerin varsayımı yoktur. U yalnız medyanları karşılaştırır.
Bağ varken exact seçmek her zaman kesindir. Sleep sıra-biserial 1: herkes yarar
gördü. Friedman'da 66 bağımsız kişi var. Genel H anlamlıysa tüm çiftler düzeltmesiz
raporlanabilir.” Her iddiayı bir hesap veya tasarım koşuluyla düzeltin.

## P1: Yeniden üretim dosyası
Kaynak sözlüğü, tamamlanmış notebook/kod, iki grafik, bütün sonuç tabloları ve
bir sayfalık rapor teslim edin. Eşleşmeyi satır karıştırarak denetleyin; kaynak
hash eşleşmesini uzaktan doğrulama diye sunmayın. U tam etiket sayımı, Wilcoxon
tam işaret sayımı, Friedman Monte Carlo ve normal/ki-kare yaklaşımlarını ayırın.
OJ Dunn, VC Dunn ve Friedman sonrası üç çift ayrı ailelerdir; bölümün bütün
testleri için tek .05 aile hatası kontrolü iddia edilmez.

| Ölçüt | Puan |
|---|---:|
| Kaynak ve eşleme | 20 |
| Bağlar ve sıfırlar | 20 |
| Kesin/yaklaşık yöntem ayrımı | 25 |
| Aile ve yorum | 25 |
| Yeniden üretim | 10 |

Yapılmamış R/SPSS çalıştırması, uzak veri doğrulaması veya yeni deney yapılmış gibi yazılmaz.