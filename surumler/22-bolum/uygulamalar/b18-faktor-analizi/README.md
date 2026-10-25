# Bölüm 18 — Açıklayıcı faktör analizi (bfi, keşif yarısı)

Kitap kökünden:

    python uygulamalar/b18-faktor-analizi/analiz.py
    Rscript uygulamalar/b18-faktor-analizi/analiz.R

SPSS: `analiz.sps` (Python betiğinin ürettiği `puanlanmis.csv` dosyasını okur).

## Veri ve bölme

- `kaynak/bfi-AC-tam.csv`: R `psych` paketindeki `bfi` verisinin 2800 kaydı; kaynak
  sıra/kayıt numarası, cinsiyet, eğitim, yaş ve A1–A5, C1–C5 maddeleri. Değerler
  kurulu `psych::bfi` ile birebir aynıdır. Normalize LF SHA-256:
  `8e527ac51cf021d05693ede83d335542d7753e5da6e4271e039e88f593f45551`.
- On maddeye tam yanıt veren 2632 kişi (168 kişide en az bir eksik) tohum 20261001
  ile rastgele permüte edilir; ilk 1316 kayıt **yarım A** (keşif), kalan 1316 kayıt
  **yarım B** (doğrulama) olur. Bölme analizden önce yapılır.
- Betik şu dosyaları üretir: `bolme.csv` (kaynak satırı → yarım), `yarim_A.csv`,
  `yarim_B.csv` (ham yanıtlar) ve `puanlanmis.csv` (yarım A, A1/C4/C5 ters çevrilmiş).
- Bölüm 19 (DFA) ve 17 (YEM) yalnız `yarim_B.csv` dosyasını kullanır. Bu bölümde
  yarım B'ye bakılmaz.

## Analiz kararları

- Pearson korelasyonu; polikorik/ordinal model yok; eksik doldurma yok.
- KMO/MSA ve Bartlett; iki paralel analiz sürümü (PCA köşegen 1 ve SMC köşegen),
  2000 sütun içi permütasyon, tohum 20261401, %95 doğrusal yüzdelik.
- PAF (SMC başlangıcı, tolerans 1e-10, en çok 2000 yineleme); 1, 2 ve 3 faktör.
  Üç faktörlü çözüm yakınsamaz ve ortak varyans 1'i aşar (Heywood); betik bu durumu
  hata vermeden raporlar.
- İki faktörlü çözüm Kaiser normalizasyonu olmadan quartimin ile döndürülür.
  Örüntü, yapı, faktör korelasyonu, yeniden üretilen ve artık matrisleri CSV olarak
  kaydedilir.
- Duyarlılık: A1 ve A4 çıkarılarak aynı kişilerde 8 madde, 2 faktör.

## Denetimler

KMO'nun kısmi korelasyonları artık regresyonlarıyla, SMC değerleri ayrı
regresyonlarla, PAF ortak matrisi statsmodels ile, rotasyonun matris özdeşlikleri
ve amaç fonksiyonu ikinci bir algoritmayla denetlenir. R betiği aynı KMO, Bartlett,
PAF ve yakınsama sonuçlarını verir; paralel analiz yüzdelikleri farklı rastgele
sayı üreteci nedeniyle son basamaklarda ayrışabilir.

## Çıktılar

`sonuclar/ozet.json`, `sonuclar/*.csv`, `assets_figures/b14-paralel-analiz.pdf`,
`assets_figures/b14-oruntu-yapi.pdf`.

## Kaynaklar (erişim: 6 Eylül 2026)

- Revelle, W. `bfi` belgesi: https://www.personality-project.org/r/html/bfi.html
- https://personality-project.org/r/psych/help/fa.html
- https://personality-project.org/r/psych/help/fa.parallel.html
- https://www.statsmodels.org/stable/generated/statsmodels.multivariate.factor.Factor.html
- https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=reference-factor

## Faktör sayısı kararının kapsamı

Betik yalnız bir, iki ve üç faktörlü PAF çözümlerini dener. SMC paralel
analizinin dört boyut önermesi, dört faktörlü PAF modelinin kurulduğu
anlamına gelmez. Üç faktörlü denemenin uygunsuzluğu dört faktörlü
modeli reddetme kanıtı sayılmamalıdır. İki faktörlü çözüm içerik ve
yük/artık incelemesiyle izlenen bir adaydır.
