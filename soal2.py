def soal2(kalimat):
    teks = ''.join(filter(str.isalnum, kalimat)).lower()
    return "eureeka!" if teks == teks[::-1] else "suka blyat"

print(soal2("Aku Suka Kamu"))
print(soal2("Ibu Ratna antar ubi"))