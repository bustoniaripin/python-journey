# MENGIRIM EMAIL SECARA MASAL
# .CONTOH
'''
for i in range(1,4):
    print(f"Email Notifikasi ke pengguna ke-{i}")

#.Contoh Kasus 2: Percobaan Pengisian PIN ATM
kesempatan = 3
while kesempatan > 0:
    print(f"Sisa Percobaan masukan PIN : {kesempatan}")
    kesempatan = kesempatan - 1
print("Kartu ATM Terblokir..")

#.Contoh Kasus 3: Pencarian Data (break) & Filter (continue)
for angka in range(1,6):
    if angka % 2 == 0:
        continue #jika angka genap akan di skip
    print(f"Angka ganjil : {angka}")
'''
total_pengeluaran = 0
for i in range(1,6):
    if i % 2 == 0:
        jam_kerja = 9
    else:
        jam_kerja = 7
    
    # hitung gaji
    if jam_kerja < 8:
        gaji = jam_kerja * 50000
    else:
        gaji = (8 * 50000) + ((jam_kerja - 8) * 75000)
    total_pengeluaran +=gaji
    print(f"Karyawan ke - {i}, Jam kerja : {jam_kerja}, gaji : Rp {gaji:,}")
print(f"{"-"*47}")
print(f"Total pengeluaran Gaji Perusahaan : Rp {total_pengeluaran:,}")









