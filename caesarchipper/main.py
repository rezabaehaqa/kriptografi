def caesar_cipher(text, shift, operation):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if operation == "1":
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif operation == "2":
                new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char

    return result

while True:
    print("Pilih operasi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    choice = input("Masukkan nomor operasi yang Anda inginkan: ")

    if choice == "3":
        break
    elif choice in ["1", "2"]:
        text = input("Masukkan teks: ")
        shift = int(input("Masukkan jumlah pergeseran (biasanya 3): "))
        if choice == "1":
            encrypted_text = caesar_cipher(text, shift, "1")
            print("Teks terenkripsi:", encrypted_text)
        elif choice == "2":
            decrypted_text = caesar_cipher(text, shift, "2")
            print("Teks terdekripsi:", decrypted_text)
    else:
        print("Pilihan tidak valid. Silakan pilih 1 (enkripsi), 2 (dekripsi), atau 3 (keluar).")
