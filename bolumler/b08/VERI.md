# Bölüm 8 — Kaynak ve analiz sözleşmesi

Cortez, P. (2008). Student Performance [Veri seti]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T. Veri lisansı CC BY 4.0.
Özgün araştırma: Cortez, P., & Silva, A. (2008). Using data mining to predict
secondary school student performance. FUBUTEC 2008, EUROSIS.

- Kaynak: https://archive.ics.uci.edu/dataset/320/student+performance
- CSV: https://archive.ics.uci.edu/static/public/320/data.csv
- Lisans: https://creativecommons.org/licenses/by/4.0/

Kitap kaynak notlarına göre Portekizce dersi tam dosyası 649 kayıt içerir.
Yerel alıntı ilk 80 satırın school, age, G1, G3 sütunlarının tarayıcıdan
aktarılmasıyla oluşturulmuş, kaynak_satir eklenmiştir. Yaş uydurulmamıştır.
Burada yerel arşiv aynı baytlarla veri.csv olarak sunulur; uzak kaynakla
otomatik hücre karşılaştırması bu hazırlıkta yapılmadı. Hesaplar özgün
makalenin bulguları değil, kitap için yeniden yapılan analizlerdir.

Bölüm 7 yerel arşiviyle ortak okul/not/sıra sütunları hazırlık sırasında
karşılaştırılır; öğrenci kodunda başka bölüm bağımlılığı yoktur.
Bu kontrol yaş sütununu uzak kaynakla doğrulamak veya örneklem temsilini
kanıtlamak değildir. Kod/açıklamalara yeni lisans atanmadı; veri lisansı
bütün depoya genişletilmez. Tam kitap metni pakete alınmaz.

## Birimler, seçim ve türetmeler

Sözlük: [veri_sozlugu.csv](veri_sozlugu.csv). Bütün 80 kayıt GP okulundandır;
ilk 60 model kurma, 61–80 sabit-model uygulama içindir. Sıra gerçek öğrenci
kimliği değildir. Seçim rastgele veya temsili değildir; sonraki 20 kayıt
bağımsız bir yeni okul/yıl örneklemi sayılmaz.

Yaş 15–18 yıl; notlar 0–20 ölçeğindedir. Eksik yoktur, sıfır not korunur.
Ham dosya değiştirilmez. age_c=age−16; hedef14=(G3≥14) yeni sütunlardır.
Ana kümede 19/60, aktarımda 5/20 olay vardır. İkili kodlama sürekli not
bilgisini azaltır. 14 bir öğretim eşiğidir; resmî geçme/başarı standardı değildir.

Normalize LF SHA-256:
`3ad427ac4ce8da8f4fc8d12fcb271d6f0a2699a0e086dc18d9ae4400636462b5`.
CRLF→LF ve sonda tek satır sonu yalnız hash hesabında kullanılır, ham
CSV'ye yazılmaz. Hash yerel bütünlük kontrolüdür, çevrimiçi kaynak doğrulaması değil.

## İki model ve sabit aktarım

G3 ~ G1 + age_c OLS ile hedef14 ~ G1 + age_c logit ayrı hedefleri modeller.
G3 yanıt/olay tanımı olarak kullanılır; G3 veya hedef14 yordayıcı yapılmaz.
G2 kullanılmaz. Yaşın kaydedildiği zaman ve tahmin anında erişilebilirliği
ayrıca doğrulanmadığından bu bir erken uyarı sisteminin kullanım onayı değildir.

Sonraki 20 kayıtta katsayılar, 16 merkezleme sabiti, olay tanımı ve önceden
belirlenmiş olasılık eşikleri değiştirilmez. Eğitim performansı iyimser olabilir.
Beş olaylı aktarım ölçüleri oynaktır; güven aralıkları bu pakette hesaplanmaz.
Eşik seçimi veya yeniden uyum sonrası aynı küme dokunulmamış test sayılmaz.

Düşük VIF bütün varsayımları, yakınsama modelin doğruluğunu, yüksek AUC
kalibrasyonu kanıtlamaz. HC3 seçilim/kümelenme ve model biçimi sorunlarını
çözmez. OLS ya da logit katsayıları burada nedensel müdahale etkisi değildir.