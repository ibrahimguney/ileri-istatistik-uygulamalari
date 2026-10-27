# Bölüm 15 — raporlama

## Bölümdeki örnek ve açıklama

Aracılık raporlanırken $a$ yolu, $b$ yolu, doğrudan etki, dolaylı etki ve dolaylı etkinin güven aralığı belirtilmelidir. Düzenleyicilik raporlanırken etkileşim katsayısı, güven aralığı, basit eğimler ve mümkünse etkileşim grafiği sunulmalıdır.

Simülasyon sonuçları için örnek raporlar:

> Simüle edilmiş 160 kayıtta $X$, $M$’yi yordadı ($a=0.63$, %95 GA $[0.49, 0.77]$); $X$ sabit tutulduğunda $M$, $Y$’yi yordadı ($b=0.82$, $[0.65, 1.00]$). Dolaylı etki $ab=0.52$ bulundu; 5000 tekrarlı persentil bootstrap aralığı $[0.37, 0.70]$ sıfırı içermedi. Doğrudan etki küçük ve belirsizdi ($c'=0.14$, $[-0.05, 0.33]$). Veri simülasyondur; nedensel sıralama üretim modelinden gelir, veriden sınanmamıştır.

> Merkezlenmiş modelde $X\times W$ etkileşimi $0.56$ bulundu ($[0.42, 0.70]$). $X$’in eğimi $W$ ortalamanın bir standart sapma altındayken $-0.18$ ($[-0.40, 0.04]$), ortalamada $0.40$ ($[0.25, 0.55]$) ve bir standart sapma üstündeyken $0.98$’dir ($[0.77, 1.18]$).

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 18: varsayım duyarlılığı ve eğim bantları

Simülasyon n160/seed202609; tam üretim fonksiyonu kullanılır, altı ondalıklı
CSV yuvarlama sınırında kontrol edilir. Gerçek katılımcı değildir. Yapısal hata
rho0/.3/.6 varsayımlarında nokta çarpımları.521844/.303306/.000665;
nokta sıfırı.600490. Bu gerçek karıştırıcılık tahmini veya aralık eşiği değil;
her rho'da belirsizlik hesaplanmadı. Gerçek üretimde rho0'dır.

Ayrı düzenleyicilik yanıtında wc noktasal sınırlar[-1.123572,-.411676],
2-parametre klasik eşzamanlı sınırlar[-1.259870,-.344350]. Ham W için
.110603 eklenir; gözlenen destek[-2.606267,2.513480] ve ortak destek gerekir.
Noktasal tarama genel %95 bant değildir; sınırlar klinik eşik/güven aralığı değil.
HC3/küme bandı, gerçek insan veya nedensel tanımlama testi yok.
İki yanıt koşullu aracılık diye birleştirilmez. Yeni ek yalnız Python.
