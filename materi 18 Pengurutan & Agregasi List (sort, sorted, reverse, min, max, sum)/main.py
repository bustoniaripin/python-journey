# Hari 18 Pengurutan & Agregasi List (sort, sorted, reverse, min, max, sum)
skor_siswa = [78,92,65,88,70]

# agresi data
terendah = min(skor_siswa)
tertinggi = max(skor_siswa)
total_nilai = sum(skor_siswa)
rata_rata = total_nilai / len(skor_siswa)

# mengurutkan list asli secara ascending
skor_siswa.sort()
print(f"""
Skor terendah : {terendah}
Skor tertinggi : {tertinggi}
Rata-rata kelas : {rata_rata}
Skor terurut (naik) : {skor_siswa}
""")
