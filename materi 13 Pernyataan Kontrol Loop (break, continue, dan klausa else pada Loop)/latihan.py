transaksi_diproses = 0
for nomor_transaksi in range(1,11):
    if nomor_transaksi % 2 == 0:
        continue
    if nomor_transaksi == 9:
        print(f"Transaksi {nomor_transaksi}: Batas limit tercapai! Sistem berhenti.")
        break
    transaksi_diproses += 1
    print(f"Transaksi {nomor_transaksi}: Berhasil diproses.")
print(f"Jumlah transakasi yang berhasil di proses {transaksi_diproses}")