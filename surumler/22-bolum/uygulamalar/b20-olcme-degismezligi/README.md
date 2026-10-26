# Bölüm 20 — Ölçme değişmezliği

## Veri
AFA bölümünün betiğinin ürettiği `../b18-faktor-analizi/yarim_B.csv`
(bfi yarım B, n=1316; 425 erkek, 891 kadın). A1/C4/C5 ters puanlanır;
maddeler ham 1–6 ölçeğinde kullanılır. Ölçüm modeli DFA bölümündeki M2'dir
(A1–A2, C1–C2, C4–C5 hata kovaryansları). Normalize SHA-256:
`6b3a399dd3aea61ab94252d81660f2c759bbf17d6084204f66a66b25da43b989`.

## Çalıştırma
```sh
python uygulamalar/b18-faktor-analizi/analiz.py      # yarım B'yi üretir
python uygulamalar/b20-olcme-degismezligi/analiz.py
Rscript uygulamalar/b20-olcme-degismezligi/analiz.R
```
SPSS'in temel modüllerinde çok gruplu DFA yoktur; AMOS adımları
`amos-kontrol-listesi.md` dosyasındadır.

## Yöntem
Ortalama yapılı çok gruplu DFA, normal kuramlı ML (grup başına n bölenli S,
T = Σ n_g F_g; lavaan varsayılanı), analitik gradyan (sayısal türevle denetlenir).
Ölçekleme: biçimsel modelde her iki grupta gizil varyans 1 ve ortalama 0;
diğerlerinde yalnız erkek grubunda. Çok gruplu RMSEA √G çarpanıyla.
Kısmi değişmezlik kuralı (önceden yazılmış): skaler modelde ki-kareyi en çok
düşüren tek kesişim, düşüş p<.001 ise serbest bırakılır; yinelenir.

Buradaki `strict` modeli yalnız 10 artık varyansını eşitler. Üç artık
kovaryansı (A1–A2, C1–C2, C4–C5) gruplara göre serbesttir; bütün artık
kovaryans matrisinin eşitliği sınanmaz. Bu, R betiğindeki
`group.equal = c("loadings", "intercepts", "residuals")` seçimiyle uyumludur;
`residual.covariances` kısıtı eklenmemiştir. Gizil ortalama karşılaştırması
katı değişmezliği zorunlu kılmaz; eşit artık varyansı da tek başına eşit
toplam puan güvenirliği sağlamaz.

## Kayıtlı kontrol noktaları (R lavaan 0.6-17 karşılaştırması)
| Model | χ² | sd | CFI | TLI | RMSEA |
|---|---|---|---|---|---|
| Biçimsel | 213.949 | 62 | .941 | .915 | .061 |
| Metrik | 229.945 | 70 | .938 | .920 | .059 |
| Skaler | 266.827 | 78 | .927 | .916 | .061 |
| Katı | 309.744 | 88 | .914 | .912 | .062 |
| Kısmi skaler (A1) | 255.799 | 77 | .931 | .919 | .059 |

Skaler model gizil farklar (kadın − erkek, erkek SD birimi): A .500 (SH .070),
C .216 (SH .074). Kısmi: A .488, C .216.

## Dosyalar
- `sonuclar/ozet.json`, `sonuclar/analiz_verisi.csv` (grup + anahtarlanmış maddeler).
- `assets_figures/od-yuk-kesisim.pdf`.

## Revizyon 23: çıpa duyarlılığı ve gizil fark

[Ek uygulama](capa-duyarliligi/README.md): sabit çıpa kümelerinde gizil
fark aralıkları, A1+A2 duyarlılığı, referans birimi dönüşümü ve model
ortalama farkının bileşenleri. Aynı veri araması sonrası koşullu çıkarımdır;
seçim belirsizliği veya yeni doğrulama kapsanmaz. Eski veri/model/arama
korunur; yeni ek yalnız Python, yedi test.
