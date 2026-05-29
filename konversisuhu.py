START

  PRINT "Memilih mode konversi:"
  PRINT "1. C to F"
  PRINT "2. C to K"
  PRINT "3. F to C"
  PRINT "4. F to K"
  PRINT "5. K to C"
  PRINT "6. K to F"
  
  INPUT pilihan_mode
  INPUT suhu_awal

  // Evaluasi pilihan mode konversi
  SWITCH pilihan_mode
  
    CASE 1: // C to F
      hasil = (9/5 * suhu_awal) + 32
      PRINT "Hasil Konversi C to F: ", hasil
      
    CASE 2: // C to K
      hasil = suhu_awal + 273.15
      PRINT "Hasil Konversi C to K: ", hasil
      
    CASE 3: // F to C
      hasil = 5/9 * (suhu_awal - 32)
      PRINT "Hasil Konversi F to C: ", hasil
      
    CASE 4: // F to K
      hasil = 5/9 * (suhu_awal - 32) + 273.15
      PRINT "Hasil Konversi F to K: ", hasil
      
    CASE 5: // K to C
      hasil = suhu_awal - 273.15
      PRINT "Hasil Konversi K to C: ", hasil
      
    CASE 6: // K to F
      hasil = 9/5 * (suhu_awal - 273.15) + 32
      PRINT "Hasil Konversi K to F: ", hasil
      
    DEFAULT:
      PRINT "Pilihan tidak valid!"
      
  ENDSWITCH

END