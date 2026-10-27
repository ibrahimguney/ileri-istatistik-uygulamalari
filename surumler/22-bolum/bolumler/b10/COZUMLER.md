# Bölüm 10 — açıklamalı çözümler

Revizyon 13; yeni T1–T3 dahil.

## Kendinizi Sınayın

Genel olarak dağılımların konumu veya bir gözlemin diğerinden büyük olma olasılığı hakkında bilgi verir; ortalama veya medyan farkı hakkında ancak dağılımların biçimi ve yayılımı benzer olduğu (yalnız kaydığı) ek varsayımıyla yorumlanabilir. Bu nedenle “ortalamalar farklıdır” yerine sıralama/konum ifadesi kullanılır.

## Kolay Düzey

1.  İki bağımsız grubun sıra dağılımlarını karşılaştırır.

2.  Eşleştirilmiş iki ölçümde kullanılabilir; t-testi ortalama farkı, Wilcoxon ise simetrik fark dağılımının konumunu hedefler. Aynı hipotez değildir.

3.  Gruplar bağımsız olmalıdır; aynı bireyin tekrarlı ölçümleri bağımsız gruplarmış gibi birleştirilmez.

4.  Üç veya daha fazla bağımlı ölçümde kullanılır.

5.  Gözlenen ve beklenen frekansları karşılaştırır.

## Orta Düzey

1.  Sıra/konum sorusu için Kruskal–Wallis düşünülebilir; yalnız normal olmama bilgisi yeterli değildir. Ortalama farkı hedefleniyorsa Welch gibi seçenekler, bağımsızlık ve aykırı değerler değerlendirilir.

2.  Ham ölçümlerin normalliği değil fark dağılımı ve hedef önemlidir. Simetrik fark konumu için Wilcoxon düşünülebilir; ciddi asimetride uygun işaret testi veya başka model gerekir.

3.  $p<.05$ olduğundan kategorik değişkenler ilişkili görünür.

4.  Test sıra temellidir; doğrudan ortalama farkı dili her zaman doğru değildir.

5.  Uygun kesin test veya daha fazla veri düşünülür. Kategoriler yalnız içerikçe savunulabilen gerekçelerle birleştirilir; p küçültmek için sonuç sonrası yeniden kodlanmaz.

## İleri Düzey

1.  Hangi grupların farklı olduğu soruluyorsa ortak sıralara dayanan Dunn gibi bir yöntem ve tanımlı ailede Holm düzeltmesi kullanılabilir. Genel H, düzeltmesiz çift taramasına izin değildir.

2.  Küçük örneklem tek başına gerekçe değildir; veri yapısı da önemlidir.

3.  Blok yapısı korunarak tanımlı ailede düzeltilmiş eşleştirilmiş karşılaştırmalar yapılır. Wilcoxon seçilirse fark simetrisi ayrıca değerlendirilir; tüm çiftler, yönler ve Kendall W gibi açık tanımlı özetler verilir.

4.  Fark şekil/yayılım farkından da kaynaklanabilir.

5.  Test adı, n, istatistik, $p$, medyan/sıra, yön, post-hoc ve etki büyüklüğü verilmelidir.

## Gerçek Veri Etkinliklerinin Açıklamalı Yanıtları

Bu yanıtlar ortak sleep/ToothGrowth dosyaları ve R belgesinden aktarılan 22 satırlık RoundingTimes matrisi içindir. Kaynak belgesindeki 18 oyuncu yorumu ile 22 satırlık kod arasındaki uyuşmazlık giderilmiş gibi sunulmaz; özgün deney kayıtları ayrıca denetlenmemiştir.

## D: Veri Yapısını Okuma

1.  Diş verisinde OJ ve VC farklı hayvanlardır; sıra numarasına göre eşleştirme yapılamaz. Sleep’te aynı ID iki ilaç altında ölçülür; sıra değişse de ID ile eşleme korunur. Uyku verisini bağımsız iki grup saymak kişi içi bağımlılığı yok sayar.

2.  Satır bir blok, sütun bir koşuldur. 22 blokta üçer koşul değeri bulunur. Her hücre iki koşunun ortalamasıdır; bu ortalamayı iki kez kopyalamak gözlem sayısını yapay artırır. 66 ölçüm bağımsız 66 katılımcı değildir.

3.  Normallik testi araştırma hedefini belirlemez. Ortalama mı, simetrik fark konumu mu, medyan mı inceleniyor; gözlemler nasıl bağlı; farklar simetrik mi; sıfır ve bağlar nasıl işlenecek soruları gerekir. Küçük örneklemde normallik testinin güç sınırlılığı da önemlidir.

## G: Rehberli Hesaplar

1.  OJ için $U=143.5-55=88.5$; VC için $100-88.5=11.5$. İlk grup U’su ile küçük U farklı rapor kurallarıdır. 88 üstün ve bir eşit çift, $\widehat A=(88+.5)/100=.885$ ve $r_{rb}=.770$ verir. Tüm 184756 atamada iki yönlü $p=.00222997$; bağ ve süreklilik düzeltmeli yaklaşık $p=.00403037$’dir.

2.  Sıfır fark ID 5’tedir; `wilcox` kuralıyla sıralamaya girmez. İki 1.3 farkın sırası 4.5’tir. Pozitif sıralar toplamı 45, negatif toplam 0, küçük toplam T=0 olur. Dokuz sıfır olmayan farkın $2^9=512$ işaret örüntüsünden iki uç örüntü p’yi verir: .00390625. Sıfırın çıkarılması 10 çiftlik kaynak örneklemi 9 kişiymiş gibi raporlama gerekçesi değildir. Yaklaşık p=.00909070; yöntemler açıkça ayrılır.

3.  OJ ortak sıra toplamları 62.5, 174 ve 228.5’tir; toplamları $30(31)/2=465$ eder. Ham H=18.47677, bağ çarpanı C=.9984427, düzeltilmiş H=18.50559 ve $p=.0000958433$’tür. Küçükten büyüğe ham Dunn p’leri .0000244637, .00459247 ve .16593614; Holm değerleri .0000733912, .00918493 ve .16593614 olur. Her ham p’yi üçle çarpmak Bonferroni’dir; Holm sıralı çarpan ve birikimli maksimum kullanır. OJ 2–1 mg çifti için fark gösterilememiştir, eşdeğerlik kanıtlanmamıştır.

4.  Friedman $Q=11.142857$ ve $W=11.142857/(22\cdot2)=.253247$ verir. Yaklaşık ki-kare p=.00380504’tür. Monte Carlo hesabı $(311+1)/(99999+1)=.003120$, yaklaşık hesap standart hatası .000176’dır. Örüntü uzayı $6^{22}$ olup 99999 atama bunun rastgele bir bölümüdür. Aynı tohum ve aynı uygulama sonucu yeniden üretir; bu, hesabı kesin teste dönüştürmez.

## B: Bağımsız Uygulamalar

1.  VC’de doz sırasıyla sıra toplamları 55, 158 ve 252; ortalama sıralar 5.50, 15.80, 25.20’dir. Bağ çarpanı .9993326, ham H=25.05548, düzeltilmiş H=25.07222, $sd=2$ ve $p=.00000359449$ bulunur. Üç çift aynı Holm ailesindedir:

    <div class="center">

    | Çift  |     $z$ |     Ham $p$ |    Holm $p$ |
    |:------|--------:|------------:|------------:|
    | 1–0.5 | 2.61708 |   .00886866 |   .01773731 |
    | 2–0.5 | 5.00548 | .0000005572 | .0000016717 |
    | 2–1   | 2.38840 |   .01692193 |   .01773731 |

    </div>

    Üç çiftte de yüksek doz daha yüksek ortak sıra gösterir. Farklar ham uzunluk biriminde değildir. Son iki büyük ham p için aynı Holm değeri çıkması birikimli maksimum kuralındandır, kopyalama hatası değildir.

2.  Gözlenen tablo OJ için (11,19), VC için (20,10); her satırın beklentisi (15.5,14.5)’tir. Düzeltmesiz Pearson istatistiği 5.4060067, $sd=1$, $p=.02006757$ ve $V=\sqrt{5.4060067/60}=.3001668$ olur. Fisher’ın iki yönlü p’si .03788721’dir. Fisher koşullu hipergeometrik olasılıkları, Pearson asimptotik ki-kare yaklaşımını kullanır; eşit p beklenmez. 20 öğretim eşiğidir ve dozlar birleştirilmiştir; bulgu klinik başarı veya doza göre düzeltilmiş etki değildir.

3.  Örnek rapor: “R belgesinin 22 satırlık kod matrisi analiz edildi; açıklamadaki 18 oyuncu ifadesiyle uyuşmazlık kaynak sınırlılığıdır. Blok içi bağ-düzeltilmiş Friedman $Q(2)=11.143$, yaklaşık $p=.003805$, $W=.253$ verdi. Blok içi Monte Carlo p=.003120 bulundu. Üç eşleştirilmiş, normal yaklaşımlı Wilcoxon testine Holm uygulandı: Narrow–Round .448962, Wide–Round .037426, Wide–Narrow .005120. Wide için daha kısa süre eğilimi görüldü; ikili testlerin fark simetrisi varsayımı ayrıca gerekir.”

## H1: Hatalı Raporun Onarımı

1.  Parametrik olmayan testler bağımsızlık, blok veya fark simetrisi gibi koşullardan bağımsız değildir.

2.  U genel olarak yalnız medyanları sınamaz; benzer şekilli konum-kayması modeli olmadan doğrudan medyan farkı dili kullanılmaz.

3.  Bağlar ve sıfırlar kesin dağılımı değiştirir. Yazılımın bağsız “exact” seçeneği yerine uygun etiket/işaret sayımı gerekebilir.

4.  Sleep’te dokuz fark pozitiftir, biri sıfırdır. Katsayının 1 olması sıfır olmayan sıraların yönünü belirtir; herkeste artış veya büyük mutlak etki demek değildir.

5.  Friedman’da 22 blok vardır; üç bağlı koşul 66 bağımsız gözleme dönüştürülemez.

6.  Genel H’nin anlamlılığı izleme ailesinin hata oranını kendiliğinden kontrol etmez. Dunn–Holm gibi planlanmış yöntemle bütün çiftler raporlanır.

## T1–T3: Üstünlük ve Belirsizlik Denetimi

1.  $P(X>Y)=.4+.6(.4)=.64$ ve $P(X=Y)=.36$; $A=.64+.18=.82$. İki medyan0’dır. Ortak dağılım eşitliği A=.5’i gerektirir; tersi gerekmez. Medyan eşitliği de A=.5’i gerektirmez. Konum-kayması gibi ek koşullar olmadan hipotezler değiştirilmez.

2.  Aynı hayvan10 karşılaştırmada tekrar kullanılır; 100 kazanım bağımsız değildir. Her grupta hayvanlar yeniden örneklenir. Seed20261025, 20000 çekilişte yaklaşık percentile aralığı\[.690,1.000\], üst sınırdaki tekrar2415’tir. Bu, küçük örneklemde sınırlı ampirik desteği gösterir; evrende kusursuz ayrımı veya tam %95 kapsamayı kanıtlamaz. Bootstrap etiket permütasyonu değildir. BM p=.001059 da klasik tam U p=.002230 yerine en küçük p diye seçilmez; kalibrasyon/hedef koşulları ayrılır.

3.  Dokuz sıfır olmayan farkın hepsi pozitiftir; iki uç işaret örüntüsü iki yöntemde de aynı p’yi üretir. İşaret testi simetri istemez, sıfır dışlandığında koşullu işaret dengesini sınar. Sıra aralığına ise bütün10 fark girer: ikinci değer .8, dokuzuncu değer 2.4, medyan 1.3 saattir. Sürekli medyanda kapsama $1-2(11/1024)=.978515625$; ayrık veri için eşitlik otomatik değildir, tutucu kapsama olabilir. Bu, D’nin medyanıdır; $\operatorname{med}(Y_2)-\operatorname{med}(Y_1)$ genel olarak farklıdır.

## P1: Yeniden Üretim Kontrolü

Tam puan için 10 ID’nin doğru eşlenmesi, altı diş hücresinin 10’ar hayvan içermesi ve 22 satırlık blok matrisinin kaynağının açıklanması beklenir. Kaynak ve eşleme 20; bağ ve sıfırlar 20; kesin/yaklaşık yöntem 25; aile ve yorum 25; yeniden üretim 10 puandır.

OJ Dunn, VC Dunn ve Friedman izleme çiftleri ayrı öğretim aileleridir. Holm p değerleri Tukey ortalama aralıklarıyla birleştirilmez. Ana paket sıra-biserial, A, W ve V için nokta tahminleri verir. Revizyon13 eki yalnız bağımsız iki gruptaki A ve dönüşümü için yaklaşık percentile bootstrap, eşli fark medyanı için sıra-istatistiği aralığı ekler. W ve V için aralık yoktur; bütün ölçüler için aralık üretilmiş sayılmaz.

## Ç1 çıkış sorusunun yanıtı

Hayır. Hedefler dağılım ve model koşullarına bağlıdır; sıra testi otomatik olarak aynı ortalama veya medyan hipotezi değildir.
