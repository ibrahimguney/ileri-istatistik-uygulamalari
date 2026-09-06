# Bölüm 4 — Öğrenci görevleri

## D — Testten önce

1. 20 satır neden 20 bağımsız kişi değildir? Eşleştirme anahtarı nedir?
2. Ana fark yönünü, sıfır hipotezini, alternatifi ve alfa değerini hesaplamadan yazın.
3. Negatif uyku artışı neden eksik veya hatalı kayıt sayılmaz?

## G — Rehberli hesap

1. ID ile on çifti oluşturun. Fark ortalaması, örneklem s ve standart hatayı bulun.
2. t istatistiği, serbestlik derecesi, iki yönlü p ve %95 güven aralığını hesaplayın.
   Sonucu `ttest_rel` ve farkların `ttest_1samp` hesabıyla karşılaştırın.
3. Farkı ters çevirin: t, p ve aralık nasıl değişir? Sağ ve sol kuyrukların
   farklı alternatiflere yanıt verdiğini açıklayın; en küçüğünü seçmeyin.
4. d_z değerini fark standart sapmasıyla hesaplayın; t=d_z×sqrt(n) eşitliğini denetleyin.

## B — Bağımsız uygulama

1. Satırları karıştırın; ID'yle eşleştirme sonucu değişiyor mu? Ayrı kopyalarda
   bir koşulu silin ve kişi–koşul kaydını çoğaltın; `pair_data` durmalı mı?
2. Kurgu dolum özeti n=25, ortalama=496, s=10, referans=500 için iki yönlü test
   ve aralık bulun. Sonuca bakıp sola tek yönlü teste geçmek neden uygun değildir?
3. Kurgusal `[[20,30],[30,20]]` tablosunda beklenen frekansları, düzeltmesiz
   Pearson ki-kare ve Cramer V'yi hesaplayın. Yates/Fisher sonucu diye yazmayın.
4. `analysis.simulate()` sonuçlarında d=0 için Tip I hata, d=.5 için güç,
   gerçek ortalama kapsaması ve veriden yön seçen yanlış kuralı karşılaştırın.
   Monte Carlo standart hatasını ve simülasyon varsayımlarını belirtin.

## H — Hatalı rapor

“p=.0028 olduğundan H0'ın doğru olma olasılığı %0.28'dir. 20 satırdan n=20
aldık. Tek yönlü p daha küçük olduğu için onu seçtik. Simülasyon gücü uyku
verisinin gerçek gücüdür. p>.05, iki koşulun eşdeğerliğini kanıtlar.”
Her iddiayı hesap birimi, önceden belirlenmiş yöntem ve yorum sınırıyla düzeltin.

## Teslim

Kısa rapor, notebook/kod ve fark grafiği teslim edin. Eşleştirme anahtarı,
fark yönü, n, ortalama fark, s, SH, t(sd), p, aralık, d_z ve tasarım sınırları
bulunsun. Gerçek veri, kurgu ve simülasyonu ayrı başlıklarda tutun.
Rubrik: tasarım/kaynak 20, hesap 30, yön/aralık 20, simülasyon/yorum 20,
yeniden üretim 10. Normallik testi, bootstrap, permütasyon veya d_z güven aralığı
bu pakette yapılmış gibi sunulmaz.