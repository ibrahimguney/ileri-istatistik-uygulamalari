# Bölüm 15 — açıklamalı çözümler

Revizyon 18; yeni T1–T3 dahil.

## Kendinizi Sınayın

İlki aracılık modelidir: M, X’ten etkilenir ve Y’yi etkiler; X’in etkisinin bir kısmı M üzerinden geçer (dolaylı etki $ab$). İkincisi düzenleyicilik modelidir: W, X’in Y üzerindeki etkisinin büyüklüğünü değiştirir; model X$\times$W etkileşim terimini içerir.

## D1–D3: Modelden Önce

1.  Aracılık zamansal bir mekanizma iddiasıdır: $X$ $M$’yi, $M$ de $Y$’yi değiştirir. $M$ aynı anda ya da $Y$’den sonra ölçülürse yön verilerle savunulamaz; kesitsel veride yalnız bir model uyumu sınanır.

2.  Hayır, iki cümle farklı sorulardır. “Değiştirir” düzenleyiciliktir ($Y\sim X+W+XW$); “açıklar” aracılıktır ($W\sim X$ ve $Y\sim X+W$). Aynı değişken kuramsal gerekçe olmadan iki role birden konamaz.

3.  İki yaklaşık normal katsayının çarpımı genel olarak normal/simetrik değildir; özellikle katsayılardan biri sıfıra yakınken simetrik aralık (Sobel) yanıltıcı olabilir.

## G1–G3: Rehberli Çözüm

1.  $0.1353+0.6333\times0.8240=0.6571=c$. Lojistik regresyonda gizil ölçek her modelde yeniden ölçeklenir; katsayılar farklı modeller arasında doğrudan toplanamaz.

2.  Sabit tohumla ilk 1000 tekrar farklı ampirik yüzdelikler verebilir; değişimin kaçıncı ondalıkta olacağı garanti değildir. Bu, sonlu tekrar sayısından gelen Monte Carlo hesap farkıdır; yeniden örneklenen asıl veri aynı kalır. Rapor tekrar sayısını ve tohumu belirtir.

3.  $d=1.0374$: eğim $0.3985+1.0374\times0.5590=0.978$; standart hata $$\sqrt{V(b_1)+d^2V(b_3)+2d\,\mathrm{Kov}(b_1,b_3)}=0.104$$ olur ve Tablo kitaptaki ilgili tablo ile aynıdır.

## B1–B2: Bağımsız Çözüm

1.  Ters model de sıfırdan farklı bir çarpım verebilir; çünkü üç değişken birbiriyle ilişkilidir. Dolaylı yol kestirimi yönü sınamaz; yön tasarım, kuram ve nedensel tanımlama varsayımlarıyla gerekçelendirilir. Zaman sırası veya X’in rastgele atanması tek başına yeterli değildir.

2.  İkiye bölme bilgi kaybettirir: etkileşim katsayısı artık iki grup arasındaki eğim farkıdır, yeni katsayının birimi/hedefi değiştiği için standart hatanın sayısal büyüklüğü doğrudan karşılaştırılmaz. Bölme noktası keyfî olabilir ve çözünürlük kaybı vardır. Sürekli $W$ ile basit eğim veya Johnson–Neyman tercih edilir.

## T1–T3: Tanımlama ve Anlamlılık Bölgesi Denetimi

1.  X rastgele olsa bile M’yi etkileyen ortak nedenler Y’yi de etkileyebilir; M rastgele atanmış değildir. Tutarlılık, zaman sırası, destek ve X–M/X–Y/M–Y karıştırıcılık koşulları gerekir; X’in etkilediği M–Y karıştırıcıları ayrıca sorun olabilir. Bootstrap ve katsayı özdeşliği bunları test etmez. Bu doğrusal çarpımın nedensel yorumu, etkileşimsiz doğru modelde birim X karşıtlığı ve ek varsayımlar ister.

2.  Çarpımlar .521844/.303306/.000665’tir. .600490 yalnız varsayıma bağlı nokta çarpımının sıfırıdır; gerçek rho kestirimi, p veya güven sınırı değildir. Eğri için aralık hesaplanmadı. Simülasyonun gerçek üretiminde $\rho=0$’dır; gözlemsel araştırmada bu bilgi bilinmez. OLS artık ortogonalliği yapısal hata bağımsızlığını kanıtlamaz.

3.  Noktasal t çarpanı 1.975288, sınırlar \[-1.123572,-.411676\]; iki-parametre eşzamanlı çarpan 2.471439, sınırlar \[-1.259870,-.344350\]. Merkezlenmiş sınırlara W ortalaması .110603 eklenir; gözlenen destek dışı yorum yapılmaz. Noktasal tarama ortak %95 bant değildir. İki eğimin farkı $b_3(w_1-w_0)$ ile doğrudan sınanır; iki ayrı p’nin farklı taraflarda olması fark testi değildir. Klasik normal/homoskedastik koşullar veya uygun başka bant yöntemi ayrıca gerekir.

## H1: Hatalı Raporu Onarma

\(1\) $c'$ aralığı sıfırı içerir ama sıfır olduğu gösterilmemiştir; üretimde $c'=.2$’dir. “Tam aracılık” etiketi yerine büyüklük ve aralık raporlanır. (2) Tek aracı modeli başka aracıları dışlamaz; “tek neden” iddiası verilerle desteklenmez. (3) Düşük $W$’de basit eğim $-0.18$, aralığı $[-0.40, 0.04]$’tür; X her W düzeyinde Y’yi artırmaz. Anlamlı etkileşim yalnız eğimlerin farklı olduğunu gösterir.

## Kolay Düzey

1.  X’in Y üzerindeki etkisinin geçtiği mekanizmayı temsil eden değişkendir.

2.  X-Y ilişkisinin gücünü veya yönünü değiştiren koşul değişkenidir.

3.  $a\times b$ çarpımıyla ifade edilir.

4.  X’in etkisinin W düzeylerine göre değişip değişmediğini test etmek için eklenir.

5.  Model ve örnekleme koşullarına göre yol çarpımının sıfırdan farklılığına kanıt bulunur; nedensel mekanizma veya tek aracı kanıtı değildir.

## Orta Düzey

1.  Aracılık “neden/nasıl”, düzenleyicilik “ne zaman/kimler için” sorusuna yanıt verir.

2.  Eski etiketlerdir; c’ aralığının sıfırı içermesi doğrudan yolun sıfır olduğunu kanıtlamaz. Dolaylı/doğrudan yolun büyüklüğü, belirsizliği ve nedensel tanımlama koşulları verilir.

3.  Planlı eğimler ilişkiyi betimleyebilir; önce anlamlı etkileşim çıkmasını bekleyip elverişli düzey seçilmez. Noktasal ve eşzamanlı belirsizlik ayrılır.

4.  Zaman sırası belirsiz olduğundan güçlü nedensel mekanizma iddiası sınırlıdır.

5.  Ana etkilerin ortalama düzeyde yorumlanmasını kolaylaştırır.

## İleri Düzey

1.  Aracı değişkenin sonuçtan önce gelmesi gerekir; aksi hâlde mekanizma yönü savunulamaz.

2.  Örneğin öğretim desteğinin başarıya etkisi motivasyon üzerinden yalnız düşük kaygılı öğrencilerde güçlenebilir.

3.  Sobel çarpım için delta/normal yaklaşım kullanır; bootstrap tahmin dağılımını yeniden örneklemeyle yaklaştırır. Bootstrap da iid/uygun birim ve model gerektirir; daha çok tekrar nedensel yanlılığı veya yanlış kapsamayı gidermez.

4.  Grafik etkinin yönünü ve büyüklüğünü görünür kılar; test yalnız etkileşimin varlığına ilişkin kanıt sunar.

5.  Rapor dolaylı/etkileşim katsayısı, bootstrap güven aralığı, basit eğimler ve kuramsal yorum içermelidir.

## P1 öğretim notu

Aynı 160 simülasyon kaydı korunur. Yol çarpımı ve nedensel etki için ek varsayımlar
ayrılır. Rho=0/.3 karşılaştırması varsayımsal duyarlılıktır; yeni veri veya rho
kestirimi değildir. Ana bootstrap aralığı yeni senaryoya otomatik taşınmaz.
Alternatif açıklama ve gerekli dış kanıt yazılır. Farklı gerekçeli seçimler
savunulabilir; rubriğin altı ölçütü ayrı değerlendirilir.

## Ç1 çıkış sorusunun yanıtı

Hayır. Zaman sırası, müdahale/ölçüm tanımı, ortak destek ve uygun karıştırıcı varsayımları ayrıca gerekir; bootstrap bunları sağlamaz.
