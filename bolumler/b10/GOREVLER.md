# Bölüm 10 — Görevler

Önce VERI.md'yi okuyun. Ana analizde kayıt silmeyin veya doldurmayın. Her sonuçta
birim, yön, n, yöntem ve yorum sınırını belirtin. Yanıtlar COZUMLER.md içindedir.

## D1–D3: Hesaplamadan önce
1. sleep dosyasında 20 satır olmasına rağmen eşli testte neden n=10 kullanılır?
   extra'nın negatif veya sıfır olması ne anlama gelir?
2. Koşul 1−0, koşul 2−1 ve doz 1 OJ−VC sorularında birimleri ve yönleri yazın.
   İki farklı kişi grubunu aynı satır sırasına göre eşlemek doğru mudur?
3. Shapiro ve Levene testlerine bakarak otomatik yöntem seçmek neden yetersizdir?
   Kaynak tasarımında bilinmeyen iki bilgiyi belirtin.

## G1–G4: Rehberli çözüm
1. Koşul 1'in ortalama, örneklem SS, SH, t ve %95 fark aralığını hesaplayın.
   p>.05 sonucu ortalama artışın tam sıfır olduğunu kanıtlar mı?
2. ID üzerinden koşul 2−1 farklarını oluşturun; ortalama, SS, SH, t, df, p ve
   aralığı hesaplayın. Fark tek örneklem testi ile eşli testi karşılaştırın.
3. Doz 1 içinde OJ−VC Welch testi için iki varyans katkısını, Welch df ve aralığı
   hesaplayın. Student sonucu neden aynı t ama farklı p/aralık verebilir?
4. Birim dönüşümüyle farkları dakika cinsinden ifade edin. t, p, ham fark,
   güven aralığı ve dz nasıl değişir? İşareti ters çevirdiğinizde ne olur?

## B1–B3: Bağımsız çözüm
1. Doz 2'de yeni OJ−VC Welch testi yapın. Aralık hangi pozitif ve negatif farklarla
   uyumludur? Bu analiz doz 1 modelinin dış doğrulaması veya eşdeğerlik testi midir?
2. Aynı uyku verilerini yanlış biçimde bağımsız gruplar sayan karşılaştırmanın p'sini
   hesaplayın. İstenen p'yi verdiği için eşli/bağımsız yöntem seçilebilir mi?
3. On ayrı çifti sırayla dışarıda bırakan duyarlılık tablosunu okuyun. ID=9 için
   değişimi raporlayın; bundan neden otomatik silme kuralı türetilemez?

## H1: Hatalı raporu onarın
“20 ölçümümüz olduğundan 20 bağımsız kişi vardır. Levene anlamlı değil, varyanslar
kesin eşittir. Doz 2 anlamsız, uygulamalar eşdeğerdir. Shapiro sonucu önemli değil,
eşli test her zaman geçerlidir. En küçük p veren dozu raporladık. %95 aralık
hastaların %95'inin yararını gösterir.” Altı iddiayı gerekçesiyle düzeltin.

## P1: Denetlenebilir test raporu
Bir sayfalık raporda üç ana soruyu ayrı kurun. Kaynak, ölçüm birimi, eşleştirme,
seçim kuralı, yöntem, ham fark, aralık ve uygun standartlaştırıcıyı yazın. İki
grafiği yorumlayın; farklarda küçük örneklem/normallik sorunu ve tüm duyarlılık
analizlerini görünür tutun. Çoklu doz incelemesinin ayrı plan gerektirdiğini belirtin.
Kişi silme, yeni veri toplama veya R/SPSS çalıştırma yapılmadıysa yapılmış gibi yazmayın.
Teslim: rapor, tamamlanmış notebook, ozet.json ve iki grafik.

| Ölçüt | Puan |
|---|---:|
| Kaynak, birim ve eşleşme | 20 |
| Formüller, yön, n ve hesaplar | 30 |
| Aralık ve etki yorumu | 20 |
| Tanı, duyarlılık ve çokluk sınırları | 20 |
| Yeniden üretim ve dürüst çalıştırma kaydı | 10 |