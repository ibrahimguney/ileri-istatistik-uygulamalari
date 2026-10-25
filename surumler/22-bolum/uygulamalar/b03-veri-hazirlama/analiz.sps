* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Bölüm 3: Veri hazırlama ve puanlama.
* Çalışma dizini kitap kökü olmalıdır. Gerekirse aşağıdaki satırı
* kendi klasörünüzle değiştirip yorumdan çıkarın:
* CD '/kitap/kok/dizini'.
* Betik veri dosyasını değiştirmez; yalnız okur ve tablo üretir.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b03-veri-hazirlama/puanlar.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES=
   kaynak_satir F8.0
   kaynak_kayit F8.0
   A1 F8.0
   A2 F8.0
   A3 F8.0
   A4 F8.0
   A5 F8.0
   C1 F8.0
   C2 F8.0
   C3 F8.0
   C4 F8.0
   C5 F8.0
   A1_t F8.0
   C4_t F8.0
   C5_t F8.0
   A_n F8.0
   A_ort5 F12.4
   A_ort4 F12.4
   A_top5 F12.4
   C_n F8.0
   C_ort5 F12.4
   C_ort4 F12.4
   C_top5 F12.4.
EXECUTE.

* 1) Aralık ve eksik denetimi: yanıtlar 1-6 olmalıdır.
FREQUENCIES VARIABLES=A1 TO C5 /ORDER=ANALYSIS.

* 2) Anahtar benzersizliği: her kaynak kaydı bir kez bulunmalıdır.
AGGREGATE /OUTFILE=* MODE=ADDVARIABLES
 /BREAK=kaynak_kayit /tekrar=N.
FREQUENCIES VARIABLES=tekrar.

* 3) Ters kodlama (7 - x) ve eşikli puanlar SPSS'te yeniden hesaplanır.
COMPUTE A1_s = 7 - A1.
COMPUTE C4_s = 7 - C4.
COMPUTE C5_s = 7 - C5.
COMPUTE A_ort5_s = MEAN.5(A1_s, A2, A3, A4, A5).
COMPUTE A_ort4_s = MEAN.4(A1_s, A2, A3, A4, A5).
COMPUTE C_ort5_s = MEAN.5(C1, C2, C3, C4_s, C5_s).
COMPUTE C_ort4_s = MEAN.4(C1, C2, C3, C4_s, C5_s).
EXECUTE.

* 4) Python puanlarıyla fark sıfır olmalıdır (eksikler her iki yanda eksik).
COMPUTE d_A5 = A_ort5_s - A_ort5.
COMPUTE d_A4 = A_ort4_s - A_ort4.
COMPUTE d_C5 = C_ort5_s - C_ort5.
COMPUTE d_C4 = C_ort4_s - C_ort4.
DESCRIPTIVES VARIABLES=d_A5 d_A4 d_C5 d_C4 /STATISTICS=MIN MAX.
DESCRIPTIVES VARIABLES=A_ort5_s A_ort4_s C_ort5_s C_ort4_s
 /STATISTICS=MEAN STDDEV MIN MAX.

* 5) Geniş -> uzun dönüşüm; boş yanıtlar /NULL=KEEP ile korunur.
DATASET NAME genis.
DATASET COPY uzun.
DATASET ACTIVATE uzun.
VARSTOCASES
 /MAKE yanit FROM A1 TO C5
 /INDEX=madde(yanit)
 /KEEP=kaynak_satir kaynak_kayit
 /NULL=KEEP.
FREQUENCIES VARIABLES=yanit.
DATASET ACTIVATE genis.
