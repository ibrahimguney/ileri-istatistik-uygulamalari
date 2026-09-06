# Bölüm 14 — Gerekçeli çözüm rehberi

Bu sayılar kitaptaki yerel 97 kayıt için hesaplanır; geçerli Türkçe ölçek veya bağımsız araştırma tekrarı değildir. Son basamaklar için beklenen.json kullanın.

## D1–D3

1. Üç ayrı satırda birer eksik bulunduğundan on maddenin ortak tam kümesi 97'dir. A=99/C=98 farklı kişi kümeleridir; bunları birleştirmek tek ortak korelasyon matrisi vermez. İkili silme çiftlerin paydasını değiştirir; burada yapılmamıştır.
2. Bir kişi/madde oranı evrensel yeterlik belgesi değildir. Ortak varyanslar, faktör başına göstergeler, örneklem seçimi ve çözüm belirsizliği ayrıca değerlendirilir. Bu sıralı küçük alıntı için genelleme onayı verilmez.
3. Ters puanlama standartlaştırılmış değişkenin işaretini değiştirir. Köşegen işaret matrisi D için R_yeni=D R D; özdeğerler ve determinant korunur, korelasyon/kısmi korelasyon kareleri aynı kalır. KMO/Bartlett değişmemesi anahtar doğruluğunu kanıtlamaz; yük yönleri ve puanın anlamı önemlidir.

## G1–G4

1. KMO=6.121619106/(6.121619106+2.308987666)=.726118448. logdet=-2.274907; Bartlett=-(96-25/6)logdet=208.912293, sd=45, yaklaşık p=5.8081e-23. Bu iki sayı ne faktör sayısını ne Türkçe geçerliği ne yeterli örneklem büyüklüğünü kanıtlar.
2. PCA'da ilk üç özdeğer 3.062119, 1.657400, 1.156765 olduğundan >1 kuralı üç önerir. Üçüncü PCA referansı 1.320067: gözlenen daha küçük. SMC üçüncü değer .356621, referans .438259: yine küçük. İlk sıradan ardışık aşma iki sürümde de iki boyut verir. SMC başlangıç azaltılmış spektrumu nihai PAF spektrumu değildir. %95 çizgisi permütasyon referansıdır; yük/özdeğer güven aralığı değildir.
3. A2 örüntüsü (.478525778,.307147347), Phi_AC=.216667619. C yapı katsayısı .307147347+.478525778×.216667619=.410828388. h²=.478525778²+.307147347²+2×.478525778×.307147347×.216667619=.387017126; özgüllük=.612982874. Eğik çözümde yalnız kare toplamı kullanmak çapraz terimi atar.
4. İki PAF faktörünün h² toplamı/10=.366554302; ilk iki PCA özdeğeri toplamı/10=.471951973. Aynı kavram değildir. On madde 10×9/2=45 benzersiz köşegen dışı çift verir; RMSR=.056761183. Köşegen veya simetrik kopya ikinci kez sayılmaz.

## B1–B3

1. A5 örüntüsü (.893597961,-.069619807). Phi ile h²=.776405531, özgüllük=.223594469. C yapı katsayısı .123993936'dır; küçük negatif örüntü katsayısı anahtara aykırı yeniden tersleme gerekçesi değildir.
2. Bir faktör: RMSR=.121292294, max|artık|=.371745882, .05'i aşan 29 çift. Üç faktör: .039941408, .111193684, 8 çift. İki faktörde 12 çift ve max=.198782747 vardır. Esneklik arttığında daha küçük artık, içerik ve bağımsız kararlılık kanıtı olmadan üçüncü faktörü onaylamaz. Bu adaylarda Heywood görülmemesi doğru model kanıtı değildir.
3. Aynı 97 kişi ve sekiz maddede RMSR=.049024939, ortak varyans oranı=.432949659; 28 çiftin 7'si .05'i aşar. Değişen madde içeriği ve payda nedeniyle ana modele karşı doğrudan üstünlük testi değildir. Ana on madde korunur.

## H1

- KMO/Bartlett ön bilgidir; dilsel, yapısal veya kültürel doğrulama değildir.
- >1 tek kural değildir; belirtilen paralel analiz iki boyut önerir, bu da kesin doğru faktör sayısı kanıtı değildir.
- Varimax aynı çıkarılmış ortak matrisi yeniden ifade eder; bu rotasyon tek başına yeniden üretilen korelasyonu/artığı iyileştirmez.
- A2'nin C örüntüsü .307147, yapısı .410828'dir; ilişkili faktörlerde farklı niceliklerdir.
- A1/A4 düşük ortak varyans nedeniyle incelemeye ayrılır; otomatik silinmez, kültürel neden uydurulmaz.
- Aynı veride bulunan modelin aynı veride DFA'sı bağımsız doğrulama değildir; bu pakette DFA yapılmadı.

## P1 örnek rapor ve sınır

“İlk 100 yerel kayıttan on A/C maddesinde ortak 97 tam kayıt seçildi. A1/C4/C5 anahtarla bir kez terslendi. Pearson matrisi için KMO=.726, yaklaşık Bartlett χ²(45)=208.91 bulundu. 2000 sütun permütasyonu ve %95 referansla PCA/SMC paralel analizleri iki boyut önerdi. SMC başlangıçlı iki faktörlü PAF, normalizasyonsuz quartimin ile döndürüldü; Phi_AC=.217, köşegen dışı RMSR=.0568 idi. A1/A4 ve A2 içerik incelemesine ayrıldı; ana analizde madde silinmedi. Sıralı küçük alt küme, Türkçe uyarlama veya bağımsız doğrulama kanıtı değildir.”

Gelecek DFA modelinin yük kısıtları ve veri toplama planı önceden gerekçelendirilmelidir. GOREVLER.md tablosundaki gelecek çalışma satırlarını plan olarak doldurun; gerçekte yapılmamış örneklem, görüşme veya DFA uyum indekslerini yazmayın.