from PIL import Image
import heapq
import os


class HuffmanNode:
    def __init__(self, intensity, frequency):
        self.intensity = intensity
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def calculate_frequency(image):
    frequency = {}
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel in frequency:
                frequency[pixel] += 1
            else:
                frequency[pixel] = 1
    return frequency


def build_huffman_tree(frequency):
    heap = []
    for intensity, freq in frequency.items():
        node = HuffmanNode(intensity, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)

        merged_node = HuffmanNode(None, left_node.frequency + right_node.frequency)
        merged_node.left = left_node
        merged_node.right = right_node

        heapq.heappush(heap, merged_node)

    return heapq.heappop(heap)


def generate_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.intensity is not None:
        huffman_codes[node.intensity] = current_code
        return

    generate_huffman_codes(node.left, current_code + "0", huffman_codes)
    generate_huffman_codes(node.right, current_code + "1", huffman_codes)


def compress_image(image, huffman_codes):
    compressed_data = ""
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            compressed_data += huffman_codes[pixel]
    return compressed_data


def pad_compressed_data(compressed_data):
    padding_amount = 8 - len(compressed_data) % 8
    padded_data = compressed_data + padding_amount * "0"
    padded_data = "{0:08b}".format(padding_amount) + padded_data
    return padded_data


def convert_to_bytes(padded_data):
    bytes_array = bytearray()
    for i in range(0, len(padded_data), 8):
        byte = padded_data[i:i + 8]
        bytes_array.append(int(byte, 2))
    return bytes_array


def compress_image_huffman(image_path):
    image = Image.open(image_path).convert("L")  # Mengonversi gambar ke skala keabuan (grayscale)
    frequency = calculate_frequency(image)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = {}
    generate_huffman_codes(huffman_tree, "", huffman_codes)
    compressed_data = compress_image(image, huffman_codes)
    padded_data = pad_compressed_data(compressed_data)
    bytes_array = convert_to_bytes(padded_data)
    return bytes_array


# Contoh penggunaan
image_path = "img.webp"
compressed_data = compress_image_huffman(image_path)
print("Compressed data:", compressed_data)
image = Image.open(image_path)
image.show()
modified_image_path = 'terkompresi.webp'
image.save(modified_image_path)
print("Gambar berhasil disimpan.")
