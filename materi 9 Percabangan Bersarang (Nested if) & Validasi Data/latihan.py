#latihan 10
#input user
usia_pengunjung = int(input("Masukkan Usia Anda : "))
tinggi_pengunjung = float(input("Masukkan Tinggi Anda : "))
#pemeriksaan usia
if usia_pengunjung >= 15:
    #jika usia >= 15, pemeriksaan tinggi badan.
    if tinggi_pengunjung >= 150.0:
        boleh_naik = True
        pesan_keamanan = "Izin Diberikan: Selamat menikmati wahana."
    else:
        boleh_naik = False
        pesan_keamanan = "Ditolak: Tinggi badan kurang dari 150cm."

else:
    boleh_naik = False
    pesan_keamanan = "Ditolak : Usia belum mencukupi (minimal 15 tahun)."

#output
print(f"""
usia              : {usia_pengunjung}
Tinggi Badan      : {tinggi_pengunjung}
Status Boleh Naik : {boleh_naik}
Catatan Petugas   : {pesan_keamanan}
""")


