# Bölüm 9 — Simülasyon ve hesap sözleşmesi

## Kaynak: Bu paket için üretilmiş veri

Gerçek katılımcı, kurum, klinik ölçüm veya anket yanıtı yoktur. Bütün değişkenler
keyfî sürekli birimdedir. Diğer bölümlerin UCI veya bfi verileri kullanılmaz;
başka veri kaynağının lisansı bu dosyaya taşınmaz. Kod/metin/veriye bu
hazırlıkta yeni lisans atanmadı. Kitabın tam metni dağıtılmaz.

`veri_uret.py`: NumPy default_rng(202609), n=160. Sırasıyla X, W, e_M,
e_aracilik, e_duzenleyicilik için bağımsız N(0,1) dizileri üretilir:

- M = .6 X + e_M.
- Y_aracilik = .2 X + .7 M + e_aracilik.
- Y_duzenleyicilik = .3 X + .2 W + .5 XW + e_duzenleyicilik.

Veri on ondalık basamakla CSV'ye yazılır. Tohum ve denklemler sonuçlara
bakılarak değiştirilmedi. Üretici katsayıları ile örneklem tahminleri aynı
olmak zorunda değildir. Kurgu aracılıkta a=.6, b=.7, c'=.2, ab=.42 ve c=.62;
düzenleyicilikte ham etkileşim .5'tir. Bunlar gerçek dünyaya ait etkiler değildir.
İki ayrı yanıtı tek bir koşullu aracılık modeli gibi yorumlamayın.

[Sözlük](veri_sozlugu.csv). Eksik değer veya katılımcı tanımlayıcısı yoktur.
Satırlar simülasyonun bağımsız birimleridir; kayit yalnız sıradır.
Normalize LF SHA-256:
`b196e8c713269cd77736669c1e6cb3469f38f9fcfea9e23ec7a6a8b092daaafa`.
CRLF→LF ve sondaki tek satır sonu yalnız hash hesabında kullanılır.

## Aracılık hesabı

Aynı 160 satırla sabit terimli M~X, Y_aracilik~X+M ve Y_aracilik~X OLS
kurulur. Doğrusal, etkileşimsiz, aynı gözlemli bu modelde c=c'+ab sayısal
özdeşliği denetlenir; bu özdeşlik tek başına nedensellik kanıtı değildir.

Bootstrap seed=202610, B=5000. Her tekrarda 160 satır yerine koyarak seçilir;
X/M/Y aynı satır indisleriyle birlikte taşınır. Her iki regresyon yeniden
kurulur ve ab kaydedilir. Yüzde 95 persentil aralık, ab dağılımının .025/.975
kantilleri, doğrusal interpolasyon ile bulunur. R karşılığı quantile type=7.
Rank kaybı veya sonlu olmayan sonuçta işlem durur; başarısız tekrarlar sessizce
atılmaz veya yeni örnekle değiştirilmez. Başarılı çalışmada 5000/5000 tamamlanır.
Bu temel öğretim yöntemi BCa değil; bütün yöntemler için en iyi aralık olduğu
iddia edilmez. Dolaylı etki için bootstrap p değeri hesaplanmaz.

## Düzenleyicilik hesabı

X ve W kendi örneklem ortalamalarıyla merkezlenir. Y_duzenleyicilik ~ X_c +
W_c + X_c W_c modeli tam alt terimleri içerir. Merkezli ve ham modelin
tahminleri ile etkileşim katsayısı eşit olmalıdır. W'nin ortalama±1 örneklem
standart sapması (n−1 böleni) ve ortalamasında basit eğim b_X+b_XW W_c'dir.
Varyans hesabı iki katsayının kovaryans terimini de içerir; t(156) ile noktasal
%95 aralıklar kurulur. Bunlar çoklu karşılaştırmaya göre düzeltilmiş aralıklar
veya eşzamanlı güven bantları değildir. Grafikte çizgiler nokta tahminidir.

## Yorum ve yapılmayanlar

Bootstrap zaman sırasını, ölçülmemiş karıştırıcıları veya gerçek verideki
kümelenmeyi düzeltmez. Simülasyon denklemlerini bilmek, bu yöntemlerin gerçek
araştırmada nedenselliği kanıtladığı anlamına gelmez. Düşük W eğiminin tekil
p'si ile yüksek W eğiminin p'sinin farklılığı etkileşim testi yerine geçmez.
Etkileşim kendi katsayısı/aralığıyla değerlendirilir. HC3, BCa, Sobel,
PROCESS, koşullu dolaylı etki ve Johnson–Neyman sonuçları üretilmedi.

## Yöntem belgeleri

6 Eylül 2026 tarihinde incelenen resmî belgeler; kurulu paket sürümleri requirements.txt içindedir:

- SciPy, bootstrap: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
- lavaan, Mediation: https://lavaan.ugent.be/tutorial/mediation.html
- statsmodels, OLSResults.t_test: https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.t_test.html

Belgeler yöntem açıklaması içindir; lavaan/PROCESS çalıştırılmadı. Kitabın
Hayes (2022), MacKinnon (2008), Preacher ve Hayes (2008) kaynakları kuramsal
okuma için korunur. Yeni veri gerçek araştırmadan alınmış gibi sunulmaz.