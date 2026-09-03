# Hari 18 Pengurutan & Agregasi List (sort, sorted, reverse, min, max, sum)
transaksi_mingguan = [150000, 450000, 80000, 320000, 210000, 510000, 120000]

# agresi
transaksi_terkecil = min(transaksi_mingguan)
transaksi_terbesar = max(transaksi_mingguan)
total_omset = sum(transaksi_mingguan)
rata_rata_transaksi = total_omset / len(transaksi_mingguan)

# buat variabel baru yang berisi hasil pengurutan data dari besar ke kecil (desecending) menggunakan fungsi sorted(..., reverse=True) sehingga data list asli transaksi_mingguan tidak berubah.
transaksi_tertinggi_ke_rendah = sorted(transaksi_mingguan, reverse=True)

print(f"""
Transaksi terkecil   : {transaksi_terkecil}
Transaksi terbesar   : {transaksi_terbesar}
Total omset          : {total_omset}
Rata-rata transaksi  : {rata_rata_transaksi}
List asli            : {transaksi_mingguan}
List terurut menurun : {transaksi_tertinggi_ke_rendah}
""")