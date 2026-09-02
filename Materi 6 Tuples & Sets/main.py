#Tuples & Sets
#. A.tuple
nama = ("bustoni","alfina","arifin")

#mengaksesnya sama seperti list
print(nama[0])

#jika dicoba
# nama[0] = "fina" #hasil akan error


#. B. Set (himpunan data unik & tanpa urutan)
#contoh pendaftar (banyak data duplikat)
pendaftar = ["bustoni","arifin","alfina","bustoni","rumaisha","arifin"]
#mengubah list menjadi set untuk menghilangkan duplikat secara instan
nama = set(pendaftar)
print(nama)
#Menambah & menghapus di set
nama.add("fina")
nama.remove("arifin")
print(nama)

#latihan
# 1
info_event = ("workshop python","15 Agustus 2026","Hall A")
# 2
log_absensi = ["p-001","p-002","p-001","p-003","p-002","p-004","p-001"]
peserta_unik = set(log_absensi)

#output
print(f"Nama Event {info_event[0]} dan Lokasinya {info_event[2]}")
print(f"Total jumlah tap kartu {len(log_absensi)}")
print(f"Jumlah peserta asli yang hadir {len(peserta_unik)}")




