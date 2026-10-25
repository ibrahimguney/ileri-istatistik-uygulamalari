# Bölüm 5 — Güç Analizi ve Örneklem Büyüklüğü Planlama

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- hedef parametreyi, önemli farkı ve planlamada kullanılan etkiyi ayırır;

- merkezi olmayan t dağılımından test gücünü hesaplar;

- grup başına kişi, toplam kişi ve tam çift sayısını doğru raporlar;

- tamsayı örneklem sonucunu bir önceki n’nin gücüyle denetler;

- pilot yayılımı, kayıp oranı ve kaynak sınırı için duyarlılık planı kurar;

- güç, hassasiyet ve yeterli kayıt kalma olasılığını birbirinden ayırır;

- modele uygun yazılım ayarlarıyla denetlenebilir örneklem gerekçesi yazar.

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
python bolumler/b05/analiz.py
```

Asıl analiz: [uygulamalar/b05-guc-analizi/analiz.py](../../uygulamalar/b05-guc-analizi/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b05-guc-analizi/README.md).
R betiği: [analiz.R](../../uygulamalar/b05-guc-analizi/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b05-guc-analizi/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
