# Bölüm 4 — Eşdeğerlik ve çoklu karşılaştırma

Ana sleep analizi ve ham veri değiştirilmez. Yeni modül; simetrik TOST ve
planlı bir kurgusal p ailesinde Holm/Bonferroni hesaplarını öğretir.

Kitap kökünden; öğrenci deposunda `surumler/22-bolum/` klasöründen:

```sh
python uygulamalar/b04-hipotez-testi/esdegerlik-cokluk/dogrula.py
python uygulamalar/b04-hipotez-testi/esdegerlik-cokluk/analiz.py
```

Ortak NumPy/pandas/SciPy/statsmodels bağımlılıkları kullanılır. Üst klasördeki
`pair_data` işleviyle 10 kişi eşlenir; ana betiğin `main` yordamı çağrılmaz.
Yeni ek yalnız Python'da doğrulandı; R/SPSS eşdeğeri hazırlanmadı.

## TOST

Hipotez H0: mu<=-delta veya mu>=delta; H1: -delta<mu<delta.
İki tek yönlü bileşen de alfa .05 düzeyinde reddedilmelidir; TOST p'si
iki p'nin büyüğüdür. Aynı model altında %90 iki yönlü aralığın tamamının
açık (-delta,delta) aralığında bulunmasına eşdeğerdir. İki bileşene otomatik
Bonferroni uygulanmaz; kesişim–birleşim mantığı vardır.

Sleep %90 aralığı [.866995,2.293005] saat. Delta=1 için TOST p=.914944,
delta=3 için p=.002656. **Bu sınırlar yalnız geriye dönük öğretim tercihleridir;
klinik kabul edilebilirlik veya önkayıt iddiası yoktur.** Daha kolay sonuç veren
sınır seçilerek gerçek çalışma iddiası kurulamaz. Ana sıfıra karşı p=.002833'tür.

Ayrı kurgusal özetlerde (yeni ham gözlem üretilmez) ortalama0, s10, delta5 için
n25/n4: %90 aralıklar ±3.421764 / ±11.766817, TOST p .009827 / .195501.
İki yönlü p her ikisinde1; yalnız ilki belirtilen sınırda eşdeğerliği destekler.
Sabit farkın tam sıfır olduğu kanıtlanmaz.

## Çokluk

Kurgusal dört karşılaştırmanın ham p'leri [.20,.004,.024,.012]. Holm p'leri
[.20,.016,.048,.036]; Bonferroni p'leri [.80,.016,.096,.048]. Holm .05'te üç,
Bonferroni iki red verir. Bu aile sleep veya kitabın diğer öğretim örneklerinden
oluşturulmuş değildir. Aile/strateji sonuçlar görülmeden gerekçelendirilmelidir.
Geçerli tekil p'ler altında Holm bağımsızlık gerektirmeden güçlü FWER kontrolü
sağlar; FDR kontrolüyle aynı hedef değildir. Düzeltilmiş güven aralıkları yoktur.

TOST, gerçek eşleşmiş farklarda statsmodels `ttost_paired` ile; Holm ise
`multipletests(method='holm')` ile karşılaştırılır. Beş test; aralık terslemesi,
sınır sıfır hipotezi, birim/yön dönüşümü, elle Holm hesabı/sıralama ve geçersiz
girdi reddini denetler. Kaynak SHA-256 ve kaynak dosyanın değişmediği kontrol edilir.

Çıktılar `sonuclar/esdegerlik.csv`, `kurgu-holm-ailesi.csv`, `ozet.json`.
Uyku verisinin aktarım/GPL notları üst README'de korunur. Normal fark ve bağımsız
kişi varsayımları bu uygulamayla kanıtlanmaz; klinik veya nedensel sonuç üretilmez.

Kaynaklar: Lakens (2017), https://doi.org/10.1177/1948550617697177 ;
Holm (1979), A simple sequentially rejective multiple test procedure,
Scandinavian Journal of Statistics, 6(2), 65–70.
