# Bölüm 5 — Güç Analizi ve Örneklem Planlama

Öğrenci paketi, kitap hesaplarının bağımsız çalıştırılabilen sürümüdür.
Önce [VERI.md](VERI.md), sonra [GOREVLER.md](GOREVLER.md) okuyun.
Ana eğitim puanı senaryosu varsayımsaldır; sleep arşivi yalnız tarihsel fark
standart sapmasını örneklemek için kullanılır. Yeni pilot veya simülasyon yoktur.

## Çalıştırma

Depo kökünden, öğrencinin kendi bilgisayarında:

```sh
python -m pip install -r bolumler/b05/requirements.txt
python bolumler/b05/analiz.py
```

Bölüm klasöründe `python analiz.py` çalışır; `veri.csv` aynı klasörde kalmalıdır.
Önceki bölümlerin kod/veri dosyaları gerekli değildir. Bu bölüm SciPy yanında
statsmodels kullanır; kendi requirements listesini kullanın. Sabitlenmiş sürümler
hazırlama ortamının sürümleridir; bu ortamda yeni paket kurulmamıştır.
`python -O` kullanmayın; hesap denetimlerini devre dışı bırakır.

Çalışma defteri `calisma.ipynb`, depo kökünden veya bölüm klasöründen çalışır.
Jupyter ortamınızda açıp None alanlarını tamamlayın. Jupyter analiz betiğinin
zorunlu bağımlılığı değildir; listeye dahil değildir. Sonra [çözüm rehberi](COZUMLER.md)
ve [beklenen değerlerle](beklenen.json) karşılaştırın.

R: `Rscript bolumler/b05/analiz.R`; bölüm klasöründe `Rscript analiz.R`.
Temel R yeterlidir. R kodu sonuçları ekrana basar; Python'un bütün dosyalarını
üretmez. R çalıştırılmadı. Pakette SPSS syntax/çıktısı yoktur; G*Power çalıştırılmadı.
R iki yönlü hesaplarda `strict=TRUE` kullanır. Yazılım adının geçmesi bağımsız
çalıştırma doğrulaması anlamına gelmez.

## Çıktılar

`sonuclar/ozet.json`, `senaryolar.csv`, `pilot_yayilim.csv`, `esli_rho.csv`,
`kayip.csv`, `guc_egrileri.csv` ve `grafikler/b05-guc-planlama.pdf` üretilir.
`pilot_yayilim.csv` adı kitapla uyumluluk için korunur; içeriği yeni pilot değil,
tarihsel yayılım ve varsayımsal alternatif yayılım senaryolarıdır.
Ham CSV değişmez. Yeniden çalıştırma üretilmiş dosyaları yeniler; kendi raporunuzu
çıktı klasörlerinden ayrı tutun. Hesaplar deterministiktir, rastgele veri üretilmez.
Denetim kaydı: [DOGRULAMA.json](DOGRULAMA.json).

## Hesap sınırı

Ana model bağımsız, normal, eşit varyanslı iki grup ve sabit örneklemli, iki yönlü
pooled Student testidir. `n` grup başına, eşli analizde tam çift/kişi sayısıdır.
Fisher-z korelasyon planı yaklaşık; kayıp hesabı bağımsız Bernoulli tutulma
varsayımına bağlıdır. Hassasiyet planı aralık genişliğinin garantisi değildir.
Bu araçların çıktıları araştırmanın temsil, küme, eksik veri veya nedensellik
sorunlarını kendiliğinden çözmez.