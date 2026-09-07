# B18 — Veri ve kaynak notları

## 1. `sleep.csv`

Kaynak, R `datasets::sleep` arşivinin bu depoda Bölüm 10'da kullanılan yerel kopyasıdır. Dosyada **20 ölçüm fakat 10 bağımsız kişi kodu** vardır; her ID iki koşulda bir kez görünür. `extra`, kontrole göre uyku artışını saat cinsinden verir. Negatif değer ve sıfır geçerli gözlemlerdir.

Alanlar:

| Alan | Anlam | Kontrol |
|---|---|---|
| `kaynak_satir` | kaynak sıra etiketi | 1–20 |
| `extra` | kontrole göre uyku artışı | saat; negatif/sıfır geçerli |
| `group` | koşul | 1 veya 2; bağımsız grup değildir |
| `ID` | kişi kodu | 1–10; her ID iki koşulda bulunur |

Python, ID×koşul anahtarının benzersizliğini ve her ID için iki koşul bulunmasını kontrol eder. `uyku_esli.csv`, satır sırasına göre değil ID üzerinden eşlenir ve `fark = kosul2 - kosul1` olarak yeniden üretilir.

## 2. `ToothGrowth.csv`

Kaynak, R `datasets::ToothGrowth` arşivinin bu depoda Bölüm 10'da kullanılan yerel kopyasıdır. Dosyada 60 hayvan kaydı, `OJ`/`VC` uygulama biçimleri ve 0.5, 1, 2 mg/gün doz düzeyleri vardır. Yanıt `len`, odontoblast uzunluğudur; kısa kaynak açıklamasında ölçüm birimi açık verilmediği için burada **kaynak ölçüm birimi** denir.

B18'in bağımsız test uygulaması yalnız **1 mg/gün** düzeyini karşılaştırır; OJ ve VC'de 10'ar kayıt vardır. `dis_veri.csv` bütün 60 kaydı korur ve bu dosyaya özgü olarak `OJ=1`, `VC=2` kodunu ekler.

## 3. Yerel bütünlük sözleşmesi

Normalize edilmiş SHA-256 değerleri:

- `sleep.csv`: `adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e`
- `ToothGrowth.csv`: `654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3`

Normalizasyon LF satır sonu ve tek son satır sonu kullanır. Bu, **yerel kopya bütünlüğü** denetimidir; her çalıştırmada uzak R kaynağıyla otomatik hücre-hücre karşılaştırma yapıldığı anlamına gelmez.

## 4. Ana analiz ile öğretim kopyalarını ayırın

- Ana uyku analizi 10 tam çifttir.
- `ID<=5` filtresi yalnız bir öğretim alt kümesidir; yeni bağımsız çalışma değildir.
- Her çifte ağırlık 2 vermek yeni kişi üretmez; mekanik tekrar karşı örneğidir.
- İki hücrenin gizlendiği eksik kopya kurgudur; gerçek arşivde bu kayıp olduğu iddia edilmez.
- Kaynak CSV'ler bu karşı örnekler için değiştirilmez.

## 5. Lisans

Bu iki kaynak veri kopyasının aktarım/lisans notları Bölüm 10 ile aynıdır. Yanındaki `GPL-2.txt` veri kaynaklarına ilişkin lisans metnini korur. Bu durum, deponun tüm özgün kod ve öğrenci materyallerinin otomatik olarak aynı lisansla sunulduğu anlamına gelmez.
