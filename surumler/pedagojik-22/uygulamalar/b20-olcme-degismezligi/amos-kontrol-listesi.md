# Ölçme değişmezliği — AMOS kontrol listesi

Bu bir kurulum rehberidir; kitaptaki sayılar Python ve R/lavaan ile hesaplanmıştır.

1. `sonuclar/analiz_verisi.csv` dosyasını SPSS'te açıp `.sav` olarak kaydedin.
   `grup` değişkenine göre iki veri kümesi (Erkek, Kadın) tanımlayın
   (Manage Groups ve grup değerini seçme).
2. DFA bölümündeki M2'yi çizin: A→A1–A5, C→C1–C5, A↔C, e_A1↔e_A2,
   e_C1↔e_C2, e_C4↔e_C5.
3. Analysis Properties → Estimation: *Estimate means and intercepts* işaretli.
4. AMOS işaretleyici madde ile ölçekler. A1 bu veride kesişimi değişmez olmayan
   maddedir; işaretleyici olarak A3 ve C4 gibi değişmez görünen maddeleri seçin
   veya gizil varyansı 1'e sabitleyin (yalnız birinci grupta, diğer grupta serbest).
5. *Multiple-Group Analysis* ile önerilen otomatik modelleri başlangıç olarak
   kullanın; eşitlik etiketlerini kitap modeline göre tek tek kontrol edin.
   Biçimsel ve metrik modellerde gizil ortalamalar iki grupta da 0'dır;
   skaler modelde birinci grupta 0 tutulur, ikinci grupta serbest bırakılır.
   Kitabın katı modelinde yalnız 10 artık varyansı eşitlenir; üç artık
   kovaryansının etiketleri gruplarda farklı kalmalıdır. AMOS otomatik olarak
   bunları da eşitlerse farklı bir model ve serbestlik derecesi elde edilir.
6. Model Fit tablosundan χ², sd, CFI ve RMSEA'yı; *Model Comparison*
   tablosundan farkları alın. Beklenen χ²: 213.95 (62), 229.95 (70),
   266.83 (78), 309.74 (88). AMOS n−1 çarpanı kullanıyorsa sayılar küçük
   farklılık gösterebilir; ayarı raporlayın.
7. Kısmi skaler model için yalnız A1 kesişiminin eşitlik etiketini iki grupta
   farklı yapın (χ² ≈ 255.80, sd 77).
8. Çalıştırılmadıysa AMOS çıktısı veya ekran görüntüsü üretmeyin.
