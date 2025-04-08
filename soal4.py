def soal4(data):
    return len(data) != len(set(data))

data = list(map(int, input("Masukkan angka (pisah dengan spasi): ").split()))
print(soal4(data))