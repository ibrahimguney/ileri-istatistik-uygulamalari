# Bölüm 19 — Doğrulayıcı faktör analizi

## Veri ve doğrulama sınırı

Veri, Bölüm 18 betiğinin ürettiği `../b18-faktor-analizi/yarim_B.csv`
dosyasıdır: `psych::bfi` verisinin on A/C maddesinde tam yanıtlı 2632 kişi,
tohum 20261001 ile rastgele ikiye bölünmüş; bu dosya AFA'da **hiç kullanılmayan**
1316 kişilik yarım B'dir. A1/C4/C5 `7-x` ile çevrilir; eksik yoktur.
Yarım B'de kadın oranı %67.7, yaş ortalaması 28.5'tir.

Bu bir **örneklem içi çapraz geçerlemedir**: model yarım A'da bulunmuş, yarım
B'de sınanmıştır; ama iki yarı aynı çevrimiçi örneklemdendir. Başka bir
anakütlede kopyalama veya Türkçe uyarlama çalışması olarak gösterilemez.
Kaynak bilgisi Bölüm 18 README'sindedir.

Yarım B dosyasının tek son LF ile normalize SHA-256 değeri:
`6b3a399dd3aea61ab94252d81660f2c759bbf17d6084204f66a66b25da43b989`.
Değer tutmazsa betik durur; önce Bölüm 18 betiğini çalıştırın.

## Çalıştırma ve dosyalar

Kitap kökünde:

```sh
python uygulamalar/b18-faktor-analizi/analiz.py   # yarım B'yi üretir
python uygulamalar/b19-dogrulayici-faktor/analiz.py
Rscript uygulamalar/b19-dogrulayici-faktor/analiz.R
```

Python betiği kendi konumuna göre yolları kurar. numpy/pandas/scipy/matplotlib
yeterlidir; sürümler JSON'dadır.

- `puanlanmis.csv`: yarım B'nin 1316 kaydı, anahtarlanmış yanıtlar ve kaynak etiketleri.
- `sonuclar/orneklem_kovaryans.csv`: ddof=1 S (Pearson matrisine eşit).
- `sonuclar/ozet.json`: tanımlar, modeller, indeksler, yükler, aralıklar,
  M1 için değişiklik indeksleri (MI/EPC) ve denetimler.
- `sonuclar/*_model.csv`, `*_artik.csv`, `*_yukler.csv`: model kovaryansları,
  örneklem varyanslarıyla standartlaştırılmış artıklar ve madde sonuçları.
- Kitap `assets_figures/b15-yuk-araliklari.pdf`: M1 standart yük aralıkları.
- `analiz.R`: kurulu lavaan ile aynı üç modeli ve MI listesini üretir; paket kurmaz.
- `amos-kontrol-listesi.md`: AMOS'ta yapılacak kurulum ve denetimler.

R betiğinde çalışma dizini kitap kökü olmalıdır. R/lavaan 0.6-17 aynı ki-kare,
uyum indeksleri, standart yükler ve MI değerlerini verir. Tablolar AMOS çıktısı
değildir; AMOS için `amos-kontrol-listesi.md` kullanılır.

## Modeller ve hedef fonksiyon

Modeller yarım B açılmadan önce yazılmıştır (Bölüm 18, P1 yanıtı):

- M0: ilişkisiz iki faktör, 20 serbest parametre, sd=35.
- M1 (ana model): ilişkili iki faktör, basit yapı, 21 parametre, sd=34.
- M2 (önceden yazılmış alternatif): M1 + A1–A2, C1–C2, C4–C5 hata
  kovaryansları, 24 parametre, sd=31. Çiftler yarım A'nın AFA artıklarından ve
  madde içeriğinden (aynı kişiye yönelik ifade, benzer sözcük) seçilmiştir.

On artık varyansı serbest; gizil varyanslar 1. M0, CFI'nin bağımsız göstergeli
başlangıç modeliyle aynı değildir (başlangıç sd=45).

Yaklaşık sürekli maddeler üzerinde normal-kuram kovaryans ML öğretim hesabıdır:
`F = logdet(Sigma) + tr(S @ inv(Sigma)) - logdet(S) - p`.
S, örneklem standart sapmasıyla standartlaştırılmış maddelerin ddof=1 kovaryansıdır.
Wishart çarpanı `T=(n-1)*F`; ortalama yapısı yok. WLSMV, MLR, FIML, polikorik
korelasyon, ölçek eşikleri veya çok gruplu model uygulanmaz.

RMSEA, lavaan'ın n paydalı tanımıyla `sqrt(max((T-df)/(n*df),0))`;
%90 aralık merkezi olmayan ki-kare CDF'sinin .95/.05 için terslenmesidir.
SRMR örneklem varyansıyla standartlaştırılmış kovaryans artıklarının köşegen dahil
55 alt üçgen hücresinin kare ortalamasının kareköküdür. Köşegen dışı 45 çiftlik
RMSR ayrıca verilir. CFI/TLI normal kuramlıdır, sağlam düzeltme içermez.
`AIC_star=T+2*q`, `BIC_star=T+q*log(n)` ortak olabilirlik sabiti çıkarılmış
karşılaştırma ölçüleridir; AMOS/lavaan'ın tam AIC/BIC sayılarıyla eşit değildir.

Artık varyansları log-parametre, faktör ilişkisi tanh-parametre, M2'nin hata
kovaryansları doğrudan parametre olarak temsil edilir (sınır [-1,1]).
Sayısal arama sınırları yükler [-3,3], log varyanslar [-12,3], korelasyonun
dönüştürülmüş parametresi [-4,4]'tür. Sonuç herhangi bir sınıra yaklaşırsa betik
durur; pozitif varyans dönüşümünün uygunsuz/Heywood çözümü gizlemediği varsayılmaz.
Bu veride sınır sorunu yoktur. Genel SEM tahminleyicisi olarak kullanmayın.

## Belirsizlik ve denetimler

Dört başlangıç L-BFGS-B ile aynı amaç değerine gelir; BFGS ayrıca denetlenir.
Küçük gradyan, kovaryans eşitliği ve sınırdan uzaklık kontrol edilir. Analitik
amaç/kovaryans türevleri merkezi sonlu farklarla karşılaştırılır. F, genelleştirilmiş
özdeğerlerle bağımsız biçimde yeniden hesaplanır. Yerel kovaryans-Jacobian rankı
parametre sayısına eşittir. Bunlar küresel tek çözüm veya model doğruluğu ispatı değil.

Beklenen bilgi `(n-1)/2 * tr(Sigma^-1 D_a Sigma^-1 D_b)` formülündendir;
model kovaryansındaki sayısal Hessian ile ayrıca doğrulanır. Standart yüklerin
SE'leri delta yöntemidir; %95 Wald aralıkları eşzamanlı değil tekildir ve sağlam
değildir. Phi aralığı tanh-parametre ölçeğinden geri dönüştürülür. BFGS durumu
JSON'a kaydedilir; `success` tek başına değil gradyan/kovaryans denetimleriyle okunur.

Sonuçlar (yarım B, n=1316):

| Model | T | sd | CFI | TLI | RMSEA [%90 GA] | SRMR |
|---|---|---|---|---|---|---|
| M0 | 393.467 | 35 | .865 | .827 | .088 [.080, .096] | .099 |
| M1 | 306.990 | 34 | .897 | .864 | .078 [.070, .086] | .051 |
| M2 | 180.541 | 31 | .944 | .918 | .061 [.052, .069] | .041 |

M1'de phi=.340 [.272, .404]. M1'in en büyük dört MI değeri C4~~C5 (63.2),
C1~~C2 (60.3), A1~~A2 (42.0) ve A1~~C4 (37.4)'tür; ilk üçü önceden yazılmış
çiftlerdir. A4–C2 (.149) ve A4–C5 (.135) artıkları M2'de de kalır; bunlar önceden
yazılmadığı için modele eklenmez, raporda sınırlılık olarak yazılır.

MI, lavaan'daki gibi n çarpanıyla hesaplanan tek parametreli puan testidir; MI
listesi betimsel amaçla verilir, model değiştirme talimatı değildir.
AVE/CR M1 ve M2 için hesaplanır; M2'de CR paydasına kapsam içindeki hata
kovaryanslarının iki katı eklenir. CR model-standartlaştırılmış madde toplamı için
omega türündedir. CR/AVE aralıkları, bootstrap, sağlam/ordinal duyarlılık ve
başka anakütlede doğrulama yapılmamıştır; ölçme değişmezliği ayrı bölümde ele alınır.

## Yöntem kaynakları

Erişim 6 Eylül 2026; veri arşivi geçmişi 5 Eylül 2026.
- Rosseel (2012): https://doi.org/10.18637/jss.v048.i02
- https://lavaan.ugent.be/tutorial/est.html
- https://lavaan.ugent.be/tutorial/cfa.html
- https://lavaan.ugent.be/tutorial/cat.html
- https://lavaan.ugent.be/tutorial/cov.html
- https://lavaan.ugent.be/tutorial/modindices.html
- https://raw.githubusercontent.com/yrosseel/lavaan/master/R/lav_fit_rmsea.R
- https://raw.githubusercontent.com/yrosseel/lavaan/master/R/lav_fit_srmr.R
- https://search.r-project.org/CRAN/refmans/semTools/html/AVE.html
- https://search.r-project.org/CRAN/refmans/semTools/html/compRelSEM.html