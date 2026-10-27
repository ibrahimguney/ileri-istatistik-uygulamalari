# Faktör sayısı ve puan belirsizliği — Revizyon 21

```bash
python dogrula.py
python analiz.py
```

Ana veri, bölme ve iki faktörlü PAF/quartimin sonuçları değişmez.
Ek yalnız önceden puanlanmış1316 keşif kaydını ve ana matrisleri kullanır.
Bölme dosyasındaki kimlikler ayrımı doğrular; yarım B yanıtları okunmaz.

## Dört faktörlü PAF doğrudan denemesi

Ana betiğin aynı SMC başlangıcı/toleransıyla dört faktör çağrılır.
2000 yinelemede yakınsamaz; en büyük ortak varyans1.669407,
son değişim normu.000128141. Negatif özgüllük/Heywood nedeniyle
yükleri kabul edilmiş model veya faktör puanı olarak sunulmaz.
Bu, bu yordam ve başlangıcın sonucudur; tüm dört faktörlü modelleri
reddetmez veya iki faktörü tek doğru saymaz. Başka başlangıç/kestirici,
ordinal yapı, içerik ve örnekleme kararlılığı ayrıca incelenmelidir.

## Aynı modelden farklı faktör puanları

Normal çalışma modeli z=Lambda*f+e, Cov(f)=Phi ve köşegen Psi ile:

- Rhat=Lambda*Phi*Lambda'+Psi
- Regresyon katsayısı B=Rhat^(-1)*Lambda*Phi; satır puanları z*B.
- Koşullu kovaryans C=Phi−Phi*Lambda'*Rhat^(-1)*Lambda*Phi.
- Modelde puan kovaryansı V=Phi−C; bu Phi değildir.
- Bartlett katsayısı Psi^(-1)*Lambda*(Lambda'*Psi^(-1)*Lambda)^(-1).

Faktör korelasyonu.317112; modelin öngördüğü puan korelasyonları
regresyonda.391331, Bartlett'te.238858'dir. Gözlenen A kayıtlarında sırasıyla
.391078 ve.238580 bulunur. Yöntem seçimi yeniden üretilen madde matrisini
değiştirmez; puanlar aynı gizil özelliğin kesin gözlemleri değildir.
Bu iki yöntem karşılaştırması faktör puanı belirlenimsizliğinin tüm boyutlarını kapsamaz.

Regresyon puanlarının faktörlerle model içi korelasyonları .881083/.869234;
koşullu standart sapmalar .472962/.494400 ve normal %95 yarı genişlikler
.926989/.969007'dir. Bunlar yükler/rotasyon/faktör sayısı sabit kabul edilen,
normal çalışma modeline ait hesaplardır. Parametre belirsizliği, model yanlışlığı,
ordinal yanıt yapısı veya yeni örneklemde kalibrasyon hesaba katılmadı.
Gizil faktörler gözlenmediğinden gerçek kişilerde puan-faktör korelasyonu ölçülmedi.
Bireysel tanı/sıralama veya doğrulanmış %95 kapsama iddiası yoktur.

Keşif yarısının ortalama/standart sapmaları ve iki puanlama katsayısı CSV'de
verilir. Yeni veriye uygulamada aynı madde sırası/anahtar, eğitim ortalamaları,
standart sapmalar ve katsayılar sabit tutulmalıdır; yeni veriye bakarak yeniden
standartlaştırma farklı puan kuralıdır. Bu ekte yarım B puanlanmadı.

Yedi test: tek faktör kapalı çözüm, posterior hassasiyet özdeşliği,
yeniden parametreleme, toplam varyans/hata, Bartlett koşullu yansızlığı,
puan korelasyonları ve uygunsuz/bilgisiz model sınırı.
Yeni ek yalnız Python; R/SPSS yeniden çalıştırılmadı.
