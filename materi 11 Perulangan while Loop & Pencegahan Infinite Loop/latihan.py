#Latihan Perulangan while Loop & Pencegahan Infinite Loop
volume_air = 0
nomor_siklus = 0

while volume_air <= 85:
    nomor_siklus += 1
    volume_air +=15
    print(f"Siklus ke-{nomor_siklus}: Menambahkan 15L | Volume air saat ini: {volume_air} Liter")

sisa_ruang = 100- volume_air 

print(f"""
Total siklus pengisian yang dilakukan   : {nomor_siklus}
Volume air akhir didalam tangki         : {volume_air} Liter
Sisa kapasitas tangki yang masih kosong : {sisa_ruang} Liter
""")



