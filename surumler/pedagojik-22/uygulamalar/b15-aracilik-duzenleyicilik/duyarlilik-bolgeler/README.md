# Varsayım duyarlılığı ve eğim bölgeleri

Gerçek katılımcı değil: üst dizinin uret() fonksiyonu, n160/seed202609.
Tam duyarlıklı değerler üretilir; eski altı ondalıklı veri.csv 5.1e-7 toleransla
eşleşir. Yeni kayıt/üretim modeli yok; eski bootstrap verisi/sonuçları korunur.

```sh
python uygulamalar/b15-aracilik-duzenleyicilik/duyarlilik-bolgeler/dogrula.py
python uygulamalar/b15-aracilik-duzenleyicilik/duyarlilik-bolgeler/analiz.py
```

Aracılık: varsayımsal yapısal hata rho'su için b(rho)=b_OLS−rho*r_e/sqrt(1−rho²).
r_e=sqrt(SSE_Y|XM/SSE_M|X); aynı n paydası kullanılır. a*b(rho), rho0/.3/.6
için .521844/.303306/.000665; nokta sıfırı.600490. Bu gerçek karıştırıcılık
kestirimi veya güven aralığı eşiği değildir; her rho'da aralık yok. Gerçek
simülasyon üretiminde rho0; OLS artık ortogonalliği nedensel koşul testi değildir.
Nokta sıfırı brentq ve kısmi korelasyon özdeşliğiyle yalnız cebirsel denetlenir.

Düzenleyicilik ayrı yanıttır; koşullu aracılık modeli kurulmaz. wc desteği
[-2.606267,2.513480], ham W ortalaması.110603. Noktasal t(156) çarpan1.975288,
sınırlar[-1.123572,-.411676]; 2-parametre normal/homoskedastik F-elipsoidi
eşzamanlı çarpan2.471439, sınırlar[-1.259870,-.344350]. Sınır kökleri
aralığın sıfıra değdiği değerlerdir, klinik eşik veya sınır güven aralığı değil.
Gözlenen destek/joint X-W seyrekliği ayrıca gerekir. Noktasal tarama global
%95 kapsama değildir. HC3/küme bandı hesaplanmadı.

Yedi test: rho0, nokta sıfırı, geçersiz rho, JN kökleri, bant iç içeliği,
merkezleme değişmezliği, doğrudan eğim testi/bölge eşliği. Yeni ek yalnız
Python; R/SPSS yeniden çalıştırılmadı. Nedensel tanımlama testi/gerçek insan
doğrulaması yok. Çıktılar: `sonuclar/ozet.json`, `sonuclar/rho-duyarlilik.csv`,
`sonuclar/egim-bantlari.csv`. Imai ve ark. (2010): https://doi.org/10.1214/10-STS321 .
