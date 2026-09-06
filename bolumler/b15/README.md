# Bölüm 15 — Doğrulayıcı Faktör Analizi

Bağımsız çalıştırılabilir öğrenci paketi; toplu GitHub aktarımı için yerel hazırlıktır. Henüz yayımlandığı iddia edilmez.

## Başlangıç

Öğrenci deposu kökünde:

```sh
python bolumler/b15/analiz.py
```

Bölüm klasöründe `python analiz.py` da çalışır. Kitap klasörlerine veya ağa gerek yoktur. `requirements.txt` doğrulama ortamındaki paket sürümlerini listeler; betikler paket kurmaz.

1. `VERI.md` ve `veri_sozlugu.csv` ile kaynağı ve sabit kararları okuyun.
2. `GOREVLER.md` görevlerini `calisma.ipynb` içinde çözün.
3. Hesapları `beklenen.json`, gerekçeleri `COZUMLER.md` ile karşılaştırın.
4. Gerçek denetimleri ve çalıştırılmayan araçları `DOGRULAMA.json` içinde inceleyin.

## Aynı veride üç model

Bölüm 13/14 ile aynı ilk 100 A/C kaydından ortak 97 tam kayıt seçilir. A1/C4/C5 bir kez ters puanlanır. Bu tekrar hesaplama bağımsız DFA doğrulaması değildir; yeni örneklem veya Türkçe uyarlama verisi üretilmez.

| Model | Kısıt | Serbest parametre | sd |
|---|---|---:|---:|
| M0 / orthogonal | İlişkisiz iki faktör | 20 | 35 |
| M1 / correlated | İlişkili iki faktör | 21 | 34 |
| M2 / cross_A2 | M1 + A2'nin C çapraz yükü | 22 | 33 |

Normal-kuram kovaryans ML, Wishart n−1 çarpanı ve ortalama yapısı olmadan hesaplanır. M0, CFI'nin bağımsız göstergeli başlangıç modeli değildir. M2 aynı verideki AFA ipucundan seçildiği için fark testinin p değeri nominaldir, seçim için düzeltilmiş doğrulayıcı kanıt değildir.

## Çıktılar

`sonuclar/ozet.json`: modeller, uyum indeksleri, belirsizlik ve sayısal denetimler.
On iki CSV: `puanlanmis`, `standartlastirilmis`, `orneklem_kovaryans` ve her model için `_model`, `_artik`, `_yukler` dosyaları. Puanlanmış dosya zaten ters kodlanmıştır. Standartlaştırılmış CSV yalnız on maddeyi içerir; satır sırası puanlanmış dosyayla aynıdır, kimlik gerekiyorsa oradan eşlenir. Model/matris CSV'lerinde ilk sütun satır etiketidir.

`grafikler/b15-yuk-araliklari.pdf`: M1 standart yüklerinin model-temelli, sağlam olmayan tekil %95 Wald aralıkları. Sonuçlar ve grafik dağıtım ZIP'ine dahil değildir; kodla yeniden üretilir. Ham kaynak değişmez.

## R/lavaan ve AMOS

Önce Python ile puanlanmış CSV'yi üretin. Sonra öğrenci deposu kökünde `Rscript bolumler/b15/analiz.R` ya da bölüm klasöründe `Rscript analiz.R` kullanılabilir. R betiği kurulu lavaan ister, yoksa durur; kurulum yapmaz. Bu ortamda R/lavaan çalıştırılmamıştır.

`amos-kontrol-listesi.md` yapılacak kurulum içindir, çalıştırılmış AMOS çıktısı değildir. Python sayıları AMOS veya lavaan tarafından doğrulanmış gibi sunulmaz. Standartlaştırma, kovaryans böleni, ki-kare çarpanı, bilgi matrisi ve aralık tanımları eşleştirilmelidir.

WLSMV, MLR, FIML, otomatik MI taraması, bootstrap, değişmezlik ve yeni veriyle doğrulama yapılmaz. Bu sabit on maddelik öğretim kodu genel amaçlı SEM tahminleyicisi değildir. Defterdeki `None` alanları öğrenci yanıtıdır; referans hesaplarının çalışması yanıtların tamamlandığı anlamına gelmez.