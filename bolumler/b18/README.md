# Bölüm 18 — IBM SPSS Uygulamaları

Bu klasör, kitabın **Bölüm 18: IBM SPSS Uygulamaları** için öğrenci uygulama paketidir. Amaç menü ezberlemek değil; veri kaynağı, analiz birimi, etkin oturum durumu, model, çıktı ve raporu aynı denetlenebilir zincirde tutmaktır.

## Ders hedefleri

Bu bölüm sonunda öğrenci:

- veri kaynağını, analiz birimini ve etkin oturum ayarlarını birlikte denetler;
- veri sözlüğünü CSV içe aktarma komutlarıyla eşleştirir;
- eşli testte doğru tabloyu, bağımsız testte doğru model satırını ayırır;
- filtre, ağırlık, eksik kod ve fark yönünün sonucu nasıl değiştirdiğini gösterir;
- SPSS ile gerçekten çalıştırılmış sonuç ile başka yazılımdaki kontrol hesabını birbirinden ayırır;
- syntax, veri, çıktı ve akademik raporu denetlenebilir bir teslim halinde birleştirir.

## Kitaptaki bölüm akışı

- 18.2 Menü Listesinden Denetlenebilir Analize
- 18.3 Oturum Sözleşmesi: Dosyadan Önce Kararlar
- 18.4 Gerçek Veriyi İçe Aktarma ve Doğrulama
- 18.5 Eşli Test: Üç Tabloyu Birbirinden Ayırma
- 18.6 Bağımsız Test: Levene Bir Otomatik Anahtar Değildir
- 18.7 Durum Deneyi: Aynı Dosyada Farklı n
- 18.8 Kitabın Yöntem Haritası
- 18.9 Çıktı Okuma ve Teslim Kontrolü
- 18.10 Rehberli ve Bağımsız Etkinlikler
- 18.11 Bölüm Sonu Özet

## Dosyalar

- `VERI.md`: kaynak, analiz birimi, kodlar, türetilmiş dosyalar ve lisans notları
- `sleep.csv`: 20 ölçümlük uzun uyku arşivi; 10 kişi × 2 koşul
- `uyku_esli.csv`: ID üzerinden oluşturulmuş geniş eşli çalışma dosyası
- `ToothGrowth.csv`: 60 hayvan kaydının kaynak kopyası
- `dis_veri.csv`: SPSS için OJ=1, VC=2 kodu eklenmiş çalışma dosyası
- `analiz.py`: **çalıştırılan Python referans hesabı** ve teknik doğrulama
- `analiz.sps`: ana SPSS oturumu için hazırlanmış syntax
- `durum-deneyi.sps`: filtre, ağırlık ve eksik-kopya karşı örnekleri
- `analiz.R`: bağımsız R kontrolü için hazırlanmış betik
- `calisma.ipynb`: öğrenci çalışma defteri
- `GOREVLER.md`, `COZUMLER.md`, `RAPORLAMA.md`: etkinlik ve raporlama zinciri
- `SPSS-KONTROL-LISTESI.md`: gerçek SPSS oturumu için teslim kontrolü
- `beklenen.json`: Python referans değer sözleşmesi
- `DOGRULAMA.json`: bölümün teknik doğrulama sınırları

## Önerilen çalışma sırası

1. `VERI.md` ve `GOREVLER.md` dosyalarını okuyun.
2. `calisma.ipynb` ile analiz birimi, eşleme, filtre ve model farklarını inceleyin.
3. Teknik kontrol için bölüm klasöründe `python analiz.py` çalıştırın.
4. SPSS erişiminiz varsa `analiz.sps` dosyasını **gerçekten çalıştırın** ve Viewer çıktısını Python referans sayılarıyla karşılaştırın.
5. `durum-deneyi.sps` karşı örneklerini ana analizden ayrı tutun.
6. Teslimden önce `SPSS-KONTROL-LISTESI.md` ve `RAPORLAMA.md` üzerinden kontrol yapın.

## Temel referans sayıları

Uyku eşli analizi: `n=10`, ortalama fark `1.58` saat, `t(9)=4.062128`, iki yönlü `p=0.002832890`, %95 GA `[0.700114, 2.459886]`, `dz=1.284558`.

ToothGrowth 1 mg/gün: OJ−VC farkı `5.93`; ana Welch modeli `t=4.032770`, `sd=15.357672`, `p=0.001038376`, %95 GA `[2.802148, 9.057852]`.

> **Yürütme ayrımı:** Depodaki Python doğrulaması SPSS'in çalıştırıldığı anlamına gelmez. `.sps` dosyasının bulunması da tek başına yürütme kanıtı değildir.
