from google.colab import files
from PIL import Image
import cv2
import numpy as np
import io
import matplotlib.pyplot as plt

# Meminta pengguna untuk mengunggah file
uploaded = files.upload()

# Ambil nama file gambar dari dictionary 'uploaded'
# Gantilah 'nama_gambar.jpg' dengan nama file yang sesuai
nama_file_gambar = list(uploaded.keys())[0]

# Baca gambar dari objek byte
gambar_byte = uploaded[nama_file_gambar]

# Konversi objek byte menjadi objek gambar menggunakan PIL
gambar = Image.open(io.BytesIO(gambar_byte))

# Konversi gambar PIL menjadi array NumPy
gambar_array = np.array(gambar)

# Menampilkan nilai piksel dari gambar
print("Nilai Piksel Gambar:")
print(gambar_array)

# Menampilkan gambar asli
print("\nGambar Asli:")
plt.imshow(gambar_array)
plt.axis('off')
plt.show()

# Gantilah ini dengan gambar hasil rekonstruksi
gambar_rekonstruksi = gambar_array

# Hitung nilai MSE
mse = np.sum(np.square(gambar_array - gambar_rekonstruksi)) / (gambar_array.shape[0] * gambar_array.shape[1])

# Hitung nilai PSNR
max_pixel_value = 255  # Jika gambar dalam skala 0-255
psnr = 10 * np.log10(max_pixel_value**2 / mse)

# Tampilkan hasil perhitungan
print("\nNilai MSE:", mse)
print("Nilai PSNR:", psnr)
