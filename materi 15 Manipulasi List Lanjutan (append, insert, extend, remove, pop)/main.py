# Manipulasi List Lanjutan (append, insert, extend, remove, pop)
antrean = ["Budi","Siti"]

# menambahkan file baru kebelakang
antrean.append("Agus")

# menyisipkan pelanggan prioritas kepaling depan (indeks 0)
antrean.insert(0,"Bustoni")

# menggabungkan rombongan baru ke antrean
antrean.extend(["Alfina","Rumaisha"])

# pelanggan batal antre berdasarkan nama
antrean.remove("Budi")

# melayani pelanggan paling depan dan mengambil namanya
pelanggan_dilayani = antrean.pop(0)

print(f"Pelanggan dilayani : {pelanggan_dilayani}")
print(f"Sisa antrean : {antrean}")