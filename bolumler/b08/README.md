# Bölüm 8 — Çoklu ve Lojistik Regresyon

İki ayrı soru: G3 koşullu ortalaması ve öğretim amaçlı G3≥14 olayının
olasılığı. Önce [VERI.md](VERI.md), sonra [GOREVLER.md](GOREVLER.md) okuyun.

## Çalıştırma

Öğrencinin bilgisayarında, öğrenci deposu kökünden:

```sh
python -m pip install -r bolumler/b08/requirements.txt
python bolumler/b08/analiz.py
```

Bölüm klasöründe `python analiz.py` yeterlidir. `veri.csv` kodla aynı klasörde
kalmalıdır. Kitap veya Bölüm 7 dosyaları gerekmez. Betik çevrimdışı çalışır;
çevrimiçi kaynak karşılaştırması yapmaz. Sürümler hazırlama ortamına aittir;
burada paket kurulmadı. `python -O` kullanmayın; iç denetimleri kapatır.

`calisma.ipynb` defterini Jupyter ortamında açın; depo kökü veya bölüm
klasöründen çalışır. None alanları öğrenci görevleridir. Jupyter analiz
betiği için zorunlu değildir ve requirements listesinde bulunmaz.
Hesaplarınızı [COZUMLER.md](COZUMLER.md) ve [beklenen.json](beklenen.json)
ile karşılaştırın; küçük kayan nokta farkları olabilir.

R: `Rscript bolumler/b08/analiz.R`; bölüm klasöründe `Rscript analiz.R`.
Temel R yeterlidir; Python çıktısı gerekmez. R sonuçları ekrana yazar;
OLS, GLM, Wald OR aralıkları, HC3 SH, VIF ve eşik tablolarını içerir.
Python ile aynı kapsamda dosya/grafik veya AUC çıktısı üretmez.
R çalıştırılmadı. Bu öğrenci paketinde SPSS syntax/çıktısı yoktur.

## Kapsam ve çıktı dosyaları

İlk 60 kayıtta iki model kurulur; sonraki 20 kayda aynı katsayılarla tahmin
üretilir. Bölüm 7 etkinliğinden farklı olarak son 20 kayıtta model yeniden
kurulmaz. Bu aynı okulun sıralı alıntısıdır; bağımsız dış doğrulama değildir.

- `veri.csv`: değiştirilmeden korunan 80 kayıt ve beş ham sütun.
- `sonuclar/hazirlanmis.csv`: 80 kayıt; age_c ve hedef14 eklenmiş çalışma kopyası.
- `sonuclar/ozet.json`: OLS/HC3, VIF, ek değişken F testi, logit/Wald OR,
  model uyumu, eğitim/aktarım eşik tabloları ve yazılım sürümleri.
- `sonuclar/tani.csv`: ilk 60 kayıt için artık, kaldıraç, Cook ve olasılık.
- `sonuclar/aktarim.csv`: son 20 kayda sabit modellerin tahminleri.
- `sonuclar/profiller.csv`: örnek G1/yaş profillerinin tahminleri.
- `grafikler/b08-uci-modeller.pdf`: koşullu ortalama ve olay olasılığı.
- `grafikler/b08-uci-tani.pdf`: doğrusal modelin artık/etki grafikleri.

Yeniden çalıştırma üretilen dosyaları yeniler; kendi raporunuzu bu
klasörlerden ayrı tutun. Denetim kapsamı [DOGRULAMA.json](DOGRULAMA.json).

## Karıştırmayın

14 not puanı öğretim amaçlı olay tanımıdır, resmî geçme sınırı değildir.
0.3/0.5/0.7 ise olasılık karar eşikleridir; aktarım sonuçlarına göre seçilmez.
OR olasılık oranı değil odds oranıdır. Lojistik Wald aralıkları normal
referanslı, doğrusal klasik/HC3 aralıklar t(57) referanslıdır.
OLS R² ve McFadden R² aynı ölçü değildir. AUC kalibrasyon, Brier yalnızca
kalibrasyon ölçüsü değildir. Brier referansı her iki kümede eğitim olay
oranı 19/60'tır; sonraki 20'nin olay oranına göre yeniden ayarlanmaz.