# Bölüm 15 — Aracılık ve Düzenleyicilik Analizleri

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- aracılık ve düzenleyicilik kavramlarını birbirinden ayırır,

- doğrudan, dolaylı ve toplam etki mantığını açıklar,

- etkileşim terimi üzerinden düzenleyici etkiyi yorumlar,

- bootstrap güven aralığı yaklaşımının aracılık analizindeki önemini açıklar,

- merkezleme ve basit eğim analizinin ne işe yaradığını belirtir,

- aracılık ve düzenleyicilik sonuçlarını akademik biçimde raporlar.

## Çalışma sırası

1. [Veri açıklamasını](VERI.md) okuyun.
2. [Görevleri](GOREVLER.md) kendi çözümünüzle tamamlayın.
3. [Defteri](calisma.ipynb) veya Python analizini çalıştırın.
4. [Raporlama rehberiyle](RAPORLAMA.md) bulguları yazın.
5. [Çözümlerle](COZUMLER.md) karşılaştırın.

## Çalıştırma

Komutlar `surumler/22-bolum/` klasöründen:

```sh
python -m pip install -r requirements.txt
python bolumler/b15/analiz.py
```

Asıl analiz: [uygulamalar/b15-aracilik-duzenleyicilik/analiz.py](../../uygulamalar/b15-aracilik-duzenleyicilik/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b15-aracilik-duzenleyicilik/README.md).
R betiği: [analiz.R](../../uygulamalar/b15-aracilik-duzenleyicilik/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b15-aracilik-duzenleyicilik/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
