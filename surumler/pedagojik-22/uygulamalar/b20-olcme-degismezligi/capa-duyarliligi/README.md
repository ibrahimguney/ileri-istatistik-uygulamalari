# Çıpa duyarlılığı, gizil fark ve belirsizlik — Revizyon 23

```bash
python dogrula.py
python analiz.py
```

Aynı önceden incelenmiş B yarısı:425 kaynak-kodu1,891 kaynak-kodu2 kişi.
Bu iki kod bütün cinsiyet kimliklerini temsil eden bir sınıflama sayılmaz.
Ana betik, model araması ve sonuçlar korunur. Kaynak SHA/anahtar doğrulanır.

## Üç sabit çıpa senaryosu

Tam skaler ve A1-serbest modellerinin mevcut parametreleri kullanılır.
A1+A2-serbest model yalnız duyarlılık için ek olarak kestirilir; eski ana
modelin yerine geçirilmez. A faktöründe A3/A4/A5, C'de beş madde çıpa kalır.

A farkı erkek gizil SD biriminde sırasıyla.500209,.487959,.435385;
koşullu yaklaşık%95 aralıklar[.363296,.637122],[.351373,.624546],
[.297154,.573615]. C farkı yaklaşık.2156 ve[.0712,.3599]'dur.
Havuz varyansını da içeren delta aralıkları JSON/CSV'dedir. Farklı modellerin
aralık örtüşmesi, modeller arası fark veya eşdeğerlik testi değildir.

Aralıklar sabit çıpa kümesine koşullu beklenen normal kuramlı bilgiye dayanır.
Ortalama ve kovaryans türevleri, paylaşılan parametreler ve tam kovaryans
hesaba katılır. Her senaryo içindeki yalnız iki ham gizil fark için ayrıca
Bonferroni ailesi verilir; bütün üç senaryonun ortak aralığı değildir.

**Seçim:** A1 aynı veride adaylar taranarak seçilmişti. Önceden yazılmış
arama kuralı, seçilen maddeyi önceden belirlenmiş tek hipoteze dönüştürmez.
Arama p değerleri nominaldir; bu aralıklar da seçim belirsizliğini içermez.
Tüm aramayı yeniden yapan bootstrap veya yeni örneklem doğrulaması yapılmadı.
İki/üç çıpa sayısı tek başına doğru çıpaları veya değişmezliği kanıtlamaz.
Ortak metrik yükler varsayımı, A5'teki olası yük farklılığı dahil, korunur.

## Referans ve gözlenen fark

A1-serbest modelde kadın−erkek A farkı erkek SD'sinde.487959'dur.
Kadın ortalaması0/SD'si1 olacak biçimde aynı model yeniden ifade edilirse
erkek−kadın farkı−.543980 olur. Yalnız işaret dönmez; birim de değişir.
Gözlenen model ortalamaları ve kovaryansları aynen korunur. Havuz SD
standardizasyonu ortak ölçek çarpanına karşı değişmezdir.

Ortak yüklerle model ortalama farkı=(kesişim farkı)+(yük*gizil fark).
A1-serbest modelin A madde ortalaması puanında bileşenler.054673+.371693
=.426366 ham puandır. Gözlenen fark.452416, kalan uyumsuzluk.026050'dir.
Bu, eşitlik modelinin öngördüğü farkı ayrıştırır; gözlenen farkın tamamını
zorla açıklamaz. Kesişim farkı nedensel/madde yanlılığı kanıtı değildir.

Yeni ek yalnız Python; normal kuramlı ve yaklaşık sürekli madde yaklaşımıdır.
R/Amos, sağlam/ordinal kestirim, tüm model-seçim belirsizliği ve yeni doğrulama
bu ekte yürütülmedi. Grup farkları nedensel veya Türkiye nüfusuna genellenmez.
