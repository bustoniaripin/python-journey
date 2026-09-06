#materi 20 Struktur Data Tuple & Konsep Immutability
'''
Tuple adalah struktur data berurutan (ordered) yang sangat mirip dengan List, namun dengan satu perbedaan fundamental: Tuple bersifat immutable (tidak dapat diubah, ditambah, atau dihapus setelah dibuat). Tuple didefinisikan menggunakan tanda kurung biasa (...).

Karakteristik Kunci Tuple:

- Immutable: Operasi seperti t[0] = 99, .append(), atau .pop() akan menghasilkan TypeError.

- Keamanan Data: Cocok untuk data konstan yang tidak boleh dimodifikasi selama program berjalan (koordinat GPS, dimensi layar, konstanta konfigurasi).

- Hemat Memori & Cepat: Alokasi memori tuple lebih efisien dibanding list.

- Unpacking: Mengeluarkan elemen tuple langsung ke dalam variabel individual secara bersamaan.
'''
# contoh kasus : menyimpan koordinat GPS & Unpacking Data
# definisi koordinat: (latitude, longitude)
titik_lokasi = (-6.2088, 106.8456)

# mengakses via indeks
print(f"Latitude: {titik_lokasi[0]}")

# tuple unpacking (membongkar nilai ke variabel terpisah)
lat, lon = titik_lokasi
print(f"Hasil Unpack ->: {lat}, Lon: {lon}")

# mencoba mengubah tuple akan memicu error:
# titik_lokasi[0] = -6.9175 #ERROR: TypeError
