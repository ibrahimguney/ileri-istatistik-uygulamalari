# Bölüm 12 — Çözüm rehberi

Değerler yerel kayıtların yeniden analizidir. Tam hassasiyet beklenen.json'dadır;
bu tablo özgün araştırma raporu değildir. Önce görevleri kendiniz çözün.

## D1–D3
1. Diş verisindeki OJ/VC farklı hayvan kayıtlarıdır; kafes/ortak çevre bilgisi
   ayrıca gerekir. Uyku koşulları aynı ID'nin iki ölçümü olduğundan eşlidir.
2. RoundingTimes'ın 22 kod satırı blok, üç sütunu koşuldur. 66 değer 66 bağımsız
   kişi değildir. Bir hücre iki koşunun ortalaması; 132 gözleme çoğaltılmaz.
   Yerel kaynak notunda açıklama 18 oyuncu, kod 22 satırdır; özgün deney sayısı doğrulanmadı.
3. Hedef ortalama mı, simetrik fark konumu mu? Gözlemler eşli mi? Farklar
   simetrik mi? Normallik testinin sonucu bu soruları yanıtlamaz.

## G1: U ve üstünlük
Doz 1'de OJ sıra toplamı=143.5, VC=66.5; U_OJ=143.5−55=88.5,
U_VC=100−88.5=11.5. 100 çapraz çiftte OJ'nin 88 kazanımı ve 1 bağı vardır:
A=(88+.5×1)/100=.885; sıra-biserial=2A−1=.77.
184756 etiket atamasının tamamı sayıldığında iki yönlü p=.002229968;
süreklilik düzeltmeli normal yaklaşım p=.004030367. İki yönlü kesin p,
küçük kuyruğun iki katı (en çok 1) olarak tanımlanmıştır. Yön ve yöntem yazılır.
A, bu çapraz çiftlerde üstünlük ölçüsüdür; tedavi başarısı olasılığı değildir.
Konum-kayması koşulları olmadan sonucu yalnız medyan farkı diye okumayın.

## G2: Sıfır ve bağlı farklar
Koşul 2−1 farkları: 1.2,2.4,1.3,1.3,0,1,1.8,.8,4.6,1.4 saat.
Bir sıfır wilcox kuralında sıralamadan çıkar; ham veride ve 10 çiftlik arşivde
kalır. İki 1.3 ortalama sıra alır. W+=45, W−=0, T=0.
Dokuz sıfır olmayan fark için 2⁹=512 işaret örüntüsü; iki yönlü kesin
p=2/512=.00390625. Yaklaşık süreklilik düzeltmeli p=.009090698.
Sıfır olmayan sıraların paydasında sıra-biserial=1; tüm kişilerin iyileştiği
anlamına gelmez: bir sıfır vardır, ayrıca fark ilaç 2−1 karşılaştırmasıdır.
Tam sayımın yorumu simetrik fark yokluk modeline bağlıdır.

## G3: Kruskal–Wallis ve Dunn–Holm
OJ doz sırasıyla sıra toplamları 62.5,174,228.5; ortalama sıralar 6.25,17.4,22.85.
Ham H=18.476774; bağ düzeltmesi C=.998442714; H/C=18.505593,
df=2, ki-kare yaklaşımı p=.0000958433.
Dunn bütün 30 OJ kaydının ortak sıralarını kullanır; her çiftte yeniden sıra üretmez.

| Doz çifti (yüksek−düşük) | Ham p | Holm p |
|---|---:|---:|
| 1−0.5 | .004592467 | .009184934 |
| 2−0.5 | .000024464 | .000073391 |
| 2−1 | .165936144 | .165936144 |

Holm sıralı p'leri 3,2,1 çarpanlarıyla ve kümülatif maksimumla düzeltir;
her p'yi üçle çarpmak Bonferroni'dir. Son çift reddedilemez; eşdeğerlik kanıtı değildir.

## G4: Friedman ve Monte Carlo
Blok içi sıra toplamları Round/Narrow/Wide için 53,47,32.
Bağ düzeltmesi=.954545455; Q=11.142857, df=2,
ki-kare yaklaşımı p=.003805041. Kendall W=Q/[22×(3−1)]=.253247.
Tohum 202612 ile 99999 rastgele blok içi atamada 311 aşım;
p_MC=(311+1)/(99999+1)=.003120, MC SH≈.00017636.
Bu SH Monte Carlo hesap belirsizliğini anlatır; etki büyüklüğü güven aralığı değildir.
Tüm 6²² blok içi atama düzenleri sayılmadığı için bu tam sayım değildir.
Küçük sıra daha kısa süreyle ilişkilidir; blok modeli nedensellik kanıtı değildir.

## B1: VC
Sıra toplamları 55,158,252; C=.999332592; H=25.072217,
df=2, p=.00000359449. Dunn–Holm p'leri doz sırasıyla
1−0.5 için .017737314, 2−0.5 için .00000167173, 2−1 için .017737314.
Üçü de .05 altında; bu aile OJ ailesinden ayrıdır. İki grubun p'lerinin
farklılığı doğrudan uygulama×doz etkileşim testi değildir.

## B2: Kategorik tablo
Satırlar OJ/VC; sütunlar len<20 / len≥20. Gözlenen tablo [[11,19],[20,10]],
beklenen tablo [[15.5,14.5],[15.5,14.5]]. Pearson düzeltmesiz
chi²=5.406007, df=1, p=.020067572; V=√(chi²/60)=.300167.
İki yönlü Fisher p=.037887213. Sayısal fark yöntemlerin aynı olmadığına işaret eder;
istenen p'yi veren yöntem seçilmez. Eşik öğretim amaçlıdır; biyolojik/klinik
başarı eşiği değildir. Dozlar birleştirilmiştir; bu tablo doza göre düzeltilmiş
etki veya ortak faktöriyel model değildir.

## B3: Friedman sonrası üç çift
İkinci koşul eksi ilk koşul yönüyle:
Narrow−Round medyan farkı=−.05, dört sıfır; Holm p=.448962219.
Wide−Round medyan farkı=−.125, sıfır yok; Holm p=.037426279.
Wide−Narrow medyan farkı=−.10, sıfır yok; Holm p=.005119631.
Medyan farklar betimseldir. İkili p'ler simetrik fark modeli, wilcox sıfır
kuralı ve süreklilik düzeltmeli normal yaklaşım kullanır; Friedman'ın Monte
Carlo p'si gibi sunulmaz.

Örnek kısa rapor: “R belgesinin 22 satırlık RoundingTimes kod matrisi yeniden
analiz edildi; açıklamadaki 18 oyuncu ile uyuşmazlık korunarak bildirildi.
Friedman Q(2)=11.143, Kendall W=.253, 99999 blok içi permütasyonla p_MC=.00312
bulundu. Üç eşli Wilcoxon normal yaklaşımından oluşan Holm ailesinde Wide−Round
ve Wide−Narrow reddedildi, Narrow−Round reddedilemedi. Bulgular kaynak ve
blok/fark varsayımlarıyla sınırlıdır.”

## H1 ve P1
Parametrik olmayan testler varsayımsız değildir; U yalnız medyan testi değildir.
Bağlar varken yazılımın exact seçeneğinin ne saydığı kontrol edilir; otomatik
etikete güvenilmez. Sıra-biserialin paydası, sıfırlar ve fark yönü yazılır.
Friedman'ın birimi bloktur; genel H ikili çokluğu otomatik düzeltmez.
P1 raporu ham veri bütünlüğü, bağımlılık, p yöntemi, ayrı aileler ve sınırlılıkları
göstermelidir. Etki büyüklüğü aralığı bu pakette üretilmedi; önceki bölümlerin
ortalama farkı aralıkları sıra ölçülerine taşınmaz. Rubrik GOREVLER.md'dedir.