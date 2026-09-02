#Method String Tingkat Lanjut (replace, split, join, find, count)
'''
Method String Penting:

teks.replace(lama, baru) : Mengganti semua kemunculan teks tertentu dengan teks baru.

teks.split(pemisah) : Memecah string menjadi pecahan list berdasarkan karakter pemisah tertentu.

pemisah.join(daftar_teks) : Menggabungkan sekumpulan teks menjadi satu string dengan penyambung tertentu.

teks.find(target) : Menemukan indeks posisi pertama dari target (mengembalikan -1 jika tidak ditemukan).

teks.count(target) : Menghitung berapa kali suatu karakter atau kata muncul.
'''
'''
# contoh
data_tag = "python, belajar_coding, data_science, python"
# 1. menghitung frequensi
jumlah_python = data_tag.count("python")
# 2. mengganti karakter garis bawah '_' menjadi '-'
tag_rapi = data_tag.replace('_','-')
# 3. memecah string berdasarkan koma dan spasi ', '
list_tag = tag_rapi.split(", ")
# 4. menggabungkan kembali dengan tanda pagar / hashtag
tag_final = "#" + " #".join(list_tag)

print(f"Data awal : {data_tag}")
print(f"Data bersih : {tag_rapi}")
print(f"Hasil split : {list_tag}")
print(f"Format tag = {tag_final}")
print(f"Kata 'python' muncul sebanyak : {jumlah_python}")
'''

'''
#latihan
# 1.buat variabel
log_transaksi = "TRX9988_LAPTOP_SUKSES_LAPTOP_2026"
# 2. hitung jumlah kata "pyton"
frekuensi_laptop = log_transaksi.count("LAPTOP")
# 3. menemukan posisi index dari kata 'SUKSES
posisi_sukses = log_transaksi.find("SUKSES")
# 4. MENGGGANTI KATA "LAPTOP" => "MACBOOK"
log_update = log_transaksi.replace("LAPTOP", "MACBOOK")
# 5. PECAH VARIABEL LOG_UPDATE BERDASARKAN TANDA GARIS BAWAH
pecahan_log = log_update.split("_")
# 6.gabung kembali pecahan data dengan spasi ' - '
log_gabung = " - ".join(pecahan_log)

print(f"Log transaksi = {log_transaksi}")
print(f"Frekuensi Laptop = {frekuensi_laptop}")
print(f"Posisi sukses = {posisi_sukses}")
print(f"Log update = {log_update}")
print(f"Pecahan log = {pecahan_log}")
print(f"Log Gabung = {log_gabung}")
'''

'''
#latihan gabungan fase 1
# 1. buat variabe;
tiket_mentah = " GA-JKT-DPS-2026"
# 2.bersihkan spasi
tiket_bersih = tiket_mentah.strip()
# 3. ambil data slicing
maskapai = tiket_bersih[0:2]
asal = tiket_bersih[3:6]
tujuan = tiket_bersih[7:10]
# 4.input user
jumlah_penumpang = int(input("Jumlah Penumpang : "))
harga_dasar = float(input("Harga Dasar Tiket : "))
# 5. perhitungan keuangan
subtotal = jumlah_penumpang * harga_dasar
#pajak 11%
pajak = subtotal * 0.11
#total bayar
total_bayar = subtotal + pajak

# 6.dapat promo
dapat_promo = jumlah_penumpang >= 3 and total_bayar > 3000000.0
# 7. Format tampilan tiket
rute_tujuan = asal + " -> " + tujuan

# print(f'''
# Kode Maskapai    : {maskapai}
# Rute penerbangan : {rute_tujuan}
# Jumlah Penumpang : {jumlah_penumpang}
# Subtotal         : {subtotal}
# Pajak            : {pajak}
# Total Bayar      : {total_bayar}
# Status Promo     : {dapat_promo}
''')
'''

#Latihan remidial
# 1.buat variabel
kode_sewa_mentah = " AVZ-BDG-JKT-2026 "
# 2.bersihkan spasi
kode_sewa_bersih = kode_sewa_mentah.strip()
# 3.slicing
jenis_mobil = kode_sewa_bersih[0:3]
kota_ambil = kode_sewa_bersih[4:7]
kota_kembali = kode_sewa_bersih[8:11]
# 4.input pengguna
lama_hari = int(input("Lama Hari : "))
tarif_harian = float(input("Tarif Sewa Perhari : "))
# 5.hitung keuangan
biaya_dasar = lama_hari * tarif_harian
asuransi = biaya_dasar * 0.05
total_tagihan = biaya_dasar + asuransi
# 6.Evaluasi fasilitas tambahan
bonus_sopir_gratis = lama_hari > 5 and total_tagihan > 2500000.0
# 6.gabungkan variabel
rute_sewa = kota_ambil + " ke " + kota_kembali
#cetak ringkasan
print(f'''
Jenis Mobil               : {jenis_mobil}
Rute Sewa                 : {rute_sewa}
Lama Hari Sewa            : {lama_hari}
Biaya Dasar               : {biaya_dasar}
Biaya Asuransi (5%)       : {asuransi}
Total Tagihan             : {total_tagihan}
Status Bonus Sopir Gratis : {bonus_sopir_gratis}
''')







