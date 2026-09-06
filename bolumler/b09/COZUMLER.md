# Bölüm 9 — Simülasyon çözüm rehberi

Bütün sonuçlar bu paket için üretilen simülasyona aittir. Gerçek araştırma
bulgusu veya PROCESS çıktısı değildir. Yuvarlanmamış sonuçlar beklenen.json içindedir.

## Aracılık

a=.633279189, b=.824034337, c'=.135300843;
ab=.521843797, c=.657144640. Aynı doğrusal modellerde c=c'+ab sağlanır.
Üretici ab=.42 olması örneklem çarpımının tam .42 olmasını gerektirmez.

5000/5000 satır-bootstrap, seed=202610, doğrusal kantillerle persentil %95
aralık [.368530044,.698100632]; bootstrap SH=.083106976.
Aralık bu örnekte sıfırı dışlar. Bu, kurgu veride model-temelli yol çarpımının
belirsizliğidir; gerçek nedensel mekanizma kanıtı değildir. BCa veya bootstrap
p değeri hesaplanmadı. Tek simülasyon aralığı kapsama oranı çalışması değildir.
X/M/Y aynı indislerle taşınır; ayrı sütun örneklemesi ortak ilişkiyi bozar.

## Düzenleyicilik

Ayrı Y_duzenleyicilik yanıtında etkileşim=.559008138;
klasik SH=.072190142, t(156)=7.743552, %95 GA=[.416411852,.701604424].
Ham ve merkezli model aynı tahminleri verir; sabit/alt terim yorumları değişir.

| W düzeyi | Ham W | Eğim | Noktasal %95 GA |
|---|---:|---:|---|
| Ortalama−1SS | −.926774 | −.181415 | [−.402023,.039193] |
| Ortalama | .110603 | .398487 | [.244682,.552293] |
| Ortalama+1SS | 1.147980 | .978389 | [.772457,1.184322] |

Varyans = Var(b_X) + W_c² Var(b_XW) + 2 W_c Cov(b_X,b_XW).
Kovaryansı atmak genellikle yanlış SH üretir; W_c=0 özel durumdur.
Sabit W'de iki X değeri arasındaki tahmin farkı eğim×X farkına eşittir.
Bunlar üç ayrı noktasal aralıktır; eşzamanlı bant veya Johnson–Neyman aralığı değildir.

Düşük W'deki tekil p=.1063, yüksek W'deki p çok küçük olsa bile etkileşim
kararı bu iki p'yi karşılaştırarak verilmez; etkileşim katsayısının kendisi
sınanır. Merkezleme etkileşimi kaldırmaz. Aynı dosyada M/W bulunması koşullu
dolaylı etki analizi yapıldığı anlamına gelmez. Doğrudan yolun tekil
anlamlılığına göre kesin “tam aracılık” veya nedensellik iddiası kurulmaz.