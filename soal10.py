def soal10(bayar, belanja):
    kembalian = bayar - belanja
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    hasil = {}
    for uang in pecahan:
        if kembalian >= uang:
            jumlah = kembalian // uang
            hasil[str(uang)] = jumlah
            kembalian -= uang * jumlah
    return hasil

bayar = int(input("\nTotal uang dibayarkan: "))
belanja = int(input("Total belanja: "))
print(f"Kembalian: {soal10(bayar, belanja)}")