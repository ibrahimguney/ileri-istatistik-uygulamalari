# Bölüm 13 — raporlama

## Bölümdeki örnek ve açıklama

Çoklu regresyon raporlanırken modelin açıkladığı varyans, genel model testi, katsayılar, standart hatalar, güven aralıkları ve varsayım kontrolleri belirtilmelidir. Lojistik regresyonda odds oranları ve güven aralıkları özellikle önemlidir.

> UCI Portekizce dersi verisinin kaynak sırasıyla seçilen ilk 60 GP kaydında G3, G1 ve yaş ile modellenmiştir ($R^2=0.581$, düzeltilmiş $R^2=0.567$). G1 katsayısı 0.640’tır; HC3 standart hatası 0.227 ve HC3 $t$ yaklaşımına dayalı %95 GA $[0.185,1.094]$’tür. Yaş katsayısı ilk kayıt çıkarıldığında 0.505’ten 0.068’e değişmiştir. Ana analiz kaydı korumuştur. Bulgular seçili kayıtlarla sınırlıdır ve nedensel etki değildir.

> Öğretim amaçlı $G3\ge14$ olayı için G1’in yaşa göre düzeltilmiş odds oranı 5.219’dur (yaklaşık %95 Wald GA $[2.049,13.296]$). Model 60 kayıtta 19 olayla kurulmuştur. Olasılık eşiği 0.50 iken eğitim duyarlılığı 0.737, özgüllüğü 0.951’dir. Model değiştirilmeden sonraki 20 kayda uygulandığında bu değerler 0.600 ve 0.933 olmuştur. Aynı okuldan alınan bu alıştırma verisi bağımsız dış doğrulama değildir; 14 puan resmî geçme sınırı olarak kullanılmamıştır.

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 16: olasılık ve kalibrasyon

İlk60/19 olay sabit Logit; son20/5 olay kontrol. 16 yaş/G1=12 olasılık.085985,
13 olasılık.329304, fark.243319 (24.33 yüzde puan). Tam kovaryans delta
SH.114630, yaklaşık aralık[.01865,.46799]. Noktasal profil GA'ları logit
ölçeğinden dönüşür; gelecekteki0/1 yanıt aralığı veya nedensel etki değildir.

Sabit logit c=.5/1/2 dönüşümlerinde AUC.760 ve .50 doğruluk.850 aynı;
Brier/log-kayıp farklı. Toplu ortalama olay oranına yaklaşsa bile bütün olasılık
düzeylerinde kalibrasyon kanıtlanmaz. Kontrolde c/olay/olasılık eşiği seçilmez.
Kalibrasyon eğrisi/eğimi, performans aralıkları veya dış doğrulama yapılmadı.
Yeni ek yalnız Python; eski ana sonuçlar korunur.
