# Bölüm 16 — Yapısal Eşitlik Modeli (YEM/SEM)

Bu bölümde **yapısal eşitlik modeli (YEM/SEM)**, ölçüm modeli ile gizil değişkenler arasındaki yapısal ilişkinin aynı model içinde nasıl birleştirildiğini göstermek için kullanılır. Amaç yalnız bir yol katsayısı veya uyum indeksi üretmek değil; **ölçüm ve yapısal bileşenleri ayırmayı, ölçeklemeyi, gizil varyansları, yapısal artığı, standartlaştırılmış yolu, R²'yi, eşdeğer modelleri ve nedensel yön sınırlarını** birlikte değerlendirmeyi öğrenmektir.

**Önemli:** Bölüm 14–15 ile aynı 97 kayıt kullanılmaktadır. Bu nedenle burada elde edilen sonuçlar bağımsız SEM doğrulaması değildir. İleri ve ters modeller aynı gözlenen kovaryansı üretir; iyi uyum veya daha büyük bir ham yol katsayısı nedensel yönü belirlemez. fileciteturn46file0

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- ölçüm modeli ile yapısal modeli ayırabilir,
- gösterge hatası ile yapısal artığı ayırt edebilir,
- marker yüküyle gizil ölçeklemenin anlamını açıklayabilir,
- gözlenen kovaryans momentlerini ve serbest parametreleri sayabilir,
- ileri, ters ve sıfır-yol modellerini tanımlayabilir,
- ham ve standartlaştırılmış yapısal yolu ayırabilir,
- içsel gizil değişkenin toplam varyansını ve R²'sini hesaplayabilir,
- Wald ve olabilirlik-oranı (LR) sınamalarını ayrı raporlayabilir,
- eşdeğer kovaryans modellerinin nedensel yönü seçemeyeceğini açıklayabilir,
- ileri ve ters ham yolların büyüklüğünü doğrudan karşılaştırmaktan kaçınabilir,
- yapısal R² ile gösterge R²'sini ayırabilir,
- dönüştürülmüş beta/R² güven aralıklarını yorumlayabilir,
- kurgusal aracılık örneğini gerçek SEM sonucundan ayırabilir,
- sonuçları akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` ile veri ve ölçüm kararlarını inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki D1–D3 görevleriyle gösterge hatası, yapısal artık ve nedensellik sınırını açıklayın.
3. `calisma.ipynb` içindeki hesapları tamamlayın.
4. 55 gözlenen momenti ve model parametrelerini sayın.
5. İleri modelde `gamma`, `u`, `psi`, `Var(C)`, standart yol ve R² ilişkisini kurun.
6. Sıfır-yol LR sınamasını ve ham yol Wald sınamasını karşılaştırın.
7. İleri ve ters modellerin gözlenen kovaryans eşdeğerliğini inceleyin.
8. Marker yükü 1 ile standart yükün neden farklı olabileceğini açıklayın.
9. Kurgusal aracılık hesabını gerçek iki-faktörlü analizden ayırın.
10. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
11. [RAPORLAMA.md](RAPORLAMA.md) ile SEM sonuçlarını bilimsel rapor diline dönüştürün.

## Veri ve ön işlem

Bölüm 13'te korunan yerel ilk 100 A/C kaydı kullanılır. A1, C4 ve C5 belgelenmiş anahtara göre bir kez `7−x` ile ters puanlanır. C1/satır 63, A2/satır 66 ve C3/satır 90'daki eksikler nedeniyle ortak tam kayıt örneklemi:

`n = 97`

olur.

Ham arşivden kayıt silinmez; ilgili satırlar yalnız tam-kayıt analizine dahil edilmez. Atama, ikili silme veya eksiklik mekanizması testi yapılmaz.

Maddeler örneklem standart sapmasıyla (`ddof=1`) standartlaştırılır. Bu ilk 100 kayıt rastgele/temsili değildir ve Bölüm 14–15 ile aynı kişileri içerir.

## Ölçüm ve yapısal model

A ve C gizil yapılarının her biri beş göstergeyle temsil edilir.

- A1 ve C1 marker yükleri `1` olarak sabitlenir.
- Diğer sekiz faktör yükü serbesttir.
- On gösterge hata varyansı serbesttir.
- Çapraz yükler ve gösterge hata kovaryansları sıfıra sabitlenir.

İleri yapısal model:

`C = gamma A + zeta_C`

şeklindedir.

Burada:

- `gamma`: A'dan C'ye ham yapısal yol,
- `u = Var(A)`: dışsal A faktörünün varyansı,
- `psi = Var(zeta_C)`: C'nin yapısal artık varyansı.

C'nin toplam gizil varyansı:

`Var(C) = gamma²u + psi`

olur.

**Gösterge hatası**, tek bir maddenin ölçüm modelindeki özgül kısmıdır. **Yapısal artık** ise A tarafından açıklanmayan gizil C kısmıdır. Bunları birbirine karıştırmayın.

## Üç model

| Model | Yapısal denklem | Parametre | sd |
|---|---|---:|---:|
| forward | `C = gamma A + zeta_C` | 21 | 34 |
| reverse | `A = delta C + zeta_A` | 21 | 34 |
| zero | `gamma = 0` | 20 | 35 |

On gösterge için:

`10×11/2 = 55`

benzersiz kovaryans momenti vardır.

İleri modelde 21 serbest parametre:

- 8 serbest yük,
- 10 gösterge hata varyansı,
- 1 dışsal faktör varyansı,
- 1 yapısal artık varyansı,
- 1 yapısal yol

olarak sayılır.

Sıfır-yol modeli CFI'nin bağımsız göstergeli başlangıç modeli değildir.

## Tahmin yöntemi

Bu bölümde **normal-kuram kovaryans ML**, Wishart `(n−1)` çarpanı ve ortalama yapısı olmadan kullanılır.

Altı kategorili maddelerin yaklaşık sürekli kabul edilmesi bu öğretim örneğinin bir sınırlılığıdır.

Bu pakette uygulanmayan yöntemler:

- WLSMV,
- MLR/sağlam ML,
- polikorik korelasyon modeli,
- FIML,
- profil olabilirlik,
- bootstrap,
- ölçüm değişmezliği,
- yeni veriyle doğrulama.

Tam kayıt analizi FIML değildir.

## İleri modelin uyumu

İleri model için:

- `χ²(34)=45.138`,
- CFI = `.936`,
- RMSEA = `.058`,
- %90 RMSEA GA = `[0,.100]`,
- SRMR = `.078`.

Bu uyum değerleri Bölüm 15'teki ilişkili iki faktör DFA modelinin gözlenen kovaryans uyumuyla aynıdır. Bunun nedeni yapısal modelin aynı gizil kovaryans yapısını farklı bir parametreleştirmeyle ifade etmesidir.

İyi uyum, `A → C` yönünün nedensel olarak doğru olduğunu kanıtlamaz.

## Yapısal yol, toplam varyans ve R²

İleri modelde:

- `gamma = .739950`,
- `u = .092572`,
- `psi = .387938`.

Buna göre:

`Var(C) = gamma²u + psi = .438624`

olur.

Standartlaştırılmış yapısal yol:

`beta = gamma × sqrt(u / Var(C)) = .339936`

ve içsel C faktörü için:

`R² = gamma²u / Var(C) = .115556`

olarak bulunur. fileciteturn45file0

Dolayısıyla model içinde A, C'nin gizil varyansının yaklaşık `%11.6`'sıyla ilişkilidir/açıklanan payını temsil eder. Bu R², herhangi bir tek maddenin gösterge R²'si değildir.

## Yapısal artık toplam varyans değildir

`psi = .387938`, C'nin A tarafından açıklanmayan **yapısal artık varyansıdır**.

C'nin toplam varyansı ise:

`.438624`

olur.

Bu iki değer aynı değildir.

## Marker yükü 1, hatasız gösterge demek değildir

A1'in ham marker yükü `1` olarak sabitlenmiştir. Bu karar gizil A faktörünün ölçeğini tanımlar; A1'in hatasız olduğu anlamına gelmez.

A1 standartlaştırılmış yükü yaklaşık:

`.304257`

ve gösterge R²'si:

`.092572`

olduğundan A1'in önemli miktarda artık/hata varyansı bulunmaktadır.

## Wald ve LR sonuçlarını birlikte raporlayın

Ham `gamma` için normal-kuram Wald %95 güven aralığı:

`[-.045682, 1.525582]`

ve:

`p = .064892`

olarak bulunmuştur.

Buna karşılık sıfır-yol modeline karşı LR testi:

- `Δχ² = 6.114847`,
- `Δsd = 1`,
- `p = .013405`.

Bu iki yaklaşık sınama küçük örneklem, marker ölçeği ve parametrizasyon nedeniyle farklı sonuç verebilir.

**Daha küçük p değeri seçilip diğeri gizlenmemelidir.** İki sonuç yöntemleri belirtilerek birlikte raporlanmalıdır.

## Standart yol ve R² belirsizliği

Standart yolun dönüştürülmüş %95 aralığı:

`[.080523, .556219]`

olarak bulunmuştur.

Bu aralığın kare görüntüsünden R² için:

`[.006484, .309380]`

elde edilir.

Beta aralığı sıfırı kapsasaydı kare dönüşümündeki R² alt sınırı `0` olurdu.

CSV/JSON'daki simetrik Wald R² aralığının negatif alt ucu negatif R² nokta tahmini değildir; farklı bir yaklaşık aralık yönteminin sonucudur ve sessizce kesilmemelidir.

## İleri ve ters modellerin eşdeğerliği

İleri modelde:

`Cov(A,C) = gamma × u`

olur.

Aynı gizil kovaryans ters yönde yeniden parametreleştirildiğinde:

- `delta = .156168`,
- `psi_A = .081875`

elde edilir.

İleri, ters ve ilişkili DFA parametreleştirmeleri aynı gözlenen kovaryansı ve:

`χ²(34)=45.138`

uyumunu üretir.

Bu nedenle:

- daha küçük ham `delta`, daha kötü uyum demek değildir;
- eşit uyum geri besleme kanıtı değildir;
- ileri ve ters model arasında `Δsd=0` üzerinden yön seçen bir fark testi p değeri üretilmez;
- kesitsel kovaryans yapısı tek başına nedensel yönü belirlemez.

## Nedensel yorum sınırı

`A → C` oku, model içinde C'nin A'ya koşullu yapısal regresyonunu ifade eder. Okun çizilmiş olması:

- zaman sırasını,
- müdahale etkisini,
- karıştırıcıların kontrol edildiğini,
- nedensel yönün kanıtlandığını

göstermez.

Nedensel yorum için araştırma tasarımı, zamanlama, kuram ve alternatif açıklamalar ayrıca gereklidir.

## Sayısal denetimler

Kod çözümün sayısal davranışını ayrıca denetler:

- üç başlangıç,
- L-BFGS-B,
- ek BFGS karşılaştırması,
- gradyan büyüklüğü,
- amaç fonksiyonu,
- model kovaryansı,
- parametre sınırları,
- yerel rank,
- türevlerin sonlu fark karşılaştırması.

Varyansların `exp` dönüşümü pozitifliği destekler; fakat bütün Heywood, tanımlanabilirlik veya yakınsama sorunlarını otomatik olarak çözmez.

Sayısal başlangıç tohumu `20260906`, yeni katılımcı veya bootstrap örneklemi üretmez.

## Yerel DFA yardımcısı

`dfa_referans.py`, Bölüm 15 Python hesap fonksiyonlarının yerel bir kopyasıdır. Birim-varyans DFA çözümünü marker ölçeğine dönüştürmek, eşdeğer kovaryansı ve RMSEA aralığını denetlemek için kullanılır.

Bu dosya:

- ikinci bir veri seti değildir,
- Bölüm 15'i çalıştırmaz,
- bağımsız yazılım doğrulaması değildir,
- genel amaçlı SEM tahminleyicisi değildir.

## Kurgusal aracılık örneği

Gerçek A/C analizinde **aracı değişken yoktur**.

Yalnız cebir öğretimi için:

- `a=.48`,
- `b=.41`,
- `c′=.19`

kurgusal değerleri verilir.

Dolaylı etki:

`ab = .48×.41 = .1968`

ve toplam etki:

`c′ + ab = .3868`

olur.

Bu sayılar BFI verisinden tahmin edilmemiştir. Veri/örnekleme modeli olmadan bunlardan p değeri veya bootstrap güven aralığı üretilemez. “5000 bootstrap yapıldı” gibi bir ifade kesinlikle kullanılmamalıdır.

## Python ile çalıştırma

Depo kökünden:

```sh
python bolumler/b16/analiz.py
```

Bölüm klasöründen:

```sh
python analiz.py
```

kullanabilirsiniz.

Kod kitap klasörlerine veya ağa ihtiyaç duymaz. `requirements.txt` doğrulama ortamındaki sürümleri listeler; betikler paket kurmaz.

## R/lavaan ile çalışma

Önce Python çıktılarını üretin. Ardından depo kökünden:

```sh
Rscript bolumler/b16/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

R betiği sistemde kurulu `lavaan` paketini gerektirir; yoksa durur ve kurulum yapmaz. Çalıştırılırsa `sonuclar_R/` klasörünü üretmek üzere hazırlanmıştır.

**Bu dağıtım hazırlanırken R/lavaan çalıştırılarak doğrulanmamıştır.**

## AMOS yolu

`amos-kontrol-listesi.md`, modeli AMOS'ta kurmak için hazırlanmış bir uygulama/kontrol listesidir; **AMOS çıktısı değildir**.

Python sonuçlarını AMOS veya lavaan tarafından doğrulanmış gibi sunmayın. Bu pakette yeni `.amw` veya `.sav` dosyası üretilmemiştir.

## Üretilen dosyalar

`sonuclar/ozet.json`, kaynak/sürüm bilgilerini, üç modeli, yapısal yol ve varyans belirsizliğini, LR sonuçlarını ve eşdeğerlik denetimlerini içerir.

Ayrıca on dört CSV üretilir:

- `puanlanmis.csv`,
- `standartlastirilmis.csv`,
- `orneklem_kovaryans.csv`,
- her model için `_kovaryans`, `_artik`, `_yukler`,
- `uyum.csv`,
- `yapisal_parametreler.csv`.

`grafikler/b16-yukler-artiklar.pdf`, ileri modelin standartlaştırılmış yüklerini ve artık ısı haritasını gösterir. Isı haritasının renk ölçeği `±.2` ile sınırlıdır; uç artıkların gerçek büyüklükleri CSV'den okunmalıdır.

Ham kaynak dosyası değiştirilmez.

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- Aynı 97 kaydı bağımsız SEM doğrulaması olarak sunmayın.
- Marker yükü `1` olan göstergeyi hatasız saymayın.
- Gösterge hata varyansı ile yapısal artık varyansını karıştırmayın.
- Yapısal artığı içsel faktörün toplam varyansı olarak sunmayın.
- Yapısal R²'yi madde R²'si olarak yorumlamayın.
- İyi CFI/RMSEA'yı nedensel yön kanıtı saymayın.
- İleri ve ters modellerin eşit uyumunu geri besleme kanıtı olarak yorumlamayın.
- Ham `gamma` ile ham `delta` büyüklüklerini yön seçmek için karşılaştırmayın.
- İleri–ters modeller için `sd=0` farkından p değeri üretmeyin.
- Wald ve LR sonuçlarından yalnız küçük p'yi seçmeyin.
- Pozitiflik dönüşümünü bütün Heywood sorunlarını çözen yöntem olarak sunmayın.
- Tam kayıt analizini FIML olarak adlandırmayın.
- Normal-kuram ML sonucunu WLSMV/MLR sonucu gibi sunmayın.
- Kurgusal aracılık katsayılarını gerçek BFI sonucu saymayın.
- Kurgusal `ab=.1968` değerine veri olmadan p veya bootstrap aralığı uydurmayın.
- Python sonuçlarını lavaan veya AMOS çıktısı olarak göstermeyin.

## Yeni araştırmada denetlenebilir SEM protokolü

Yeni bir SEM çalışmasında sonuçlar görülmeden önce mümkün olduğunca şu kararlar yazılmalıdır:

1. kuramsal yapılar ve göstergeleri,
2. ölçüm zamanları,
3. veri türü ve ölçek düzeyi,
4. faktör ölçekleme yöntemi,
5. sıfır/eşitlik kısıtları,
6. tanımlanabilirlik değerlendirmesi,
7. tahminleyici,
8. eksik veri yaklaşımı,
9. örneklem planı,
10. uyum ölçütleri,
11. yol ve belirsizlik raporlama planı,
12. alternatif/eşdeğer modeller,
13. modifikasyon sınırları,
14. bağımsız doğrulama planı.

Aracılık gerçekten araştırma sorusuysa aracı yapının ölçüm modeli, zaman sırası, dolaylı etki tanımı, bootstrap birimi ve başarısız çözüm kuralı ayrıca önceden belirtilmelidir.

## Akademik raporlama

SEM sonuçlarının yöntem ve bulgu bölümünde nasıl raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi bir SEM raporu yalnız yol katsayılarını ve CFI/RMSEA değerlerini sıralamaz. **Ölçüm modelini, yapısal denklemi, ölçeklemeyi, tahmin yöntemini, toplam ve artık varyansları, standartlaştırılmış yolu, R²'yi, belirsizliği, eşdeğer modelleri, nedensellik sınırını ve gerçekten yapılmayan analizleri** açıkça belirtir.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Gerçekte hangi denetimlerin ve yazılımların çalıştırıldığı `DOGRULAMA.json` dosyasında belirtilmiştir.

Yerel hash, optimizasyon ve eşdeğer kovaryans denetimleri yeniden üretilebilirliği destekler; uzak kaynak doğrulaması, örneklem temsiliyeti, nedensellik veya bağımsız SEM doğrulaması anlamına gelmez.