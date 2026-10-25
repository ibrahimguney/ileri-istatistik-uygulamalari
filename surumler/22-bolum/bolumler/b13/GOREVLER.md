# Bölüm 13 — görevler

Güncel Revizyon 16 görevleri; önce kendiniz çözün.

## D1–D3: Model Kurmadan Önce Düşünün

1.  Ortalama G3’ü modellemek ile $G3\ge14$ olayını modellemek neden aynı soru değildir? G3=13 ve G3=0 hangi bilgileri kaybederek aynı sınıfa girer?

2.  Bütün kayıtlar GP okulundaysa modele okul göstergesi eklemek ne kazandırır? Yaşı 16 çevresinde merkezlemek yeni bilgi üretir mi?

3.  G2’yi eklemek eğitim performansını artırsa bile birinci dönem sonu uygulamasında neden sorunludur? İlk 60 ve sonraki 20 kaydı iki bağımsız okul örneklemi sayabilir miyiz?

Etkinliklerin gerekçeli yanıtları Ek F’de, s. kitaptaki ilgili sayfa’tedir.

# Rehberli ve Bağımsız Etkinlikler

## G1–G3: Rehberli Uygulama

1.  16 yaş ve G1=12 için doğrusal modelden ortalama G3 tahminini bulun. Aynı profilde lojistik olasılığı hesaplayın; iki sayının neden birbirinin yerine geçemeyeceğini açıklayın.

2.  $R^2=0.581404$, $n=60$, $k=2$ ile düzeltilmiş $R^2$’yi hesaplayın. Yaşın klasik $t$ değerinin karesini değişim $F$ testiyle karşılaştırın. Düşük VIF neden yaş katsayısının kararlı olduğunu garanti etmez?

3.  16 yaşta G1=12’den 13’e geçiş için odds oranını ve olasılık farkını hesaplayın. OR güven aralığı için katsayı aralığının iki ucuna hangi dönüşümü uygularsınız?

## B1–B3: Sonraki 20 Kayda Sabit Modeli Uygulayın

Bölüm 12’nin yeniden model kurma etkinliğinden farklı olarak burada ilk 60 kaydın **katsayılarını değiştirmeyin**. Kaynak sırası 61–80 olan kayıtlara tahmin üretin.

1.  Kaynak sırası 80 olan kaydın yaş ve G1 değerlerini bulun. İki modelin tahminlerini hesaplayın ve gözlenen G3 ile karşılaştırın.

2.  $c=0.50$ için dört hücreli sınıflandırma tablosunu oluşturun; duyarlılık, özgüllük ve doğruluğu hesaplayın. Herkesi sıfır sınıfına atayan kuralla karşılaştırın.

3.  Eğitim ve aktarım AUC/Brier değerlerini karşılaştırın. Neden bu sonuçlara bakıp hedef not eşiğini veya olasılık eşiğini değiştirerek aynı grubu yeniden “test” sayamayız? En fazla 120 sözcüklük bir sınırlılık paragrafı yazın.

## H1: Araştırma Raporundaki Hataları Bulun

Her iddiayı veri, yöntem ve kullanım bağlamı açısından ayrı düzeltin.

## T1–T3: Olasılık ve Kalibrasyon Denetimi

1.  16 yaşta G1=12 ve 13 için olasılıkları, OR’yi ve olasılık farkını karşılaştırın. İki olasılık aynı katsayılardan geldiğinde fark aralığı neden tam kovaryans gerektirir? Bu aralık bir kişinin 0/1 sonucu için tahmin aralığı mıdır?

2.  $c\hat\eta$ dönüşümünde AUC ve .50 sınıfları neden korunur? Brier/log-kaybın değişmesi ne gösterir? Ortalama tahminin .25’e yaklaşması tek başına neden iyi kalibrasyon değildir?

3.  Son 20 kayıtta 5 olay varken tabloya bakıp c seçmek ve aynı grubu yeniden test saymak neden uygun değildir? Profil güven aralığı ile performans belirsizliği ve dış doğrulamayı ayırın.

## P1: İki Model İçin Analiz Denetimi

İlk 60 kaydın katsayılarını ve klasik/HC3 doğrusal aralıklarını, ilk kayıt dışarıda bırakıldığındaki değişimi ve sonraki 20 kaydın sabit-model sonuçlarını yeniden üretin. G3’ü yanıt olarak kullanmanın geçerli, `hedef14`’ü yordayıcı olarak kullanmanın sızıntı olduğunu açıklayın. Teslim: kaynak sözlüğü, çalıştırılabilir kod, iki tanı/sonuç grafiği ve bir sayfalık yorum.

<div class="center">

| Değerlendirme ölçütü                                 | Puan |
|:-----------------------------------------------------|-----:|
| Kaynak, seçim, olay tanımı ve bilgi zamanı           |   20 |
| Katsayılar, OR ve belirsizlik hesaplarının doğruluğu |   25 |
| Gözlem etkisi, VIF ve HC3 ayrımı                     |   20 |
| Sabit-model aktarımı ve eşik tabloları               |   20 |
| Yeniden üretilebilir kod ve ölçülü akademik rapor    |   15 |

</div>

# Alıştırmalar

Bu alıştırmalar çoklu doğrusal regresyon, lojistik regresyon, varsayım kontrolü ve çıktı yorumlama becerilerini pekiştirmek için üç düzeyde düzenlenmiştir.

## Kolay Düzey

1.  Çoklu regresyonda bağımlı ve bağımsız değişkenleri tanımlayınız.

2.  $R^2$ değerinin neyi gösterdiğini açıklayınız.

3.  Standartlaştırılmış beta katsayısı ne amaçla kullanılır?

4.  Lojistik regresyonda odds oranı nasıl yorumlanır?

5.  Çoklu bağlantı neden sorun oluşturur?

## Orta Düzey

1.  Aynı modelde anlamlı genel $F$ testi varken bazı katsayıların anlamsız çıkmasını yorumlayınız.

2.  VIF değerlerinin yüksek olduğu bir modelde hangi adımlar izlenebilir?

3.  Lojistik regresyonda sınıflandırma doğruluğunun tek başına neden yeterli olmadığını açıklayınız.

4.  Artık grafikleri regresyon varsayımları hakkında hangi bilgileri verir?

5.  Kontrol değişkeni eklemek katsayı yorumunu nasıl değiştirebilir?

## İleri Düzey

1.  Çoklu regresyonda nedensel yorum yapabilmek için gereken tasarım koşullarını tartışınız.

2.  Lojistik regresyonda kesme noktasının duyarlılık ve özgüllük üzerindeki etkisini açıklayınız.

3.  Aykırı ve etkili gözlemlerin model kararlarına etkisini örnekle yorumlayınız.

4.  Hiyerarşik regresyon ile standart çoklu regresyon raporlamasını karşılaştırınız.

5.  Bir lojistik regresyon sonucunu odds oranı, güven aralığı ve pratik önem birlikte yer alacak biçimde raporlayınız.
