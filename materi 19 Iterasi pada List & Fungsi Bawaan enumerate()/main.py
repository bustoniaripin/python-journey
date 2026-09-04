# materi 19 Iterasi pada List & Fungsi Bawaan enumerate()
# iterasi biasa
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(item)

# iterasi dengan enumerate()
# fungsi bawaan enumerate() mengembalikan pasangan (indeks), nilai
# default indeks mulai dari 0
# contoh kasus

list_nama = ["Bustoni", "Alfina", "Rumaisha"]

# enumerate dengan start= 1
for nomor, nama in enumerate(list_nama, start=1):
    print(f"{nomor}. Nama : {nama}")
