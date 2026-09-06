# İleri İstatistik Uygulamaları — Öğrenci Materyalleri

Prof. Dr. İbrahim Güney'in kitabına eşlik eden veri, kod ve uygulama paketi.
**Pilot sürüm: 0.1.0 — 6 Eylül 2026.** Şu anda yalnız Bölüm 2 hazırlanmıştır.
Diğer 17 bölüm için uygulama paketi bu depoya henüz eklenmemiştir.
Kitabın tam metni bu pakette yer almaz.

- Hedef depo: https://github.com/ibrahimguney/ileri-istatistik-uygulamalari
- Yayın sonrası site: https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/
- [Bölüm 2 rehberi](bolumler/b02/README.md)
- [Yayınlama ve kontrol listesi](YAYINLAMA.md)
- [Kaynak ve kullanım ayrımı](KULLANIM.md)

Bu dosyaların yerelde hazırlanması GitHub'a yüklenmiş oldukları anlamına gelmez.
Site adresi, Pages yayını etkinleştirilip kontrol edildikten sonra kullanılmalıdır.

## Öğrenci için başlangıç

Depoyu bir bütün olarak indirin ve ZIP'i açın. Yalnız `analiz.py` dosyasını
indirmek yeterli değildir: yanındaki `veri.csv` de gereklidir.
Komutları bu README'nin bulunduğu **depo kökünde** çalıştırın:

```sh
python -m pip install -r requirements.txt
python bolumler/b02/analiz.py
```

Kurulum komutu öğrencinin kendi bilgisayarı içindir; hazırlama ortamında paket
kurulmamıştır. Python 3.11 veya üstünü kullanın. Sabitlenmiş paket sürümleri
pilotun Python çalıştırmasında kullanılan sürümlerdir; farklı ortamlarda
sonuçları `beklenen.json` ile karşılaştırın.

Python betiği tabloları `bolumler/b02/sonuclar/`, grafiği
`bolumler/b02/grafikler/` altında üretir. Grafik kitabın TikZ dosyalarına
bağımlı değildir. Kaynak CSV değiştirilmez. Betik her çalıştırmada kendi
ürettiği çıktıları yeniler; öğrenci raporunuzu bu çıktı klasörlerinde tutmayın.

İsteğe bağlı çalışma defteri: `bolumler/b02/calisma.ipynb`.
Jupyter ortamınızda açın; hücreleri sırayla çalıştırıp boş cevapları tamamlayın.
Jupyter, analiz betiğinin zorunlu bağımlılığı değildir.
R için depo kökünde `Rscript bolumler/b02/analiz.R` kullanılabilir; yalnız temel R gerekir.
Bu pilotta SPSS syntax dosyası yoktur; Python çıktıları SPSS çıktısı diye sunulmaz.

## Öğrenme sırası

1. [Veri kaynağını ve sözlüğünü](bolumler/b02/VERI.md) okuyun.
2. [Görevleri](bolumler/b02/GOREVLER.md) önce kendiniz çözün.
3. Python betiği veya çalışma defteriyle hesapları yeniden üretin.
4. [Ayrı çözüm rehberi](bolumler/b02/COZUMLER.md) ve [kontrol değerleri](bolumler/b02/beklenen.json) ile karşılaştırın.
5. Kaynak, kapsam, hesap tanımı ve sınırlılıkları içeren kendi raporunuzu yazın.

## Yürütme durumu

Python pilot paketi yerelde doğrulanır; ayrıntılar `DOGRULAMA.json` dosyasındadır.
R ve SPSS çalıştırılmış sayılmaz. GitHub Pages statik indirme sayfasıdır;
Python/R kodunu kendiliğinden çalıştıran bir sunucu değildir.

Bölüm sayfa yollarını (`bolumler/b02/` gibi) baskıdan sonra değiştirmeyin.
Baskıyla eşleşen sürümü ayrıca arşivleyin. Pilot 0.1.0, kitabın nihai baskı
sürümü olarak etiketlenmemelidir.