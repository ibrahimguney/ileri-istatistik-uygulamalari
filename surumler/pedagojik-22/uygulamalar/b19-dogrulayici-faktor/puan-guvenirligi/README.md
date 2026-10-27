# Puan hedefi ve DFA güvenirlik belirsizliği — Revizyon 22

```bash
python dogrula.py
python analiz.py
```

Mevcut M1/M2 tahminleri, veri ve model seçimleri değişmez. Önceden incelenmiş
yarım B'deki aynı1316 kayıt kullanılır; yeni doğrulama örneklemi değildir.
Kaynak SHA, anahtar ve kayıt kimlikleri kontrol edilir. Ana beklenen bilgi
matrisi(n−1) ve yük standart hataları yeniden oluşturularak eşleştirilir.

## Hangi puan?

Belirli alt ölçeğin hedefi yalnız kendi faktörü olduğunda, bir puanın hedef
faktör payı (w'lambda)²/[ (w'lambda)²+w'Theta*w ] olarak hesaplanır.
Artık matrisi M2'de kovaryansları da içerir. Bu tanım bütün artıkların her
uygulama/zaman evreninde rasgele hata olduğu anlamına gelmez.

Ham, anahtarlanmış1–6 madde toplamı ile model-standartlaştırılmış maddelerin
toplamı ayrı hedeflerdir. Ana modelin veri-standartlaştırılmış birimlerinde
ham toplamın ağırlıkları kaynak madde SD'leri; model-standart toplamın
ağırlıkları1/sqrt(model madde varyansı) olur. İki modelde aynı puan hedefi
açıkça belirtilmelidir. Veri üzerindeki z dönüşümü başlı başına daha doğru
güvenirlik üretmez. Sabitler puanın varyansını etkilemez.

M1'de ham A toplamı için CR=.706272, standart toplam için.716047;
C için.733043/.735613. M2'de sırasıyla A=.679242/.687803,
C=.670648/.676134. Bunlar farklı modeller ve/veya farklı puan hedefleridir;
M1−M2 farkının güven aralığı bu ekte hesaplanmadı.

## Delta aralıkları

Beklenen normal kuramlı tam parametre kovaryansı ve karmaşık adım türeviyle
Var(g)=G*Vtheta*G' kullanılır. Sonuçlar merkezi fark türeviyle de kontrol edilir.
Yalnız parametre varyanslarını almak kovaryans terimlerini kaybettirir;
bu yanlış kısayolun sonuçları ayrı karşı örnek alanında verilir.

M1 standart toplam CR aralıkları A[.692920,.739173], C[.713143,.758083];
M2 A[.661002,.714604], C[.644613,.707654]. AVE aralıkları da JSON/CSV'dedir.
Bunlar dönüştürülmemiş, noktasal yaklaşık%95 Wald aralıklarıdır; sınırlar
keyfi olarak0–1'e kırpılmaz. Sınıra yakın veya zayıf tanımlanan modellerde
Wald yaklaşımı uygun olmayabilir; bootstrap/profil yöntemleri ayrıca gerekir.

Her sabit model içinde yalnız iki karşılaştırmadan oluşan aile için
AVE_A−phi² ve AVE_C−phi² aralıkları Bonferroni ile ayrı etiketlenir:
z_(1−.05/4)=2.241403. M1'de[.176368,.289290] ve[.185919,.300966].
Bu iki tarama eşitsizliğinin pozitif olması tüm ayrışan geçerliği kanıtlamaz;
M1+M2+CR+AVE'nin bütün raporu için ortak%95 kapsama iddiası yoktur.

Aralıklar normal kuramlı modele koşulludur; sağlam/ordinal tahmin, model
seçimi/modifikasyon belirsizliği, yeni örneklem veya kültürel geçerlik yoktur.
Eski ana normal kuramlı tablolar ve kod korunur; yeni ek yalnız Python ile
doğrulandı, R/Amos yeniden çalıştırılmadı. Yedi test ve ana SE eşliği vardır.
