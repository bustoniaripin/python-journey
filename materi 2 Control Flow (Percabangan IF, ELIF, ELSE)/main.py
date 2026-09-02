'''
username = input("Masukkan username : ")
password = input("Masukkan password : ")

if username == "bus" and password == "1234":
    print("Login")
elif username == "bus" and password != "1234":
    print("password salah")
else:
    print("akun tidak ditemukan")


# total belanja
total_belanja = 200000
if total_belanja >= 200000:
    diskon = 0.20
    print(f"anda dapat potongan 20%")
elif total_belanja >= 150000:
    diskon = 15000
    print(f"anda dapat diskon 15%")
else:
    diskon = 0
    print(f"anda tidak mendapatkan diskon")
potongan = total_belanja * diskon
total = total_belanja - potongan
print(f"total yang harus dibayar {total}")



saldo = 2000000
tarik_tunai = 200000
if saldo >= tarik_tunai:
    print(f"anda tarik tunai sebesar Rp {tarik_tunai:,}".replace(",","."))
else:
    print("saldo anda tidak cukup")
sisa_saldo = saldo - tarik_tunai
print(f"sisa saldo anda Rp {sisa_saldo:,}".replace(",","."))


harga_laptop = 8000000
jumlah_beli = 1
pajak = 0.11 #11%

total_sebelum_pajak = harga_laptop * jumlah_beli
total_pajak = total_sebelum_pajak * pajak
total_bayar = total_sebelum_pajak + total_pajak
print(f"total bayar = {total_bayar}")



# kasus parkir
parkir_perjam = 3500
lama_parkir = 12
admin = 2000
biaya_parkir = parkir_perjam * lama_parkir + admin
print(f"biaya parkir anda {biaya_parkir}")



# kasus sembako
jumlah_butir_telur = 105
kapasitas_kotak = 10
jumlah_kotak = jumlah_butir_telur // kapasitas_kotak
sisa_telur = jumlah_butir_telur % kapasitas_kotak
print(f"jumlah kotak yang diperlukan {jumlah_kotak} dan sisa telurnya {sisa_telur}")


# kasus perbandingan harga
harga_toko_A = 25000
harga_toko_B = 27000
toko_a_lebih_murah = harga_toko_A < harga_toko_B
print(f"harga toko a lebih murah dari toko b = {toko_a_lebih_murah}")

# kasus kelayakan kredit
gaji_perbulan = 6000000
umur = 19
status_kredit = gaji_perbulan > 6000000 and umur > 21
print(f"status kelayakan kredit anda = {status_kredit}")
'''
'''
total_belanja = 250000
status_member = True

# menentukan diskon
if total_belanja >= 500000:
    diskon = 0.20
elif total_belanja >= 200000 and status_member:
    diskon = 0.10 #khusus member yang belanja >=200000
elif total_belanja >= 100000:
    diskon = 0.05 #khusus bukan member yang belanja >= 100000
else :
    diskon = 0.0
potongan_diskon = total_belanja * diskon
total_bayar = total_belanja - potongan_diskon

print(f"Total belanja :Rp {total_belanja:,}".replace(",","."))
print(f"Diskon        :Rp {int(potongan_diskon):,}".replace(",","."))
print(f"Total Bayar   :Rp {int(total_bayar):,}".replace(",","."))
'''

# TARIF TOL OTOMATIS
jenis_kendaraan = "sedan"
metode_pembayaran = "e-money"

# aturan tarif dasar
if jenis_kendaraan == "bus":
    tarif_dasar = 15000
elif jenis_kendaraan == "sedan":
    tarif_dasar = 10000
elif jenis_kendaraan == "truk":
    tarif_dasar = 25000
else:
    tarif_dasar = 0
    print("Jenis kendaraan tidak dikenal")

# aturan casback / diskon
if metode_pembayaran == "e-money":
    diskon = 0.10
elif metode_pembayaran == "tunai":
    diskon = 0

cashback = diskon * tarif_dasar
total = tarif_dasar - cashback
print(f"Jenis kendaraan : {jenis_kendaraan}")
print(f"Tarif dasar     : Rp {tarif_dasar}")
print(f"Casback         : Rp {cashback:.0f}")
print(f"Total dibayar   : Rp {total:.0f}")













