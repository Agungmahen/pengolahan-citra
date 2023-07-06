import numpy as np
import matplotlib.pyplot as plt

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

# Membuat citra acak
image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)

# Peregangan kontras pada citra
stretched_image = stretch_contrast(image)

# Menampilkan citra asli dan hasil peregangan kontras
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Citra Asli')
ax[0].axis('off')
ax[1].imshow(stretched_image, cmap='gray')
ax[1].set_title('Hasil Peregangan Kontras')
ax[1].axis('off')

# Menampilkan plot
plt.show()
