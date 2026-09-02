# A. Membuat & Mengakses List(Indexing & Slicing)
buah = ["apel","pisang","jeruk","mangga"]

# Mengakses berdasarkan index
print(buah[0]) #output : apel (Elemen pertama)
print(buah[-1]) #output : mangga (Elemen terakhir)

#Slicing (mengambil sebagian elemen) -> [start:stop]
print(buah[1:3]) #outpu : ['pisang','jeruk'] (index 1 sampai sebelum 3)

########################################################################
#Menambahkan Elemen ke List
'''
Ada 3 cara profesional untuk menambah data:
.append(nilai) : Menambahkan elemen ke posisi paling akhir.
.insert(index, nilai) : Menyelipkan elemen ke posisi index tertentu.
.extend(list_lain) : Menggabungkan list lain ke dalam list saat ini.
'''
stok = ["Laptop","Mouse"]

stok.append("Keyboard")
stok.insert(1,"Monitor")
stok.extend(["Headset", "Mic"])
print(stok)
########################################################################
#.C. Menghapus Elemen dari List
'''
1. .remove(nilai) : Menghapus berdasarkan nilai/isi datanya.
2. .pop(index) : Menghapus berdasarkan index dan mengembalikan/mengambil nilai yang dihapus. Jika index diosongkan, akan menghapus elemen paling akhir.
3. del list[index] : Menghapus elemen pada index tertentu menggunakan keyword del.
4. .clear() : Mengosongkan seluruh isi list.
'''
angka = [10,9,8,7,6,5]

angka.remove(5)
dihapus = angka.pop(4) #menghapus index 4 (6). variabel 'dihapus berisi 6
del angka [1]
print(angka)
print(dihapus)

#D. Meng-copy List (PENTING! Sering Jadi Bug)
'''
Di Python, menulis list_b = list_a BUKAN mengcopy, melainkan membuat dua variabel menunjuk ke alamat memori yang sama. Jika list_b diubah, list_a ikut berubah!
Cara mengcopy yang benar (pilih salah satu):
1. .copy() (Metode resmi)
2. list_a[:] (Slicing)
'''
#cara salah
a = [1,2,3]
b = a
b.append(4) # variabel a akan ikut berubah
print(a)

#cara benar 
c = [1,2,3,4]
d = c.copy()
d.append(5)
print(c)
print(d)

#E. Method List Penting Lainnya
'''
1. .sort() : Mengurutkan list secara ascending (A-Z / kecil ke besar). Tambahkan reverse=True untuk descending.
2. .reverse() : Membalik urutan elemen list.
3. len(list) : Menghitung jumlah total elemen di dalam list.
4. nilai in list : Cek apakah suatu nilai ada di dalam list (menghasilkan True/False).
'''

#.Contoh Kasus Riil: Sistem Manajemen Inventaris Gudang

#Inisialiasi Inventaris Awal
inventaris_lama = ["Komputer","Laptop","Printer"]
inventaris_baru = inventaris_lama.copy()

#Penambahan Inventaris
inventaris_baru.append("Server")
inventaris_baru.append("Mouse")
inventaris_baru.insert(0,"Scanner")

#Barang Rusak / Keluar
barang_rusak = inventaris_baru.pop(1) #inventaris pada index satu akan di hapus dan akan masuk pada variabel 'barang_rusak'

#cek ketersediaan
ada_barang = "Printer" in inventaris_baru

#Urutkan sesuai abjad
inventaris_baru.sort()

print(f"Daftar Inventaris lama ({len(inventaris_lama)} Item): {inventaris_lama}")
print(f"Barang Rusak dipindahkan : {barang_rusak}")
print(f"Daftar Invertaris Baru ({len(inventaris_baru)} Item) : {inventaris_baru}")
print(f"Apakah Ada Printer di Inventaris : {ada_barang}")





