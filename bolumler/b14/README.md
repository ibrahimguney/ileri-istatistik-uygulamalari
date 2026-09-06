# Bölüm 14 — Faktör Analizi

Bu bağımsız öğrenci paketi kitabın ortak 97 kayıt üzerinde yürütülen AFA örneğini yeniden üretir. GitHub'a toplu aktarım için yerelde hazırlanmıştır; yayımlandığı iddia edilmez.

## Başlangıç

Öğrenci deposu kökünde:

```sh
python bolumler/b14/analiz.py
```

Bölüm klasöründe `python analiz.py` da kullanılabilir. Kitap klasörlerine veya ağa ihtiyaç yoktur. Gerekli Python paketlerinin doğrulama ortamındaki sürümleri `requirements.txt` içindedir; betikler kurulum yapmaz.

1. `VERI.md` ve `veri_sozlugu.csv` ile kaynağı, eksikleri ve tek seferlik ters kodlamayı okuyun.
2. `GOREVLER.md` içindeki D/G/B/H/P görevlerini `calisma.ipynb` ile çözün.
3. Sayısal yanıtları `beklenen.json`, gerekçeleri `COZUMLER.md` ile karşılaştırın.
4. `DOGRULAMA.json` içinde gerçekten çalıştırılan ve çalıştırılmayan denetimleri ayırın.

## Analiz kapsamı

- İlk 100 kayıtta on A/C maddesi; 63, 66 ve 90 dışarıda, ortak 97 tam kayıt. A1/C4/C5 bir kez `7-x` ile anahtarlanır.
- Pearson korelasyonu, KMO ve madde MSA'ları, yaklaşık Bartlett testi.
- SMC başlangıçlı temel eksenler faktörleştirmesi (PAF); aynı kişilerde bir, iki ve üç faktör adayları.
- İki faktörde Kaiser satır normalizasyonu olmadan quartimin; örüntü, yapı, faktör korelasyonu ve yeniden üretilen korelasyonlar.
- 2000 bağımsız sütun permütasyonu, tohum 20261401, doğrusal %95 referans niceliği; PCA ve başlangıç SMC spektrumları. İkisi de iki aday boyut önerir.
- A1/A4 çıkarma yalnız duyarlılıktır; ana analizde madde silinmez. Sekiz maddeli incelemede aynı 97 kişi korunur.

Bu paket Türkçe uyarlama, tüm kişilik yapısının keşfi veya bağımsız DFA doğrulaması değildir. Polikorik analiz, yük güven aralığı, bootstrap yük kararlılığı ve yeni veriyle DFA yapılmaz. Paralel analizdeki sütun permütasyonu Bölüm 13'ün kişi-satırı bootstrap'ı değildir.

## Yerelde üretilen dosyalar

`sonuclar/ozet.json` bütün sayısal özetleri ve sürümleri içerir. Sekiz CSV üretilir: `puanlanmis`, `korelasyon`, `kismi_korelasyon`, `oruntu`, `yapi`, `yeniden_uretilen`, `artik`, `faktor_korelasyon`. `puanlanmis.csv` zaten anahtarlanmıştır; tekrar ters kodlanmaz. Diğer CSV'lerde ilk sütun matris satır etiketidir, yeni bir madde değildir.

`grafikler/b14-paralel-analiz.pdf` ve `grafikler/b14-oruntu-yapi.pdf` yeniden üretilir. Sonuçlar ve grafikler dağıtım ZIP'ine alınmaz. Kaynak dosyasının baytları değişmeden kalır.

## R ve yazılım karşılaştırması

Önce Python ile puanlanmış CSV'yi üretin; ardından öğrenci deposu kökünden `Rscript bolumler/b14/analiz.R` veya bölüm klasöründen `Rscript analiz.R` kullanılabilir. R betiği hazırlanmıştır, bu ortamda çalıştırılmamıştır. Temel R hesaplarına ek olarak yalnız kuruluysa GPArotation ile quartimin çalışır; paket kurulmaz. R'nin yük işareti/sırası ve rastgele dizileri Python'dan farklı olabilir. Ortak matrisler ve yöntem ayarları eşleştirilmeden doğrudan yük eşitliği beklenmez.

Bu öğrenci paketinde SPSS betiği yoktur; kitap menü yönergeleri ayrıca kullanılabilir. Python sayıları SPSS veya R çıktısı olarak sunulmaz. Çalışma defterindeki boş yanıt alanları öğrenci içindir; referans kodlarının çalışması bu yanıtların tamamlandığı anlamına gelmez.