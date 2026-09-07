# İleri İstatistik Uygulamaları — Öğrenci Materyalleri

Prof. Dr. İbrahim Güney'in kitabına eşlik eden veri, kod ve çalışma dosyaları.
**6 Eylül 2026 toplu yayın adayı: Bölüm 2–17, toplam 16 bölüm.**
Bölüm 1 ve 18 bu dağıtımda yoktur; kitabın tam metni yüklenmez.
Yerel hazırlık tamamlanması GitHub veya Pages yayını yapıldığı anlamına gelmez.

- Hedef depo: https://github.com/ibrahimguney/ileri-istatistik-uygulamalari
- Hedef site: https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/
- [Ana sayfa](index.html) · [Yayınlama](YAYINLAMA.md) · [Kullanım](KULLANIM.md)

## Bölümler

- [02 — Betimsel İstatistik](bolumler/b02/README.md)
- [03 — Veri Hazırlama](bolumler/b03/README.md)
- [04 — Hipotez Testleri](bolumler/b04/README.md)
- [05 — Güç Analizi](bolumler/b05/README.md)
- [06 — Korelasyon](bolumler/b06/README.md)
- [07 — Regresyon](bolumler/b07/README.md)
- [08 — Çoklu ve Lojistik Regresyon](bolumler/b08/README.md)
- [09 — Aracılık ve Düzenleyicilik](bolumler/b09/README.md)
- [10 — Parametrik Testler](bolumler/b10/README.md)
- [11 — Varyans Analizi](bolumler/b11/README.md)
- [12 — Parametrik Olmayan Testler](bolumler/b12/README.md)
- [13 — Ölçek Uyarlama ve Güvenirlik](bolumler/b13/README.md)
- [14 — Faktör Analizi](bolumler/b14/README.md)
- [15 — Doğrulayıcı Faktör Analizi](bolumler/b15/README.md)
- [16 — Yapısal Eşitlik Modeli](bolumler/b16/README.md)
- [17 — Kovaryans Analizi](bolumler/b17/README.md)

## Öğrenci için başlangıç

Depoyu bütün olarak indirin; yalnız Python dosyası yeterli değildir.
Önce ilgili `VERI.md`, sonra `GOREVLER.md` dosyasını okuyun. `calisma.ipynb`
öğrenci yanıtları boş olan defterdir; çözümler ayrı dosyadadır.

Gerekli paketler kuruluysa depo kökünde:
```sh
python bolumler/b02/analiz.py
python bolumler/b17/analiz.py
```
Bölüm klasörüne geçildiğinde `python analiz.py` kullanılabilir.
`requirements.txt` tüm paketlerin birleşimini listeler; sürümler bölümün
`requirements.txt` ve doğrulama kaydıyla birlikte değerlendirilir.
Kurulum gerekiyorsa kendi bilgisayarınızda:
```sh
python -m pip install -r requirements.txt
```
Bu hazırlama ortamında paket kurulmaz. Jupyter arayüzü isteğe bağlıdır;
Python analiz betiklerinin çalışması için Jupyter zorunlu değildir.

R/SPSS yönergeleri her bölümde farklıdır; hazırlanmış dosya çalıştırılmış
çıktı sayılmaz. R için gereken ek paketler bölüm rehberlerinde belirtilir.

## Sonuçlar ve sınırlar

Kodlar kendi `sonuclar/` ve `grafikler/` dosyalarını yeniden üretir; kişisel
raporlarınızı bu çıktı klasörlerinde saklamayın. Kaynak CSV'ler korunur.
Dağıtıma üretilmiş sonuç klasörleri, önbellekler ve tam kitap alınmamıştır.
Referans sayılar `beklenen.json`; hesapların ve yazılımların gerçek yürütme
durumu bölüm `DOGRULAMA.json` dosyalarındadır. Toplu paket kontrolü kökteki
[DOGRULAMA.json](DOGRULAMA.json) içinde ayrıca tutulur.

Pages yalnız statik dosya sunar. Önceki bölüm hazırlık kayıtları tarihseldir;
canlı site/yükleme durumunu otomatik değiştirmez. Uzak veri doğrulaması,
yeni araştırma veya R/SPSS çalıştırması yapılmış varsayılmaz.