# Dengesiz hücreler: hangi ortalama farkı? — Revizyon 25

```bash
python dogrula.py
python analiz.py
```

Ana60 hayvan kaydı ve eski analizler korunur. Öğretim alt kümesi, sonuçlara
bakılmadan tanımlanmış kaynak sırası seçimiyle OJ hücrelerinden5/10/8,
VC hücrelerinden10/6/9 kayıt alır(n48). Bu seçimin temsil veya rastgele kayıp
varsayımını sağladığı iddia edilmez; tutulan kaynak satırları kaydedilir.

Üç OJ−VC hedefi farklıdır: eşit doz ağırlığı4.376111, ortak örneklem doz
ağırlığı4.220660 ve grupların ayrı doz bileşimleriyle ham fark5.654783.
Sonuncusu aynı doz dağılımına standartlaştırılmış fark değildir.
Hücre ortalamaları modeli ve HC3 kovaryansı kullanılır; statmodels ile eşleşir.
t yaklaşımı artık sd42'yi kullanır; küçük hücrelerde tam sonlu-örneklem veya
kesin heteroskedastik hata denetimi iddiası yoktur.

İki planlı etkileşim farkı, dozdaki OJ−VC farkından .5 dozundaki farkı çıkarır.
1−.5 için−2.570, ortak%95 Bonferroni aralığı[−9.354,4.214];
2−.5 için−7.461667,[−14.603,−.320]. Aile yalnız bu iki kontrasttır;
üç marjinal hedefi veya bütün raporu kapsamaz. Bir koşulda anlamlılık ve
diğerinde anlamsızlık, kendi başına etkileşim testi değildir.
Noktasal hedef aralıkları ve kaynak kayıtları JSON/CSV'de verilir.
Yeni ek yalnız Python; SPSS/R yeniden çalıştırılmadı.
