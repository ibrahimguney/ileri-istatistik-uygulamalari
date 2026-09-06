# Bölüm 3 — Veri Hazırlama

Kitaptaki analizden uyarlanan bağımsız öğrenci paketi. Bölüm 2 dosyaları veya
kitabın `uygulamalar/` klasörü gerekmez. Bu paket tek başına da indirilebilir.

## Öğrenme sırası

1. [Kaynak ve veri sözlüğünü](VERI.md) okuyun.
2. [Görevleri](GOREVLER.md) çalışma defterinde çözün.
3. Analizi çalıştırıp kendi sonuçlarınızla karşılaştırın.
4. [Çözüm rehberini](COZUMLER.md) ve [kontrol değerlerini](beklenen.json) inceleyin.
5. Veri hazırlama kararlarını kısa bir rapora dönüştürün.

## Çalıştırma

Depo kökünden (öğrencinin kendi bilgisayarında):

```sh
python -m pip install -r bolumler/b03/requirements.txt
python bolumler/b03/analiz.py
```

Yalnız bu klasörü indirdiyseniz klasör içinde `python analiz.py` çalıştırın.
Python betiği çalışma dizininden bağımsızdır. `veri.csv` betikle aynı klasörde
kalmalıdır. `python -O` kullanmayın; iç hesap denetimleri devre dışı kalır.
Python bağımlılıkları Bölüm 2 ile aynıdır; bu hazırlama ortamında kurulmadı.

`calisma.ipynb` dosyasını Jupyter ortamınızda açıp hücreleri sırayla çalıştırın;
`None` alanları öğrenci içindir. Jupyter bağımlılık listesine dahil değildir.
Notebook depo kökünden veya kendi bölüm klasöründen çalıştırılabilir.

R için `Rscript bolumler/b03/analiz.R`; bölüm klasöründe `Rscript analiz.R`.
Yalnız temel R gerekir. R betiği temel puan/reshape denetimlerini ekrana basar;
Python ile aynı çıktı dosyalarının tamamını üretme iddiası yoktur.
R çalıştırılmamıştır; bu pakette SPSS syntax veya çalıştırılmış SPSS çıktısı yoktur.

## Üretilen dosyalar

- `puanlar.csv`: 100 kayıt, korunmuş ham maddeler, ters sütunlar ve puanlar.
- `uzun.csv`: 1000 kişi–madde satırı; boş yanıtlar korunur.
- `sonuclar/`: eksik özeti, desenler, puan özetleri, çift paydaları,
  karar günlüğü, standartlaştırma, üretilmiş sözlük ve `ozet.json`.
- `grafikler/b03-eksik-puan-paydalari.pdf`: eksik deseni ve puan paydaları.

Her çalıştırma bu çıktıları yeniler; kendi raporunuzu ayrı yerde saklayın.
`veri.csv` ve dağıtılan `veri_sozlugu.csv` değiştirilmez. Ana dosyadan satır
silinmez. R ve Python uygulama kapsamları ve çalıştırma durumu ayrı tutulur.
Denetim kaydı: [DOGRULAMA.json](DOGRULAMA.json).