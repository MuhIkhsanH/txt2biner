def binary_to_text(binary_data):
    # Pisahkan data biner menjadi setiap 8 bit dan konversi menjadi karakter ASCII
    text = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    return text

# Panggil fungsi binary_to_text dengan representasi biner yang ingin Anda konversi
binary_data = str(input("Masukkan Biner:")) # Contoh biner
text = binary_to_text(binary_data)
print("Teks:", text)

input('Enter to end...')
