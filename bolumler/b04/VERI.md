# Bölüm 4 — Kaynak, sözlük ve hesap sözleşmesi

## Kaynak

R datasets paketinin `sleep` verisinin kitap arşivindeki CSV aktarımı kullanılır.
Bu pakette `sleep.csv`, içeriği değiştirilmeden `veri.csv` adıyla sunulur.
Kitaptaki aktarım notuna göre kayıtlar 5 Eylül 2026'da tarayıcıda görünen R kaynak
metninden aktarılmış; CSV başlıkları, sayı yazımı ve kaynak_satir dizini düzenlenmiştir.
Bu nedenle özgün R dosyasının bayt kopyası değildir. Bu paket ise yerel CSV ile
tam bayt eşitliği bakımından denetlenir. Uzak kaynakla otomatik hücre karşılaştırması
ve özgün makalelerin bireysel kayıtlarının denetimi bu pakette yapılmamıştır.

- R sözlüğü: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/sleep.html
- R kaynak metni: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/sleep.R
- Kaynak çalışmalar: Cushny ve Peebles (1905), DOI 10.1113/jphysiol.1905.sp001097;
  Student (1908), DOI 10.2307/2331554.
- R dağıtım bildirimi: https://raw.githubusercontent.com/wch/r-source/trunk/COPYING

Normalize LF SHA-256:
`adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e`.
Hash yalnız yerel kopyanın bütünlüğünü denetler. Normalleştirme CRLF→LF ve
sonda tek satır sonudur; ham dosyaya yazılmaz.

R kaynak dağıtımına ait mevcut GNU GPL v2 bildirimi [GPL-2.txt](GPL-2.txt)
dosyasında aynen korunmuştur. Bu veriye Bölüm 2'nin UCI/CC BY lisansı atfedilmez.
Yazara ait kod ve açıklamalar için bu çalışmada yeni lisans seçilmemiştir.
Makalelerin metin ve şekilleri dağıtılmaz; bu pakette yalnız yerel veri aktarımı
ve kitap için hazırlanmış analiz/öğrenci materyalleri yer alır.

## Sözlük ve eşleştirme

| Alan | Anlam |
|---|---|
| kaynak_satir | Aktarım sıra dizini; kişi kodu değildir. |
| extra | Kontrole göre uyku artışı, saat; mutlak uyku süresi değildir. |
| group | Koşul 1 veya 2; iki bağımsız kişi grubu değildir. |
| ID | On kişinin kaynak eşleştirme kodu. |

20 ölçüm satırı, aynı 10 kişide iki koşuldur. ID–group birleşimi benzersiz
olmalıdır. Dosyada eksik yoktur. Sıfır ve negatif extra değerleri korunur.
Makinece okunabilir sözlük: [veri_sozlugu.csv](veri_sozlugu.csv).
Ana fark koşul2−koşul1; H0: ortalama fark=0, H1: ortalama fark≠0, alfa=.05.
Bu öğretim sözleşmesi tarihsel çalışmada yapılmış önkayıt olarak sunulmaz.

Bağımsız kişiler ve normal fark modeli altında klasik t hesabı öğretilir;
bu koşulların doğrulandığı iddia edilmez. Küçük n ve 4.6 saatlik fark incelenir,
hiçbir kişi silinmez. Sıra, taşıma etkileri, randomizasyon ve temsil ayrıntıları
bu kısa kopyadan doğrulanmaz. Bulgular yeni deney veya tedavi önerisi değildir.

## Üç ayrı bilgi türü

1. Gerçek veri: bu CSV'deki on eşleşmiş kişi.
2. Kurgu: ders/dolum gibi verilen özetler ve 2×2 tablo; bunlar için yeni ham
   gözlem uydurulmaz.
3. Simülasyon: açık tohum ve ideal normal modelle oluşturulan yapay örnekler;
   gerçek sleep verisine karıştırılmaz.