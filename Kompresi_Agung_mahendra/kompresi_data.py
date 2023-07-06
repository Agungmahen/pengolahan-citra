def encode_rle(data):
    encoded_data = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded_data += str(count) + data[i - 1]
            count = 1
    encoded_data += str(count) + data[-1]
    return encoded_data

def decode_rle(encoded_data):
    decoded_data = ""
    for i in range(0, len(encoded_data), 2):
        count = int(encoded_data[i])
        character = encoded_data[i + 1]
        decoded_data += count * character
    return decoded_data

# Contoh penggunaan
data = "AGUNGMAHENDRAAAMMMG"
encoded_data = encode_rle(data)
print("Encoded data:", encoded_data)
decoded_data = decode_rle(encoded_data)
print("Decoded data:", decoded_data)
