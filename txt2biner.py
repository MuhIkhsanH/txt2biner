def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data


text = str(input("Masukkan Text:"))
binary_representation = text_to_binary(text)
print("Teks:", text)
print("Biner:", binary_representation)
input('Enter to end...')

