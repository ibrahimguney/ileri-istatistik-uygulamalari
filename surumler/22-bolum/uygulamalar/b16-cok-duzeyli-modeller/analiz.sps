* Encoding: UTF-8.
* ------------------------------------------------------------------.
* İleri İstatistik Uygulamaları — Çok düzeyli modeller (HSB).
* Çalışma dizini kitap kökü olmalıdır; önce analiz.py çalıştırılır.
* CD '/kitap/kok/dizini'.
* Not: MIXED komutu IBM SPSS Statistics içindir; GNU PSPP desteklemez.
* ------------------------------------------------------------------.
SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='uygulamalar/b16-cok-duzeyli-modeller/sonuclar/analiz_verisi.csv'
 /ENCODING='UTF8' /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS=',' /QUALIFIER='"' /FIRSTCASE=2
 /VARIABLES= School A4 Sector A8 katolik F1.0 Minority A3 Sex A6
   SES F8.3 ses_ort_hazir F10.6 ses_m_hazir F10.6 MathAch F8.3.
EXECUTE.

* Okul ortalama SES'i ve grup ortalamasına merkezleme SPSS içinde yeniden hesaplanır.
AGGREGATE /OUTFILE=* MODE=ADDVARIABLES /BREAK=School /ses_ort=MEAN(SES).
COMPUTE ses_m = SES - ses_ort.
EXECUTE.

* 1) Boş model: ICC = tau00 / (tau00 + sigma2).
MIXED MathAch
 /FIXED=INTERCEPT
 /RANDOM=INTERCEPT | SUBJECT(School) COVTYPE(VC)
 /METHOD=REML
 /PRINT=SOLUTION TESTCOV.

* 2) Grup içi ve gruplar arası SES.
MIXED MathAch WITH ses_m ses_ort
 /FIXED=ses_m ses_ort
 /RANDOM=INTERCEPT | SUBJECT(School) COVTYPE(VC)
 /METHOD=REML
 /PRINT=SOLUTION.

* 3) Rastgele eğim ve düzeyler arası etkileşim.
MIXED MathAch WITH ses_m ses_ort katolik
 /FIXED=ses_m ses_ort katolik ses_m*ses_ort ses_m*katolik
 /RANDOM=INTERCEPT ses_m | SUBJECT(School) COVTYPE(UN)
 /METHOD=REML
 /PRINT=SOLUTION TESTCOV.

* Sabit etkileri karşılaştırmak için aynı modeller /METHOD=ML ile kurulur ve
* -2 log olabilirlik farkı ki-kare olarak değerlendirilir.
