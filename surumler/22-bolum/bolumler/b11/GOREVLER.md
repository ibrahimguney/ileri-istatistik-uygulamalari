# Bölüm 11 — görevler

Güncel Revizyon 14 görevleri; önce kendiniz çözün.

## D1–D3: Hesaplamadan Önce Düşünün

1.  Şekil <a href="#fig:b06-uci" data-reference-type="ref" data-reference="fig:b06-uci">[fig:b06-uci]</a>’nin ham not panelinde ilişkinin yönünü ve diğerlerinden ayrılan kaydı belirleyin. Tek katsayı bu grafikte hangi bilgiyi kaybettirir?

2.  “Puanlar doğrusal biçimde birlikte değişiyor mu?” ve “Yüksek not alanlar diğer dönemde de üst sıralarda mı?” soruları için hangi katsayıyı seçersiniz? İkisini de hesaplamak neden yararlı olabilir?

3.  İlk kayıtta $G1=0$, $G3=11$ bulunması bu kaydı eksik veya hatalı saymak için yeterli midir? Kontrol etmek için hangi kaynak bilgisi gerekir?

Yanıtları önce kendiniz yazın. Bu bölümdeki yeni etkinliklerin gerekçeli çözümleri Ek F’de, s. kitaptaki ilgili sayfa’tedir.

# Rehberli ve Bağımsız Etkinlikler

## G1–G3: Rehberli Uygulama

1.  60 kayıt içinde $G1=12$ ve $G3=12$ için ortalama sıraları hesaplayın. Kaynak sırası 3 olan kaydın sıra çiftini yazın. Yalnızca ilk altı kaydı sıralamak neden aynı sonucu vermez?

2.  Yalnız G1’i $M=5G1$ ile 100’lük ölçeğe dönüştürün. Pearson ve Spearman değişir mi? Sayısal hesap ve kavramsal gerekçeyi birlikte verin.

3.  $s_x=2.5558$, $s_y=1.9923$ kullanarak $b_1=r(s_y/s_x)$ ve $R^2=r^2$ hesaplayın. Bölüm 12 ile karşılaştırın; $r_s^2$ neden aynı açıklama değildir?

## B1–B3: Sonraki 20 Kayıtta Bağımsız Çözüm

Kaynak satırları 61–80’i seçin; ana grubun katsayılarını bu gruba taşımayın.

1.  Grafiği çizin; Pearson ve ortalama sıralı Spearman katsayılarını yeniden hesaplayın. Pearson hesabını $S_{xx}=78.8$, $S_{yy}=85.2$, $S_{xy}=51.4$ ile denetleyin.

2.  Pearson için yaklaşık Fisher %95 aralığını hesaplayın. İlk 60 kaydın aralığıyla karşılaştırıp yalnızca aralıkların örtüşmesine dayanarak bir fark testi yapmanın neden yeterli olmadığını açıklayın.

3.  En fazla 100 kelimelik raporda değişkenleri, seçimi, iki katsayıyı ve iki sınırlılığı belirtin. Bu 20 kaydı “bağımsız dış doğrulama örneklemi” olarak adlandırmayın.

## H1: Hatalı Raporu Düzeltin

Her iddiayı ayrı değerlendirin ve veriyle desteklenen bir alternatif yazın.

## T1–T3: Birlikte Belirsizlik ve Uyum Denetimi

1.  Pearson ve Spearman aralıkları hesaplanırken neden aynı öğrenci satırları birlikte çekilir ve sıralar her çekilişte yeniden hesaplanır? Sütunları ayrı örneklemek ve aynı kişilerin katsayılarını bağımsız Fisher formülüyle karşılaştırmak hangi yapıyı bozar?

2.  $r_s-r$ yaklaşık aralığı $[-.0865,.2018]$ neden yöntem üstünlüğü veya eşdeğerlik kanıtı değildir? İlk satırın olmadığı 7164 bootstrap örneği neden yeni bir doğrulama grubu değildir?

3.  $r(X,X+5)=1$ neden uyum değildir? $Y=X^2$, $X\sim U(-1,1)$ neden sıfır korelasyonun bağımsızlık olmadığını gösterir? Her örnekte hangi hipotez ve hangi grafik gerekir?

## P1: Tekrarlanabilir Duyarlılık Projesi

İlk 60 kayıt için ana analizi, ilk kaydı dışarıda bırakma analizini ve sırayla her bir kaydı dışarıda bırakan 60 karşılaştırmayı üretin. Her alt kümede sıraları yeniden hesaplayın. Pearson ve Spearman’ın en küçük/en büyük değerlerini ve bunlara karşılık gelen kaynak satırlarını bulun. Bir sayfalık raporu veri seçimi, grafik, yöntem, sonuç, sınırlılıklar ve yeniden çalıştırma komutuyla teslim edin.

<div class="center">

| Değerlendirme ölçütü                                             | Puan |
|:-----------------------------------------------------------------|-----:|
| Kaynak atfı, seçim kuralı ve değişmeyen verinin belgelenmesi     |   20 |
| Grafikler, bağlı sıralar ve doğru katsayılar                     |   25 |
| Yeniden sıralanan dışarıda bırakma karşılaştırmaları             |   25 |
| Belirsizlik, silme kararı ve genelleme sınırlarının tartışılması |   20 |
| Kod, sürümler ve yeniden çalıştırma yönergesi                    |   10 |

</div>

# Alıştırmalar

## Kolay Düzey

1.  $r=-1$ neyi gösterir?

2.  Belirlilik katsayısı $r^2$ temel olarak neyi gösterir?

3.  $r=.75$ yön ve güç bakımından nasıl yorumlanır?

4.  $r^2$ hangi aralıkta değer alır?

5.  Pearson korelasyonu hangi tür ilişkiye daha duyarlıdır?

## Orta Düzey

1.  Bir araştırmada çalışma süresi ile sınav puanı arasındaki korelasyon $r=.62$ bulunmuştur. Bu sonucu yön ve güç bakımından açıklayınız.

2.  Bir korelasyon analizinde $r=-.40$ ve $p<.05$ elde edilmiştir. Katsayı ve anlamlılık sonucunu birlikte yorumlayınız.

3.  Pearson korelasyonu sıfıra yakın bulunmuş, ancak saçılım grafiği belirgin eğrisel örüntü göstermiştir. Bu durumu açıklayınız.

4.  Bir araştırmacı iki değişken arasında $r=.50$ bulmuştur. $r^2$ kaçtır ve nasıl yorumlanır?

5.  İki sıralı tutum puanı arasındaki ilişki incelenecektir. Pearson mı Spearman mı daha uygundur? Kısaca açıklayınız.

## İleri Düzey

1.  Bir saçılım grafiğinde tek bir uç gözlemin korelasyonu güçlü biçimde yukarı çektiği görülmüştür. Araştırmacı sonucu raporlamadan önce ne yapmalıdır?

2.  Fiziksel aktivite ile yaşam doyumu arasında $r=.55$ bulunmuştur. Araştırmacının “fiziksel aktivite yaşam doyumunu artırır” demesi neden sorunludur?

3.  Bir korelasyon tablosunda stres ve uyku kalitesi için $r=-.68$, $p=.002$, $n=42$ raporlanmıştır. Kısa akademik yorum yazınız.

4.  Bir veri setinde Pearson korelasyonu $r=.20$, Spearman korelasyonu $r_s=.71$ bulunmuştur. Bu fark neyle açıklanabilir?

5.  İki değişken için $r=.00$ bulunmasına karşın araştırmacı bağımsız olmadıklarından şüphelenmektedir. Sıfır korelasyon hangi durumlarda bağımsızlık anlamına gelmeyebilir?
