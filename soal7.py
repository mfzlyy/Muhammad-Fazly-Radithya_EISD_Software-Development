def soal7(chat):
    hasil = ''
    for huruf in chat:
        if huruf.isalpha():
            geser = chr((ord(huruf) - ord('a') + 5) % 26 + ord('a'))
            hasil += geser
        else:
            hasil += huruf
    return hasil

chat = input("Masukkan chat terenkripsi: ").lower()
print(f"Isi chat: {soal7(chat)}")