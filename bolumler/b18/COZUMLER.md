# B18 — Çözümler ve kontrol değerleri

## D1–D3

**D1.** Her ID iki koşulda ölçülür; 20 ölçümden 10 eşli fark oluşur. `group` koşul etiketidir, bağımsız kişi grubu değildir.

**D2.** `FILTER OFF` yalnız filtreyle dışlanan kayıtları yeniden kullanılabilir yapar; silinmiş/değiştirilmiş değerleri geri getirmez. Ham kaynağı yeniden okumak çalışma kopyasındaki değişiklikleri geri alabilir. Gerçek tasarım ağırlıkları hedef anakütle ve belirsizlik hesabının parçası olabilir.

**D3.** Syntax planı belgeler; yürütmeyi kanıtlamaz. Gerçek yürütme için yazılım sürümü, çıktı, uyarı/hata ve veri/syntax sürümü birlikte kaydedilmelidir.

## G1–G4

**G1. Uyku eşli testi**

- `n=10`, ortalama fark `1.58`, `sD=1.2299954833`
- `SH=0.3889587239`
- `t(9)=4.0621276834`
- iki yönlü `p=0.0028328902`
- %95 GA `[0.7001142367, 2.4598857633]` saat
- `dz=1.2845575626`
- koşul korelasyonu `r=0.7951702058`, `p=0.0059649958`

Korelasyon testi `rho=0`, eşli t testi ise ortalama fark için `muD=0` hipotezini sınar; p değerleri birbirinin yerine yazılmaz.

**G2. ToothGrowth, 1 mg/gün**

OJ: `n=10`, ortalama `22.70`, `s=3.9109532796`; VC: `n=10`, ortalama `16.77`, `s=2.5153086844`. Fark `5.93`, SH `1.4704534448`, `t=4.0327696337`.

- Welch: `sd=15.3576716282`, `p=0.0010383759`, GA `[2.8021482492, 9.0578517508]`
- Student: `sd=18`, `p=0.0007807262`, GA `[2.8406919487, 9.0193080513]`
- ortalama merkezli Levene: `F=2.2714507307`, `p=0.1491262589`

Levene'nin anlamsızlığı varyans eşitliğini kanıtlamaz; model daha küçük p verdiği için seçilmez.

**G3. İlk beş ID filtresi**

Farklar `1.2, 2.4, 1.3, 1.3, 0`; `n=5`, ortalama `1.24`, `s=0.8502940668`, `SH=0.3802630668`, `t(4)=3.2609004348`, `p=0.0310544215`, GA `[0.1842204694, 2.2957795306]`. Filtre kapanınca ana `n=10`, ortalama `1.58` geri gelmelidir.

**G4. İki hücre gizleme senaryosu**

Her koşulda 9 geçerli ölçüm vardır; ortak tam çiftler ID3–10 olmak üzere 8 kişidir. Fark ortalaması `1.525`, `t(7)=3.1928859278`, `p=0.0152154827`, GA `[0.3955979276, 2.6544020724]`. Eski 10 farkı kullanmak yeni eksik kuralla tutarsızdır.

## B1–B3

**B1.** Yön ters çevrilirse ortalama `-1.58`, t `-4.0621276834` olur; iki yönlü p değişmez. Güven aralığı `[-2.4598857633, -0.7001142367]` olur.

**B2.** Aynı 10 farkı iki kez mekanik saymak `n=20`, ortalama `1.58`, `s=1.1971896917`, `SH=0.2676997533`, `t(19)=5.9021346892`, `p=0.0000110591`, GA `[1.0196979771, 2.1403020229]` üretir. Bu yeni bağımsız bilgi değildir.

**B3.** Önce aynı kayıt/eksik kümesi ile filtre-ağırlık-bölünme; sonra grup/fark yönü ve analiz birimi; ardından eşli-bağımsız ve Student-Welch modeli; sonra SH/sd, güven düzeyi, tek/iki yön ve çoklu düzeltme; en son yuvarlama ve yazılım sürümü karşılaştırılır.

## H1 — Düzeltilmiş ilkeler

1. 20 satır, 20 bağımsız kişi değildir; 10 tam çift ID üzerinden eşlenir.
2. `0.005965` koşullar arası korelasyon testinin p'sidir; ortalama farkın p'si `0.002833` civarındadır.
3. Levene `0.149` eşit varyansı kanıtlamaz; burada ana yöntem Welch'tir.
4. Ağırlık 2 yeni kişi yaratmaz.
5. Koşul hücreleri değiştiyse fark yeniden hesaplanır ve ortak tam çift sayısı kullanılır.
6. Syntax dosyası yürütme kanıtı değildir. Bu depo Python referansını çalıştırabilir; SPSS sonucu ancak gerçek SPSS oturumu kaydedildiğinde öyle adlandırılır.

## P1 — Örnek teslim omurgası

Uyku örneğinde kaynak ve aktarım notu; 20 ölçüm/10 kişi ayrımı; ID eşleme; geçerli negatif/sıfır ölçümler; ana oturumda filtre/ağırlık/bölünmenin kapalı olduğu; `kosul2-kosul1` yönü; `n=10`, `t(9)=4.062128`, `p=0.002833`, GA `[0.700114,2.459886]` ve `dz=1.284558` aynı modele bağlanır. Küçük n ve tarihsel tasarım/genelleme sınırları raporlanır. SPSS çalıştırılmadıysa açıkça “syntax hazır, SPSS çalıştırılmadı” denir.
