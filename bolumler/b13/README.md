# Bölüm 13 — Ölçek Uyarlama ve Güvenirlik

Ham/standart alfa, madde–kalan korelasyonu ve satır-bootstrap için bağımsız
öğrenci paketi. **Toplu aktarım için yerel hazırlık; GitHub'da yayımlandığı
iddia edilmez.** Kitap veya başka bölüm klasörü gerekmez.

## Ne yapıldı, ne yapılmadı?
psych::bfi kaynağının yerel ilk 100 kayıt, A1–A5/C1–C5 alıntısı yeniden analiz
edilir. Bu, yeni Türkçe ölçek geliştirme veya uyarlama çalışması değildir.
Türkçe ifade taslakları, görüşme soruları ve revizyon tablosu GOREVLER.md'de
öğrenci planı olarak sunulur; uzman onayı/görüşme/pilot yapılmış gibi gösterilmez.
Kaynak John ve arkadaşlarının Big Five Inventory ölçeğiyle karıştırılmamalıdır.

## Çalışma sırası
1. `VERI.md` ve `veri_sozlugu.csv`: kaynak, anahtar, eksikler ve kullanım sınırları.
2. `GOREVLER.md`: kitaptaki D/G/B/H/P etkinlikleri ve uyarlama kanıt şablonu.
3. `calisma.ipynb`: önce boş hesapları tamamlayın, sonra referans hücreleri.
4. `COZUMLER.md` ve `beklenen.json`: gerekçeli yorum ve sayısal kontrol.
5. `DOGRULAMA.json`: çalıştırılmış denetimler ve yapılmamış işlemler.

## Çalıştırma
Python ve requirements.txt paketleri kuruluysa öğrenci deposu kökünden:

```sh
python bolumler/b13/analiz.py
```

Bölüm klasöründe `python analiz.py` de çalışır. Kod veri indirmez ve paket kurmaz.
requirements.txt doğrulama ortamındaki sürümlerdir. Notebook ayrıca Jupyter ortamı
ister. A ve C için ayrı ayrı 20000 satır-bootstrap çalıştırılır.

R kuruluysa `Rscript bolumler/b13/analiz.R`; etkileşimli R'de bölüm klasöründen
`source("analiz.R")`. Temel R yeterlidir; psych zaten kuruluysa ek alfa
karşılaştırması yapılır, paket kurulmaz. **R bu ortamda çalıştırılmadı.**
Aynı tohum R/Python'da aynı bootstrap örneklerini garanti etmez. SPSS komut
dosyası bu öğrenci paketinde yoktur; kitapta menü/yöntem açıklamaları vardır.

## Sabit puanlama
- Yanıt aralığı 1–6; A1, C4, C5 belgelenmiş anahtarla bir kez 7−x yapılır.
- A için 99, C için 98 tam kayıt; karşı örnek A+C için 97 ortak tam kayıt.
- Eksikler sıfır veya ortalamayla doldurulmaz. Madde silinirse aynı kişiler korunur.
- A bootstrap tohumu 202613, C tohumu 202614; %95 persentil, doğrusal nicelikler.
- Ham alfa, standart alfa ve madde korelasyonları farklı özetlerdir.
- A+C toplamı ve madde çoğaltma yalnız karşı örnektir; geçerli yeni ölçek önerilmez.

| Küme | n | Ham alfa | Standart alfa | %95 persentil GA |
|---|---:|---:|---:|---|
| A | 99 | .629588 | .651399 | [.464423,.736637] |
| C | 98 | .722610 | .731783 | [.579608,.811465] |

Katsayı veya eşik tek başına geçerlik, kültürel eşdeğerlik ve kullanım uygunluğu
kanıtı değildir. Omega, test–tekrar test veya değişmezlik sonucu üretilmez.

## Çıktılar
`sonuclar/`: ozet.json; puanlanmis_A.csv, puanlanmis_C.csv; madde_A.csv,
madde_C.csv; kovaryans_A.csv, kovaryans_C.csv; korelasyon_A.csv, korelasyon_C.csv.
Puanlanmış CSV'lerde ters anahtar zaten uygulanmıştır; ikinci kez terslemeyin.

`grafikler/`: b13-madde-analizi.pdf ve b13-bootstrap.pdf.

Ham CSV değiştirilmez; üretilmiş çıktılar ZIP'te bulunmaz, yeniden üretilir.
Kaynak ve kullanım açıklamasını VERI.md ile birlikte koruyun. IPIP maddeleri
hakkındaki kamu malı açıklaması tüm veri aktarımlarına veya başka ölçeklere
aynı lisansı atamak anlamına gelmez; bu pakette yeni lisans atanmadı.