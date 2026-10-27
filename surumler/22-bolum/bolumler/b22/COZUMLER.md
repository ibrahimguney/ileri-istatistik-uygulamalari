# Bölüm 22 — açıklamalı çözümler

Revizyon 25 bütünlük düzeltmeleri.

## Kendinizi Sınayın

Filtre açık kalırsa sonraki bütün analizler yalnız seçili alt kümede yapılır; raporlanan n ve istatistikler bütün örneklem sanılır. Filtre durumu çıktıda kontrol edilmeli, analizden sonra kapatılmalı (FILTER OFF / USE ALL) ve her tabloda n açıkça doğrulanmalıdır.

## Kolay Düzey

1.  Dört başlık: kaynak/birim ve anahtar; sözlük/ölçüm/eksik/tersleme; etkin filtre/ağırlık/bölünme; modele özgü varsayımlar ve planlanan karşılaştırma. Aykırı görünen kayıt kaynağı incelenmeden silinmez. Bir normallik p’si bu kontrollerin tamamının yerine geçmez.

2.  `Analyze` $\rightarrow$ `Correlate` $\rightarrow$ `Bivariate`. Pearson/Spearman, yön, eksik kuralı ve kullanılan çift sayısı ayrıca belirlenir; yalnız menüye ulaşmak doğru analiz garantisi değildir.

3.  Levene, grup varyanslarının eşitliğiyle ilgili tanısal bilgi verir; bağımsızlık veya normallik testi değildir. Anlamsızlığı eşitliği kanıtlamaz. Bu bölümde Welch önceden ana modeldir; Levene p’sine göre otomatik Student/Welch geçişi yapılmaz.

4.  Hangi karşılaştırmaların araştırma sorusuna ait olduğu ve aile düzeltmesi incelenir. Planlı kontrast veya uygun çoklu karşılaştırmalar yorumlanabilir; bütün çiftleri gelişigüzel sınamak gerekmez. Etkileşimli tasarımda koşullu karşılaştırmalar gerekebilir.

5.  Belirli model ve kovaryat referansındaki ortalamaları gösterirler. Ham ortalama, grup farkı ve bireysel tahmin değildirler. Ortak destek, eğim/biçim ve karşılaştırma ailesi belirtilmeden “bütün farklar giderildi” denemez.

## Orta Düzey

1.  `Sig.` hangi tablo/hipoteze ait olduğu bilinmeden okunamaz. Kullanılan n, yön/birim, tahmin, SH, aralık, etki tanımı, varsayım ve kapsam eksik kalır. Uyku korelasyon p’si .005965, ortalama fark p’si .002833’tür; aynı soruyu sınamazlar.

2.  Eşit varyans varsayılan Student satırının gerekçesi zayıflar; bağımsız iki ortalama için Welch satırı değerlendirilir. Bu bölüm zaten Welch’i ana yöntem seçer. Levene anlamlılığı normallik veya bağımsızlık sorunlarını çözmez; daha küçük p veren satır seçilmez.

3.  KMO tek başına faktör sayısını, yük örüntüsünü veya kuramsal geçerliği belirlemez. Çıkarım yöntemi, döndürme, faktör sayısı gerekçesi, ortaklıklar, çapraz yükler ve artıklar raporlanır; PCA ile ortak faktör analizi ayrılır.

4.  Model F’si yordayıcıların ortak sıfır kısıtını, katsayı testi ise diğer değişkenler modeldeyken ilgili katsayıyı sınar. Ortak kanıt varken tekil katsayı belirsiz kalabilir; çoklu bağlantı ve aralıklar incelenir. Model F’sinin anlamlılığı her değişkenin nedensel etkili olduğunu göstermez.

5.  Doğru analiz sıfır hipotezini reddedemeyebilir. Tahmin/aralık, tasarım ve veri kalitesi raporlanır; sırf p büyük diye hata aramak veya anlamlılık elde edene kadar yöntem değiştirmek uygun değildir. Reddedememe eşdeğerlik kanıtı da değildir.

## İleri Düzey

1.  Ham tablolar gereksiz basamaklar, belirsiz kodlar ve farklı hipotezleri bir arada taşıyabilir. Akademik rapor hedefi, kullanılan n’yi, yöntemi, yön/birimi, belirsizliği ve sınırlılığı açıklar; teknik çıktı izlenebilir ek olarak korunabilir.

2.  Ölçüm anlamı uygun özet ve model seçiminin temelidir. `Scale` etiketi ordinal maddeyi aralık ölçeğine çevirmediği gibi sayısal ID de nicel yanıt olmaz. Saklama türü, ölçüm düzeyi ve model varsayımları ayrı değerlendirilir.

3.  Çoklu arama ve seçici raporlama nominal hata oranını bozabilir. Aile, yön, dışlama ve durdurma kuralları belirlenmeli; keşfedici değişiklikler açıkça yazılmalıdır. Yalnız son anlamlı tabloyu sunmak yürütme izini gizler.

4.  İçe aktarma, dönüşüm ve model ayarlarını kaydeder; aynı ham kaynaktan yeniden çalıştırılmasını sağlar. Ancak veri/sürüm, dosya yolu, etkin filtre/ağırlık, uyarılar ve gerçekten yürütülme kaydı olmadan yalnız sözdizimi yeterli değildir.

5.  Kaynak/tasarım, bağımsız birim/geçerli n, kodlama/yön, eksik/dışlama ve oturum ayarları, model/varsayımlar, tahmin/SH/sd/p/aralık, tanımlı etki büyüklüğü, duyarlılık/sınırlılık ve yazılım/sözdizimi/çıktı sürümü verilir. SPSS çalıştırılmadıysa Python sonucu SPSS sonucu diye yazılmaz.

## D1–D3: Çalıştırmadan Önce

1.  Her ID iki koşulda ölçülmüştür; 20 ölçümden 10 eşli fark oluşur. Kaynaktaki `group` koşul adıdır, bağımsız hasta grubu değildir. Bağımsız kişiler ve normal farklar burada çıkarımın model varsayımlarıdır; satır sayısı bu varsayımları kanıtlamaz.

2.  Filtreyi kapatmak yalnız filtreyle dışlanan kayıtları tekrar kullanılabilir yapar; silinmiş veya değiştirilmiş hücreleri onarmaz. Ham kaynaktan yeniden kurmak değişiklikleri geri alabilir. Gerçek örnekleme ağırlıkları hedefi temsil etmek için gerekli olabilir; keyfî kapatmak farklı hedef/yanlış belirsizlik üretir.

3.  Hayır. Komut dosyası yalnız planlanmış işlemleri gösterir. Yürütme için sürüm, çıktı ve uyarı/hata kaydı gerekir. Bu paketin doğrulayıcısı tanımlı arşiv şemasını denetler; bütün yeni veri sorunlarına karşı evrensel güvence sağlamaz.

## G1–G4: Rehberli Çözüm

1.  $SH=1.229995/\sqrt{10}=.388959$, $t=1.58/.388959=4.062128$, sd=9’dur. $1.58\pm2.262157(.388959)=[.700114,2.459886]$ saat, iki yönlü p=.002833 olur. Korelasyon tablosu $\rho=0$ hipotezini, eşli test $\mu_D=0$ hipotezini sınar. Aynı veride .005965 ile .002833 bu nedenle birbirinin yerine yazılamaz.

2.  İki grupta n=10 olduğunda Student ve Welch SH’si burada aynıdır: $\sqrt{15.295556/10+6.326778/10}=1.470453$. Fark 5.93, t=4.032770’tir. Welch sd=15.357672, p=.001038; Student sd=18, p=.000781 verir. Aralıklar sırasıyla \[2.802148,9.057852\] ve \[2.840692,9.019308\]’dir. Levene .149126 eşit varyansı kanıtlamaz; ana yöntem daha küçük p’ye göre seçilmez.

3.  İlk beş fark toplamı 6.2, ortalama 1.24; n=5, s=.850294, SH=.380263’tür. $t(4)=3.260900$, p=.031054 olur. Filtre kapanınca n=10 ve ana ortalama 1.58 döner. Veri ekranında 10 satırın bulunması, o prosedürün 10’unu kullandığını göstermez.

4.  Koşul1 ve koşul2’de ayrı ayrı 9 geçerli değer, ortak ID3–10 kümesinde 8 çift vardır. Kalan fark toplamı $15.8-1.2-2.4=12.2$, ortalama $12.2/8=1.525$ olur. $t(7)=3.192886$, p=.015215; GA \[.395598,2.654402\]’dir. Eski fark sütunu değiştirilmeden kullanılırsa hâlâ 10 fark içerir; bu yeni eksik kuralla çelişir. Gizleme gerçek kayıp değildir.

## B1–B3: Bağımsız Çözüm

1.  Ortalama $-1.58$, t=$-4.062128$; iki yönlü p=.002833 değişmez. Aralık uçları işaret değiştirip sıralanır: $[-2.459886,-.700114]$. Bu yeni etki veya bağımsız doğrulama değildir; referans yönü değişmiştir.

2.  On farkın kareli sapmalar toplamı 13.616’dır. İki kez saymada toplam 27.232, mekanik s=$\sqrt{27.232/19}=1.197190$, SH=$1.197190/\sqrt{20}=.267700$ olur. $t(19)=5.902135$, p yaklaşık .0000111 ve GA \[1.019698,2.140302\] çıkar. İki kopya bağımsız değildir; gerçek 10 kişinin bilgi miktarı artmamıştır. Bu geçerli yeni çıkarım değil, yanlış frekans ağırlığının karşı örneğidir.

3.  Önce aynı kayıt/eksik kümesi ve ağırlık/filtre/bölünme, sonra grup/çift yönü ile birim, ardından eşli-bağımsız ve Student-Welch seçimi karşılaştırılır. SH/sd, güven düzeyi, tek/iki yön ve aile düzeltmesi denetlenir. En son yuvarlama ve yazılım sürümü incelenir. Ortalama eşitliği aralık yönteminin de eşit olduğunu kanıtlamaz.

## H1: Hatalı Raporu Onarma

1.  Kaynak 20 bağımsız kişi değil 10 tam çifttir; kişi ID’si üzerinden eşli test gerekir. Bağımsız testin farklı p vermesi tasarımı değiştirme gerekçesi değildir.

2.  .005965 iki koşulun korelasyon testine aittir. Ortalama farkın iki yönlü p’si .002833’tür; doğru tablo/hipotez belirtilmelidir.

3.  Levene .149 eşitlik kanıtı değildir. Welch ana yöntem olarak korunur; Student’ın .000781 p’sini .001038’den küçük olduğu için seçmek sonuç odaklı yöntem seçimidir.

4.  Her çifte ağırlık 2 vermek yeni kişi yaratmaz. Mekanik ağırlıklı n ile bağımsız birim sayısı ayrılır; bu arşivde gereksiz ağırlık kapatılır.

5.  Değişen koşullardan fark yeniden hesaplanmalı ve 8 tam çift kullanılmalıdır. Eski fark, değiştirilmiş koşullar ve yanlış payda tek raporda birleştirilmez.

6.  Sözdizimi dosyasının varlığı yürütme kanıtı değildir. Gerçek SPSS sürümü ve çıktısı saklanmadan sayılar SPSS sonucu diye tanıtılmaz.

## P1: Denetlenebilir Analiz Teslimi

Örnek teslim uyku karşılaştırmasını seçer: kaynak ve aktarım notu; 20 ölçüm/10 kişi ayrımı; ID eşleme; geçerli sıfır/negatif ölçümler; filtre/ağırlık/bölünmenin kapalı olduğu ana sözleşme yazılır. Tam içe aktarma komutu ve iki yönlü eşli test saklanır. Koşul 2 eksi koşul 1 farkı, n=10, t(9)=4.062128, p=.002833 ve \[.700114,2.459886\] saat aralığı aynı modele bağlanır. Etki $d_z=1.284558$ ve standartlaştırıcısı belirtilir; etki aralığı hesaplanmadığı açık yazılır.

Küçük n, farkların biçimi, tarihsel tasarım bilgisi ve genelleme sınırları raporlanır. İlk beş filtre, sahte tekrar ağırlığı ve iki-hücre gizleme çıktıları ayrı karşı örneklerdir; yeni deney veya eksiklik çözümü sayılmaz. Kaynak dosya özeti, Python sürümleri ve üretilen CSV/JSON/PDF dosyaları saklanır. SPSS erişimi varsa ana sözdizimi gerçekten çalıştırılır; n/SH/sd/aralık ve uyarılar kontrol edilip SAV/SPV sürümlenir. Erişim yoksa “sözdizimi hazır, SPSS çalıştırılmadı” denir. Rubrik: kaynak/birim 20, içe aktarma/durum 25, model/hesap 25, yorum/sınırlılık 20, yeniden üretim 10 puan.

## T1–T3: Çıktı Sözleşmesi

1.  Model etiketi, iki grubun n’si, sd, SH ve aralık birlikte gerekir. Aynı fark/t, eş-varyans Student ile Welch’in aynı model olduğu anlamına gelmez. Eşli uyku satırı 10 kişi ve sd9 içindir; 20 bağımsız ölçüm değildir.

2.  .00051 mutlak tolerans üç ondalık gösterimin yuvarlama düzeyini denetler; varsayım, kaynak eşitliği veya gerçek SPSS yürütmesini kanıtlamaz. p=0 reddedilir; uygun üst sınır veya daha fazla basamak kullanılır. Kişi sayıları toleranssız eşleşir.

3.  Beklenen dosyanın kendisiyle eşleşmesi aynı hesabın iç kontrolüdür; SPSS çalıştırıldığına dair bağımsız kanıt değildir. Gerçek sürüm/lisans, tam komut, veri hash’i, Viewer/OMS dosyası, alan eşlemesi ve hata/uyarılar saklanır. Bu ortamda yalnız Python kontrolü ve hazır sözdizimi vardır; SPSS yürütülmüş gibi raporlanmaz.

## Ç1 çıkış sorusunun yanıtı

Hayır. Gerçek oturum, kullanılan veri/ayarlar ve üretilen çıktı kaydı gerekir; Python referansı SPSS yürütmesi değildir.
