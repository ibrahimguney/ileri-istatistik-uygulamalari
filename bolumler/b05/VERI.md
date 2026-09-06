# Bölüm 5 — Veri ve planlama girdileri

## Gerçek verinin sınırlı rolü

`veri.csv`, kitabın R datasets/sleep arşivinin aynı baytlarla alınmış kopyasıdır.
20 ölçüm satırı ID ile eşlenen 10 kişiye aittir. extra, kontrole göre uyku artışı
(saat); group koşul1/2; ID kaynak kişi kodu; kaynak_satir aktarım sırasıdır.
İki bağımsız grup değildir. Sıfır ve negatif extra değerleri korunur; eksik yoktur.
[Sözlük CSV](veri_sozlugu.csv) ham alanları açıklar.

Kitaptaki aktarım notuna göre R metninden CSV'ye aktarım 5 Eylül 2026'da yapılmış;
başlıklar, sayı yazımı ve kaynak_satir alanı düzenlenmiştir. Yerel CSV özgün R
metninin bayt kopyası değildir. Bu öğrenci paketi yerel CSV ile bayt eşitliği
bakımından denetlenir; uzak kaynağa otomatik hücre karşılaştırması yapılmaz.

- Sözlük: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/sleep.html
- Kaynak: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/sleep.R
- Kaynak çalışmalar: Cushny ve Peebles (1905), DOI 10.1113/jphysiol.1905.sp001097;
  Student (1908), DOI 10.2307/2331554.
- R dağıtım bildirimi: https://raw.githubusercontent.com/wch/r-source/trunk/COPYING

Normalize LF SHA-256:
`adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e`.
CRLF→LF ve sonda tek satır sonu yalnız denetimde kullanılır; ham dosya değişmez.
Hash, kaynakla bağımsız doğrulama veya temsil kanıtı değildir.

R kaynak dağıtımına ait mevcut [GPL-2.txt](GPL-2.txt) aynen korunmuştur.
UCI/CC BY lisansı bu veriye uygulanmaz. Yazara ait kod/açıklamalar için bu
çalışmada yeni lisans seçilmedi; makalelerin metin veya şekilleri dağıtılmaz.

Tarihsel farkların s_D=1.229995 değeri yayılım örneğidir; yeni pilot değildir.
Gözlenen ortalama fark 1.58 yeni planın etkisi olarak alınmaz. Öngörülen .5 saat
fark öğretim girdisidir; klinik önem standardı veya tedavi önerisi değildir.

## Varsayımsal ana plan

| Girdi | Değer ve anlam |
|---|---|
| Ham fark Δ | 5 varsayımsal eğitim puanı |
| Ortak σ | 10 puan |
| Standart etki d | Δ/σ=.5 |
| Alfa | .05, iki yönlü |
| Hedef güç | .80 |
| Tahsis | Eşit iki bağımsız grup |
| Örneklem | Analiz edilebilir kişi, grup başına |

Bu plan için ham öğrenci yanıtları uydurulmaz. Güç iki yönlü merkezsiz F
kuyruğundan (T² özdeşliği), ek denetimler merkezsiz t ve statsmodels ile hesaplanır.
Farklı d, alfa, hedef güç ve tahsis senaryoları aynı dosyada ayrı etiketlenir.
Eşli d_z farklı standartlaştırıcıya dayanır; bağımsız d ile karıştırılmaz.

%85 tutulma ve gruplar/kişiler arası bağımsız tutulma varsayımı, kayıp mekanizmasının
kanıtı değildir. Fisher-z korelasyon planı normal yaklaşımıdır. Küme örneği yalnız
m=20, ICC=.05 tasarım etkisi hesabıdır; tam çok düzeyli güç analizi değildir.