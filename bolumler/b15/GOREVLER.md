# Bölüm 15 — Öğrenci görevleri

Önce VERI.md'yi okuyun. `calisma.ipynb` hesapları incelemek, COZUMLER.md gerekçeleri karşılaştırmak içindir.

## D1–D3: Modelden önce

1. Aynı 97 kayıtta AFA/DFA'nın öğretim yararını ve bağımsız doğrulama sınırını açıklayın.
2. Anahtarı, eksik satırları ve standartlaştırmayı yazın. S köşegeninin 1 olması neden gizil varyansları kendiliğinden belirlemez?
3. ML, sağlam ML, WLSMV ve FIML kavramlarından hangileri gerçekten uygulanıyor? Bir tabloya yeni yöntem adı yazmak neden yeni analiz değildir?

## G1–G4: Rehberli çözüm

1. 55 momenti ve M0/M1/M2'nin 20/21/22 parametresini sayın. Pozitif sd ile yerel tanımlanabilirliği ayırın.
2. M1 F'sinden T'yi, bağımsız göstergeli başlangıçtan CFI'yi ve n paydalı RMSEA'yı yeniden hesaplayın. %90 RMSEA aralığının üst sınırını yorumlayın.
3. A1 standart yükünden R² ve standart artık varyansını bulun. %95 yük aralığı sıfırı dışlasa da neden güçlü temsil kanıtı değildir?
4. C için AVE ve model-standartlaştırılmış toplamın CR'sini yük tablosundan bulun. İki payın farkını açıklayın.

## B1–B3: Bağımsız çözüm

1. M0−M1 T farkını, sd farkını ve nominal p'yi hesaplayın. M0'ı CFI başlangıç modeliyle karıştırmayın.
2. M1−M2 farkını ve M2 uyum özetini bulun. M2 A2 için birincil yükün karesiyle R² aynı mı? AFA sonrası alternatif seçiminin sınırını yazın.
3. A alt ölçeğinin AVE/CR'sini ve M1 Phi²'sini hesaplayın. Geçerlik için eksik kalan kanıtları sıralayın.

## H1: Hatalı raporu onarma

“Ki-kare anlamsız ve RMSEA .06'nın altında: model doğru. CFI .94, bütün maddeler iyi. C'nin CR'si .74, AVE gereksiz. AFA'da gördüğümüz A2 çapraz yükünü aynı veride DFA'ya ekledik: bağımsız doğrulama. Bu tablolar AMOS çıktısıdır.”

Beş iddiayı ayrı düzeltin. Ayrıca AIC*/BIC*'yi tam yazılım AIC/BIC'si, nominal p'yi seçim-düzeltilmiş p gibi sunmayın.

## P1: Bağımsız doğrulama protokolü

Yeni veride sınanacak modeli, önceden gerekçelendirilmiş alternatifleri, hedef grubu, örneklem planını, eksik/tahminleyici kararlarını ve modifikasyon sınırlarını yazın. A1/A4 içeriği ve A2 çapraz yükünü sonuçları görmeden nasıl değerlendireceğinizi belirtin.

| Karar / kanıt | Burada yapılan | Yeni çalışma planı | Eksik dayanak |
|---|---|---|---|
| Kaynak ve puanlama | Yerel arşiv ve aynı 97 kişi | … | Uzak hücre doğrulaması yok |
| M0/M1/M2 karşılaştırması | Normal-kuram ML öğretimi | … | M2 AFA sonrası seçildi |
| Ordinal / sağlam duyarlılık | Yapılmadı | … | Sonuç uydurulmaz |
| İçerik / uzman incelemesi | Sayısal işaretleme | … | Yeni görüşme yok |
| Bağımsız veriyle DFA | Yapılmadı | … | Yeni örneklem yok |
| Ölçüm değişmezliği | Yapılmadı | … | Grup modeli kurulmadı |

Teslim: kaynak/karar tablosu, çalıştırılabilir kod, uyum/parametre/artık tabloları, yük aralığı grafiği ve bir sayfalık protokol. Rubrik kitapla aynıdır: kaynak/ön işlem 20, model/hesap 30, belirsizlik/yorum 25, bağımsız doğrulama planı 15, yeniden üretim 10 puan. Gerçekte yapılmamış veri toplama veya uzman onayı yazılmaz.