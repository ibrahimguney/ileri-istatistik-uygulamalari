# Bölüm 10 — görevler

Güncel Revizyon 13 görevleri; önce kendiniz çözün.

## D1–D3: Analizden Önce

1.  ToothGrowth 1 mg/gün grubunda OJ ile VC neden bağımsız; sleep verisinde iki ilaç neden eşleştirilmiştir?

2.  Friedman örneğinde satır ve sütun neyi gösterir? İki koşunun ortalamasını iki ayrı gözlem gibi saymak neden yanlıştır?

3.  “Shapiro anlamlıysa Wilcoxon seç” kuralında hangi araştırma sorusu ve varsayım bilgileri eksiktir?

Cevaplar Ek F, Bölüm 10’dadır (s. kitaptaki ilgili sayfa).

# Rehberli ve Bağımsız Etkinlikler

## G1–G4: Hesap ve Yorum

1.  OJ sıra toplamından U’yu, çift kazanımlarından $\widehat A$’yı bulun. 88.5 ve 11.5 aynı veride nasıl birlikte doğrudur?

2.  Sleep’te bir sıfır ve iki bağlı 1.3 farkını işleyin. $W^+$, $W^-$, T ve kesin p’yi bulun; neden 10 çift varken 512 işaret örüntüsü vardır?

3.  OJ’nin H istatistiğini bağ düzeltmesiyle hesaplayın. Dunn’ın üç ham p değerine Holm uygulayın; neden her p’yi üçle çarpmak aynı işlem değildir?

4.  Friedman’da W’yi ve Monte Carlo p’yi yeniden hesaplayın. 99999 rastgele atama neden tam sayım değildir?

## B1–B3: Bağımsız Çözüm

1.  VC grubundaki üç doz için ortak sıra toplamlarını, bağ-düzeltilmiş H’yi ve Dunn–Holm tablosunu üretin.

2.  İkili uzunluk tablosunun beklenen frekanslarını, düzeltmesiz Pearson istatistiğini ve Cramér V’yi elle bulun. Fisher p’siyle farkını ve doz birleştirmesini yorumlayın.

3.  100 kelimeyi aşmadan Friedman ve üç ikili karşılaştırmayı raporlayın; veri kaynağındaki 18/22 uyuşmazlığını ve yaklaşık p kullanımını saklamayın.

## H1: Hatalı Raporu Düzeltin

Her iddiayı bu bölümden bir hesap veya tasarım koşuluyla düzeltin.

## T1–T3: Üstünlük ve Belirsizlik Denetimi

1.  İki dağılımın medyanı0 iken $A=.82$ olabilmesini verilen kurgu ile hesaplayın. $F=G$, $A=.5$ ve eşit medyan hipotezleri neden farklıdır?

2.  ToothGrowth’taki 100 çift neden 100 bağımsız deneme değildir? Bootstrap birimini, .690–1.000 aralığını ve 2415 sınır tekrarını yorumlayın. Bu aralık kesin %95 kapsama veya evrende $A=1$ kanıtı mıdır?

3.  Sleep’te işaret ve Wilcoxon p’leri neden aynı çıkıyor? Sıfır hangi hesapta çıkarılır? Medyan aralığını bütün10 farkla, $k=2$ ve sürekli-model %97.85 kapsamayı kullanarak bulun; iki marjinal medyanın farkından ayrımını açıklayın.

## P1: Yeniden Üretim Dosyası

Kaynak sözlüğü, çalışan kod, iki grafik, bütün karşılaştırma tabloları ve bir sayfalık rapor teslim edin. Puanlama: kaynak/eşleme 20; bağ ve sıfırlar 20; kesin/yaklaşık yöntem 25; aile ve yorum 25; yeniden üretim 10. OJ Dunn, VC Dunn ve Friedman sonrası üç çift ayrı öğretim aileleridir; bölümün tüm testleri için tek bir %5 aile hatası kontrolü iddia edilmez.

# Alıştırmalar

## Kolay Düzey

1.  Mann–Whitney U testi hangi durumda kullanılır?

2.  Wilcoxon işaretli sıralar testi hangi parametrik testin alternatifidir?

3.  Kruskal–Wallis testinde grup gözlemleri bağımsız mı, eşleştirilmiş mi olmalıdır?

4.  Friedman testi hangi veri yapısında kullanılır?

5.  Ki-kare testinde temel karşılaştırma nedir?

## Orta Düzey

1.  Üç bağımsız grubun başarı puanları küçük gruplarda belirgin biçimde çarpık ve uç değerlidir. Hangi test neden düşünülebilir?

2.  Aynı öğrencilerin ön-test ile son-test arasındaki fark puanları küçük örneklemde belirgin biçimde çarpıksa hangi test düşünülebilir?

3.  Çapraz tabloda Pearson ki-kare testi $p=.03$ vermiştir. Bu sonucu %5 düzeyinde nasıl yorumlarsınız?

4.  Mann–Whitney U sonucu anlamlıdır. Yorum neden otomatik olarak ortalama farkı biçiminde yazılmamalıdır?

5.  Ki-kare tablosunda beklenen frekansı çok düşük hücreler vardır. Ne düşünülmelidir?

## İleri Düzey

1.  Dört bağımsız grup için Kruskal–Wallis anlamlıdır. Hangi izleme adımı gerekir ve neden?

2.  Araştırmacı yalnızca örneklem küçük olduğu için parametrik olmayan test seçmiştir. Bu gerekçe neden eksiktir?

3.  Friedman testinde üç tekrarlı ölçüm anlamlı farklıdır. Analiz ve raporlama nasıl sürdürülür?

4.  Mann–Whitney U testi $p<.05$ verirken dağılım şekilleri çok farklıdır. Hangi dikkat gerekir?

5.  Güçlü bir parametrik olmayan test raporunda bulunması gereken en az beş unsuru yazınız.

## Çekirdek öğrenme rotası

1. Sıra testinin hangi hipotezi sınadığını belirtir.
2. Bağımsız, eşli ve bloklu tasarımları ayırır.
3. Bağ, sıfır fark ve çoklu aile kararlarını raporlar.

**İleri rota:** Üstünlük olasılığı, zayıf sıfır ve kesin/Monte Carlo hesapları temel sıra yorumundan sonra.

**Ç1:** Mann–Whitney ile t testi her koşulda aynı ortalama farkını mı sınar?

**Karar görevi:** Üstünlük olasılığı veya ortalama farkı hedefini seçin; yöntem değişince sorunun aynı kalıp kalmadığını açıklayın.

[Rubrik ve teslim rehberi](RUBRIK.md).
