# latihan fungsi bawaan enumerate()
finalis = ["Andi", "Budi", "Citra", "Dewi", "Eko"]
for nomor_urut, nama_peserta in enumerate(finalis, start=1):
    id_peserta = f"REG-{nomor_urut:03d}"
    print(f"Nomor Urut : {nomor_urut} | ID : {id_peserta} | Nama Finalis : {nama_peserta}")
print(f"Total finalis yang terdaftar : {len(finalis)}")