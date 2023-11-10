def encrypt(text, key1, key2):
    result = []
    key1_length = len(key1)
    key2_length = len(key2)

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift1 = ord(key1[i % key1_length].lower()) - ord('a')
            shift2 = ord(key2[i % key2_length].lower()) - ord('a')
            if char.isupper():
                result.append(chr(((ord(char) - ord('A') + shift1 + shift2) % 26) + ord('A')))
            else:
                result.append(chr(((ord(char) - ord('a') + shift1 + shift2) % 26) + ord('a')))
        else:
            result.append(char)

    return ''.join(result)

def decrypt(text, key1, key2):
    result = []
    key1_length = len(key1)
    key2_length = len(key2)

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift1 = ord(key1[i % key1_length].lower()) - ord('a')
            shift2 = ord(key2[i % key2_length].lower()) - ord('a')
            if char.isupper():
                result.append(chr(((ord(char) - ord('A') - shift1 - shift2 + 26) % 26) + ord('A')))
            else:
                result.append(chr(((ord(char) - ord('a') - shift1 - shift2 + 26) % 26) + ord('a')))
        else:
            result.append(char)

    return ''.join(result)

def main():
    choice = input("Pilih 'E' untuk enkripsi atau 'D' untuk dekripsi: ")
    text = input("Masukkan teks: ")
    key1 = input("Masukkan kunci pertama: ")
    key2 = input("Masukkan kunci kedua: ")

    if choice == 'E' or choice == 'e':
        encrypted_text = encrypt(text, key1, key2)
        print("Teks terenkripsi:", encrypted_text)
    elif choice == 'D' or choice == 'd':
        decrypted_text = decrypt(text, key1, key2)
        print("Teks terdekripsi:", decrypted_text)
    else:
        print("Pilihan tidak valid. Silakan pilih 'E' atau 'D'.")

if __name__ == "__main__":
    main()
