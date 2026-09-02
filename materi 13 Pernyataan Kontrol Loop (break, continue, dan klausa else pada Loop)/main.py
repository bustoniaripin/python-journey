# Contoh Kasus: Sistem Pemindai Barang & Deteksi Barang Rusak
# Lewati barang cacat (continue), hentikan jika barang berbahaya ditemukan (break)

for nomor_paket in range(1,6):
    if nomor_paket == 2:
        print(f"Paket nomor #{nomor_paket}: Rusak, lewati pengecekan.")
        continue
    if nomor_paket == 5:
        print(f"Paket nomor #{nomor_paket}: Berbahaya, hentikan pengecekan.")
        break
    print(f"Paket nomor #{nomor_paket}: Lulus uji pengecekan")