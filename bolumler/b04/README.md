# Bölüm 4 — Hipotez Testi

Gerçek eşleşmiş veri, kurgusal özet örnekler ve ideal model simülasyonu ayrı
incelenir. Önce [VERI.md](VERI.md), sonra [GOREVLER.md](GOREVLER.md) okunmalıdır.
Bölüm 2/3 veya kitap dosyalarına bağımlılık yoktur.

## Çalıştırma

Depo kökünden, öğrencinin kendi bilgisayarında:

```sh
python -m pip install -r bolumler/b04/requirements.txt
python bolumler/b04/analiz.py
```

Bölüm klasöründe `python analiz.py` yeterlidir. CSV aynı klasörde kalmalıdır.
Bu bölüm NumPy, pandas, matplotlib yanında SciPy kullanır; kendi requirements
listesini kullanın. Sabit sürümler hazırlama ortamının sürümleridir; bu ortamda
paket kurulmamıştır. `python -O` iç hesap denetimlerini kaldırır; kullanmayın.

`calisma.ipynb` çalışma defterini Jupyter ortamınızda açın. Depo kökünden veya
bölüm klasöründen çalışır. `None` alanlarını tamamlayın; çözümler
[COZUMLER.md](COZUMLER.md), sayısal denetimler [beklenen.json](beklenen.json) içindedir.
Jupyter, bu analiz betiğinin zorunlu bağımlılığı değildir ve listeye eklenmemiştir.

R için `Rscript bolumler/b04/analiz.R`; bölüm klasöründe `Rscript analiz.R`.
Temel R yeterlidir. R betiği sonuçları ekrana basar; Python'un çıktı dosyalarının
aynısını üretmez. R çalıştırılmadı; bu pakette SPSS syntax/çıktı dosyası yoktur.
Aynı tohum R ile Python'da aynı rastgele diziyi garanti etmez; simülasyonlar
kuramsal hedef ve Monte Carlo hatasıyla karşılaştırılır.

## Üretilen dosyalar

- `esli_veri.csv`: ID ile eşlenmiş on çift; koşul1, koşul2, fark.
- `sonuclar/testler.csv`: gerçek analiz ve açıkça etiketlenen kurgu testleri.
- `sonuclar/kurgu_capraz.csv`: yalnız kurgusal çapraz tablo.
- `sonuclar/simulasyon.csv`, `sonuclar/ozet.json`: simülasyon ve hesap denetimleri.
- `grafikler/b04-test-mantigi.pdf`: kişi farkları, t dağılımı ve iki yönlü kuyruklar.

Ham CSV değişmez; yeniden çalıştırma üretilmiş dosyaları yeniler. Kendi raporunuzu
bu çıktı klasörlerinden ayrı saklayın. Her simülasyon koşulunda 20000 tekrar,
n=25, normal model, tohum 20260906 kullanılır. Bu, uyku verisinin gerçek gücü
veya varsayım doğrulaması değildir. Çalıştırma kaydı: [DOGRULAMA.json](DOGRULAMA.json).