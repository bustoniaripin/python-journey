#Percabangan Bersarang (Nested if) & Validasi Data
saldo_rekening = 5000000.0
jumlah_tarik = float(input("Masukkan Jumlah Penarikan : "))

if jumlah_tarik > 0:
    #validasi 2 (nested):apakah saldo mecukupi
    if jumlah_tarik <= saldo_rekening:
        saldo_rekening -= jumlah_tarik #mengurangi saldo
        print(f"""
Penarikan berhasil
Jumlah penarikan : {jumlah_tarik}
Sisa saldo       : {saldo_rekening}
        """)
    else:
        print("Transaksi gagal: Saldo Anda tidak mencukupi.")
else:
    print("Transaksi gagl: Nominal penarikan harus lebih besar dari 0.")