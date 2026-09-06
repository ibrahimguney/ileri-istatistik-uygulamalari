# Bölüm 5 — Öğrenci görevleri

## D — Planlamadan önce

1. Ana planın Δ, σ, d, alfa, yön, güç ve tahsis değerlerini yazın. Hangileri
   varsayımsaldır? sleep CSV ana eğitim puanı senaryosunun verisi midir?
2. Grup başına n, toplam kişi, ölçüm satırı ve tam çift sayılarını ayırın.
3. Önemli farkı gözlenen p/etki sonucuna bakarak seçmek neden aynı plan değildir?

## G — Rehberli plan

1. `minimum_count()` ile ana minimum tamsayı n'yi bulun; n−1 ve n güçlerini
   karşılaştırın. Sürekli çözümü aşağı yuvarlamak neden yetersizdir?
2. d=.2,.3,.5,.8 ve güç hedefi .80/.90 senaryolarını karşılaştırın.
   Alfa .01 ve üç karşılaştırmalı Bonferroni planında n nasıl değişir?
3. %15 kayıp için ceil(64/.85) hesabını yapın. Bu kayıt sayısında iki grupta da
   en az64 kişinin kalma olasılığını hesaplayın. .90 olasılık hedefinin minimumunu bulun.
4. n=40/grup için d=.5 gücünü ve güç .80'e ulaştıran minimum saptanabilir d'yi bulun.

## B — Bağımsız uygulama

1. Tarihsel CSV'yi ID ile eşleyip s_D'yi bulun. Δ=.5 saat için σ_D=1,
   tarihsel s_D ve 1.5 senaryolarında gerekli tam çift sayılarını karşılaştırın.
2. İkiye bir tahsiste n1, n2 ve toplamı; eşli d_z=.5 için tam çift sayısını bulun.
   Birini diğerinin yerine yazabilir misiniz?
3. Fisher-z yaklaşımıyla rho=.3 için n minimumunu ve bir önceki n'nin gücünü bulun.
   Sonucu tam korelasyon gücü veya G*Power doğrulaması olarak sunmayın.
4. σ yerine konarak planlanan t-aralığının yarı genişliği .2σ olduğunda grup
   başına n'yi bulun. Bu hedef neden .80 güç hedefinden farklıdır?
5. Geçersiz n/alfa/etki girdilerinin reddedildiğini ayrı denemelerde gösterin.
   Sonuçlara bakıp tek yönlü plana geçmeyin.

## H — Hatalı rapor

“64 toplam kişi yeterlidir. %15 kayıp için76 kişi alınırsa her grupta64 kesin
kalır. Tarihsel gözlenen etki yeni planın doğru etkisidir. Korelasyon n'si tamdır.
Küme tasarım etkisini hesapladığımızdan çok düzeyli güç de doğrulanmıştır.”
Beş iddiayı sayı birimi, varsayım, hassasiyet ve yapılmamış analiz açısından düzeltin.

## Teslim

Bir örneklem planlama tablosu, çalışma defteri/kod ve kısa gerekçe raporu.
Ana plan, duyarlılık, kayıp varsayımı, n birimi, minimalite ve yöntem sınırı
bulunsun. Rubrik: hedef/tasarım25, girdiler20, hesap/minimalite25,
kayıp/duyarlılık20, yeniden üretim10. Yapılmamış pilot, simülasyon veya önkayıt
sonuç gibi sunulmaz.