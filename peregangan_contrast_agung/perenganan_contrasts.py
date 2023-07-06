import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def stretch_contrast(image, r_min=0, r_max=255):
    """
    Fungsi untuk melakukan peregangan kontras pada citra.
    
    Parameters:
        image (numpy.ndarray): Citra dalam bentuk array numpy.
        r_min (int): Rentang minimum yang diinginkan (default: 0).
        r_max (int): Rentang maksimum yang diinginkan (default: 255).
    
    Returns:
        numpy.ndarray: Citra hasil peregangan kontras.
    """
    # Normalisasi rentang pixel citra
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = (image - min_val) * ((r_max - r_min) / (max_val - min_val)) + r_min
    return stretched_image.astype(np.uint8)

# Baca gambar kustom
image_path = 'img.webp'  # Ganti dengan path gambar Anda
image = np.array(Image.open(image_path)) 

# Peregangan kontras pada citra
# Peregangan kontras pada citra dengan rentang kontras 50 hingga 200
stretched_image = stretch_contrast(image, r_min=300, r_max=200)


# Menampilkan citra asli dan hasil peregangan kontras
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image)
ax[0].set_title('Citra Asli')
ax[0].axis('off')
ax[1].imshow(stretched_image, cmap='gray')
ax[1].set_title('Hasil Peregangan Kontras')
ax[1].axis('off')

# Menampilkan plot
plt.show()
