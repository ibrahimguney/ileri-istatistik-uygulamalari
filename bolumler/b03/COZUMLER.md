# Bölüm 3 — Çözüm ve yorum rehberi

Önce GOREVLER.md sorularını çözün. Sayısal denetimler beklenen.json içindedir.

## G1 — Paydalar

100 kayıt × 10 madde = 1000 hücre. A2 kaynak satırı 66, C1 satırı 63,
C3 satırı 90'da boş: 3/1000 = %0.3 hücre; 3/100 = %3 eksikli kayıt.
On maddede ortak tam küme 97'dir. Düşük eksik oranı MCAR kanıtı değildir.

## G2 — Puanlar

A1/C4/C5 için 7−x; boşlar boş kalır. Terslenmiş dosyayı yeniden terslemeyin.

| Puan | Geçerli n | Ortalama |
|---|---:|---:|
| A 5/5 | 99 | 4.563636 |
| A 4/5 | 100 | 4.565500 |
| C 5/5 | 98 | 4.187755 |
| C 4/5 | 100 | 4.191500 |

Satır 63: A_n=5, A_ort4=5.6; C_n=4, C_ort4=5.25.
Satır 66: A_n=4, A_ort4=4.75; C_n=5, C_ort4=5.0.
Satır 90: A_n=5, A_ort4=4.4; C_n=4, C_ort4=3.5.
5/5 toplam, 5 × 5/5 ortalamadır. Dört yanıtla ortalama, beş yanıt toplamı
olarak raporlanmaz. Puan üretilemeyen hücre boş kalır; satır silinmez.

## G3–G4 — Dönüşümler

Uzun tabloda 1000 satır, 997 gözlenen yanıt vardır. Kişi–madde anahtarı
benzersizdir; yeniden genişletilmiş değerler eksikler dahil aslıyla eşleşir.
A_ort5'in 99 kullanılabilir kaydı için z ortalaması yaklaşık 0, örneklem s=1.
Bu cebirsel standartlaştırma normallik veya geçerlik sağlamaz.

## B — Hatalı örnekler ve karşı örnek

99, 2.5, metin ve boş/yinelenen anahtar reddedilmelidir. Kurgu kontrolleri gerçek
kaynağın bozuk olduğunu göstermez. Tam boş satırın varsayılan toplamı 0 olabilir;
bu gerçek sıfır puan değildir. Tek yanıtın ortalaması 6 olsa bile 4/5 puanı boştur.
`[6,4,5,3,NA]` için 4/5 ortalama 4.5, 5/5 puan boştur.

C1 gözlenen n=99, ortalama 4.454545; örneklem varyansı 1.515770.
Tek eksiğe bu ortalamayı koyunca varyans 1.500459 olur (öncekinin 98/99'u).
Ortalama değişmese de yayılım azalır; bu işlem ana veriye uygulanmaz.

İki satırlık sol tablo ile sağdaki `[1,1,2]` anahtarları kontrolsüz birleşirse
üç satır oluşur. Bire bir birleşim bunu reddeder. Yinelenen kişi–madde kaydını
pivot_table ile sessizce ortalamak veri sorununun çözümü değildir.

## H — Raporun onarımı

Eksik oranı mekanizmayı belirlemez; boş yanıt sıfır değildir. Ortalama ile toplam,
ana puan ile duyarlılık ayrılır. z puanı dağılım şeklini normalleştirmez.
7−(7−x)=x: yeniden tersleme yapılan işi geri alır. Analiz daima ham CSV'den başlar.