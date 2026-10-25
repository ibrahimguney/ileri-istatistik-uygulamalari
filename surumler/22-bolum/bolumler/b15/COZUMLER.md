# Bölüm 15 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

İlki aracılık modelidir: M, X’ten etkilenir ve Y’yi etkiler; X’in etkisinin bir kısmı M üzerinden geçer (dolaylı etki $ab$). İkincisi düzenleyicilik modelidir: W, X’in Y üzerindeki etkisinin büyüklüğünü değiştirir; model X$\times$W etkileşim terimini içerir.

## D1–D3: Modelden Önce

1.  Aracılık zamansal bir mekanizma iddiasıdır: $X$ $M$’yi, $M$ de $Y$’yi değiştirir. $M$ aynı anda ya da $Y$’den sonra ölçülürse yön verilerle savunulamaz; kesitsel veride yalnız bir model uyumu sınanır.

2.  Hayır, iki cümle farklı sorulardır. “Değiştirir” düzenleyiciliktir ($Y\sim X+W+XW$); “açıklar” aracılıktır ($W\sim X$ ve $Y\sim X+W$). Aynı değişken kuramsal gerekçe olmadan iki role birden konamaz.

3.  İki normal yaklaşık katsayının çarpımı çarpık dağılır; özellikle katsayılardan biri sıfıra yakınken simetrik aralık (Sobel) yanıltıcı olabilir.

## G1–G3: Rehberli Çözüm

1.  $0.1353+0.6333\times0.8240=0.6571=c$. Lojistik regresyonda gizil ölçek her modelde yeniden ölçeklenir; katsayılar farklı modeller arasında doğrudan toplanamaz.

2.  Sınırlar genellikle ikinci ondalıkta değişir. Bu, sonlu tekrar sayısından gelen Monte Carlo hatasıdır; örneklem belirsizliği aynı kalır. Rapor tekrar sayısını ve tohumu belirtir.

3.  $d=1.0374$: eğim $0.3985+1.0374\times0.5590=0.978$; standart hata $$\sqrt{V(b_1)+d^2V(b_3)+2d\,\mathrm{Kov}(b_1,b_3)}=0.104$$ olur ve Tablo (kitaptaki ilgili başvuru) ile aynıdır.

## B1–B2: Bağımsız Çözüm

1.  Ters model de sıfırdan farklı bir çarpım verebilir; çünkü üç değişken birbiriyle ilişkilidir. Dolaylı etki kestirimi yönü sınamaz; yön tasarımdan (zaman sırası, deneysel müdahale) gelir.

2.  İkiye bölme bilgi kaybettirir: etkileşim katsayısı artık iki grup arasındaki eğim farkıdır, standart hatası genellikle büyür ve bölme noktası keyfîdir. Sürekli $W$ ile basit eğim veya Johnson–Neyman tercih edilir.

## H1: Hatalı Raporu Onarma

\(1\) $c'$ aralığı sıfırı içerir ama sıfır olduğu gösterilmemiştir; üretimde $c'=.2$’dir. “Tam aracılık” etiketi yerine büyüklük ve aralık raporlanır. (2) Tek aracı modeli başka aracıları dışlamaz; “tek neden” iddiası verilerle desteklenmez. (3) Düşük $W$’de basit eğim $-0.18$, aralığı $[-0.40, 0.04]$’tür; X her W düzeyinde Y’yi artırmaz. Anlamlı etkileşim yalnız eğimlerin farklı olduğunu gösterir.

## Kolay Düzey

1.  X’in Y üzerindeki etkisinin geçtiği mekanizmayı temsil eden değişkendir.

2.  X-Y ilişkisinin gücünü veya yönünü değiştiren koşul değişkenidir.

3.  $a\times b$ çarpımıyla ifade edilir.

4.  X’in etkisinin W düzeylerine göre değişip değişmediğini test etmek için eklenir.

5.  Dolaylı etkinin istatistiksel olarak desteklendiği yorumu yapılır.

## Orta Düzey

1.  Aracılık “neden/nasıl”, düzenleyicilik “ne zaman/kimler için” sorusuna yanıt verir.

2.  Tam aracılıkta doğrudan etki kaybolur; kısmi aracılıkta dolaylı etkiyle birlikte doğrudan etki de sürer.

3.  Etkileşim anlamlı olduğunda ilişkinin düzenleyici düzeylerinde nasıl değiştiğini görmek için gerekir.

4.  Zaman sırası belirsiz olduğundan güçlü nedensel mekanizma iddiası sınırlıdır.

5.  Ana etkilerin ortalama düzeyde yorumlanmasını kolaylaştırır.

## İleri Düzey

1.  Aracı değişkenin sonuçtan önce gelmesi gerekir; aksi hâlde mekanizma yönü savunulamaz.

2.  Örneğin öğretim desteğinin başarıya etkisi motivasyon üzerinden yalnız düşük kaygılı öğrencilerde güçlenebilir.

3.  Bootstrap dolaylı etkinin normal olmayan dağılımına daha dayanıklıdır; Sobel testi normal yaklaşım varsayımına daha duyarlıdır.

4.  Grafik etkinin yönünü ve büyüklüğünü görünür kılar; test yalnız etkileşimin varlığına ilişkin kanıt sunar.

5.  Rapor dolaylı/etkileşim katsayısı, bootstrap güven aralığı, basit eğimler ve kuramsal yorum içermelidir.
