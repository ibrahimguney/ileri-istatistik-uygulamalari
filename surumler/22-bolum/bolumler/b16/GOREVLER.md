# Bölüm 16 — görevler

Güncel Revizyon 19 görevleri; önce kendiniz çözün.

## D1–D3: Analizden Önce

1.  Bu veride düzey 1 ve düzey 2 birimleri nelerdir? SES ve okul türü hangi düzeydedir?

2.  7185 öğrenciyi bağımsız sayan bir regresyonda okul türü katsayısının standart hatası neden fazla küçük çıkar?

3.  Okul ortalama SES’ini kaynaktaki sütundan almak yerine örneklemden hesaplamanın gerekçesi ne olabilir?

Yanıtlar Ek F, Bölüm 16’dadır (s. kitaptaki ilgili sayfa).

# Rehberli ve Bağımsız Etkinlikler

## G1–G4: Rehberli Çözüm

1.  Boş model varyanslarından ICC’yi, tasarım etkisini ve etkili örneklem büyüklüğünü hesaplayın.

2.  14 öğrencili bir okulun ortalamasının güvenirliğini ($\lambda_j$) bulun. BLUP bu okulun ortalamasını neden daha çok büzer?

3.  Grup içi ve gruplar arası eğimlerden bağlamsal etkiyi bulun ve bir cümleyle yorumlayın.

4.  Rastgele eğim LR testinin karışım p değerini hesaplayın. Neden $\chi^2_2$ kullanılmaz?

## B1–B3: Bağımsız Çözüm

1.  Düzeyler arası etkileşim modelinden okul ortalama SES’i $+0.5$ olan bir Katolik okulda okul içi SES eğimini hesaplayın.

2.  Eğim varyansındaki %86’lık azalmayı ve bunun neden bir “$R^2$” gibi dikkatle okunması gerektiğini açıklayın.

3.  Naif OLS, küme-sağlam OLS ve rastgele kesişimli modelin sabit terim standart hatalarını karşılaştırın. Hangisi hangi soruya yanıt verir?

## H1: Hatalı Raporu Onarma

Beş iddiayı düzeltin.

## P1: Çok Düzeyli Çalışma Planı

Türkiye’de sınıflar içindeki öğrencilerde bir okuma müdahalesinin etkisini inceleyecek bir çalışma için plan yazın: düzeyler ve atama birimi (öğrenci mi sınıf mı), beklenen ICC ve buna göre sınıf/öğrenci sayısı, merkezleme kararları, rastgele etki yapısı, kestirim (ML/REML), düzey 2 örneklemi ve sd düzeltmesi, raporlanacak tablolar. Rubrik: tasarım 25, örneklem 20, model 30, raporlama 15, yeniden üretim 10 puan.

## T1–T3: Hedef ve Tahmin Denetimi

1.  HSB’deki üç ortalamayı ve ağırlıklarını karşılaştırın. Hangisi ulusal ortalamadır? Okul büyüklüğü sonuçla ilişkiliyse neyi sorgularsınız?

2.  Eşit ve eşitsiz büyüklük tasarım etkilerini karşılaştırın. 757.95 sayısını okul türü katsayısına doğrudan uygulamak neden yanlıştır?

3.  Okul 8367 için okul ortalaması ve yeni öğrenci aralıklarını ayırın. Yeni okuldan 30 öğrenci alınca okul varyansı neden kaybolmaz? Yeni okula genelleme için doğrulama bölmesini nasıl yaparsınız?

P1 planınıza hedef birimi, büyüklük dağılımını, bilinen/yeni küme hedefini ve parametre belirsizliğinin nasıl ele alınacağını ekleyin.

- Kümelenmiş veriyi bağımsız sayıp okul düzeyindeki etkileri aşırı kesin raporlamak.

- Ham bir yordayıcıyla tek eğim kestirip okul içi ve okullar arası ilişkileri karıştırmak.

- Rastgele eğim varyansını naif ki-kare veya Wald z ile sınamak.

- Sabit etkileri farklı modelleri REML olabilirlikleriyle karşılaştırmak.

- Yazılımın “yakınsadı” iletisini denetlemeden kabul etmek; sınırdaki varyansları gözden kaçırmak.

# Alıştırmalar

## Kolay Düzey

1.  Sınıf içi korelasyon (ICC) neyi gösterir?

2.  Rastgele kesişim ile rastgele eğim arasındaki fark nedir?

3.  Grup ortalamasına merkezleme ne demektir?

4.  Tasarım etkisi neden küme büyüklüğüne bağlıdır?

5.  REML ne zaman, ML ne zaman kullanılır?

## Orta Düzey

1.  ICC=.05, küme büyüklüğü 30’dur. Tasarım etkisini hesaplayıp çok düzeyli modelin gerekliliğini tartışın.

2.  Grup içi eğim 1.5, gruplar arası eğim 1.5 bulunmuştur. Bağlamsal etki nedir, ne anlama gelir?

3.  Bir yordayıcı eklendiğinde $\tau_{00}$ artmıştır. Bu nasıl mümkündür?

4.  12 okuldan toplanan veride okul düzeyindeki bir değişkenin etkisi sınanacaktır. Hangi sorunlar beklenir?

5.  Rastgele eğim varyansı sıfıra çok yakın ve yazılım uyarı veriyor. Ne yaparsınız?

## İleri Düzey

1.  Ekolojik ve atomistik yanılgıyı HSB örneği üzerinden açıklayın.

2.  Rastgele etkilerin yordayıcılarla ilişkili olması hangi yanlılığa yol açar? Grup ortalamasına merkezleme bu sorunu nasıl ele alır?

3.  Düzeyler arası etkileşimde düzey 1 yordayıcısını genel ortalamaya merkezlemek yorumu nasıl değiştirir?

4.  Küme-sağlam standart hatalı OLS ile çok düzeyli model ne zaman tercih edilir?

5.  Güçlü bir çok düzeyli model raporunda bulunması gereken en az beş unsuru yazın.
