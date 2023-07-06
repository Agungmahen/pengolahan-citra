import cv2
import numpy as np

# membaca citra
img = cv2.imread('Agung.jpg')

# mengambil dimensi citra
rows, cols = img.shape[:2]

# membuat matriks transformasi untuk translasi
M = np.float32([[2, 0, 50], [0, 1, 50]])

# melakukan translasi menggunakan cv2.warpAffine
translated_img = cv2.warpAffine(img, M, (cols, rows))

# menampilkan citra asli dan hasil translasi
cv2.imshow('Original Image', img)
cv2.imshow('Translated Image', translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()