# Bölüm 13 — raporlama

## Bölümdeki örnek ve açıklama

“ToothGrowth arşivindeki 60 kayıtta uygulama biçimi karşılaştırıldı. Doz 1 mg/günde merkezlenerek ortak ve ayrı doğrusal eğimler sınandı. Ortak eğim kısıtı için $F(1,56)=5.333$, $p=.025$; ayrı doğrusal eğimlerin altı hücre modeline göre uyumsuzluğu için $F(2,54)=8.399$, $p<.001$ bulundu. Bu nedenle doz bazındaki yorum hücre ortalamalarına dayandırıldı. OJ–VC farkları .5, 1 ve 2 mg/günde sırasıyla 5.25, 5.93 ve -.08 idi; üç karşılaştırmalı Bonferroni aralıkları $[1.24,9.26]$, $[1.92,9.94]$, $[-4.09,3.93]$ olarak hesaplandı. HC3 duyarlılığında genel yorum değişmedi. Son dozda farkın reddedilememesi eşdeğerlik diye yorumlanmadı; doz ön-test olarak sunulmadı.”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 17: sabit hedef dağılım

Aynı60 hayvan/6 hücre, doz(.5,1,2); iki gruba ortak sabit ağırlıklar eşit,
düşük(.6,.3,.1), yüksek(.1,.1,.8). Hücre modelinde hedef farkları
3.700/4.921/1.054; OLS üçlü aralıklar[1.3833,6.0167],
[2.1995,7.6425],[-2.2059,4.3139]. HC3/t yaklaşık duyarlılık ayrıca verilir.
Bu üç hedef genel olarak aynı parametrenin sağlamlık koşuları değildir.

Hücre/ayrı eğimde aile3; ortak eğimde aynı kontrast, aile1. Modeller arası
arama ve önceki doz ailesiyle ortak hata kontrolü yok. Ağırlıklar biliniyor
kabul edilir; dış örneklem/ağırlık belirsizliği veya nedensel taşıma yok.
Ortalama dozda hücre tahmini kurmak, gözlenen hücreleri ağırlıklandırmak
değildir. Destek uydurulmaz. Doz ön-test değildir; aynı ölçekte ön-test/son-test
modelinin değişim eşitliği ayrı teorik tartışmadır. Yeni ek yalnız Python.
