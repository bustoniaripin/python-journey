#latihan 8
'''
usia_penonton = int(input("Masukkan usia anda : "))
if usia_penonton >= 17:
    print("Akses Diberikan : Anda boleh menonton film kategori Dewasa (R-17)")
    harga_tiket = 50000.0
else:
    print("Akses Terbatas : Anda hanya boleh menonton film kategori Semua Umur (SU)")
    harga_tiket = 35000.0
print(f"Total yang harus dibayar : {harga_tiket}")
'''

#latihan 9
#INPUT USER
nama_mahasiswa = input("Masukkan Nama : ")
skor_angka = float(input("Masukkan Skor Angka : "))
#PERCABANGAN
if skor_angka >= 85.0:
    grade = "A"
    predikat = "Sangat Memuaskan"
elif skor_angka >= 75.0 and skor_angka < 85.0:
    grade = "B"
    predikat = "Memuaskan"
elif skor_angka >= 60.0 and skor_angka < 75.0:
    grade = "C"
    predikat = "Cukup"
elif skor_angka >= 50.0 and skor_angka < 60.0:
    grade = "D"
    predikat = "kurang"
else:
    grade = "E"
    predikat = "Gagal"

#boolean
lulus = grade != "E"

print(f"""
Nama Mahasiswa   : {nama_mahasiswa}
Skor Angka       : {skor_angka}
Grade            : {grade}
Predikat         : {predikat}
Status Kelulusan : {lulus}
""")