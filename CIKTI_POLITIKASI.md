# Çıktı Dağıtım Politikası

Bu belge, **Bölüm 1–18** analizlerinin ürettiği `sonuclar/` ve `grafikler/` klasörlerinin depoda nasıl ele alınacağını açıklar.

## Temel ilke

Kaynak veri, analiz kodu ve öğrenci çalışma dosyaları ile **yeniden üretilebilir analiz çıktıları** birbirinden ayrılır.

- `sonuclar/` = **sürümlenmiş referans/doğrulama çıktıları**
- `grafikler/` = **yeniden üretilebilir çalışma çıktıları; varsayılan olarak Git'e alınmaz**

Bu klasörler öğrenci ödevi teslim alanı değildir.

## `sonuclar/` politikası

Bölümlerde izlenen `sonuclar/` dosyaları, ilgili `analiz.py` çalıştırıldığında elde edilen referans sonuçların bir anlık görüntüsüdür. Amaçları:

1. analizin yeniden üretilebilirliğini kontrol etmek,
2. `beklenen.json` ve `DOGRULAMA.json` kayıtlarıyla birlikte teknik doğrulamayı desteklemek,
3. öğrencinin kendi çalışmasını tamamladıktan sonra sonuç biçimini karşılaştırabilmesine yardımcı olmak.

B18'de Python ile üretilen referans çıktılar, SPSS Syntax'ın ayrıca SPSS içinde çalıştırıldığı anlamına gelmez. `.spv` gibi kişisel SPSS çıktı dosyaları öğrenci teslimi niteliğindedir ve referans `sonuclar/` alanına eklenmez.

### Öğrenci kullanımı

Öğrenci:

- kendi ödevini, `.spv` dosyasını veya raporunu `sonuclar/` içine kaydetmemelidir,
- `sonuclar/` içindeki dosyaları başlangıç cevabı olarak kullanmamalıdır,
- analiz çalıştırıldığında yerel `sonuclar/` dosyalarının değişebileceğini bilmelidir,
- bu değişiklikleri kişisel çalışma olarak GitHub'a göndermemelidir.

### Bakım ve güncelleme

İzlenen bir `sonuclar/` dosyası yalnız şu durumda güncellenmelidir:

1. analiz kodunda veya veri kaynağında bilinçli bir değişiklik yapılmışsa,
2. analiz yeniden çalıştırılmışsa,
3. yeni sonuçlar `beklenen.json`, ilgili bölüm `DOGRULAMA.json` ve bilimsel açıklamalarla karşılaştırılmışsa,
4. farkın nedeni anlaşılmış ve belgelenmişse.

Yalnızca paket/kütüphane sürümü değiştiği için oluşan sayısal farklar otomatik olarak kabul edilmemelidir. Otomatik Python doğrulamasında bilimsel geçme/kalma ölçütü ham dosya farkı değil, `beklenen.json` ile anlamsal ve toleranslı sayısal karşılaştırmadır.

## `grafikler/` politikası

`grafikler/` klasörleri analiz sırasında yeniden üretilebilen PDF/PNG/SVG vb. görseller içindir.

Varsayılan politika:

- `grafikler/` Git tarafından izlenmez,
- analiz çalıştırıldığında yerelde oluşturulur,
- kişisel öğrenci grafikleri depoya gönderilmez,
- aynı grafiğin tekrar tekrar sürümlenmesiyle depo şişirilmez.

Bir görselin kalıcı olarak yayımlanması gerekiyorsa, otomatik çıktı klasörüne güvenmek yerine bakım amacı açık olan bir konuma (örneğin `assets/` altında küratörlü bir web görseli) bilinçli olarak eklenmelidir.

## Öğrenciye önerilen kişisel çalışma alanı

Öğrenciler kendi tablolarını, raporlarını, SPSS `.spv` dosyalarını ve son teslim dosyalarını depo dışındaki kişisel klasörlerinde tutmalıdır. Gerekirse yerel olarak `ogrenci-ciktilari/` adlı bir klasör kullanılabilir; bu klasör Git tarafından izlenmez.

## Git bakım ilkesi

Depoda aşağıdaki dosyalar kaynak/referans materyali olarak sürümlenir:

- ham veya öğretim için sabitlenmiş veri dosyaları,
- `analiz.py`, `analiz.R`, `analiz.sps` ve yardımcı kod,
- `calisma.ipynb`,
- `GOREVLER.md`, `COZUMLER.md`, `RAPORLAMA.md`,
- bölümün gerektirdiği yazılım kontrol listeleri,
- `beklenen.json`, `DOGRULAMA.json`,
- doğrulanmış referans niteliğindeki mevcut `sonuclar/` dosyaları.

Aşağıdakiler varsayılan olarak sürümlenmez:

- `grafikler/`,
- `ogrenci-ciktilari/`,
- kişisel SPSS `.spv` çıktı dosyaları,
- Jupyter geçici dosyaları ve checkpoint'ler,
- işletim sistemi ve editör geçici dosyaları.

## Kısa karar kuralı

Bir dosya için şu soruyu sorun:

> Bu dosya bilimsel/teknik doğrulama için bilinçli bir referans mı, yoksa analiz yeniden çalıştırıldığında üretilebilen geçici bir çıktı mı?

- **Referans ise:** doğrulanarak sürümlenebilir.
- **Yeniden üretilebilir geçici çıktı ise:** Git'e alınmaz.

Bu politika, veri lisanslarından bağımsızdır. Veri ve kullanım sınırları için her bölümün `VERI.md` dosyasına ve kökteki `KULLANIM.md` belgesine bakılmalıdır.
