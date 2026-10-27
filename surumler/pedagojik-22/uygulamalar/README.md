# Uygulama paketleri

Her bölümün klasöründe veri, veri sözlüğü, Python (`analiz.py`), R (`analiz.R`)
ve gerektiğinde SPSS (`analiz.sps`) dosyaları bulunur. `ecls-k-2011` klasörü,
22 bölümde ortak bağlam olarak kullanılacak öğretim SAV dosyasını yerel ham
veriden üreten ayrı bir hazırlık paketidir. Bütün komutlar **kitap kökünden**
çalıştırılır; dosya yolları buna göre yazılmıştır.

## Kurulum

Python (3.11 ve üstü):

    python -m pip install -r uygulamalar/requirements.txt

R (4.3 ve üstü) için gereken paketler:

    install.packages(c("psych", "lavaan", "emmeans", "GPArotation", "lme4", "nlme",
                       "afex", "car", "sandwich", "lmtest"))

Betikler paket kurmaz; eksik paket varsa açık bir hata iletisiyle durur.

SPSS: `analiz.sps` dosyaları IBM SPSS Statistics 27 ve üstü için yazılmıştır
(Bölüm 5'teki `POWER` komutu 27 sürümüyle gelmiştir). SPSS'te çalışma dizini
kitap köküne ayarlanmalıdır; gerekirse dosyanın başındaki `CD` satırı
düzenlenir.

## Çalıştırma

    python uygulamalar/b12-regresyon/analiz.py
    Rscript uygulamalar/b12-regresyon/analiz.R

Python betikleri sonuçları `sonuclar/` klasörüne yazar ve kitapta kullanılan
grafikleri yeniden üretir. Her betik sonunda sayısal denetimlerini çalıştırır;
denetimlerden biri tutmazsa hata vererek durur.

## Doğrulama

Kitapta raporlanan sayılar Python ile üretilmiş, aynı analizler R ile
bağımsız olarak yeniden hesaplanmıştır. Kullanılan veri alıntıları
özgün kaynaklarıyla hücre hücre karşılaştırılmıştır:

| Veri | Özgün kaynak | Kullanıldığı bölümler |
|---|---|---|
| UCI Student Performance (Portekizce, ilk 80 kayıt) | Cortez (2008), UCI Machine Learning Repository, CC BY 4.0 | 1, 2, 11–13 |
| `sleep` | R `datasets` paketi | 4–6, 10, 22 |
| `ToothGrowth` | R `datasets` paketi | 6, 7, 10, 14, 22 |
| `RoundingTimes` | R `stats::friedman.test` yardım örneği | 10 |
| `sleepstudy` | R `lme4` paketi; Belenky vd. (2003) | 8 |
| `Orthodont` | R `nlme` paketi; Potthoff ve Roy (1964) | 8 |
| `sat.act` | R `psych` paketi (SAPA projesi) | 9 |
| `MathAchieve`, `MathAchSchool` (High School and Beyond) | R `nlme` paketi; Raudenbush ve Bryk (2002) | 16 |
| `bfi` (ilk 100 kayıt, A ve C maddeleri) | R `psych` paketi | 3, 17 |
| `bfi` (A ve C maddelerinde tam yanıtlı 2632 kişi; rastgele iki yarı) | R `psych` paketi | 18 (yarım A), 19–21 (yarım B) |
| Aracılık/düzenleyicilik simülasyonu | Üretim kodu `b15-aracilik-duzenleyicilik/analiz.py` | 15 |
| ECLS-K:2011 K-5 kamu dosyasından belgelenmiş öğretim alıntısı | NCES ECLS-K:2011 kamu kullanım dosyası; yerel üretim için `ecls-k-2011/eclsk_ogretim_secim.sps` | 1–22 için ortak SPSS bağlamı (pilot: 2, 8, 16, 18) |

Her Python betiği kaynak dosyanın SHA-256 özetini de denetler; dosya
değiştirilmişse analiz başlamaz.
