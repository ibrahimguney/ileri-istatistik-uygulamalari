# Bölüm 13 — Çözüm rehberi

Değerler yerel ilk 100 kayıt alıntısının yeniden analizidir; Türkçe uyarlama
sonucu değildir. Tam hassasiyet beklenen.json'dadır. Önce kendi çözümünüzü yazın.

## D1–D3
1. kaynak_satir alıntı sırasını, kaynak_kayit yayımlanmış CSV etiketini izler;
   kişi kimliği çıkarımı yapılmaz. İlk-sıra seçimi rastgele veya temsili değildir.
2. 1–6 sınırlarında 7−x: A1=6 → 1, C5=1 → 6. Eksik yanıt sıfır değildir;
   0 ayrıca geçerli yanıt aralığının dışındadır. Anahtar veriye bakarak seçilmez.
3. A2/sıra66 eksiği A için n=99; C1/sıra63 ve C3/sıra90 C için n=98 bırakır.
   On madde ortak tam kümesi n=97. Silinirse alfa için yeniden tam kayıt seçmek
   madde değişimiyle örneklem değişimini karıştırır; aynı kişiler korunur.

## G1: A'nın iki alfası
k=5, madde varyansları toplamı=9.130076, toplam puan varyansı=18.395176.
Ham alfa=5/4×(1−9.130076/18.395176)=.629588.
Ortalama r=.272051; standart alfa=5r/(1+4r)=.651399.
A1 anahtarlanmadan alfa=.437554; farklı yönler aynı toplamda karıştırılmıştır.
Bu fark daha yüksek alfa aramak için keyfî ters kodlama izni vermez.

## G2: Madde–kalan ve silinirse alfa
A1 madde–kalan r=.198701; düzeltilmemiş madde–toplam r=.513648.
İkinci toplam maddenin kendisini de içerir; aynı tanım değildir.
A4 silinirse, aynı 99 kişide alfa=.675706; beş maddelik .629588'e göre
artış yaklaşık .046118. Bu iki bağımlı tahminin farkı için test yapılmadı;
istatistiksel anlamlılık veya otomatik madde silme kararı değildir.
İçerik, ölçülmek istenen yapı, madde anlamı ve yeni veriyle kanıt gerekir.

## G3: Satır-bootstrap
A için 99 kişinin beş maddelik satırları birlikte iadeli çekilir. Hücreleri
bağımsız çekmek maddeler arası kovaryansı değiştirir. 20000 tekrar, tohum 202613,
%2.5/%97.5 doğrusal nicelikleriyle persentil GA=[.464423,.736637]. BCa değildir.
Bu koşuda geçersiz tekrar yoktur; sıfır toplam varyanslı tekrar oluşursa betik
sessizce elemek yerine durur. Aralık örneklem içi belirsizliği gösterir;
seçim yanlılığı, eksik mekanizması veya kültürel eşdeğerlik sorunlarını düzeltmez.

## B1–B3: C maddeleri
C4/C5 bir kez 7−x; n=98. Ham alfa=.722610, standart alfa=.731783,
ortalama r=.353029. Anahtarlanmamış alfa=−.082651; negatif sonuç gizlenmez.
Bu örnekte puan yönünü kontrol ettirir; başka veride her negatif katsayı
mutlaka ters anahtar hatası demek değildir.

| Madde | Madde–kalan r | Aynı kişilerde silinirse alfa |
|---|---:|---:|
| C1 | .545418 | .653951 |
| C2 | .502439 | .667962 |
| C3 | .512805 | .664335 |
| C4 | .493804 | .670744 |
| C5 | .387612 | .723448 |

C5 silme artışı yaklaşık .000837'dir; küçük sayısal kazanç tek başına içerik
kaybına gerekçe olmaz. C için 20000 tekrar, tohum 202614, persentil
GA=[.579608,.811465]. Aralık alfa eşiklerini otomatik kabul kuralına dönüştürmez.

Örnek kısa rapor: “psych::bfi aktarımının ilk 100 kaydında beş C maddesi
incelendi. C4/C5 bir kez 7−x ile anahtarlandı; tam kayıt kuralıyla n=98 kullanıldı.
Ham alfa=.723, standart alfa=.732; 20000 katılımcı satırı bootstrap ile %95
persentil aralığı [.580,.811] bulundu. Sonuç seçili kayıtlara aittir;
Türkçe uyarlama, yapı geçerliği veya klinik kullanım kanıtı değildir.”

## H1: Sayısal artış yeni kanıt değildir
- .70 eşiği dilsel/kültürel uyarlama kanıtı değildir.
- Negatif ilişki otomatik anahtar seçtirmez; belge, içerik ve veri incelenir.
- Madde–toplam korelasyonu, maddenin kendisini içerdiği için madde–kalanla eşitlenmez.
- A maddelerinin birebir iki kopyası alfa=.835372 verir; bağımsız yeni madde/kanıt yoktur.
- Bootstrap rastgele olmayan ilk-sıra seçimini temsili hâle getirmez.
- Omega için ölçüm modeli ve uygun varsayımlar gerekir; bu pakette omega hesaplanmadı.

A'nın ilk maddesini 10 ile çarpmak ham alfayı .145256'ya değiştirir, korelasyon
matrisi ve standart alfa değişmez. Bu karşı örnek ham/standart ayrımını gösterir.
A+C ortak 97 kayıtta alfa=.727369 hesaplanabilmesi on maddeyi geçerli tek toplam
olarak birleştirme gerekçesi değildir. Madde çoğaltma veya ölçekleme ham arşive uygulanmaz.

## P1: Yalnız öğretim taslakları
Kitaptaki A4 anlam özeti “çocukları sevme” için iki olası ifade taslağı:
1. “Çocukları severim.”
2. “Çocuklara karşı sevgi duyarım.”

Bunlar onaylanmış çeviriler değildir; aynı anlamı, kapsamı veya yanıt sürecini
korudukları varsayılmaz. Tercih gerçek inceleme kanıtıyla gerekçelendirilmelidir.
Olası bilişsel görüşme soruları (görüşme yapılmadı):
- Bu ifadeyi kendi sözcüklerinizle nasıl anlatırsınız?
- Yanıtlarken hangi çocukları veya hangi durumları düşündünüz?
- “Sevmek/sevgi duymak” sizin için hangi duygu veya davranışları kapsıyor?
- 1–6 arasındaki yanıtınızı nasıl seçtiniz; anlaşılmayan bir seçenek oldu mu?

Revizyon örneği ancak “önerildi; kanıt henüz yok” olarak kaydedilebilir.
GOREVLER.md'deki boş tabloda gerçek görüşme alıntısı, uzman adı veya örneklem
uydurmayın. Hedef grupta pilot, yapı ve değişmezlik kanıtları bu paket tarafından
üretilmedi. Rubrik, yapılmış analizle planlanan kanıtı doğru ayırmayı değerlendirir.