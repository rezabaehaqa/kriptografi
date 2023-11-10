def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def affine_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                result += chr((key[0] * (ord(char) - 65) + key[1]) % 26 + 65)
            else:
                result += chr((key[0] * (ord(char) - 97) + key[1]) % 26 + 97)
        else:
            result += char
    return result

def affine_decrypt(ciphertext, key):
    result = ""
    mod_inverse = modinv(key[0], 26)
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                result += chr((mod_inverse * (ord(char) - 65 - key[1])) % 26 + 65)
            else:
                result += chr((mod_inverse * (ord(char) - 97 - key[1])) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("Program Affine Cipher")
    print("1. Enkripsi")
    print("2. Dekripsi")

    choice = int(input("Masukkan pilihan (1/2): "))
    if choice not in [1, 2]:
        print("Pilihan tidak valid. Keluar.")
        return

    plaintext = input("Masukkan plainteks: ")
    key_a = int(input("Masukkan kunci A (bilangan bulat yang relatif prima dengan 26): "))
    key_b = int(input("Masukkan kunci B (bilangan bulat): "))

    key = (key_a, key_b)

    if choice == 1:
        ciphertext = affine_encrypt(plaintext, key)
        print("\nTeks Terenkripsi: {}".format(ciphertext))
    elif choice == 2:
        decrypted_text = affine_decrypt(plaintext, key)
        print("\nTeks Terdekripsi: {}".format(decrypted_text))

if __name__ == "__main__":
    main()
