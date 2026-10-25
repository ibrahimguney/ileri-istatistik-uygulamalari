# Bölüm 12 — açıklamalı çözümler

Revizyon 15; yeni T1–T3 dahil.

## Kendinizi Sınayın

Korelasyon iki değişkenin standartlaştırılmış birlikte değişimidir; birimler pay ve paydada birbirini götürür. Eğim ise $b=r\,s_Y/s_X$’tir: X’teki bir birimlik değişime karşılık Y’deki beklenen değişimi verir ve birimi “Y birimi / X birimi”dir (ör. puan/yıl).

## Kolay Düzey

1.  Bağımsız değişkendeki bir birim artışın bağımlı değişkende beklenen ortalama değişimini ifade eder.

2.  Bağımlı değişkendeki toplam değişimin ne kadarının model tarafından açıklandığını gösterir.

3.  $F$ testi ile değerlendirilebilir; tek bağımsız değişkenli durumda eğim $t$ testiyle eşdeğerdir.

4.  Gözlenen değer ile tahmin edilen değer arasındaki farktır: $e_i=Y_i-\hat{Y}_i$.

5.  $X=0$ olduğunda modelin tahmin ettiği ortalama $Y$ değeridir; yorum, $X=0$ değerinin gözlem aralığı içinde anlamlı olduğu durumlarda güçlüdür.

## Orta Düzey

1.  Sabit terimli, tek açıklayıcılı en küçük kareler regresyonunda, aynı gözlemler kullanıldığında $R^2=r^2$ olur. Sabit terimi kaldırılmış bir model için bu özdeşlik doğrudan kullanılamaz.

2.  Eğim 3 olduğundan, çalışma süresindeki her bir saatlik artış sınav puanında ortalama 3 puan artışla ilişkilidir. Sabit terim 40 olduğundan, çalışma süresi sıfır olduğunda modelin tahmin ettiği puan 40’tır.

3.  Bağımlı değişkendeki toplam varyansın %58’i model tarafından açıklanır; kalan %42’lik kısım modele dâhil edilmeyen faktörler ve rassal hata ile ilişkilidir.

4.  Sabit varyans (homoskedastisite) varsayımı ihlal ediliyor olabilir; bu durum heteroskedastisite olarak adlandırılır.

5.  $b_1=30/10=3$ ve $b_0=\bar{y}-b_1\bar{x}=10-3(4)=-2$; denklem $\hat{Y}=-2+3X$ olur.

## İleri Düzey

1.  Gözlem aralığı dışına tahmin (ekstrapolasyon) yapılır; doğrusal ilişkinin bu aralıkta da geçerli olduğu bilinemez ve tahmin belirsizliği büyür.

2.  Yüksek $R^2$’ye rağmen eğrisel artık deseni, doğrusal model biçiminin yanlış olabileceğini gösterir; dönüşüm veya eğrisel model düşünülmelidir.

3.  Gözlem veri hatası açısından denetlenir, kaldıraç ve etki ölçüleri incelenir, model gözlem dâhil ve hariç kurularak duyarlılık analizi yapılır; karar gerekçesiyle raporlanır.

4.  Tahmin aralığı daha geniştir; çünkü ortalama tahminindeki belirsizliğe ek olarak tek gözlemin kendi rassal değişkenliğini de içerir.

5.  Regresyon denklemi, katsayı yorumları ve anlamlılıkları, $R^2$, örneklem büyüklüğü, güven aralıkları ve varsayım kontrollerine ilişkin kısa değerlendirme verilmelidir.

## Bölüm 12: Gerçek Veri Etkinliklerinin Gerekçeli Yanıtları

Bu yanıtlar Bölüm 12’deki UCI birinci dönem notu–yıl sonu başarısı etkinliklerine aittir. Ana analiz, Portekizce dersi dosyasındaki ilk 60 gerçek kaydı; B etkinlikleri sonraki 20 kaydı kullanır. Sayılar özgün araştırmadan aktarılmış bulgular değil, bu kitap için yapılan yeniden analizdir. Önce kendi çözümünüzü tamamlayın; sayıları ve gerekçeleri birlikte karşılaştırın.

## D1–D3: Hesaplamadan Önce

1.  Yanıt G3 yıl sonu notu, açıklayıcı G1 birinci dönem notudur. Notlar 0–20 ölçeğindedir ve soru koşullu ortalama tahminidir; G1’i keyfî iki gruba ayırmak soruyu değiştirir. Model birinci dönem notu bilindikten sonra kullanılabilir. Yıl başlamadan tahmin isteniyorsa G1 henüz elde değildir; onu kullanmak gerçek kullanım zamanına aykırıdır. Kaynak sıra numarası yordayıcı değildir.

2.  Pozitif genel eğim beklenir; ancak bütün öğrenciler aynı sıralamayı korumaz. Kaynak sırası 3 olan öğrencide $G1=12$, $G3=12$; sıra 8’de $G1=10$, $G3=13$ bulunur. Daha yüksek ilk not burada daha yüksek son not getirmemiştir. Bu, pozitif koşullu ortalama ilişkisiyle çelişmez.

3.  Önceki bilgi düzeyi, öğrenme koşulları, öğretmen değerlendirmesi veya notlandırma sürecinin sürekliliği gerekçeli örneklerdir. Gözlemsel not ilişkisi, kayıt üzerindeki ilk notu yükseltmenin öğrenmeyi veya yıl sonu performansını artıracağını göstermez. Eğitsel bir müdahalenin etkisi için uygun karşılaştırma tasarımı ve mümkünse rastgele atama gerekir; yalnızca notlar arası regresyon yeterli değildir.

## G1–G3: Rehberli Uygulama

1.  $G1=12$ için $\widehat{G3}=12.7251$ bulunur. Kaynak sırası 3 olan kaydın artığı $12-12.7251=-0.7251$ puandır. Gözlenen not model tahmininden yaklaşık 0.73 puan düşüktür; bu tek başına veri hatası değildir. Nokta tahmini kesin bireysel not olarak yorumlanmaz.

2.  Ortalama yanıtın klasik standart hatası yaklaşık $1.3368\sqrt{0.0166926}=0.1727$ puandır. Aralıklar $$\text{Ortalama GA: }12.7251\pm0.3457=[12.3794,13.0709],$$ $$\text{Bireysel TA: }12.7251\pm2.6981=[10.0271,15.4232]$$ olarak bulunur. İlk aralık G1=12 düzeyindeki koşullu ortalama içindir; ikinci aralık aynı koşuldaki yeni bir bireyin model-temelli tahmin aralığıdır. İlk kaydın yüksek etkisi, artıkların uç davranışı ve klasik–HC3 standart hata farkı, model varsayımlarını sorgulamayı gerektirir. Burada gerçek yüzde 95 kapsamanın doğrulandığı iddia edilmez. HC3 eğim aralığı kullanmak, bu bireysel tahmin aralığını otomatik olarak sağlamlaştırmaz.

3.  Ortalama tahmininin standart hatası $x_0=\bar{x}=12.1$ iken en küçüktür; uzaklık terimi sıfırdır. $x_0=17$’de genişler. G1=20 not ölçeğinde mümkündür, ancak analiz alt kümesinin 0–17 gözlem aralığının dışındadır. Geçerli bir not değeri olması, bu değerde modelin iyi tahmin yapacağını göstermez; ekstrapolasyon ve sınır etkileri incelenmelidir.

## B1–B3: Sonraki 20 Gerçek Kayıt

1.  $n=20$, $\bar{x}=12.4$, $\bar{y}=12.2$, $S_{xx}=78.8$ ve $S_{xy}=51.4$ elde edilir. Böylece $$b_1=51.4/78.8=0.6523,\qquad b_0=12.2-0.6523(12.4)\approx4.1117,$$ $\widehat{G3}=4.1117+0.6523G1$ ve $R^2=0.3935$ olur. Hesaplar bu 20 kayıt üzerinde yeniden kurulan modele aittir; ilk 60 kaydın denklemi kullanılmaz.

2.  G1=12 için tahmin $11.9391$’dir. Kaynak sırası 80 olan kayıtta $G3=11$ olduğundan artık $-0.9391$ puandır. Yalnızca açıklayıcı not $M=5G1$ olarak dönüştürülürse $$\widehat{G3}=4.1117+\frac{0.6523}{5}M
    =4.1117+0.1304569M.$$ Sabit terim, tahminler, artıklar ve $R^2$ değişmez; eğimin değeri ve birimi değişir. Yanıt G3 de 100’lük ölçeğe çevrilseydi farklı bir dönüşüm hesabı gerekirdi; soru bunu istemez.

3.  Örnek rapor: “UCI Portekizce dersi verisinin 61–80. kayıtlarında G1 ile G3 ilişkisi $\widehat{G3}=4.112+0.652G1$ ile betimlenmiştir ($n=20$, $R^2=0.394$). Alt küme kaynak sırasıyla seçilmiştir; rastgele örneklem veya dış doğrulama grubu değildir. Bulgular seçili kayıtlarla sınırlıdır.” İlk 60 ve sonraki 20 kaydın eğimleri farklı olsa da, bu sayısal fark iki ayrı öğrenci anakütlesi için fark kanıtı değildir. Seçim kuralı, ortak okul, örnekleme değişkenliği ve model belirsizliği göz önüne alınmalıdır.

## H1: Hatalı Rapordaki Sorunlar

1.  **Nedensellik ve kesinlik:** Eğim gözlemsel koşullu ortalama ilişkisidir; her öğrencide aynı değişimi veya notu idari olarak artırmanın etkisini göstermez.

2.  **$R^2$ yorumu:** 0.557 açıklanan örneklem değişkenliği oranıdır; başarı olasılığı veya doğru tahmin yüzdesi değildir.

3.  **Varsayımlar:** Küçük eğim testi $p$-değeri normallik, sabit varyans veya bağımsızlık kanıtı değildir. İlk kaydın etkisi ve farklı standart hatalar ayrıca raporlanmalıdır.

4.  **Aralık türü:** $[12.38,13.07]$ koşullu ortalama içindir. Klasik yeni birey aralığı $[10.03,15.42]$’dir; bunun da model koşullarına bağlı olduğu belirtilmelidir.

5.  **Ekstrapolasyon:** G1=20 not ölçeğinde geçerli olmakla birlikte gözlenen aralığın dışındadır; aynı güvenilirlik varsayılamaz.

6.  **Genelleme:** GP okulunun ilk 60 sıralı kaydından Türkiye’deki öğrencilere veya kaynağın bütün 649 kaydına sonuç taşınamaz. Atıf vermek temsil sorununu çözmez.

7.  **Gözlem silme:** G1=0 kaydı etkilidir; ama sıfırın hata veya eksik olduğu gösterilmemiştir. Ana analizde korunur, dâhil/hariç sonuçlar duyarlılık olarak sunulur. Sadece eğimi büyüttüğü için silinmez.

Düzeltilmiş bir özet şöyle olabilir: “İlk 60 UCI Portekizce dersi kaydında birinci dönem notu ile yıl sonu notu pozitif ilişkilidir ($b_1=0.582$, $R^2=0.557$). Klasik eğim SH’si 0.068, HC3 SH’si 0.281’dir. İlk kaydın etkisi yüksektir; duyarlılık hesabında çıkarılınca eğim 0.856’ya değişir. Ana analiz bütün seçili kayıtları korur. Sonuç, rastgele seçilmemiş tek okul alt kümesi için betimseldir; nedensellik ve geniş topluluklara genelleme iddiası taşımaz.”

## T1–T3: Eğitim, Kalibrasyon ve Tahmin Denetimi

1.  Model yalnız ilk 40 kayıtta kurulur, sonraki 20 mutlak artık eşiğini seçer, son 20 betimsel kontrol içindir. 60 kayıtta tekrar kurulan modelde eski skorlar yeni fonksiyonun bağımsız kalibrasyon hataları değildir. Kontrol yanıtlarına göre seçme de veri sızıntısı yaratır. Bu kaynak sırası bölmesi rastgele örneklem/değiştirilebilirlik kanıtı değildir.

2.  $k=\lceil21(.95)\rceil=20$, en büyük skor $q=2.876083$; $m=18$ için $k=19>18$ ve genişletilmiş eşik sonsuzdur. Sıradan %95 yüzdeliği sıra düzeltmesini içermez. $\hat f(12)=12.817702$, aralık $[9.9416,15.6938]$’dir. Bu, 40 eğitim kaydının yeni birey aralığıdır; önceki 60 kaydın ortalama güven aralığı değildir.

3.  .90 yalnız bu 20 kaydın gözlenen kapsamıdır; ne gelecek için .90 garantisi ne de yöntemin evrensel geçersizlik kanıtıdır. Uygun değiştirilebilirlikte nominal garanti yeni rastgele (X,Y) için marjinaldir; her x/alt grup ve bütün 20 yanıt için ortak garanti değildir. Seçili tek okulda varsayım ayrıca gerekir. HC3 katsayı kovaryansını değiştirir; yeni bireyin hata dağılımını veya conformal değiştirilebilirliğini kurmaz.

## P1: Mini Proje İçin Kontrol Noktaları

Rapor Tablo <a href="#tab:b07-rubrik" data-reference-type="ref" data-reference="tab:b07-rubrik">[tab:b07-rubrik]</a>’teki ölçütlerle değerlendirilir. Karşılaştırma değerleri $n=60$, $b_0=5.7412$, $b_1=0.5820$, klasik $SH(b_1)=0.0681$, $R^2=0.5574$ ve $s_e=1.3368$’dir. G1=12 için aralıklar G2 etkinliğindeki değerlerle eşleşmelidir. Kaynak atfı, lisans ve ilk 60 kayıt seçim kuralı raporda bulunmalıdır.

Altmış ayrı modelde birer kayıt çıkarıldığında eğimler 0.5435–0.8556 arasında değişir. Alt uç kaynak sırası 19 olan kayıt, üst uç kaynak sırası 1 olan kayıt çıkarıldığında oluşur. İlk kaydın kaldıracı 0.3966, Cook uzaklığı 8.4269’dur. İşaretin pozitif kalması etki duyarlılığını önemsiz kılmaz; notun kaynağı araştırılmadan değer değiştirilmez.

İleri rotada eğitim RMSE’si 1.3143, LOOCV RMSE’si 1.6202 puandır. Eğitim RMSE’sinin $s_e=1.3368$’den farklılığı, $n$ ve $n-2$ paydalarından kaynaklanır. Her ayrılan kaydın tahmini, o kayıt kullanılmadan kalan 59 gözlemle kurulan modelden üretilmelidir. Aynı model artıklarını yeniden kullanmak çapraz doğrulama değildir; tek okul içindeki LOOCV de yeni okul başarısını sınamaz.

HC3 eğim standart hatası 0.2806, $t(58)$ referansıyla HC3 %95 güven aralığı $[0.0203,1.1437]$’dir. Bu değerler klasik aralığın $[0.4457,0.7183]$ olduğu belirtilerek karşılaştırılmalıdır. HC3’ün örnekleme veya kümelenme sorunlarını gidermediği, bireysel tahmin aralığına otomatik bir düzeltme sağlamadığı açıklanmalıdır.

Yeniden üretim denetiminde UCI kaynağı ile kitap yeniden analizi birbirinden ayrılmalı; 649 kayıt varmış gibi rapor yazılmamalıdır. Veri dosyasındaki kaynak sırası, model sütunları, sabit terim, standart hata türü, aralık düzeyi ve yazılım sürümleri kontrol edilir. Grafik üretmek tek başına tanısal değerlendirme değildir; ilk kaydın etkisi ve seçim sınırları gerekçeli olarak tartışılmalıdır.
