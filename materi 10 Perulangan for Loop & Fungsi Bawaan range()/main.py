saldo = 0
setoran_tetap = 50000
#menghitung setoran selama 5 bulan dengan setoran tetap
for i in range(1,6):
    saldo += setoran_tetap
    
print(f"Hasil akhir saldo tabungan setelah 5 bulan = {saldo}")