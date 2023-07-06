import heapq
import os
from PIL import Image


# Node untuk membangun pohon Huffman
class HuffmanNode:
    def __init__(self, intensity, frequency):
        self.intensity = intensity
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


# Fungsi untuk menghitung frekuensi intensitas piksel dalam citra
def calculate_frequency(image):
    frequency = [0] * 256
    width, height = image.size

    for y in range(height):
        for x in range(width):
            intensity = image.getpixel((x, y))
            frequency[intensity] += 1

    return frequency


# Fungsi untuk membangun pohon Huffman
def build_huffman_tree(frequency):
    heap = []

    for i in range(256):
        if frequency[i] > 0:
            node = HuffmanNode(i, frequency[i])
            heapq.heappush(heap, node)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged_frequency = node1.frequency + node2.frequency
        merged_node = HuffmanNode(None, merged_frequency)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(heap, merged_node)

    return heap[0]


# Fungsi rekursif untuk menghasilkan kode Huffman untuk setiap intensitas piksel
def generate_huffman_codes(node, code, huffman_codes):
    if node.intensity is not None:
        huffman_codes[node.intensity] = code
        return

    generate_huffman_codes(node.left, code + "0", huffman_codes)
    generate_huffman_codes(node.right, code + "1", huffman_codes)


# Fungsi untuk mengompresi citra menggunakan kode Huffman
def compress_image(image, huffman_codes):
    compressed_data = ""

    width, height = image.size
    for y in range(height):
        for x in range(width):
            intensity = image.getpixel((x, y))
            compressed_data += huffman_codes[intensity]

    padding = 8 - len(compressed_data) % 8
    compressed_data += padding * "0"  # Menambahkan padding nol untuk memastikan panjang data terkompresi adalah kelipatan 8

    # Mengonversi data terkompresi menjadi byte array
    compressed_bytes = bytearray()
    for i in range(0, len(compressed_data), 8):
        byte = compressed_data[i:i + 8]
        compressed_bytes.append(int(byte, 2))

    return compressed_bytes, padding


# Fungsi untuk menulis data terkompresi ke file
def write_compressed_data(compressed_data, output_path):
    with open(output_path, "wb") as file:
        file.write(compressed_data)


# Path file gambar
image_path = 'img.webp'

# Membuka gambar
image = Image.open(image_path)

# Menghitung frekuensi intensitas piksel dalam citra
frequency = calculate_frequency(image)

# Membangun pohon Huffman
huffman_tree = build_huffman_tree(frequency)

# Membangkitkan kode Huffman untuk setiap intensitas piksel
huffman_codes = {}
generate_huffman_codes(huffman_tree, "", huffman_codes)

# Mengompresi citra menggunakan kode Huffman
compressed_data, padding = compress_image(image, huffman_codes)

# Menyimpan data terkompresi ke file
output_path = 'path/ke/file_terkompresi.bin'
write_compressed_data(compressed_data, output_path)

print("Kompresi selesai.")


