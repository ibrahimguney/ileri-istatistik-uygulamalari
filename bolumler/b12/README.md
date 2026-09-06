# Bölüm 12 — Parametrik Olmayan Testler

Mann–Whitney U, Wilcoxon, Kruskal–Wallis/Dunn–Holm, Friedman ve kategorik
sayım testleri için bağımsız öğrenci paketi. **Toplu aktarım için yerel hazırlık;
GitHub'da yayımlandığı iddia edilmez.** Kitap veya başka bölümün klasörü gerekmez.

## Çalışma sırası
1. `VERI.md` ve `veri_sozlugu.csv`: kaynak, analiz birimi, bağlar ve sıfırlar.
2. `GOREVLER.md`: kitaptaki D/G/B/H/P etkinlikleriyle uyumlu görevler.
3. `calisma.ipynb`: önce boş hesapları tamamlayın, sonra referans hücrelerini çalıştırın.
4. `COZUMLER.md` ve `beklenen.json`: gerekçeli yorum ve sayısal kontrol.
5. `DOGRULAMA.json`: yapılmış denetimler ve çalıştırılmamış yazılımlar.

## Çalıştırma
Python ve requirements.txt paketleri kuruluysa öğrenci deposu kökünden:

```sh
python bolumler/b12/analiz.py
```

Bölüm klasöründe `python analiz.py` de çalışır. Kod veri indirmez, paket kurmaz.
requirements.txt doğrulama ortamının sürümleridir. Notebook ayrıca Jupyter ortamı
ister. Tam U sayımı ve blok permütasyonları nedeniyle hesap anlık olmayabilir.

R kuruluysa `Rscript bolumler/b12/analiz.R`; etkileşimli R'de bölüm klasöründen
`source("analiz.R")`. **R bu ortamda çalıştırılmadı.** R betiği yaklaşık testleri,
Dunn–Holm'u ve uyku verisinin tam işaret sayımını içerir; U'nun tüm etiket
atamalarını ve Friedman Monte Carlo hesabını üretmez. SPSS komut dosyası bu
öğrenci paketinde yoktur; kitapta yöntem/menü açıklamaları vardır.

## Hangi p değeri?
| Analiz | Yöntem ve kapsam |
|---|---|
| U: doz 1, OJ−VC yönü | Süreklilik düzeltmeli normal yaklaşım ve 184756 etiket atamasının tam sayımı |
| Wilcoxon: uyku 2−1 | Bir sıfır için wilcox kuralı; kalan 9 farkın 512 işaret örüntüsü |
| OJ/VC Kruskal–Wallis | Bağ düzeltmeli H; her uygulama için ayrı üç çiftlik Dunn–Holm ailesi |
| Friedman | 22 tam blok; ki-kare yaklaşımı ve 99999 rastgele blok içi permütasyon |
| Friedman sonrası | Üç Wilcoxon normal yaklaşımı, süreklilik düzeltmesi ve ayrı Holm ailesi |
| Uzunluk ≥20 tablosu | Düzeltmesiz Pearson ki-kare ve iki yönlü Fisher karşılaştırması |

Friedman tohumu 202612; Monte Carlo p=(b+1)/(B+1), tam sayım değildir.
“Kesin” p varsayımsızlık anlamına gelmez. Bağ, sıfır, yön ve yaklaşım türünü yazın.
Etki büyüklükleri nokta tahminleridir; bu paket güven aralığı üretmez.

## Kaynak sınırı
sleep: 20 ölçüm, 10 kişi. ToothGrowth: 60 ayrı hayvan. RoundingTimes: yayımlanan
kod matrisinden 22 blok ve 66 değer. Yerel kaynak notunda R belgesinin açıklaması
18 oyuncu, kodu 22 satır olarak kaydedilmiştir; özgün deney sayısı burada doğrulanmaz.
Her RoundingTimes hücresi iki koşunun ortalamasıdır; kayıtlar çoğaltılmaz.
Öğretim eşiği len≥20 resmî/biyolojik başarı eşiği değildir. Dozların birleştirilmesi
doza göre düzeltme sağlamaz. Sonuçlar tedavi önerisi veya insanlara genelleme değildir.

## Çıktılar
`sonuclar/`: ozet.json, uyku_genis.csv, dis_analiz.csv, uyku_farklar.csv,
dunn_OJ.csv, dunn_VC.csv, friedman_ikili.csv.

`grafikler/`: b12-sira-ve-fark.pdf, b12-friedman.pdf.

Dunn karşılaştırma indeksleri 0/1/2 → 0.5/1/2 mg/gün;
Friedman indeksleri 0/1/2 → Round Out/Narrow Angle/Wide Angle.
Fark ve sıra farkı daima ikinci indeks eksi ilk indeks yönündedir.
Tablolardaki medyan fark, Wilcoxon'un test ettiği parametreyle koşulsuz eşitlenmez.
Üç ham CSV değiştirilmez. Çıktılar ZIP'te yoktur, yeniden üretilir.
Kaynak açıklaması ve GPL-2.txt veri dosyalarıyla birlikte korunmalıdır.