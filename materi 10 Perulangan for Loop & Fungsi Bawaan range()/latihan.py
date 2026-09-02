#LATIHAN
jarak_hari_ini = 3.0
total_akumulasi_jarak = 0.0
for i in range(1,8):
    total_akumulasi_jarak += jarak_hari_ini
    print(f"Hari ke-{i}: {jarak_hari_ini} km | Total Sementara: {total_akumulasi_jarak} km")
    jarak_hari_ini += 2.5
   

rata_rata_jarak = total_akumulasi_jarak / 7
print(f"""
Total jarak tempuh selama 7 hari = {total_akumulasi_jarak}
Rata-rata jarak lari perhari = {rata_rata_jarak}
""")

jarak_hari_ini = 3.0
total_akumulasi_jarak = 0.0
jumlah_hari = 7

for i in range(1, jumlah_hari + 1):
    total_akumulasi_jarak += jarak_hari_ini
    print(f"Hari ke-{i}: {jarak_hari_ini:.1f} km | Total Sementara: {total_akumulasi_jarak:.1f} km")
    jarak_hari_ini += 2.5

rata_rata_jarak = total_akumulasi_jarak / jumlah_hari

print(f"""
Total jarak tempuh selama {jumlah_hari} hari = {total_akumulasi_jarak:.1f} km
Rata-rata jarak lari per hari = {rata_rata_jarak:.2f} km
""")