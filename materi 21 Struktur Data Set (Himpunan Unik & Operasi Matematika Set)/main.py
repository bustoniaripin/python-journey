# materi 21 Struktur Data Set (Himpunan Unik & Operasi Matematika Set)
'''
Set adalah struktur data tidak berurutan (unordered) yang hanya menyimpan nilai unik (tidak boleh ada duplikasi). Set ditulis menggunakan kurung kurawal {...} atau fungsi set().

- Karakteristik Kunci Set:

- Unik: Nilai duplikat otomatis disingkirkan.

- Tidak Berurutan (Unordered): Tidak mendukung indexing (s[0] akan memicu error).

- Operasi Himpunan Matematika:

- Gabungan (Union): A | B atau A.union(B)

- Irisan (Intersection): A & B atau A.intersection(B)

- Selisih (Difference): A - B atau A.difference(B)
'''
# contoh kasus: membersihkan data duplikat & analisis minat
email_mentah = ['a@gmail.com', "b@gmail.com", "a@gmail.com", "c@gmail.com"]
# membersihkan daftar email yang duplikat
email_unik = set(email_mentah)
print(email_unik) #otomatis hanya 3 email unik

# Operasi himpunan minat bahasa pemrograman
kelas_python = {"toni", "Bus", "Budi", "Citra"}
kelas_javascript = {"Budi", "Dewi", "toni", "Citra"}

# siswa yang mengambil kedua kelas (irisan / intersection)
kedua_kelas = kelas_python.difference(kelas_javascript)
print("Ikut keduanya:", kedua_kelas)