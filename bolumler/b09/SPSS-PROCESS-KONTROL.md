# B09 — SPSS 29 / PROCESS doğrulama oturumu

Durum: SPSS ve PROCESS için çalıştırma hazırlığı yapıldı; **gerçek yazılım çıktısı henüz doğrulanmadı**. Aşağıdaki sayılar mevcut `beklenen.json` referansıdır, SPSS/PROCESS çıktısı değildir. Veri 160 satırlık simülasyondur.

## 1. Önce SPSS ile başlayın

1. Bu klasördeki `veri.csv`, `analiz.sps` ve `process-modeller.sps` dosyalarını bilgisayarınızda aynı klasöre indirin.
2. SPSS 29'da yeni oturum açın; File > Open > Syntax yoluyla `analiz.sps` dosyasını açın.
3. Dosyanın başındaki `CD 'C:/B09'.` satırına kendi B09 klasörünüzün tam yolunu yazın. Yol içindeki tek tırnak ve son noktayı koruyun.
4. Run > All ile çalıştırın. Veri okuma hatası varsa sonraki tabloları değerlendirmeyin.
5. İlk betimsel tabloda altı değişkenin her birinde N=160, kayit için min=1 ve max=160 olmalıdır.
6. Katsayı tablolarında standartlaştırılmamış **B** sütununu aşağıdaki referansla karşılaştırın.
7. Viewer çıktısını `B09_SPSS29_YYYY-AA-GG.spv` olarak ayrı çalışma klasörünüze kaydedin. Hata ve uyarıları da koruyun.

CSV sütunları konumlarına göre okunur; özgün CSV değiştirilmez:

| CSV değişkeni | SPSS adı | Rol |
|---|---|---|
| kayit | kayit | Kayıt numarası; modele alınmaz |
| x | x | Her iki örnekte X |
| araci | araci | Yalnız aracılık modelinde M |
| w | w | Yalnız düzenleyicilik modelinde W |
| y_aracilik | ymed | Model 4 yanıtı |
| y_duzenleyicilik | ymod | Model 1 yanıtı |

## 2. Ardından PROCESS

Resmî dağıtım: [PROCESS indirme sayfası](https://www.processmacro.org/download.html).
Makronun kendisi bu depoda dağıtılmaz.

`process-modeller.sps` dosyasını açın. `INSERT FILE` satırına indirdiğiniz resmî `process.sps` dosyasının tam yolunu yazın. B09'un OLS betiğini çalıştırdığınız aynı SPSS oturumunda Run > All seçin. İlk çağrı Model 4, ikinci çağrı Model 1 içindir. PROCESS sürümünü çıktı başlığından kaydedin; bu çağrı taslağının kurulu sürümünüzde çalıştığı ancak gerçek çıktıyla doğrulanabilir. Bir seçenek tanınmazsa hata metnini ve sürüm başlığını birlikte paylaşın.

Aracılıkta 5000 satır bootstrap, %95 persentil aralık ve seed=202610 hedeflenir. Çıktı dipnotundaki aralık türünü, örneklem büyüklüğünü ve tekrar sayısını kontrol edin. Düzenleyicilikte klasik OLS standart hataları, X/W ortalamadan merkezleme ve W'nin ortalama ±1 örneklem SS noktaları kullanılır. Sağlam standart hata, standartlaştırma veya farklı bootstrap seçeneği uygulanırsa aynı doğrulama koşulu sağlanmaz.

## 3. Sayısal karşılaştırma

| Model / ölçüt | Beklenen değer |
|---|---:|
| Analiz N | 160 |
| a: x → araci | 0.633279 |
| b: araci → ymed, x sabitken | 0.824034 |
| Doğrudan c′ | 0.135301 |
| Toplam c | 0.657145 |
| Dolaylı ab | 0.521844 |
| Merkezlenmiş düzenleyicilik sabiti | -0.040097 |
| xc katsayısı | 0.398487 |
| wc katsayısı | 0.111885 |
| xc × wc katsayısı | 0.559008 |
| Düzenleyicilik R² | 0.375246 |
| Düzenleyicilik hata sd | 156 |
| W ortalama−1SS: basit eğim | -0.181415 |
| W ortalama: basit eğim | 0.398487 |
| W ortalama+1SS: basit eğim | 0.978389 |

W ham ölçekte -0.926773824, 0.110602930 ve 1.147979683 noktalarında; merkezlenmiş ölçekte -1.037376753, 0 ve 1.037376753 noktalarında değerlendirilir. `analiz.sps` alt/üst noktalar için W'yi yeniden merkezleyip aynı modeli kurar; ilgili modelin **xc** katsayısı basit eğimdir. Standart hataları ve güven aralıkları da bu modelden okunur. Ortalamadaki eğim ilk merkezlenmiş modeldedir.

Deterministik katsayılarda tam duyarlık mevcutsa mutlak fark 0.000001'i aşmamalıdır. Yalnız dört ondalık gösteriliyorsa referansı dört ondalığa yuvarlayarak karşılaştırın; görüntüdeki yuvarlamayı analiz hatası saymayın. Daha büyük farkta veri aktarımı, model terimleri ve merkezleme ayarlarını inceleyin.

Python persentil bootstrap referansı [0.368530, 0.698101]'dir. Aynı seed farklı yazılımlarda aynı örnekleri üretmez; bu uçlar PROCESS için birebir geçme/kalma sınırı değildir. PROCESS uçlarını, yöntemini ve tekrar sayısını ayrı kaydedin; yalnız sıfırı dışlama kararının aynı olması tam sayısal eşdeğerlik kanıtı değildir. Aralığı BCa olarak adlandırmayın.

## 4. Gerçek yürütme kaydı

- [ ] SPSS ve PROCESS tam sürümleri, tarih ve kullanılan dosyalar kaydedildi.
- [ ] Veri aktarımı, N=160 ve eksiksiz altı sütun doğrulandı.
- [ ] Filtre, ağırlık ve split-file kapalı.
- [ ] Model 4'te ymed; Model 1'de ymod kullanıldı.
- [ ] Katsayılar, standart hatalar, t, p ve %95 aralıklar beklenen.json ile karşılaştırıldı.
- [ ] c = c′ + ab özdeşliği kontrol edildi.
- [ ] Model 1 merkezleme ve W noktaları doğrulandı.
- [ ] Bootstrap yöntemi, 5000 tekrar, seed ve varsa başarısız tekrar/uyarılar kaydedildi.
- [ ] PROCESS çıktısı ile Python/R referansı ayrı etiketlendi.
- [ ] SPV ve okunabilir PDF çıktısı saklandı; hata/uyarılar eklendi.

Çıktılar incelenmeden `SPSS_PROCESS_calistirildi` alanını true yapmayın.
