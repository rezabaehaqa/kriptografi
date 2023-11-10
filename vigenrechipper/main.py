def encrypt_vigenere(plain_text, keyword):
    encrypted_text = ""
    keyword_repeated = (keyword * (len(plain_text) // len(keyword))) + keyword[:len(plain_text) % len(keyword)]

    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            if plain_text[i].islower():
                encrypted_char = chr(((ord(plain_text[i]) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(plain_text[i]) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = plain_text[i]
        encrypted_text += encrypted_char

    return encrypted_text

def decrypt_vigenere(encrypted_text, keyword):
    decrypted_text = ""
    keyword_repeated = (keyword * (len(encrypted_text) // len(keyword))) + keyword[:len(encrypted_text) % len(keyword)]

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            if encrypted_text[i].islower():
                decrypted_char = chr(((ord(encrypted_text[i]) - ord('a') - shift + 26) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(encrypted_text[i]) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            decrypted_char = encrypted_text[i]
        decrypted_text += decrypted_char

    return decrypted_text

while True:
    print("Menu:")
    print("1. Enkripsi Teks")
    print("2. Dekripsi Teks")
    print("3. Keluar")

    choice = input("Pilih menu (1/2/3): ")

    if choice == '1':
        plain_text = input("Masukkan teks yang akan dienkripsi: ")
        keyword = input("Masukkan kata kunci: ")
        encrypted_text = encrypt_vigenere(plain_text, keyword)
        print("Teks terenkripsi:", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Masukkan teks terenkripsi: ")
        keyword = input("Masukkan kata kunci: ")
        decrypted_text = decrypt_vigenere(encrypted_text, keyword)
        print("Teks terdekripsi:", decrypted_text)
    elif choice == '3':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
