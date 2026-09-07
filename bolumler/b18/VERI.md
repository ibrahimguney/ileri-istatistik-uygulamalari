# Bölüm 18 — Veri, kaynak ve analiz sözleşmesi

## Kullanılan dosyalar

Bu bölüm iki sabit öğretim verisini ve bir türetilmiş eksik-kopyayı kullanır:

- `sleep.csv` — R `datasets::sleep` verisinin yerel öğretim kopyası,
- `ToothGrowth.csv` — R `datasets::ToothGrowth` verisinin yerel öğretim kopyası,
- `sleep_eksik.csv` — yalnız eksik eş davranışını göstermek amacıyla `sleep.csv` dosyasından türetilmiş kopya.

`sleep.csv` ve `ToothGrowth.csv` değerleri Bölüm 10'da kullanılan sabit kopyalarla aynıdır. Kaynak ve lisans bildirimi aynı sınırlarla korunur.

## Kaynaklar

R kaynakları:

- `sleep`: R `datasets` paketi; kaynak çalışmalar Cushny ve Peebles (1905) ve Student (1908).
- `ToothGrowth`: R `datasets` paketi; R sözlüğü Bliss (1952) kaynağına atıf verir.

R kaynak dağıtımına ilişkin GNU GPL v2 bildirimi depoda `bolumler/b10/GPL-2.txt` dosyasında korunur. B18 aynı iki sabit veri kopyasını yeniden kullandığı için bu kaynak/lisans kaydına açıkça referans verir. Bu bildirim kitabın özgün metni veya depodaki bütün materyaller için yeni bir genel lisans tanımlamaz.

## `sleep.csv`

20 ölçüm satırı, 10 ID ve her ID için iki `group` değeri içerir.

| Değişken | Anlam |
|---|---|
| `kaynak_satir` | yerel sıra numarası |
| `extra` | kontrole göre uyku artışı (saat) |
| `group` | koşul/ilaç kodu 1 veya 2 |
| `ID` | eşleştirmeyi sağlayan kişi kodu |

Eşli analizde bağımsız gözlem sayısı 20 değil, **10 eşleşmiş ID**'dir. Ana fark `group2 − group1` olarak tanımlanır.

## `ToothGrowth.csv`

60 ayrı hayvan kaydı içerir. Ana SPSS etkinliğinde yalnız `dose=1` gözlemleri filtrelenir.

| Değişken | Anlam |
|---|---|
| `kaynak_satir` | yerel sıra numarası |
| `len` | kaynak ölçüm birimindeki odontoblast uzunluğu |
| `supp` | `OJ` veya `VC` destek türü |
| `dose` | 0.5, 1.0 veya 2.0 mg/gün kaynak dozu |

Ana öğretim karşılaştırması: `dose=1` içinde `OJ − VC`.

Filtre öncesi N=60, filtre sonrası N=20'dir. Filtreyi açık bırakmak daha sonraki analizleri sessizce değiştirebileceği için oturum sonunda `FILTER OFF` kullanılmalıdır.

## `sleep_eksik.csv`

Bu dosya özgün veri kaynağı değildir. Yalnız öğretim amacıyla `sleep.csv` kopyasında `ID=10, group=2` değeri eksik bırakılmıştır.

Amaç:

- dosyada satır sayısı 20 olarak kalırken,
- geçerli eş sayısının 10'dan 9'a düşebildiğini,
- eski t-testi sonucunun eksik veri bulunan yeni dosyaya kopyalanmaması gerektiğini

göstermektir.

Bu türetilmiş eksiklik gerçek araştırmadaki bir kayıp gözlem iddiası değildir.

## SPSS içe aktarım denetimi

CSV içe aktarımından sonra en az şu kontroller yapılmalıdır:

1. satır sayısı,
2. değişken adları,
3. sayısal/string türleri,
4. `group`, `ID`, `dose` kodları,
5. eksik değer sayıları,
6. aktif `FILTER`, `WEIGHT` ve `SPLIT FILE` durumu.

Dosyanın açılması, doğru analiz örneklemiyle çalışıldığı anlamına gelmez.

## Bilimsel sınırlar

- Bu veriler yeni veya temsili bir örneklem değildir.
- `sleep` sonuçları klinik tedavi kararı için kullanılmaz.
- `ToothGrowth` hayvan deneyidir; insanlara doğrudan genellenmez.
- Filtre/ağırlık/split durumları araştırma tasarımını veya bağımsız birimlerin gerçek sayısını değiştirmez.
- `sleep_eksik.csv` yalnız öğretim amaçlı türetilmiş bir durum deneyidir.
