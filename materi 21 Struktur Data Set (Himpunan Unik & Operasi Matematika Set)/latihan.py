# Latihan materi 21 Struktur Data Set (Himpunan Unik & Operasi Matematika Set)
peserta_it_mentah = ["Andi", "Budi", "Citra", "Andi", "Beni"]
it_set = set(peserta_it_mentah)
data_set = {"Budi", "Citra", "Eka", "Fani"}
semua_peserta = it_set | data_set
peserta_ganda = it_set & data_set
khusus_it = it_set - data_set

print(f"""
Set It unik                     : {it_set}
Set Data                        : {data_set}
Seluruh peserta (Union)         : {semua_peserta}
Peserta ganda (Intersection)    : {peserta_ganda}
Peserta khusus IT (Difference)  : {khusus_it}
Total peserta unik              : {len(semua_peserta)}
""")

