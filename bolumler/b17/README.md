# Bölüm 17 — Kovaryans Analizi

**Yerel öğrenci paketi; henüz yayımlanmadı.** Başka bölüm klasörü gerekmez.
60 ToothGrowth kaydıyla ortak eğim, ayrı eğimler ve hücre ortalamalarını karşılaştırın.
Doz bir ön-test değildir; hücre modeli sayısal kovaryatlı ANCOVA değildir.

## Başlangıç

Önce `VERI.md`, sonra `GOREVLER.md` ve `calisma.ipynb` dosyalarını açın.
Çözümleri denemeden önce kendi yanıtınızı yazın. `COZUMLER.md` denetim içindir.
Python ve `requirements.txt` sürümleri kurulu olmalıdır; betikler paket kurmaz.

Çalışma alanı kökünden:
```sh
python ogrenci-deposu/bolumler/b17/analiz.py
```
Öğrenci deposu kökünden veya ZIP'i depo köküne açtıktan sonra:
```sh
python bolumler/b17/analiz.py
```
Bölüm klasöründen:
```sh
python analiz.py
Rscript analiz.R
```
R için önceden kurulu `emmeans` gerekir. R betiği Rscript ile dosya yolunu bulur;
R/SPSS burada çalıştırılmamıştır. `spss-kontrol-listesi.md` uygulama planıdır,
çalışmış SPSS çıktısı veya `.sps` dosyası değildir.

## Neyi hesaplar?

- `additive`: ortak eğim, 3 parametre, hata sd=57.
- `interaction`: ayrı doğrusal eğimler, 4 parametre, hata sd=56.
- `cells`: altı hücre ortalaması, 6 parametre, hata sd=54.
- Her iki iç içe karşılaştırmanın paydasında kendi tam modelinin hata karesi kullanılır.
- Kontrast yönü daima OJ−VC'dir. Ortak modelde tek fark vardır; üç dozda
  tekrar gösterilmesi aileyi büyütmez. Diğer iki modelde üç doz farkı bir ailedir.
- Ortalama aralıkları tekil %95; üçlü farklar Bonferroni ile aile düzeyinde en az
  %95 kapsama hedefler. JSON'daki `ci95`, `family_size` ile birlikte okunur.
- HC3 + hata sd'li t yaklaşımı duyarlılıktır; 60 tek-kayıt dışlama ise ayrı bir
  gözlem etkisi incelemesidir. Hiçbir kayıt ana analizden silinmez.

## Çıktılar ve denetim

`sonuclar/ozet.json` sürümleri, katsayıları, F testlerini, ortalamaları, kontrastları
ve duyarlılık özetlerini içerir. CSV'ler katsayı kovaryanslarını, HC3 matrislerini,
ortalamaları, karşılaştırmaları, altı hücre özetini, tanıları ve 60 dışlama sonucunu
saklar. Türetilmiş `doz_uzunluk.csv` de `sonuclar/` içine yazılır.
`grafikler/b17-egimler-karsilastirmalar.pdf` kodla üretilir.
Kaynak CSV değiştirilmez. Çalıştırma eski üretilmiş çıktıları yeniler.

`beklenen.json` kitabın dondurulmuş sayısal referansıdır; defterde bütün alanları
karşılaştırılır. Analiz NumPy/OLS, elle HC3, F=t², hücre ortalamaları, kaynak
hash'i ve merkezleme kontrollerini içerir. Kontroller için Python'u `-O` ile
çalıştırmayın. Defter öğrenci deposu kökü ve bölüm klasöründen çalışır;
öğrenci yanıtları ve kaydedilmiş hücre çıktıları boş bırakılmıştır.
Gerçekleşen testler ve sınırları `DOGRULAMA.json` dosyasındadır.

## Yorum sınırı

Ortak eğim ve doğrusal biçim ayrı kısıtlardır. Bu örnekte koşullu yorum hücre
modeline dayanır; etkileşim eklemek doğrusal biçim sorununu bitirmez.
2 mg/günde anlamsız fark eşdeğerlik değildir. Doz 3 mg/güne genellenmez.
Model başına düzeltme bütün model aramasının hata kontrolü değildir.
Hash arşiv bütünlüğünü sınar; uzak veri doğrulaması veya randomizasyon kanıtı değildir.
İnsanlara yönelik tedavi önerisi yapılmaz.