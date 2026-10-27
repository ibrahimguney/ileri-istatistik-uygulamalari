# Dışa aktarılmış çıktı sözleşmesi — Revizyon 25

```bash
python dogrula.py
python analiz.py
python analiz.py --observed gercek-oturum-kontrol.csv
```

İlk iki komut SPSS çalıştırmaz. Python/SciPy ile iki modelin beklenen
kontrol satırlarını `sonuclar/beklenen-kontrol.csv` dosyasına yazar.
Bu dosya gerçek SPSS çıktısı diye sunulmamalıdır.

Kendi SPSS oturumunuzun Viewer/OMS çıktısından aşağıdaki alanları eşleyip
ondalık noktalı, virgülle ayrılmış CSV hazırlayın:

`model,n1,n2,df,difference,se,t,p,ci_low,ci_high`

İki model etiketi tam olarak `paired_2_minus_1` ve
`welch_OJ_minus_VC_dose1` olmalıdır. Eşli n1=10,n2=0,sd9;
bağımsız Welch n1=10,n2=10; fark yönleri etiketlerde yazılıdır.
Bu dosya formatı doğrudan her OMS dışa aktarımının biçimi değildir;
tablo başlığı ve alan eşlemesi kullanıcı tarafından doğrulanmalıdır.

Sayısal alanlarda3 ondalık basamak yuvarlaması için mutlak.00051 tolerans,
kişi sayılarında tam eşitlik aranır. Model satırı/sd/yön/SH/aralık birlikte
kontrol edilir. `p=0` reddedilir; uygun üst sınır veya daha çok basamak yazılır.
`<0.01` gibi bir sınır yalnız beklenen p gerçekten bu sınırın altındaysa kabul
edilir; sayısal eşitlik veya yeterli rapor ayrıntısı kanıtı değildir.

Doğru sayıların eşleşmesi yazılımın gerçekten çalıştırıldığını, aynı ham
dosyanın kullanıldığını veya varsayımların sağlandığını kanıtlamaz.
Gerçek oturumun sürümü/lisansı, komutu, veri hash'i, Viewer dosyası ve
hata/uyarıları ayrıca saklanır. Bu ortamda SPSS yürütülmedi;
`SPSS_executed=false` alanı korunur. Gözlenen dosya kontrolü geçici rapor
üretir; kaynak beklenen değerlerin üzerine yazmaz. Yedi reddetme/eşleme testi vardır.
