# Bölüm 14 — Faktör Analizi

Bu bölümde **açımlayıcı faktör analizi (AFA)**, on A/C maddesinin ortak 97 tam kaydı üzerinden adım adım incelenir. Amaç yalnız bir faktör çözümü üretmek değil; **verinin faktör analizine uygunluğunu, faktör sayısı kararını, çıkarım ve rotasyon yöntemlerini, örüntü–yapı ayrımını, faktör korelasyonunu, ortak varyansı ve artık uyumunu birlikte değerlendirmeyi** öğrenmektir.

Bölüm bağımsız çalışır ve başka bölüm klasörlerine ihtiyaç duymaz.

**Önemli:** Bu analiz yeni bir Türkçe ölçek uyarlaması, bütün kişilik yapısının keşfi veya bağımsız doğrulayıcı faktör analizi değildir. Aynı küçük ve sıralı veri alıntısında keşfedilen yapının aynı veride yeniden uyarlanması bağımsız doğrulama sayılmaz.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- ortak tam kayıt örneklemini doğru oluşturabilir,
- ters puanlamanın korelasyon yapısındaki rolünü açıklayabilir,
- Pearson korelasyon matrisi ile analiz kapsamını tanımlayabilir,
- KMO ve madde MSA değerlerini yorumlayabilir,
- Bartlett küresellik testinin neyi gösterip neyi göstermediğini açıklayabilir,
- özdeğer >1 kuralını paralel analizle karşılaştırabilir,
- PCA ve SMC tabanlı referans spektrumlarını ayırabilir,
- temel eksenler faktörleştirmesini (PAF) açıklayabilir,
- eğik quartimin rotasyonunda örüntü ve yapı matrislerini ayırabilir,
- faktör korelasyonu `Phi`'yi yorumlayabilir,
- eğik çözümde ortak varyansı doğru hesaplayabilir,
- özgüllük, yeniden üretilen korelasyon ve artık matrislerini değerlendirebilir,
- RMSR'yi doğru payda ile hesaplayabilir,
- madde silme duyarlılığını ana model kararından ayırabilir,
- AFA sonucunu gelecekteki DFA için bir hipotez olarak konumlandırabilir,
- sonuçları akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` ile veri kaynağını, eksikleri ve puanlama anahtarını inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki D1–D3 sorularıyla analiz kararlarını açıklayın.
3. `calisma.ipynb` içindeki boş hesapları tamamlayın.
4. Pearson korelasyon matrisi, KMO/MSA ve Bartlett sonuçlarını inceleyin.
5. Özdeğer >1 kuralını PCA ve SMC paralel analiziyle karşılaştırın.
6. Bir, iki ve üç faktörlü PAF adaylarını değerlendirin.
7. İki faktörlü çözümü normalizasyonsuz quartimin ile döndürün.
8. Örüntü, yapı, `Phi`, ortak varyans, özgüllük ve artık matrislerini inceleyin.
9. A1/A4 çıkarma analizini yalnız duyarlılık çalışması olarak değerlendirin.
10. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
11. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla AFA bulgularını bilimsel rapor diline dönüştürün.

## Veri ve analiz örneklemi

Bölüm 13 arşivindeki `bfi-ilk100-AC.csv` dosyasının aynısı kullanılır. Yerel dosya, Rdatasets `psych/bfi` aktarımının ilk 100 veri satırından A1–A5 ve C1–C5 maddelerini içerir.

Üç farklı satırdaki eksikler nedeniyle on maddenin ortak tam kayıt örneklemi:

`n = 97`

olarak belirlenmiştir.

A1, C4 ve C5 belgelenmiş anahtara göre bir kez `7−x` ile ters puanlanır. Bölüm 13'te A için 99 ve C için 98 kayıttan elde edilen ayrı matrisler burada tek bir korelasyon matrisi oluşturmak üzere birleştirilmez. İkili silme veya eksik değer ataması yapılmaz.

İlk 100 kayıt rastgele veya temsili değildir. Sonuçlar hedef anakütleye genellenebilirlik onayı olarak yorumlanmamalıdır. [Kitap, Bölüm 14](../../KITAP_ESLESMESI.md)

## Faktör analizine uygunluk

Ortak 97 kaydın Pearson korelasyon matrisi üzerinden:

- KMO = `.726118`,
- yaklaşık Bartlett `χ²(45)=208.912`,
- `p≈5.81×10⁻²³`

elde edilir.

KMO ve Bartlett sonuçları korelasyon yapısının faktör analizi açısından incelenmesine yardımcı olur; ancak:

- doğru faktör sayısını,
- yeterli örneklem büyüklüğünü,
- kültürel geçerliği,
- Türkçe uyarlamayı,
- doğru ölçüm modelini

tek başına kanıtlamaz.

## Faktör sayısı kararı

PCA'nın ilk üç özdeğeri:

- `3.062119`,
- `1.657400`,
- `1.156765`

olduğundan yalnız Kaiser `>1` kuralı kullanılırsa üç bileşen önerilebilir.

Ancak 2000 bağımsız sütun permütasyonuna dayanan paralel analizde üçüncü boyut için:

- PCA gözlenen = `1.156765`,
- PCA %95 referans = `1.320067`,
- SMC gözlenen = `.356621`,
- SMC %95 referans = `.438259`.

Üçüncü gözlenen değer iki yaklaşımda da referansın altında kalır. İlk sıradan ardışık aşma kuralıyla **iki aday boyut** desteklenir.

Paralel analiz referans çizgisi gözlenen özdeğerin güven aralığı değildir. SMC başlangıç spektrumu da yakınsamış PAF faktör özdeğerleriyle aynı kavram değildir.

## PAF ve quartimin çözümü

Faktör çıkarımı, SMC başlangıç ortak varyanslarıyla **temel eksenler faktörleştirmesi (PAF)** kullanılarak yapılır. Bir, iki ve üç faktör adayları aynı 97 kişi üzerinde değerlendirilir.

İki faktörlü çözüm, Kaiser satır normalizasyonu olmadan **quartimin** eğik rotasyonuyla döndürülür.

Eğik çözümde:

- örüntü matrisi `L`,
- faktör korelasyon matrisi `Phi`,
- yapı matrisi `L @ Phi`,
- yeniden üretilen ortak korelasyon matrisi `L @ Phi @ L.T`

olarak ele alınır.

Faktör korelasyonu:

`Phi_AC = .216668`

olarak bulunmuştur. Bu nedenle örüntü ve yapı katsayılarının aynı olması beklenmez.

## Örüntü ve yapı ayrımı — A2 örneği

A2 için örüntü katsayıları yaklaşık:

`(.478526, .307147)`

şeklindedir.

C faktörü yapı katsayısı:

`.307147 + .478526 × .216668 = .410828`

olur.

Dolayısıyla `.410828` değeri A2'nin C faktöründeki örüntü çapraz yükü değildir; **yapı katsayısıdır**.

Eğik çözümde A2 ortak varyansı:

`h² = .387017`

ve özgüllüğü:

`u² = .612983`

olarak bulunur. Ortak varyans hesabında yalnız yüklerin karelerini toplamak faktör korelasyonundan gelen çapraz terimi kaybettirir.

## Açıklanan ortak varyans ve artıklar

İki PAF faktörünün ortak varyans oranı:

`.366554`

iken ilk iki PCA bileşeninin toplam özdeğer oranı:

`.471952`

olmaktadır. Bunlar aynı kavram değildir.

On madde için `10×9/2=45` benzersiz köşegen dışı korelasyon çifti vardır. İki faktörlü çözümde:

- RMSR = `.056761`,
- `|artık|>.05` olan çift sayısı = `12`,
- en büyük mutlak artık ≈ `.198783`.

RMSR hesabında köşegen veya simetrik matris kopyaları ikinci kez sayılmaz. Buradaki RMSR, DFA'daki SRMR veya RMSEA değildir.

## Alternatif faktör sayıları

Bir faktörlü çözüm:

- RMSR = `.121292`,
- en büyük |artık| = `.371746`,
- `.05`'i aşan 29 çift.

Üç faktörlü çözüm:

- RMSR = `.039941`,
- en büyük |artık| = `.111194`,
- `.05`'i aşan 8 çift.

Üç faktörlü modelin daha küçük artık üretmesi tek başına üçüncü faktörü doğrulamaz. Daha esnek modeller aynı veride daha iyi yeniden üretim gösterebilir; içerik, paralel analiz ve yeni veride kararlılık ayrıca değerlendirilmelidir.

Mevcut bir, iki ve üç faktör adaylarında Heywood durumu görülmemiş olması da doğru modelin kanıtı değildir.

## Madde duyarlılığı

A1 ve A4'ün çıkarılması yalnız **duyarlılık analizi** olarak yapılır; ana analizde maddeler silinmez.

Aynı 97 kişiyle sekiz maddelik iki faktörlü incelemede:

- RMSR = `.049025`,
- ortak varyans oranı = `.432950`,
- 28 benzersiz çiftin 7'sinde `|artık|>.05`.

Madde sayısı, içerik ve RMSR paydası değiştiğinden bu sonuç on maddelik modele karşı doğrudan “daha iyi model” testi değildir.

## Python ile çalıştırma

Depo kökünden:

```sh
python bolumler/b14/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

kullanabilirsiniz.

Kod ağa veya kitap klasörlerine ihtiyaç duymaz. Gerekli paketlerin doğrulama ortamındaki sürümleri `requirements.txt` dosyasındadır; betikler paket kurmaz.

## R ile çalıştırma

Önce Python ile puanlanmış CSV'yi üretin. Ardından depo kökünden:

```sh
Rscript bolumler/b14/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

R betiği hazırlanmıştır ancak bu dağıtım hazırlanırken çalıştırılarak doğrulanmamıştır. Temel R hesaplarına ek olarak yalnız sistemde zaten kuruluysa `GPArotation` ile quartimin çalışır; paket kurulmaz.

R ve Python'da faktörların sırası/işareti ve rastgele diziler farklı olabilir. Yöntem, veri matrisi ve rotasyon ayarları eşleştirilmeden yüklerin birebir aynı olması beklenmemelidir.

Bu öğrenci paketinde SPSS betiği veya doğrulanmış SPSS çıktısı yoktur. Python sonuçlarını R veya SPSS sonucu olarak sunmayın.

## Analizde inceleyeceğiniz temel kavramlar

- ortak tam kayıt,
- Pearson korelasyon matrisi,
- ters puanlama,
- KMO ve madde MSA,
- Bartlett küresellik testi,
- PCA özdeğerleri,
- SMC başlangıç ortak varyansları,
- paralel analiz,
- PAF,
- eğik quartimin rotasyonu,
- örüntü matrisi,
- yapı matrisi,
- faktör korelasyonu,
- ortak varyans ve özgüllük,
- yeniden üretilen korelasyonlar,
- artık matrisi,
- RMSR,
- Heywood durumu,
- madde duyarlılığı,
- AFA'dan DFA'ya geçiş.

## Üretilen dosyalar

`sonuclar/ozet.json` sayısal özetleri ve sürüm bilgilerini içerir.

Ayrıca şu CSV dosyaları üretilir:

- `puanlanmis.csv`,
- `korelasyon.csv`,
- `kismi_korelasyon.csv`,
- `oruntu.csv`,
- `yapi.csv`,
- `yeniden_uretilen.csv`,
- `artik.csv`,
- `faktor_korelasyon.csv`.

`puanlanmis.csv` dosyasında ters anahtar zaten uygulanmıştır; ikinci kez terslemeyin. Matris CSV'lerindeki ilk sütun satır etiketidir, yeni bir madde değildir.

`grafikler/` klasöründe:

- `b14-paralel-analiz.pdf`,
- `b14-oruntu-yapi.pdf`

oluşturulur.

Ham kaynak CSV değiştirilmez.

## Sonuçları yorumlarken dikkat

Özellikle şu hatalardan kaçının:

- KMO ve anlamlı Bartlett sonucunu geçerlik veya Türkçe uyarlama kanıtı saymayın.
- “Madde başına 10 kişi” gibi tek bir oranı evrensel örneklem yeterliği kuralı olarak kullanmayın.
- Özdeğer >1 kuralını tek faktör sayısı ölçütü yapmayın.
- Paralel analiz referans çizgisini güven aralığı olarak yorumlamayın.
- SMC başlangıç spektrumunu nihai PAF spektrumu olarak sunmayın.
- Eğik rotasyonda örüntü ve yapı katsayılarını birbirine karıştırmayın.
- Faktörler ilişkiliyken ortak varyansı yalnız yük karelerinin toplamıyla hesaplamayın.
- Varimax gibi farklı bir rotasyonun aynı çıkarılmış ortak matriste tek başına yeniden üretilen korelasyonları veya artıkları iyileştirdiğini söylemeyin.
- Küçük negatif çapraz yük nedeniyle maddeyi otomatik yeniden terslemeyin.
- Düşük ortak varyans veya yüksek artık nedeniyle maddeleri yalnız sayısal optimizasyon için otomatik silmeyin.
- Üç faktörün daha düşük RMSR vermesini üçüncü faktörün kesin kanıtı saymayın.
- Heywood görülmemesini doğru model kanıtı saymayın.
- Aynı veride yapılan gelecekteki DFA'yı bağımsız doğrulama olarak sunmayın.
- Bu pakette yapılmayan polikorik analiz, yük güven aralığı, bootstrap yük kararlılığı veya yeni veriyle DFA sonuçlarını rapora eklemeyin.

## Keşiften doğrulamaya

AFA'nın amacı yalnız “kaç faktör çıktı?” sorusunu yanıtlamak değildir. Bulgular, içerik bilgisiyle birlikte gelecekte sınanacak ölçüm modeline dönüştürülmelidir.

Bu bölümde iki faktörlü yapı **aday model** olarak ele alınır. A1/A4 ortak varyansları ve A2 çapraz örüntüsü içerik açısından ayrıca incelenmelidir. Gelecekteki DFA'da yük kısıtları ve veri toplama planı mümkün olduğunca yeni veriyi görmeden önce gerekçelendirilmelidir.

Aynı küçük sıralı veri setini ikiye bölmek veya aynı veride AFA sonrası DFA yapmak hedef anakütlede bağımsız doğrulama sağlamaz.

## Akademik raporlama

KMO/Bartlett, paralel analiz, PAF, quartimin, örüntü–yapı ayrımı, faktör korelasyonu ve artıkların bilimsel bir raporda nasıl sunulabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi bir AFA raporu yalnız faktör sayısını ve birkaç yüksek yükü vermez; **veri seçimini, eksik veri kuralını, korelasyon türünü, faktör sayısı kararını, çıkarım yöntemini, rotasyonu, tam örüntü/yapı ilişkisini, faktör korelasyonunu, artık uyumunu, alternatifleri ve doğrulama sınırlarını** açıkça belirtir.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Gerçekte hangi denetimlerin çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir.

Yerel hash ve kaynak dosyasının değişmediğinin denetlenmesi dosya bütünlüğünü destekler; uzak veri doğrulaması, örneklem temsiliyeti veya ölçüm modelinin dış doğrulaması anlamına gelmez.