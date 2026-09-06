# Bölüm 10 — Parametrik Testler

Bu bağımsız öğrenci paketi tek örneklem, eşli ve bağımsız iki örneklem t testlerini
aynı yerel arşivlerden yeniden üretir. **GitHub'a toplu aktarım için hazırlanmıştır;
yayında olduğu iddia edilmez.** Kitabın veya başka bölümün dosyaları gerekmez.

## Öğrenme sırası
1. `VERI.md` ve `veri_sozlugu.csv`: birim, eşleşme, kaynak ve seçim kararları.
2. `GOREVLER.md`: D/G/B/H/P etkinlikleri; önce kendi çözümünüzü yazın.
3. `calisma.ipynb`: yerel Jupyter ortamında açın, boş hesapları tamamlayın.
4. `analiz.py`: tam referans hesap; `COZUMLER.md`: gerekçeli yorumlar.
5. `beklenen.json`: kitabın sayısal kontrol değerleri; `DOGRULAMA.json`: çalıştırma kapsamı.

## Çalıştırma
Python ve requirements.txt içindeki paketlerin kurulu olduğu ortamda, öğrenci deposu kökünden:

```sh
python bolumler/b10/analiz.py
```

Ya da bölüm klasöründe `python analiz.py`. Ağ erişimi, kitap klasörü veya uzak veri
indirmesi gerekmez. `requirements.txt` doğrulamada kullanılan sürümleri kaydeder;
analiz kodu bağımlılık kurmaz. Notebook için ayrıca Jupyter ortamı gerekir.

R kuruluysa `Rscript bolumler/b10/analiz.R` kullanılabilir. Bu betik yerel CSV'leri
kurulu R datasets tablolarıyla da karşılaştırır. **R bu ortamda çalıştırılmadı**;
bu karşılaştırmanın geçtiği iddia edilmez. R betiği sonuçları konsola basar;
Python'daki grafik ve tüm tanı çıktılarının birebir eşdeğeri değildir.
SPSS komut dosyası bu öğrenci paketinde yoktur; kitapta menü/yöntem açıklamaları vardır.

## Üretilen dosyalar
- `sonuclar/ozet.json`: testler, tanılar, duyarlılık, kaynak hash'leri ve sürümler.
- `sonuclar/uyku_esli.csv`: ID ile eşlenmiş 10 kişi ve koşul 2−1 farkı.
- `sonuclar/dis_veri.csv`: 60 hayvan kaydı, ek supp_kod sütunu.
- `sonuclar/cift_duyarlilik.csv`: her bir çift dışarıda bırakıldığında sonuçlar.
- `grafikler/b10-uyku-eslestirme.pdf`: eşli ölçümler ve farkların Q–Q grafiği.
- `grafikler/b10-welch-farklar.pdf`: doz 1 ham değerler, doz 1/2 fark aralıkları.

Bu çıktılar yeniden üretilir; iki ham CSV değiştirilmez. ZIP'te üretilmiş çıktılar
bulunmaz. `sleep.csv`, `ToothGrowth.csv`, `GPL-2.txt` ve kaynak açıklaması birlikte korunmalıdır.

## Üç farklı soru
| Soru | Birim ve yön | Ana sonuç |
|---|---|---|
| Koşul 1 kontrole göre ortalama artışı | 10 kişi; referans 0 saat | p=.217598 |
| İki koşulun kişi içi farkı | 10 tam çift; koşul 2−1 | fark 1.58 saat; p=.002833 |
| Doz 1'de uygulama farkı | 10 OJ + 10 VC; OJ−VC | Welch fark 5.93; p=.001038 |

Bütün testler iki yönlüdür; alfa .05, fark aralıkları %95'tir. Doz 2 ayrı etkinliktir,
modelin dış doğrulaması değildir. Doz 0.5 de hesaplanır; en küçük p seçilmez.
Aralıklar bireylerin %95'ini kapsayan aralıklar değildir. Etki katsayılarının
standartlaştırıcıları farklıdır; katsayılar için güven aralığı hesaplanmaz.
Farkların Shapiro p=.0333 bulgusu ve küçük örneklem sınırı gizlenmez.
Tarihsel veriyle öğretim yapılır; nedensellik, eşdeğerlik veya tedavi önerisi üretilmez.