# Bölüm 16 — Yapısal Eşitlik Modeli

Bağımsız çalıştırılabilir öğrenci paketi; toplu GitHub aktarımı için yerel hazırlıktır. Canlı yayın yapıldığı iddia edilmez.

## Başlangıç

Öğrenci deposu kökünde:

```sh
python bolumler/b16/analiz.py
```

Bölüm klasöründe `python analiz.py` da çalışır. Kitap klasörlerine veya ağa ihtiyaç yoktur. `requirements.txt` doğrulama ortamındaki sürümleri listeler; betikler paket kurmaz.

1. `VERI.md` ve `veri_sozlugu.csv` ile kaynak/ölçüm kararlarını okuyun.
2. `GOREVLER.md` görevlerini `calisma.ipynb` ile çözün.
3. Sayıları `beklenen.json`, gerekçeleri `COZUMLER.md` ile karşılaştırın.
4. Gerçek denetimler ve yapılmayanlar `DOGRULAMA.json` içinde ayrılır.

## Üç model, aynı kişiler

On A/C maddesinde ortak 97 tam kayıt; A1/C4/C5 bir kez ters puanlanır. Bölüm 14–15 ile aynı kayıtlar olduğu için bağımsız doğrulama değildir. Türkçe uyarlama veya yeni örneklem üretilmez.

| Model | Yapısal denklem | Parametre / sd |
|---|---|---|
| forward | C = gamma A + zeta_C | 21 / 34 |
| reverse | A = delta C + zeta_A | 21 / 34 |
| zero | gamma = 0 | 20 / 35 |

A1 ve C1 işaretleyici yükleri 1; diğer sekiz yük, on gösterge hatası, dışsal varyans ve yapısal artık varyansı serbesttir. Serbest yollu modellerde yol da tahmin edilir. Gösterge hatası, yapısal artık ve içsel faktörün toplam varyansı farklıdır.

Normal-kuram kovaryans ML, Wishart n−1 çarpanı ve ortalama yapısı olmadan hesap yapılır. İleri/ters modeller aynı gözlenen kovaryansı üretir; iyi uyum nedensel yönü seçmez. İleri–ters için sd=0 ile fark testi p'si üretilmez. Sıfır-yol LR testi ve ham yol Wald testi farklı yaklaşımlardır; küçük p seçilmez.

## Yerel DFA yardımcısı

`dfa_referans.py`, kitabın Bölüm 15 Python dosyasındaki hesap fonksiyonlarının kopyasıdır; `main` ve dosya üretimi içermez. Birim-varyans DFA çözümünü marker ölçeğine çevirmek, eşdeğer kovaryansı ve RMSEA aralığını denetlemek için yüklenir. Ayrı B15 klasörü gerekmez; bu ikinci bir veri seti veya farklı yazılımda doğrulama değildir. Kod genel amaçlı SEM tahminleyicisi değildir.

## Üretilen dosyalar

`sonuclar/ozet.json`: kaynak/sürümler, üç model, yol/ varyans belirsizliği, LR ve eşdeğerlik denetimleri.

On dört CSV: `puanlanmis`, `standartlastirilmis`, `orneklem_kovaryans`, her model için `_kovaryans`, `_artik`, `_yukler`, ayrıca `uyum` ve `yapisal_parametreler`. İki veri CSV'sinde kaynak sıra/etiketleri korunur; yalnız on madde göstergedir. Anahtarlamayı veya z-puan dönüşümünü tekrar etmeyin. Matris CSV'lerinin ilk sütunu satır etiketidir.

`grafikler/b16-yukler-artiklar.pdf`: ileri modelin standart yükleri ve artık ısı haritası. Renk ölçeği ±.2 ile sınırlıdır; uç artıkların büyüklüğü CSV'den okunur. Sonuçlar/grafikler dağıtıma eklenmez; kodla yeniden üretilir. Ham kaynak değişmez.

## R/lavaan ve AMOS

Önce Python çıktılarını üretin. Öğrenci deposu kökünden `Rscript bolumler/b16/analiz.R` veya bölüm klasöründen `Rscript analiz.R` kullanılabilir. Kurulu lavaan yoksa durur; kurulum yapmaz. R, ileri/ters eşdeğerliği ve Python kovaryansını karşılaştırmak üzere hazırlanmıştır; çalıştırılırsa `sonuclar_R/` üretir. Bu ortamda R/lavaan ve AMOS çalıştırılmamıştır.

`amos-kontrol-listesi.md` yapılacak uygulamadır, AMOS çıktısı değildir. Python sayıları AMOS veya lavaan tarafından doğrulanmış gibi gösterilmez. Betikte yeni AMW/SAV dosyası yoktur.

## Kurgu ve gerçek analiz ayrımı

Gerçek iki faktörlü örnekte aracı değişken yoktur. a=.48, b=.41, c′=.19 yalnız kurgu cebir örneğidir: ab=.1968, toplam=.3868. Bunlar BFI tahmini değildir; kurgu için bootstrap/p/aralık üretilmez. WLSMV, MLR, FIML, değişmezlik, profil olabilirlik ve yeni veriyle doğrulama da yapılmaz. Defterdeki boş yanıt alanlarını öğrenciler doldurur.