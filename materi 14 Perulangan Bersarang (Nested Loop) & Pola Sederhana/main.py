# Perulangan Bersarang (Nested Loop) & Pola Sederhana
for baris in range(1,4):
    print(f"Baris ke-{baris}", end=" ")
    for kolom in range(1,4):
        print(f"kolom ke-{kolom}", end=" ")
    print() #pindah ke baris baru setelah loop dalam selesai
#(Catatan: Parameter end=" " pada fungsi print() berguna agar teks tidak langsung berganti baris, melainkan disambung dengan spasi).
# Contoh Kasus: Cetak Matriks Koordinat Grid Sederhana
for x in range(1,5):
    for y in range(1,4):
        print(f"({x},{y})", end=" ")
    print()

