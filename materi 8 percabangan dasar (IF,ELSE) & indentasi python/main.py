#PERCABANGAN DASAR (if, else)
'''
#contoh sistem verifikasi kelulusan
nilai_ujian = float(input("Masukkan nilai ujian anda : "))
if nilai_ujian >= 75.0:
    print("Selamat! Anda dinyatakan LULUS.")
    print("Pertahankan prestasi belajar anda.")
else:
    print("Mohon maaf, Anda dinyatakan BELUM LULUS.")
    print("Silahkan ikuti ujian perbaikan (Remidial.)")
print("Pemeriksaan nilai selesai.")
'''

#percabangan (if,elif,else)
total_belanja = 350000.0
if total_belanja >= 500000.0:
    persen_diskon = 0.20
    kategori = "Platinum"
elif total_belanja >= 250000.0:
    persen_diskon = 0.10
    kategori = "Gold"
elif total_belanja >= 100000.0:
    persen_diskon = 0.05
    kategori = "Silver"
else:
    persen_diskon = 0.0
    kategori = "Reguler"
potongan = total_belanja * persen_diskon
total_akhir = total_belanja - potongan

print(f"""
Kategori    : {kategori}
Potongan    : {potongan}
Total Bayar : {total_akhir}
""")


