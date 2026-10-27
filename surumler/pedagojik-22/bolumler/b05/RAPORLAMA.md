# Bölüm 5 — raporlama

## Bölümdeki örnek ve açıklama

Raporda araştırma sorusu, kaynak ve seçim kuralı, analiz birimi, fark yönü, grup özetleri, test türü, $t$, serbestlik derecesi, iki yönlü $p$, ham farkın aralığı, etki büyüklüğünün paydası ve sınırlılıklar yer almalıdır.

**Örnek rapor.** “R ToothGrowth verisinin 1 mg/gün dozunda OJ ($n=10$, ort.=22.70, SS=3.91) ile VC ($n=10$, ort.=16.77, SS=2.52) grupları Welch testiyle karşılaştırılmıştır. OJ$-$VC ortalama farkı 5.93 kaynak ölçüm birimidir (%95 GA $[2.80,9.06]$), $t(15.36)=4.03$, $p=.00104$; birleştirilmiş SS ile $d=1.80$ bulunmuştur. İnceleme bu doz ve tarihsel hayvan örneklemiyle sınırlıdır; bağımsızlık ve dağılım varsayımları kısa veri tablosundan bütünüyle doğrulanamaz.”

**Eşli rapora eklenecek sınır.** “On kişide ilaç 2$-$ilaç 1 farkı 1.58 saattir (%95 GA $[0.70,2.46]$), $t(9)=4.06$, $p=.00283$, $d_z=1.28$. Küçük örneklemde farkların normalliğine ilişkin tanılar sorun gösterdiğinden t-modeline dayalı aralık temkinli yorumlanmıştır. Uygulama sırası ve taşıma etkileri bu kısa veri tablosundan denetlenememektedir.”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Kalibrasyon ve ayrı hedef

Normal kurgu: n1=10/n2=30, gerçek fark0. Sigma1/2=3/1 için Student/Welch
red oranları .210145/.051055; 1/3 için .004045/.049930; 1/1 için .049160/.050320.
Her senaryoda 200.000 çekiliş; bunlar gerçek hayvan verisi veya test gücü değildir.
Gerçek doz1'de Yuen (%20 her kuyruk) fark6.80, GA[3.18698,10.41302],
p=.003369; h6/grup. Bu kırpılmış konum hedefidir, ana Welch fark5.93'ü değiştirmez.
Küçük p seçilmez; ham veri korunur; sağlam yöntem varsayımsız değildir.
