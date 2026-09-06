# Bölüm 9 — Aracılık ve Düzenleyicilik

**Bütün veriler simülasyondur; gerçek katılımcı veya araştırma sonucu değildir.**
Kitapta hazır bir ham veri uygulaması bulunmadığından öğrenci çalışması için
iki ayrı mekanizma açık denklemlerle üretildi. Önce [VERI.md](VERI.md) ve
[GOREVLER.md](GOREVLER.md) okuyun.

## Çalıştırma

Öğrencinin bilgisayarında, öğrenci deposu kökünden:

```sh
python -m pip install -r bolumler/b09/requirements.txt
python bolumler/b09/analiz.py
```

Bölüm klasöründe `python analiz.py` yeterlidir. Kod kendi klasöründeki
veri.csv dosyasını okur. Kitap veya başka bölüm gerekmez, ağ erişimi kullanılmaz.
Sürümler hazırlama ortamına aittir; burada yeni paket kurulmadı.
`python -O` kullanmayın; iç denetimleri kapatır.

`calisma.ipynb` defterindeki None alanlarını tamamlayın. Defter öğrenci deposu
kökünden veya b09 içinden çalışabilir. Jupyter ayrıca gerekir; betiğin
bağımlılığı değildir ve requirements listesinde yoktur. Ardından
[COZUMLER.md](COZUMLER.md) ve [beklenen.json](beklenen.json) ile karşılaştırın.
Beklenen dosya bu yeni simülasyonun doğrulanmış hesabıdır; eski gerçek veri sonucu değildir.

R: `Rscript bolumler/b09/analiz.R`; bölüm klasöründe `Rscript analiz.R`.
Temel R yeterlidir, Python çıktısı gerekmez; sonuçlar ekrana yazılır.
R için de 5000 satır-bootstrap ve yüzde 95 persentil aralık tanımlandı.
**R çalıştırılmadı.** Aynı seed numarası R ve NumPy'da aynı yeniden örnekleri
üretmez; R bootstrap uçlarının Python ile birebir eşleşmesi beklenmez.
Bu pakette SPSS/PROCESS dosyası veya çıktısı yoktur.

## Çıktılar

- `sonuclar/ozet.json`: yollar, ab, persentil bootstrap aralığı, etkileşim ve basit eğimler.
- `sonuclar/bootstrap.csv`: 5000 gerçek çalıştırılmış yeniden örneklemin ab değerleri.
- `sonuclar/basit-egimler.csv`: üç W düzeyinde noktasal t aralıkları.
- `sonuclar/merkezlenmis.csv`: ham sütunlar korunarak merkezlenmiş X/W kopyası.
- `grafikler/b09-simulasyon.pdf`: bootstrap dağılımı ve ayrı düzenleyicilik örneğinin eğimleri.

Yeniden çalıştırma bu çıktıları yeniler, ham CSV'yi değiştirmez. Kendi
raporunuzu çıktı klasörlerinden ayrı saklayın. Denetim kapsamı:
[DOGRULAMA.json](DOGRULAMA.json).

## Simülasyonu yeniden üretme

Ana analizi çalıştırmak için veri üretmek gerekmez. Aynı CSV'yi farklı adla üretmek için:

```sh
python bolumler/b09/veri_uret.py --cikti bolumler/b09/veri-yeniden.csv
```

Var olan hedefin üzerine yazılmaz. Yeni CSV aynı sürümlerle bayt düzeyinde
karşılaştırılabilir; ana betik dondurulmuş veri.csv hash'ini kontrol eder.
Farklı deneyler için kod/veriyi ayrı kopyada değiştirin; özgün dosyaları koruyun.

## İki örneği birleştirmeyin

Aracılık: y_aracilik ~ X + M, M ~ X. Düzenleyicilik: y_duzenleyicilik ~ X * W.
İkinci yanıt ilk modelin yanıtı değildir. Bu paket koşullu dolaylı etki,
aracılı düzenleyicilik veya Johnson–Neyman analizi yapmaz. Bootstrap yöntemi
satır bazlı persentildir; BCa/PROCESS çıktısı değildir. Basit eğim aralıkları
noktasal ve klasik t referanslıdır, eşzamanlı güven bandı değildir.