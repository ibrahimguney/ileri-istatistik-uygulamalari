# Öğrenci görevleri

Önce [veri sözlüğünü](VERI.md) okuyun. Aşağıdaki soruların hesabını ve yorumunu
kendi raporunuza yazın; yalnız ekran çıktısı teslim etmeyin.

## D — Hesaptan önce

1. Satır, okul kodu ve iki not sütunu neyi temsil eder? Bağımsız kayıt kaçtır?
2. İlk satırdaki G1=0 neden korunmalıdır? Bu kayıt için fark kaçtır?
3. n−1 kullanmak alıntıyı temsili örnekleme dönüştürür mü?

## G — Rehberli hesap

1. G3 toplamını bulun. Ortalama, kareli sapmalar toplamı, n−1 varyansı ve s'yi hesaplayın.
   Aynı toplamı n'ye bölerek kapalı 80-kayıt varyansını ayrıca yazın.
2. G1'i sıralayın. 60. ve 61. değerlerden tip 7 üst çeyreğini bulun.
   Q1, IQR, iki tarama sınırı ve iki bıyık ucunu birbirinden ayırın.
3. İlk 60 ve son 20 G3 kaydının ortalamalarını bulun. Kişi sayılarıyla ağırlıklı
   birleştirme ile iki ortalamanın basit ortalamasını karşılaştırın.
4. G1/G3 kovaryansı, korelasyonu ve G3−G1 fark varyansını bulun.
   Fark varyansı özdeşliğini kontrol edin; artan, eşit ve azalan notları sayın.

## B — Bağımsız deneme

1. G1'in iki 40'lık yarısının medyanlarıyla Q1/Q3 hesaplayın.
   Tip 7 sonucuyla işaretlenen kayıtları karşılaştırın.
2. G3'e 10 ekleyin; ayrı bir kopyada 5 ile çarpın. Ortalama, s ve mekanik CV nasıl değişir?
3. Ana veri değişmeden yalnız ilk satırı dışlayan bir duyarlılık kopyası oluşturun.
   G1 ortalaması, s ve G1/G3 korelasyonunu karşılaştırın. Silme kararı çıkar mı?

## H — Hatalı yorumu düzeltin

“Ortalama medyandan büyük; dağılım kesin sağa çarpık. Kutu grafikte işaretlenen
her satırı sildik. n−1 kullandığımızdan örnek temsilidir. Ortalama artmış,
demek ki herkesin notu artmıştır.” Her iddiayı ayrı düzeltin.

## Teslim

Bir kısa rapor, çalıştırılan kod/notebook ve histogram/kutu grafiği teslim edin.
Kaynağı, 80 kayıt kapsamını, çeyrek tanımını, ana/duyarlılık ayrımını ve kullanılan
Python/R sürümünü yazın. Yapılmamış test veya yazılım çalıştırmasını raporlamayın.

Değerlendirme: kapsam/ölçüm 20, hesap/tanımlar 30, grafik/uç kayıt 20,
yorum 20, yeniden üretim 10 puan.