# Hari 20: Struktur Data Tuple & Konsep Immutability
'''
Tantangan Latihan Hari 20

- Sebuah server aplikasi menyimpan konfigurasi awal koneksi database dalam bentuk Tuple agar nilainya aman dan tidak sengaja terubah oleh proses lain:

- Data konfigurasi terdiri dari: ("localhost", 5432, "admin_db", True)

* Elemen 0: Host (str)

* Elemen 1: Port (int)

* Elemen 2: Username (str)

* Elemen 3: Status SSL Aktif (bool)

* Kerjakan instruksi berikut:

- Buat variabel tuple bernama konfigurasi_db yang berisi keempat elemen di atas.

- Ambil nilai host menggunakan indeks pertama ([0]) dan simpan di variabel host_cek.

- Ambil nilai port menggunakan indeks kedua ([1]) dan simpan di variabel port_cek.

- Lakukan Tuple Unpacking pada konfigurasi_db ke dalam 4 variabel baru sekaligus: host, port, user, dan ssl_aktif.

- Hitung total elemen di dalam tuple menggunakan fungsi len() (simpan di total_pengaturan).

- Tampilkan ringkasan konfigurasi ke layar menggunakan f-string:

* Host (dari hasil indexing)

* Port (dari hasil indexing)

* Hasil Unpack: Host, Port, User, dan Status SSL

* Total Pengaturan

Tipe data dari variabel konfigurasi_db menggunakan type()
'''
konfigurasi_db = ("localhost", 5432, "admin_db", True)
host_cek = konfigurasi_db[0]
port_cek = konfigurasi_db[1]
host, port, user, ssl_aktif = konfigurasi_db
total_pengaturan = len(konfigurasi_db)

# tampilan print
print(f"""
Host                    : {host_cek}
Port                    : {port_cek}
Hasil Unpack: Host, Port, User, dan Status SSL  : {host}, {port}, {user}, {ssl_aktif}
Total Pengaturan        : {total_pengaturan}
Tipe data dari variabel : {type(konfigurasi_db)}
""")



