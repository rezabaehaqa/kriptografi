from stegano import lsb

# Path gambar hasil steganografi
path_gambar_stegano = r'D:\kampus\semester 5\KRIPTOGRAFI\kriptografi\stigano\g.png'

# Membaca pesan yang disembunyikan
pesan_terungkap = lsb.reveal(path_gambar_stegano)

# Menampilkan pesan yang terungkap
print("Pesan yang terungkap:", pesan_terungkap)


