# Install modul stegano
!pip install stegano

from google.colab import files
from stegano import lsb
from PIL import Image

# Fungsi untuk mengunggah file gambar
def upload_image():
    uploaded = files.upload()
    file_name = list(uploaded.keys())[0]
    return file_name

# Mengunggah file gambar
image_file = upload_image()

# Mengekstrak pesan rahasia dari gambar hasil steganografi
revealed_message = lsb.reveal(Image.open(image_file))

# Menampilkan pesan rahasia yang diekstrak
print("Pesan Rahasia / ekstrak :", revealed_message)