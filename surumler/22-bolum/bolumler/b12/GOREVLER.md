# Bölüm 12 — görevler

Güncel Revizyon 15 görevleri; önce kendiniz çözün.

## Hesaplamadan Önce: Tahmin Et ve Gerekçelendir

1.  **\[Yöntem seç\]** Açıklanan ve açıklayıcı değişkeni belirleyin. Neden iki grup ortalaması karşılaştırması yerine basit regresyon düşünürsünüz? Bu tahmin hangi zamanda kullanılabilir?

2.  **\[Yorumla\]** Eğimin işaretini tahmin edin. Birinci dönem notu daha yüksek olan herkesin yıl sonu notunun da daha yüksek olması gerekir mi? Tablodaki kayıtlarla tartışın.

3.  **\[Eleştir\]** Önceki ve sonraki notların ilişkisini etkileyebilecek iki etmen önerin. Bu ilişki, birinci dönem notunu idari olarak yükseltmenin yıl sonu başarısını artıracağını gösterir mi? Neden?

Yanıtlarınızı yazdıktan sonra ilerleyin. Etkinliklerin gerekçeli yanıtları Ek F’dedir (s. kitaptaki ilgili sayfa).

# Rehberli ve Bağımsız Etkinlikler

## Rehberli Uygulama: Şimdi Siz Tamamlayın

Birinci dönem notu 12 olan bir öğrenci düşünün. Cevap anahtarını açmadan aşağıdaki adımları tamamlayın.

1.  **\[Hesapla ve yorumla\]** $\hat{y}_0=5.7412+0.5820(12)=\ldots$ bulunur. Kaynak sırası 3 olan öğrencinin yıl sonu notu 12’dir; artık $12-\hat{y}_0=\ldots$ olur. Nokta tahmini bu öğrencinin kesin notu mudur?

2.  **\[İleri: hesapla\]** $h_0=1/60+(12-12.1)^2/385.4=0.0166926$ veriliyor. $s_e=1.3368$ ve $t^*=2.0017$ ile ortalama yanıtın ve yeni bireyin klasik %95 aralıklarını hesaplayın. Bu aralıkların geçerliliğini hangi tanısal bulgular nedeniyle temkinli yorumlamalısınız?

3.  **\[İleri: yorumla\]** $x_0=\bar{x}$ ve $x_0=17$ için aralık genişliğini karşılaştırın. Ortalama tahmini nerede en hassastır? Not ölçeğinde mümkün olan 20, bu alt kümede gözlenmiş midir? Formüle yazılabilmesi güvenilir tahmin için yeterli midir?

## Bağımsız Uygulama: Sonraki 20 Gerçek Kayıt

`aktarim.csv`, aynı resmi kaynağın 61–80. sıralarındaki 20 gerçek kaydı içerir. Buradaki “bağımsız”, alıştırmayı yardım almadan çözmeyi belirtir; istatistiksel bağımsızlık veya dış doğrulama tasarımı iddiası değildir. Bu kayıtlar da GP okuluna aittir. Ana veriye eklemeyin ve iki ayrı örnekleme yapılmış gibi yorumlamayın.

1.  **\[Analiz et\]** Saçılım grafiğini çizip $G3\sim G1$ sabit terimli modelini kurun. $n$, $b_0$, $b_1$ ve $R^2$ değerlerini bulun; kodunuzu veya hesaplama yolunuzu ekleyin.

2.  **\[Hesapla\]** $G1=12$ için tahmini ve kaynak sırası 80 olan kaydın ($G3=11$) artığını hesaplayın. Yalnızca açıklayıcı notu 100’lük ölçeğe, $M=5G1$ biçiminde dönüştürün. Yanıt G3 hâlâ 20’lik ölçekte kalsın. Eğim, sabit, tahminler ve $R^2$ nasıl değişir?

3.  **\[Raporla\]** En fazla 100 sözcüklük sonuç yazın. İlk 60 ve sonraki 20 kaydın eğimleri farklıysa bu, iki öğrenci topluluğu arasında gerçek fark kanıtı mıdır? Seçim kuralını ve belirsizliği dikkate alarak açıklayın.

## Hatalı Raporu Düzeltme Atölyesi

**H1 \[Eleştir ve yeniden yaz\].** Aşağıdaki metin **kasıtlı olarak hatalıdır**. En az beş sorunu belirleyip gerekçeleriyle düzeltin.

> “Birinci dönem notunu bir puan artırmak her öğrencinin yıl sonu notunu kesinlikle 0.582 artırır. $R^2=0.557$, öğrencilerin yüzde 55.7’sinin başarılı olacağını gösterir. $p<.001$ olduğundan bütün varsayımlar sağlanmıştır. G1 notu 12 olan yeni öğrencinin yıl sonu notu yüzde 95 güvenle 12.38–13.07 arasındadır. Aynı model G1=20 için de aynı güvenilirliktedir. Bu bulgular Türkiye’deki bütün öğrenciler için geçerlidir. İlk kayıttaki sıfır notu hatadır; onu silerek daha doğru sonucu buluruz.”

Bir arkadaşınızın düzeltmesinde nedensellik dili, aralık türü, etkili gözlem kararı ve örnekleme sınırlarını kontrol edin. Kaynağa atıf verilmesi, bu hatalı yorumları geçerli kılmaz.

## T1–T3: Eğitim, Kalibrasyon ve Tahmin Denetimi

1.  Eğitim 1–40, kalibrasyon 41–60, kontrol 61–80 rollerini açıklayın. Kalibrasyondan sonra 60 kayıtta yeniden uyum veya kontrol yanıtlarına göre eşik seçimi neden aynı geçerli split conformal hesabı değildir?

2.  $m=20$, $\alpha=.05$ için k ve q’yu; $m=18$ için k’yi bulun. Sıradan enterpolasyonlu yüzdelik neden kullanılmaz? G1=12 için aralığı model ve q’dan hesaplayın.

3.  Son 20 kayıtta 18/20 kapsama ne söyler, ne söylemez? Marjinal, x’e koşullu ve eşzamanlı kapsama ayrımını yapın; HC3 eğim aralığı neden bunların yerine geçmez?

## Mini Proje: Yeniden Üretilebilir Analiz Raporu

**P1 \[Analiz et ve raporla\].** Ana senaryodaki veriyle 2–3 sayfalık bir analiz raporu hazırlayın. Raporunuza çalıştırılabilir kod veya SPSS sözdizimi ekleyin; yalnızca ekran görüntüsü teslim etmeyin.

1.  Araştırma sorusunu, değişkenleri, birimleri, UCI kaynağını ve ilk 60 kayıt seçim kuralını açıklayın. Atıf, bağımsızlık ve genelleme sınırlarını belirtin.

2.  Saçılım ve artık grafiklerini üretin. Modeli kurup katsayıları, eğim güven aralığını, $R^2$’yi ve artık standart sapmasını raporlayın. Gözlem sayısını ve yuvarlama tercihinizi yazın.

3.  G1=12 için klasik ortalama güven aralığını ve bireysel tahmin aralığını hesaplayın; öğretim elemanına hangi sorunun hangi aralıkla yanıtlandığını açıklayın.

4.  Etki duyarlılığı için her seferinde bir gözlemi dışarıda bırakarak 60 model kurun. Eğimlerin aralığını gösterin. Bir gözlemi silmeye karar vermek ile duyarlılığı araştırmak arasındaki farkı tartışın; gözlemleri yalnızca $p$-değerini küçültmek için çıkarmayın.

5.  Sonuç, sınırlılıklar ve yeniden üretim yönergeleri yazın. Analiz dosyaları, veri sözlüğü ve kullanılan yazılım sürümlerini teslim paketine ekleyin.

### İleri Rota: Açıklama ile Yeni Gözlem Tahminini Ayırma

Aynı veride modelin eğitim hatasını ve *birini dışarıda bırakmalı çapraz doğrulama* (LOOCV) hatasını karşılaştırın. Her döngüde bir kaydı ayırın, modeli kalan 59 kayıtla **yeniden kurun** ve ayrılan kaydın puanını tahmin edin. Sonra $$RMSE_{\text{eğitim}}=\sqrt{\frac{1}{n}\sum e_i^2},\qquad
RMSE_{\mathrm{LOOCV}}=\sqrt{\frac{1}{n}\sum(y_i-\hat{y}_{i,(-i)})^2}$$ hesaplayın. $\hat{y}_{i,(-i)}$, $i$. kayıt kullanılmadan kurulan modelin o kayıt için tahminidir. Eğitim RMSE’sindeki paydanın $n$, artık standart sapmasındaki paydanın $n-2$ olduğuna dikkat edin. Eğitimde açıklanan varyans ile ayrılmış bir gözleme ilişkin tahmin performansının aynı soru olmadığını tartışın. Sıralı tek okul alt kümesindeki çapraz doğrulama, yeni okullardaki veya daha sonraki yıllardaki başarıyı garanti etmez. İleri rotada klasik ve HC3 eğim standart hatalarını da karşılaştırın; HC3 hesaplamasının bireysel tahmin aralığını kendiliğinden düzeltmediğini açıklayın.

| Puan | Tam puan için beklenen kanıt                                                             |
|:-----|:-----------------------------------------------------------------------------------------|
| 15   | Soru, değişken rolleri, birimler ve gerçek veri kaynağı/seçim kuralı açık.               |
| 20   | Model, katsayılar ve temel hesaplamalar doğru ve izlenebilir.                            |
| 20   | Grafikler yorumlanmış; duyarlılık ve varsayım sınırları tartışılmış.                     |
| 15   | İki aralık doğru hesaplanmış ve doğru sorularla eşleştirilmiş.                           |
| 20   | Rapor bağlama uygun; nedensellik, başarı olasılığı ve genelleme hatalarından kaçınılmış. |
| 10   | Veri, kod, sürüm ve çalıştırma yönergeleriyle sonuç yeniden üretilebilir.                |

Mini proje değerlendirme ölçütleri: toplam 100 puan

Her ölçütte tam ve gerekçeli kanıt tam puan; kısmen doğru fakat eksik gerekçe yarım puan; yanlış veya sunulmamış kanıt sıfır puan olarak değerlendirilir. İleri rota uzantısı temel rota notuna ek zorunluluk getirmez; ileri rotada tanısal değerlendirme ölçütünün içinde ele alınır.

# Alıştırmalar

Bu alıştırmalar, basit doğrusal regresyonun katsayı yorumu, model uyumu, varsayım denetimi ve raporlama becerilerini pekiştirmek için üç düzeyde düzenlenmiştir. Yanıtlar ve kısa çözüm ipuçları Ek F’dedir.

## Kolay Düzey

1.  Basit regresyonda eğim katsayısı neyi ifade eder?

2.  $R^2$ değeri neyi gösterir?

3.  Basit regresyonda genel model anlamlılığı hangi testle değerlendirilebilir?

4.  Artık değeri nasıl tanımlanır?

5.  Basit regresyonda sabit terim ($b_0$) neyi ifade eder ve yorumu hangi koşulda anlamlıdır?

## Orta Düzey

1.  Basit regresyonda $R^2$ ile korelasyon katsayısı arasında nasıl bir ilişki vardır?

2.  Bir araştırmada çalışma süresi ($X$) ile sınav puanı ($Y$) arasındaki ilişki için şu regresyon denklemi elde edilmiştir: $\hat{Y}=40+3X$. Eğim ve sabit terimi açıklayınız.

3.  Bir regresyon analizinde $R^2=0.58$ bulunmuştur. Bu değeri açıklayınız.

4.  Bir regresyon modelinde artık grafiği huni biçiminde görünüyorsa hangi varsayım ihlalinden söz edilebileceğini belirtiniz.

5.  Bir veri setinde $\sum(x_i-\bar{x})(y_i-\bar{y})=30$, $\sum(x_i-\bar{x})^2=10$, $\bar{x}=4$ ve $\bar{y}=10$ verilmiştir. Eğim ve sabit terimi hesaplayınız.

## İleri Düzey

1.  $X$ değişkeninin 2–7 aralığında gözlendiği bir modelle $X=20$ için tahmin üretmek neden risklidir?

2.  $R^2$ oldukça yüksek olduğu hâlde artık grafiği belirgin eğrisel bir desen gösteriyorsa ne düşünülmelidir?

3.  Tek bir yüksek kaldıraçlı gözlemin eğim katsayısını ciddi biçimde değiştirdiği görülmüştür. Araştırmacı sonucu raporlamadan önce hangi adımları izlemelidir?

4.  Aynı $X$ düzeyi için ortalama yanıtın güven aralığı ile tek bir yeni gözlemin tahmin aralığından hangisi daha geniştir? Nedenini açıklayınız.

5.  Güçlü bir basit regresyon raporunda bulunması gereken en az beş unsuru yazınız.
