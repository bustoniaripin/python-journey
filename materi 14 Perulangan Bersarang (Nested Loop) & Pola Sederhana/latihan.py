# Hari 14: Perulangan Bersarang (Nested Loop) & Pola Sederhana
'''
total_kursi_tercetak = 0
for baris in range(1,5):
    for kursi in range(1,6):
        print(f"B{baris}-K{kursi}",end=" ")
        total_kursi_tercetak += 1
    print()
print(f"Total kursi yang tercetak : {total_kursi_tercetak}")

'''
'''
# latihan gabungan
saldo_pengguna = 50000.0
stok_minuman = 0
harga_minuman = 10000.0
while True :
    pengguna = input("Masukkan pilihan : ")
    if pengguna == "1" :
        if stok_minuman == 0:
            print("Transaksi gagal: Stok minuman habis")
            break
        elif saldo_pengguna >= harga_minuman:
            stok_minuman -= 1
            saldo_pengguna -= harga_minuman
            print("Pembelian berhasil: Silahkan ambil minuman.")
        else:
            print("Transaksi gagal: Saldo anda tidak mencukupi.")
            break
    elif pengguna == "2":
        print("Terimakasih telah menggunakan layanan kami.")
        break
    else:
        print("Pilihan tidak valid, silahkan coba lagi.")
        continue
print(f"sisal saldo = {saldo_pengguna}")
print(f"stok minuman = {stok_minuman}")
'''
'''
# latihan remidial
saldo_dompet = 75000.0
stok_voucher = 2
harga_paket = 25000.0
while True:
    print(f"""
Saldo Dompet = {saldo_dompet}
stok Voucher = {stok_voucher} 
""")
    pilihan_pengguna = input("Masukkan pilihan : ")
    if pilihan_pengguna == "1":
        if stok_voucher == 0:
            print("Transaksi gagal: Stok voucher habis.")
            break
        else:
            if saldo_dompet >= harga_paket:
                stok_voucher -=1
                saldo_dompet -= harga_paket
                print("Pembelian berhasil: Paket internet aktif.")
            else:
                print("Transaksi gagal: Saldo dompet tidak cukup.")
                break
    elif pilihan_pengguna == "2":
        print("Terimakasih telah bertransaksi.")
        break
    else:
        print("Pilihan Tidak valid.")
print(f"Sisa Saldo Akhir = {saldo_dompet}")
print(f"Sisa stok voucher = {stok_voucher}")
'''

# remidial 2
saldo = 100000.0
sisa_kursi = 2
harga_tiket = 40000.0
while True:
    print(f"Saldo : {saldo}")
    print(f"Sisa kursi : {sisa_kursi}")
    pilihan_pengguna = input("Masukkan pilihan : ")
    if pilihan_pengguna == "1":
        if sisa_kursi == 0:
            print("Tiket Habis!.")
        else:
            if saldo >= harga_tiket:
                sisa_kursi -= 1
                saldo -= harga_tiket
                print("Tiket berhasil dipesan.")
            else:
                print("Saldo tidak cukup!.")

    elif pilihan_pengguna == "2":
        print("Sesi Selesai.")
        break
    else:
        print("Menu tidak valid.")

print(f"Saldo Akhir = {saldo}")
print(f"Sisa Kursi  = {sisa_kursi}")
    





