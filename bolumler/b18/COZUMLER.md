# Bölüm 18 — Çözüm ve kontrol notları

Bu dosyayı görevleri tamamladıktan sonra kullanın.

## G1 — Oturum sözleşmesi

Doğru analiz komutu tek başına yeterli değildir. Aktif filtre, ağırlık veya Split File önceki bir analizden kalmışsa SPSS aynı komutu farklı bir aktif örneklem üzerinde çalıştırabilir. Bu nedenle veri dosyası, analiz birimi ve oturum durumu analizden önce kaydedilmelidir.

## G2–G3 — `sleep` eşli test

Uzun veri 20 satırdır fakat 10 ID vardır. ID üzerinden geniş biçime dönüştürüldüğünde 10 geçerli çift bulunur.

Kontrol değerleri:

- group1: M=0.75, SS=1.7890,
- group2: M=2.33, SS=2.0022,
- eşler arası korelasyon r=0.79517, p=.005965,
- fark yönü: group2−group1,
- ortalama fark=1.58,
- fark SS=1.229995,
- t(9)=4.062128,
- p=.00283289,
- %95 GA [0.700114, 2.459886].

Paired Samples Correlations tablosundaki p=.005965, iki koşul arasındaki **farkın** p değeri değildir. Fark testi için Paired Samples Test tablosu kullanılır.

## G4–G5 — `ToothGrowth`, dose=1

Tam veri N=60'tır. `dose=1` filtresi sonrası N=20 olur.

- OJ: n=10, M=22.70, SS=3.910953,
- VC: n=10, M=16.77, SS=2.515309,
- OJ−VC=5.93.

Levene:

- F=2.271451,
- p=.149126.

Eş varyans satırı:

- t(18)=4.032770,
- p=.0007807.

Welch satırı:

- t=4.032770,
- df=15.357672,
- p=.00103838,
- %95 GA [2.802148, 9.057852].

Bu pakette Welch ana yöntem olarak önceden belirlenmiştir. Levene p>.05 olması Welch sonucunu geçersiz kılmaz ve eş varyans satırını zorunlu hale getirmez.

## G6 — Aynı dosyada farklı n

- `sleep.csv`: 20 satır, 10 kişi, 10 eşli analiz birimi.
- `ToothGrowth.csv`: 60 kayıt.
- `dose=1` filtresi: 20 kayıt.
- `sleep_eksik.csv`: 20 satır fakat 9 geçerli çift.

Bu nedenle dosya satır sayısı ile analizdeki bağımsız/geçerli birim sayısı aynı kavram değildir.

## G7 — Eksik kopya

`sleep_eksik.csv` için:

- geçerli çift n=9,
- ortalama fark=1.60,
- fark SS=1.302881,
- t(8)=3.684142,
- p=.00618215,
- %95 GA [0.598517, 2.601483].

Bir eş eksildiğinde yalnız n değil; standart hata, df, t, p ve güven aralığı da yeniden hesaplanır.

## G8 — Ağırlık

Ağırlıklandırma gözlenen satırların analize katkısını değiştirebilir. Ancak veri setinde gözlenmeyen yeni bağımsız bireyler üretmez. Bir ağırlık değişkenini “örneklem büyütme” amacıyla kullanmak araştırma tasarımındaki gerçek n'yi değiştirmez. Kullanım sonrası `WEIGHT OFF` ile oturum temizlenmelidir.

## G9 — Yöntem haritası için örnek

| Araştırma sorusu | Analiz birimi | Yöntem | Kritik SPSS kontrolü |
|---|---|---|---|
| Aynı kişilerin iki ölçümü farklı mı? | eşleşmiş kişi | eşli t-testi | doğru ID eşleştirmesi |
| İki bağımsız grubun ortalaması farklı mı? | kişi/hayvan | Welch t-testi | doğru grup ve filtre |
| Üç grubun ortalamaları farklı mı? | bağımsız birim | ANOVA/Welch | Split File ve filtre durumu |
| İki değişken ilişkili mi? | bağımsız birim | korelasyon | eksik değer ve aktif filtre |
| Bir sonuç kovaryat kontrolünde farklı mı? | bağımsız birim | ANCOVA | faktör/kovaryat kodlaması |

## G10 — Minimum denetlenebilir teslim

İyi bir teslim yalnız `.spv` çıktı dosyası değildir. En az veri adı, Syntax, aktif oturum durumları, kullanılan n, doğru çıktı tablosu, raporlama paragrafı ve sınırlılık birlikte verilmelidir.
