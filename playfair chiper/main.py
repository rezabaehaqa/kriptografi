def generate_playfair_key(key):
    # Membuat matriks 5x5 untuk kunci Playfair
    key = key.replace(" ", "").upper()  # Mengonversi kunci ke huruf kapital dan menghilangkan spasi
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Abaikan huruf 'J' (diganti dengan 'I')
    key_matrix = []

    # Mengisi matriks dengan huruf-huruf dari kunci
    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)

    # Mengisi sisa matriks dengan huruf-huruf yang tidak ada di kunci
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    # Membuat matriks 5x5 untuk Playfair Cipher
    playfair_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_char_position(matrix, char):
    # Mencari posisi karakter di dalam matriks Playfair
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_playfair(plain_text, key):
    playfair_matrix = generate_playfair_key(key)
    plain_text = plain_text.upper().replace(" ", "").replace("J", "I")  # Mengonversi teks ke huruf kapital dan mengganti 'J' dengan 'I'
    encrypted_text = ""
    i = 0

    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'  # Menggunakan 'X' jika panjang teks ganjil
        row1, col1 = find_char_position(playfair_matrix, char1)
        row2, col2 = find_char_position(playfair_matrix, char2)

        if row1 == row2:  # Jika karakter berada dalam baris yang sama
            encrypted_text += playfair_matrix[row1][(col1 + 1) % 5]
            encrypted_text += playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Jika karakter berada dalam kolom yang sama
            encrypted_text += playfair_matrix[(row1 + 1) % 5][col1]
            encrypted_text += playfair_matrix[(row2 + 1) % 5][col2]
        else:  # Jika karakter membentuk persegi
            encrypted_text += playfair_matrix[row1][col2]
            encrypted_text += playfair_matrix[row2][col1]

        i += 2

    return encrypted_text

def decrypt_playfair(cipher_text, key):
    playfair_matrix = generate_playfair_key(key)
    decrypted_text = ""
    i = 0

    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]
        row1, col1 = find_char_position(playfair_matrix, char1)
        row2, col2 = find_char_position(playfair_matrix, char2)

        if row1 == row2:  # Jika karakter berada dalam baris yang sama
            decrypted_text += playfair_matrix[row1][(col1 - 1) % 5]
            decrypted_text += playfair_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Jika karakter berada dalam kolom yang sama
            decrypted_text += playfair_matrix[(row1 - 1) % 5][col1]
            decrypted_text += playfair_matrix[(row2 - 1) % 5][col2]
        else:  # Jika karakter membentuk persegi
            decrypted_text += playfair_matrix[row1][col2]
            decrypted_text += playfair_matrix[row2][col1]

        i += 2

    return decrypted_text

def main():
    choice = int(input("Choose an option:\n1. Encrypt\n2. Decrypt\nEnter your choice: "))
    key = input("Enter the key for the Playfair cipher: ")

    if choice == 1:
        plain_text = input("Enter the plaintext: ")
        encrypted_text = encrypt_playfair(plain_text, key)
        print("Encrypted Text: " + encrypted_text)
    elif choice == 2:
        cipher_text = input("Enter the ciphertext: ")
        decrypted_text = decrypt_playfair(cipher_text, key)
        print("Decrypted Text: " + decrypted_text)
    else:
        print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")

if __name__ == '__main__':
    main()
