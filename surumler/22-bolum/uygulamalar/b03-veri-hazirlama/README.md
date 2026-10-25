# Bölüm 3 — Veri hazırlama ve analize hazırlık

## Kaynak ve sınırlar
Bölüm 17'nin `../b17-guvenirlik/kaynak/bfi-ilk100-AC.csv` arşivi kullanılır.
psych/bfi, SAPA/IPIP verisinden A1–A5 ve C1–C5 alanlarının ilk 100 kaydıdır;
2800 kişilik kaynak dosyanın tamamı veya rastgele/temsili örneklem değildir.
Türkçe uyarlama ya da klinik değerlendirme yapılmaz. Kaynak sözlüğü ve anahtar:
https://www.personality-project.org/r/html/bfi.html
Kaynak aktarımı: https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/psych/bfi.csv
Bölüm 17'deki aktarım/lisans notları korunur. IPIP maddelerinin kullanım açıklaması
her veri aktarımına veya başka testlere otomatik lisans olarak genişletilmez.
Veri, `psych::bfi` verisinin ilk 100 kaydıyla birebir aynıdır.
Normalize LF SHA-256: `8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557`.
Bu özet, dosyanın sonradan değişmediğini denetler.

`kaynak_satir` 1–100 aktarım sırası; `kaynak_kayit` kaynak satır etiketidir.
İkisi de kişiyi gerçek yaşamda tanımlayan kimlik olarak yorumlanmaz.
Maddeler ordinal, 1–6 tamsayı; boş hücre eksik, 0/99 geçerli yanıt değildir.
A1/C4/C5 için yeni `_t` sütunları 7−x ile üretilir. Kaynak sütunlar değiştirilmez.
`veri_sozlugu.csv` madde alanlarını; bu belge anahtar ve türetilen alanları açıklar.

## Çalıştırma
Kitap kökünden `python uygulamalar/b03-veri-hazirlama/analiz.py`.
numpy/pandas/matplotlib kullanılır; ağ bağlantısı gerekmez.
`analiz.R` temel R ile bağımsız puan/reshape hesabıdır ve Python ile aynı
sonuçları verir. `analiz.sps` yalnız doğrulanmış arşiv için kurulmuştur:
bilinmeyen yeni dosyadaki geçersiz kodları otomatik onaran doğrulayıcı değildir.
SPSS okuma uyarıları, frekanslar ve anahtar benzersizliği ayrıca incelenmelidir.
VARSTOCASES /NULL=KEEP boş yanıt satırlarını da saklar; madde indeksi 1–10'dur.
R/SPSS dosyalarının bulunması yazılımlar arası doğrulama iddiası değildir.

## Dosyalar
- `puanlar.csv`: 100 kaynak kaydı, ham maddeler, üç ters sütun, A/C geçerli madde
  sayıları, 5/5 ana ve 4/5 duyarlılık ortalamaları, yalnız 5/5 toplamlar.
- `uzun.csv`: 1000 kişi-madde satırı, 997 gözlenen ve 3 boş yanıt.
- `sonuclar/eksik_ozeti.csv`, `desenler.csv`: hücre ve kayıt eksikliği ayrı.
- `puan_ozeti.csv`, `cift_paydalari.csv`, `karar_gunlugu.csv`,
  `standartlastirma.csv`, `ozet.json` sonuclar klasöründedir.
- `../../assets_figures/b03-eksik-puan-paydalari.pdf`: gerçek eksik deseni ve puan paydaları.

## Beklenen sonuçlar ve yorum
Eksikler A2/satır66, C1/satır63, C3/satır90. 3/1000=%0.3 hücre eksik;
3/100=%3 kayıtta en az bir eksik var. Ortak on maddelik tam kayıt n=97.
A: 5/5 n=99, ortalama4.563636; 4/5 n=100, ortalama4.565500.
C: 5/5 n=98, ortalama4.187755; 4/5 n=100, ortalama4.191500.
Ana dosyada kayıt silinmez; puan üretilemeyen hücre boş bırakılır.
4/5 eşik onaylanmış test kılavuzu kuralı değil, öğretim duyarlılığıdır.
Dört maddelik ortalama tam beş maddelik toplam değildir; puanlama eksik veri
mekanizmasını çözmez. Korelasyon/modelde ortak kullanılabilir n ayrıca belirlenir.

C1'in tek eksik hücresini gözlenen ortalama4.454545 ile dolduran geçici karşı
örnekte varyans1.515770'ten1.500459'a düşer; oran98/99'dur. Ana dosyaya yazılmaz.
Ana gerçek-veri hazırlama betiğinde çoklu atama, FIML, MCAR testi, alfa,
AFA/DFA veya puan güven aralığı uygulanmaz. Ayrı sürekli simülasyon eki
için aşağıdaki yeni uygulama başlığına bakınız.
A_ort5, 99 kaydın örneklem standart sapmasıyla z'ye çevrilir; n=99, ortalama0,
s=1 kontrolleri normallik veya geçerlik göstermez.

## İç denetimler ve kurgu örnekleri
Şema, sayısal tür, tamsayı/aralık, boş/tekrarlı anahtar, 3 gerçek eksik, ham hash,
toplam=5×ortalama, geniş–uzun–geniş eşitliği ve z özdeşliği denetlenir.
Gerçek yanıtları bozmayan ayrı kopyalarda 99, 2.5, metin ve yinelenen anahtar
bilinçli eklenir; doğrulayıcının durması beklenir. Bu hatalar gerçek arşivde yoktur.
Tam boş ve yalnız bir maddesi dolu kurgusal satırlar için 4/5 puanı boş kalır.
Kurgusal [6,4,5,3,NA] için 4/5 ortalama4.5, 5/5 puan eksiktir.
İki satırlık sol tablo ve [1,1,2] anahtarlı sağ tablo kontrolsüz birleşince üç satır
verir; `validate="one_to_one"` bunu engeller. Uzun dosyaya aynı kişi-madde
tekrarı eklendiğinde `pivot` durur; otomatik ortalama alan `pivot_table` kullanılmaz.
İdempotans kaynak dosyadan yeniden hesaplamayla sağlanır; 7−(7−x)=x olduğundan
zaten puanlanmış dosyayı yeniden terslemek güvenli değildir.

Yöntem belgeleri (erişim 6 Eylül 2026):
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html
https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=expressions-missing-values
https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=expressions-statistical-functions

## Yeni ileri uygulama: çoklu atama

`coklu-atama/` alt klasörü, sürekli yanıt ve bilinen MAR üretim mekanizmasıyla
ayrı bir simülasyon sunar. Regresyon parametreleri her atamada çekilir; Rubin
birleştirmesi, küçük örneklem sd'si, Monte Carlo hatası ve delta duyarlılığı
hesaplanır. Ana BFI verisine veya yukarıdaki hazırlama sonuçlarına dokunmaz.
Çalıştırma ve yöntem sınırları alt klasörün README dosyasındadır.
