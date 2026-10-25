# Bölüm 21 — Ölçüm modelinden yapısal modele

## Veri
Bölüm 18 betiğinin ürettiği `../b18-faktor-analizi/yarim_B.csv`: `psych::bfi`
verisinin on A/C maddesinde tam yanıtlı 2632 kişisinden tohum 20261001 ile
ayrılan ve AFA'da kullanılmayan yarım B (n=1316). Aynı kişiler Bölüm 19'daki
DFA'da kullanıldı; bu bölüm onların ölçüm modelinin üzerine yapısal kısım kurar,
yeni bir bağımsız doğrulama değildir.
Tanım: https://www.personality-project.org/r/html/bfi.html

A1/C4/C5 ters anahtarlanır (7-x). Kaynaktaki `gender` (1 erkek, 2 kadın) aracılık
örneği için K = 1 kadın / 0 erkek olarak kodlanır (891 kadın, 425 erkek).
Normalize SHA-256 (tek son LF):
`6b3a399dd3aea61ab94252d81660f2c759bbf17d6084204f66a66b25da43b989`.

## Çalıştırma
Kitap kökünden:
```sh
python uygulamalar/b18-faktor-analizi/analiz.py   # yarım B'yi üretir
python uygulamalar/b21-yapisal-esitlik/analiz.py  # ~1-2 dk (2000 bootstrap)
Rscript uygulamalar/b21-yapisal-esitlik/analiz.R
B17_BOOTSTRAP=1 Rscript uygulamalar/b21-yapisal-esitlik/analiz.R  # isteğe bağlı lavaan bootstrap
```
Python NumPy/SciPy/pandas/matplotlib kullanır. Betik küçük bir RAM motoru içerir:
`Sigma = F (I-A)^-1 S (I-A)^-T F'`; analitik türevler sayısal türevlerle
denetlenir. Genel amaçlı SEM kütüphanesi değildir. Bölüm 19 `analiz.py`
dosyası, SEM'in DFA M2 ile aynı kovaryansı verdiğini denetlemek için modül
olarak yüklenir. R/lavaan 0.6-17 aynı ki-kare, uyum, yol ve delta SE
değerlerini verir.

## Ölçüm modeli (Bölüm 19 M2)
A→A1 ve C→C1 marker yükleri 1; diğer sekiz yük, on gösterge hata varyansı ve
önceden yazılmış üç hata kovaryansı (A1–A2, C1–C2, C4–C5) serbest.

## Modeller
| Model | Yapısal kısım | q | sd | T | CFI | TLI | RMSEA [%90] | SRMR |
|---|---|---|---|---|---|---|---|---|
| İleri | C = gamma A + zeta_C | 24 | 31 | 180.541 | .944 | .918 | .061 [.052, .069] | .041 |
| Ters | A = delta C + zeta_A | 24 | 31 | 180.541 | .944 | .918 | .061 [.052, .069] | .041 |
| Sıfır yol | gamma = 0 | 23 | 32 | 269.146 | .911 | .875 | .075 [.067, .083] | .095 |
| Aracılık | A = a K; C = b A + c' K | 27 | 39 | 215.022 | .936 | .910 | .059 [.051, .066] | .042 |

İleri model: gamma=.628889 (SE .100355), Var(A)=.085234, psi=.226930,
Var(C)=.260640, standart yol=.359634 (= Bölüm 19 M2 phi), R²_C=.129336.
Ters model: delta=.205659; aynı Sigma. Sıfır-yol LR: Δchi²(1)=88.605.

Aracılık (ham ölçek; K 0/1, gizil değişkenler marker ölçeğinde):
a=.160953, b=.601265, c'=.012046, ab=.096775, toplam=.108822.
std.nox (gizil değişkenler standart, K ham): a=.530, b=.359, c'=.024,
ab=.190, toplam=.214. Delta SE: ab .017051 (ham), .030778 (std.nox).

Bootstrap: kişi (satır) yeniden örneklemesi, tohum 20261701, 2000 çekiliş, her
çekilişte maddeler yeniden standartlaştırılır ve bütün SEM yeniden kestirilir;
yakınsamayan çekiliş sayısı JSON'dadır (bu koşuda 0). Yüzdelik %95 aralıklar:
ab [.062, .141], std.nox ab [.125, .274], c' [-.063, .082]. Çekilişler
`sonuclar/bootstrap_cekilisler.csv` dosyasındadır.

## Tahmin ve belirsizlik sözleşmesi
Normal-kuram ML: F=logdet(Sigma)+tr(S Sigma^-1)-logdet(S)-p; Wishart (n-1)F;
S ddof=1; ortalama yapısı yok. Maddeler 1–6 kategorili; sürekli-normal
yaklaşım bir öğretim sınırlamasıdır. WLSMV, polikorik matris, FIML yoktur.
Varyanslar exp dönüşümündedir; sınır yakınlığı, rank eksikliği veya büyük
gradyan varsa betik durur. Beklenen bilgi I_ab=(n-1)/2 tr(Sigma^-1 D_a Sigma^-1 D_b);
türetilmiş büyüklükler için delta yöntemi. RMSEA n paydalı; SRMR köşegen dahil.
AIC_star=T+2q, BIC_star=T+q log(n) ortak sabiti çıkarılmış karşılaştırma sayılarıdır.

## Dosyalar
- `puanlanmis.csv`: anahtarlanmış yanıtlar + K; `standartlastirilmis.csv`: z-puanları + K.
- `sonuclar/ozet.json`: kaynak/sürüm, dört model, belirsizlik, LR, bootstrap ve denetimler.
- `sonuclar/*_kovaryans.csv`, `*_artik.csv`, `*_yukler.csv`, `*_parametreler.csv`, `uyum.csv`.
- `assets_figures/b16-yukler-artiklar.pdf`, `assets_figures/b16-dolayli-bootstrap.pdf`.
- `amos-kontrol-listesi.md`: AMOS kurulumu ve beklenen değerler.

Bu sonuçlar nedensellik kanıtı değildir: K rastgele atanmamıştır, A→C yönü
ters modelle aynı uyumu verir ve kesitsel veride zaman sırası yoktur.

## Yöntem belgeleri (6 Eylül 2026)
https://lavaan.ugent.be/tutorial/sem.html
https://lavaan.ugent.be/tutorial/est.html
https://lavaan.ugent.be/tutorial/mediation.html
