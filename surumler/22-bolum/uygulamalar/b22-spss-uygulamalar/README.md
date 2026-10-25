# Bölüm 22 — SPSS'te denetlenebilir analiz oturumu

## Çalıştırma ve durum
Kitap kökünden `python uygulamalar/b22-spss-uygulamalar/analiz.py` çalıştırılır.
Python referans hesaplarını üretir; R betiği aynı sonuçları bağımsız olarak verir.
CSV/JSON/PDF dosyaları SPSS çıktısı değildir. `analiz.sps` ana oturumu,
`durum-deneyi.sps` karşı örnekleri çalıştırır; çıktınızı kontrol sayılarıyla karşılaştırın.
R karşılaştırması: `Rscript uygulamalar/b22-spss-uygulamalar/analiz.R`.
Yeni paket kurulmaz; Python NumPy/SciPy/pandas/matplotlib kullanır, R temel paketlerle çalışır.

SPSS'te kaydedilmemiş veriyi koruyun; tercihen ayrı, temiz bir oturum kullanın.
Çalışma dizini `03-AdvancedStaticalAppTR` kitap kökü olmalıdır. Gerekirse oturuma
uygun göreli `CD` komutunu ekleyin. Önce Python çalıştırıldığında giriş CSV'leri
ve `sonuclar` klasörü oluşur. `analiz.sps` bütünüyle çalıştırılır. Sonra ayrı
`durum-deneyi.sps` kullanılır; bu kopyadaki işlemler ham CSV'ye yazılmaz.
Komut dosyaları `SET DECIMAL=DOT` ile nokta ondalığa geçer; bu bir oturum
ayarıdır. CSV sütun sırasını `/VARIABLES` ile eşleştirin, içe aktarma uyarılarını
inceleyin. F giriş biçimindeki açık ondalık nokta korunur; çıktı biçimleri ayrıca
altı ondalık olarak ayarlanır. Kullandığınız sürümde menüden Paste ile üretilen
syntax ile karşılaştırın. Hazırlanmış syntax, keyfî yeni veriyi otomatik doğrulamaz.
SAV/SPV dosyaları yalnız SPSS gerçekten çalıştırılırsa oluşur; aynı hedef adları
tekrar çalıştırmada değişebilir. Önceki gerçek oturum çıktılarını ayrıca sürümleyin.

## Kaynak ve sözlük
Bölüm 6 `kaynak/sleep.csv` ve `kaynak/ToothGrowth.csv` dosyaları değiştirilmez.
Kaynak/aktarım ve GPL notları o klasörde ve Bölüm 6 README'sindedir.
- sleep: 20 koşul satırı, 10 kişi; `extra` kontrole göre saat artışıdır.
  Negatif ve sıfır geçerli değerlerdir. `ID` üzerinden eşleştirilir;
  hazırlanmış dosyada `kosul1`, `kosul2`, `fark=kosul2-kosul1` bulunur.
- ToothGrowth: 60 hayvan kaydı. `len` kaynak uzunluk ölçeği; kısa sözlükte birim
  belirtilmediğinden mikrometre uydurulmaz. `dose` mg/gün. Yeni dosyada
  `supp=1` OJ, `supp=2` VC'dir; kaynak dosyada metin kodları korunur.
  1 mg/günde iki grupta 10'ar kayıt karşılaştırılır; diğer dozlar silinmez.

LF satır sonuna ve tek son satır sonuna normalize SHA-256:
- sleep: `adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e`
- ToothGrowth: `654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3`
Veriler kurulu R `datasets` tablolarıyla birebir aynıdır. Kısa arşivlerden rastgeleleştirme, körleme, taşıma etkisi,
kafes bağımsızlığı veya geniş anakütle temsili varsayılmaz. Bunlar yöntem öğretimidir;
yeni veri, tedavi önerisi veya yeni önkayıt değildir.

## Hesap sözleşmesi
İki yönlü t testleri, alfa .05, ham ortalama farkına %95 t aralığı kullanılır.
Uyku farkı için n=10, s farkların örneklem s'sidir. Eşli test ve farkın sıfıra
karşı testi aynı hipotezin iki hesap denetimidir; iki bağımsız kanıt değildir.
ToothGrowth doz 1 karşılaştırmasında Welch esas, Student yalnız yöntem
karşılaştırmasıdır. Ortalama merkezli Levene hesabı ayrıca verilir; medyan
merkezli Brown–Forsythe ile karıştırılmaz. Levene sonucuyla otomatik yöntem
seçilmez. Çoklu doz araması yapılmaz; diğer dozlar için Bölüm 7/17'deki aile
ve ortak model planına dönülür. Etki büyüklükleri dz ve d_pooled farklı
standartlaştırıcılardır; bu pakette etki büyüklüğü aralığı hesaplanmaz.
Normallik testi, bootstrap veya permütasyon yapılmaz; küçük örneklem ve fark
biçimi sınırlılıkları Bölüm 4/10 ile birlikte okunur.

## Karşı örnekler
`durum-deneyi.sps` ilk beş kişiye filtre uygular, sonra kapatır. Ardından her
kişiye 2 frekans ağırlığı verilmesinin bağımsız örneklem sayısını artırmadığını
gösterir. Python bu yanlış çıkarım hesabını fiziksel iki kez yinelemeyle
referans olarak üretir; ağırlıklı sonuç yeni 20 kişilik araştırma değildir.
Son olarak ayrı çalışma kopyasında ID1 koşul2 ve ID2 koşul1 gizlenir; her
sütunda 9 geçerli, eşli testte 8 tam kayıt kalır. Fark yeniden hesaplanır;
eski fark sütununun bırakılması tutarsızlık yaratır. Bu gerçek eksiklik değildir.
Deney sonunda ana CSV yeniden okunur; FILTER/WEIGHT/SPLIT kapalıdır.
Gerçek karmaşık örneklemde gerekli tasarım ağırlıkları keyfî kapatılmaz;
buradaki OFF komutları yalnız ağırlıksız öğretim sözleşmesini uygular.

## Çıktılar ve denetim
- `uyku_esli.csv`, `dis_veri.csv`: SPSS/R giriş dosyaları.
- `sonuclar/uyku_betimsel.csv`, `doz1_betimsel.csv`: betimsel hesaplar.
- `sonuclar/durum_karsilastirmasi.csv`: ana/filtre/kurgu eksik/yanlış tekrar hesapları.
- `sonuclar/ozet.json`: yöntemler, sayılar, sürümler, yürütme durumu.
- Kitapta `assets_figures/b18-durum-kontrolu.pdf`: gerçek farklar ve filtre karşılaştırması.

Betik sıralama değişmezliğini, dört bozuk eşleme/eksik kontrol kopyasının reddini,
kovaryans özdeşliğini, işaret terslemesini, açık t/df/CI hesaplarını SciPy ile
ve Levene F'yi mutlak sapmaların Student t karesiyle denetler. Bütün ham dosyaların
baytları çalışma sonunda tekrar karşılaştırılır. SPSS başlıkları/sütun konumları
sürüme göre değişebilir; eşleşen büyüklükleri denetleyin, görüntü eşitliği aramayın.

## Kaynaklar (erişim: 6 Eylül 2026)
R datasets: sleep ve ToothGrowth resmi belgeleri; IBM SPSS Statistics 31
Command Syntax Reference (GET DATA), FILTER, WEIGHT, SPLIT FILE belgeleri;
IBM T-TEST genel başvuru ve çıktı açıklamaları; Delacre, Lakens ve Leys (2017),
DOI 10.5334/irsp.82. Tam erişim adresleri bölüm kaynakçasındadır.