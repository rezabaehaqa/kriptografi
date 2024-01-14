from stegano import lsb

def ekstrak_pesan(gambar_tersembunyi):
    # Ekstrak pesan dari gambar menggunakan metode LSB (Least Significant Bit)
    pesan_tersembunyi = lsb.reveal(gambar_tersembunyi)
    return pesan_tersembunyi

# Contoh penggunaan
gambar_tersembunyi = "Screenshot_20231210-061822_Lite.jpg.png"
pesan_tersembunyi = ekstrak_pesan(gambar_tersembunyi)

print("Pesan Tersembunyi:", pesan_tersembunyi)