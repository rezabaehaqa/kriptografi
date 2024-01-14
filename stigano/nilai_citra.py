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
nama_file_gambar = 'zoom.png'

# Baca gambar dari objek byte
gambar_byte = uploaded['zoom.png']

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