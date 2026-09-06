# Veri kaynağı ve sözlüğü

Kaynak: Cortez, P. (2008). Student Performance [Veri seti].
UCI Machine Learning Repository. DOI: 10.24432/C5TG7T.
https://archive.ics.uci.edu/dataset/320/student+performance

Veri lisansı: CC BY 4.0, https://creativecommons.org/licenses/by/4.0/
Bu atıf ve alıntı/değişiklik açıklaması yeniden paylaşımda korunmalıdır.

## Bu CSV ne içerir?

Kitabın Bölüm 7 arşivindeki `uci-portekizce-ilk80-notlar.csv` dosyasının
aynı baytlarla `veri.csv` adıyla paketlenmiş kopyasıdır. Yerel arşiv açıklamasına
göre Portekizce dersi kaynağının ilk 80 satırındaki school, G1 ve G3 alınmış,
izleme için kaynak_satir eklenmiştir. Not değerleri değiştirilmemiştir.
Arşivin ilk aktarımı tarayıcıda görülen kaynaktan yapılmıştır; bu paketi
hazırlarken uzak dosyayla yeniden hücre eşleştirmesi yapılmamıştır.

UCI kaynağının bütün değişkenlerini veya bütün 649 kaydını içermez.
Alıntının tümü GP'dir. Rastgele/temsili örneklem, Türkiye verisi veya yeni
veri toplama değildir. Aynı kişinin iki notu iki bağımsız kişi sayılmaz.

| Alan | Anlam | Kontrol |
|---|---|---|
| kaynak_satir | Alıntıdaki kaynak sıra numarası | 1–80, benzersiz; gerçek kişi kimliği diye yorumlanmaz |
| school | Kaynak okul kodu | Bu alıntıda yalnız GP; nominal |
| G1 | Birinci dönem notu | 0–20, tamsayı; sıfır geçerli |
| G3 | Yıl sonu notu | 0–20, tamsayı; sıfır geçerli |

80 satırda eksik hücre yoktur. İlk satır G1=0 ve G3=11'dir.
Ad, iletişim, aile, sağlık ve diğer analiz dışı alanlar bu CSV'de yoktur.
Kayıtları kimliklendirmeye çalışmayın.

LF satır sonu ve tek terminal LF ile normalize SHA-256:
`51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9`.
Bu hash yerel bütünlüğü denetler; uzak kaynağa eşitlik veya bilimsel geçerlik kanıtlamaz.

Özgün çalışma: Cortez, P., & Silva, A. (2008). Using data mining to predict
secondary school student performance. FUBUTEC 2008, 5–12.