from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util import Counter

#constants
KEY = b"aesexamplekey123"      #16-byte ASCII key
IV = b"initialvector123"       #16-byte ASCII IV / initial value

#images
INPUT_IMAGE = "linux-logo.png" 
ECB_OUTPUT = "ecb_encrypted.png"
CBC_OUTPUT = "cbc_encrypted.png"
CTR_OUTPUT = "ctr_encrypted.png"

#print first 32 bytes
def print_first_32(label, data):
    first_32 = data[:32]
    print(f"{label} first 32 bytes:")
    print(first_32)
    print()

#saves the encrypted image
def save_encrypted_image(ciphertext, width, height, original_len, output_name):
    # Use only first N bytes where N = number of original pixel bytes
    truncated = ciphertext[:original_len]
    encrypted_img = Image.frombytes("RGB", (width, height), truncated)
    encrypted_img.save(output_name)

#encryption functions for each mode
def encrypt_ecb(pixel_bytes):
    padded = pad(pixel_bytes, AES.block_size)
    cipher = AES.new(KEY, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    return ciphertext

#CBC mode requires padding and an IV
def encrypt_cbc(pixel_bytes):
    padded = pad(pixel_bytes, AES.block_size)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(padded)
    return ciphertext

#CTR mode does not require padding, but we need to set up a counter
def encrypt_ctr(pixel_bytes):
    # Use the same 16-byte value as the initial counter value
    initial_value = int.from_bytes(IV, byteorder="big")
    ctr = Counter.new(128, initial_value=initial_value)
    cipher = AES.new(KEY, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(pixel_bytes)
    return ciphertext

#main function to execute the steps
def main():
    #part 1: Load and preprocess image
    img = Image.open(INPUT_IMAGE).convert("RGB")
    width, height = img.size
    pixel_bytes = img.tobytes()

    print("Image width:", width)
    print("Image height:", height)
    print("Number of pixel bytes:", len(pixel_bytes))
    print()

    #part 2: ECB
    ecb_ciphertext = encrypt_ecb(pixel_bytes)
    print_first_32("ECB", ecb_ciphertext)
    save_encrypted_image(ecb_ciphertext, width, height, len(pixel_bytes), ECB_OUTPUT)

    #part 3: CBC
    cbc_ciphertext = encrypt_cbc(pixel_bytes)
    print_first_32("CBC", cbc_ciphertext)
    save_encrypted_image(cbc_ciphertext, width, height, len(pixel_bytes), CBC_OUTPUT)

    #part 4: CTR
    ctr_ciphertext = encrypt_ctr(pixel_bytes)
    print_first_32("CTR", ctr_ciphertext)
    save_encrypted_image(ctr_ciphertext, width, height, len(pixel_bytes), CTR_OUTPUT)

    print("Done.")
    print(f"Saved: {ECB_OUTPUT}, {CBC_OUTPUT}, {CTR_OUTPUT}")


if __name__ == "__main__":
    main()
