# Bölüm 14 — Öğrenci görevleri

Önce VERI.md'yi okuyun. Çözüm için calisma.ipynb kullanın; gerekçeleri ayrı yazın. Beklenen sonuçlar cevap kontrolüdür, yeni araştırma verisi değildir.

## D1–D3: Analiz öncesi

1. Neden n=97? Bölüm 13'teki A=99 ve C=98 korelasyonlarını tek matriste birleştirmek veya ikili silme kullanmak hangi seçimi değiştirir?
2. “Madde başına yaklaşık on kişi, kesin yeterli örneklem” iddiasını eleştirin; içerik, temsil ve çözüm kararlılığı bakımından gereken kanıtı yazın.
3. Anahtarlanmamış veride KMO/Bartlett ve özdeğerler değişmeyebilir mi? Bunun ters kodlamayı gereksiz kılmadığını açıklayın.

## G1–G4: Rehberli çözüm

1. Korelasyon ve kısmi korelasyon karelerinden KMO'yu; n=97, p=10 ve logdet ile Bartlett'i hesaplayın. Bu testler neyi kanıtlamaz?
2. Özdeğer >1 kuralını PCA ve SMC paralel analiziyle karşılaştırın; üçüncü gözlenen/referans çiftiyle kararı açıklayın. Referans çizgisi güven aralığı mı?
3. A2 için C yapı katsayısını, ortak varyansı ve özgüllüğü L/Phi üzerinden hesaplayın. Phi'yi birim matris sayınca hangi terim kaybolur?
4. İki faktörün ortak varyans oranıyla iki PCA bileşeninin oranını karşılaştırın. Köşegen dışı RMSR'nin paydasını gerekçelendirin.

## B1–B3: Bağımsız inceleme

1. A5'in ortak varyansını ve özgüllüğünü hesaplayın. Küçük negatif C örüntü katsayısı anahtarı değiştirmenizi gerektirir mi?
2. Bir/üç faktör adaylarının RMSR, en büyük artık ve .05'i aşan çift sayılarını yeniden üretin. Üç faktörde daha küçük artık niçin otomatik karar değildir?
3. Yalnız duyarlılık kopyasında A1/A4'ü çıkarın; aynı 97 kişiyle iki faktör uydurun. Sekiz maddelik oran ve 28 çiftlik RMSR'yi on maddelik sonuçla neden doğrudan üstünlük diye yorumlayamazsınız?

## H1: Hatalı raporu onarma

“KMO .73 ve Bartlett anlamlı: Türkçe ölçek doğrulandı. Üç özdeğer 1'i geçti, üç faktör kesin. Varimax artık uyumunu iyileştirdi. A2'nin C yapı katsayısı .41 onun örüntü çapraz yüküdür. A1/A4 otomatik silindi. Aynı veriyle DFA bağımsız doğrulamadır.”

Altı iddiayı ayrı ayrı düzeltin. Yapılmamış yük kararlılığı, görüşme veya yeni veri toplama işlemi uydurmayın.

## P1: Keşiften doğrulamaya kanıt dosyası

Kaynak/seçim/anahtar, eksikler, korelasyon türü, aday sayısı, PAF/rotasyon ayarları, tam örüntü/yapı/Phi ve artık tabloları ile bir sayfalık yorum hazırlayın. A1/A4 içeriğini ve A2 çapraz örüntüsünü yeni veride nasıl inceleyeceğinizi planlayın. Sırf ikiye bölmek bağımsız hedef anakütle doğrulaması sağlamaz; bu küçük sıralı alıntıyı kesin eğitim/doğrulama çalışması diye sunmayın.

| Kanıt / karar | Mevcut işlem | Gelecek çalışma planı | Dayanak / sınırlılık |
|---|---|---|---|
| Yerel kaynak ve anahtar | Arşiv ve hash kontrolü | Uzak kaynağı ayrıca karşılaştırma | İlk 100 sıralı seçim |
| Ortak 97 kayıt ve Pearson | Yapıldı | Eksiklik/ordinal yöntem duyarlılığı | Polikorik analiz yapılmadı |
| AFA ve artıklar | Bu pakette hesaplanır | Yeni örneklemde kararlılık incelemesi | Yük güven aralığı yok |
| A1/A4 ve A2 içerik incelemesi | Sayısal işaretleme; madde silinmedi | … | Görüşme/uzman onayı yok |
| Önceden tanımlanmış DFA | Yapılmadı | … | Aynı veride yeniden uyum bağımsız kanıt değil |
| Hedef gruba genelleme | Yapılmadı | … | Türkçe uyarlama onayı yok |

Teslim: kaynak notu, çalışan kod, iki grafik, bütün matrisler, doldurulmuş karar tablosu ve ölçülü rapor. Öğrenci paketi rubriği: kaynak/puanlama 20; KMO/paralel analiz 20; matris ve artık hesapları 25; içerik/alternatifler 20; yeniden üretim ve doğrulama sınırı 15 puan.