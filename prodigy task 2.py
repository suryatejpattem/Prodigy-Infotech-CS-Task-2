from PIL import Image

def encrypt_image(image, shift):
    width, height = image.size
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            new_r = (r + shift) % 256
            new_g = (g + shift) % 256
            new_b = (b + shift) % 256
            pixels[x, y] = (new_r, new_g, new_b)

    return image

def decrypt_image(image, shift):
    width, height = image.size
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            new_r = (r - shift) % 256
            new_g = (g - shift) % 256
            new_b = (b - shift) % 256
            pixels[x, y] = (new_r, new_g, new_b)

    return image

def main():
    image_path = input("Enter the image file path: ")
    shift = int(input("Enter the shift value (for encryption and decryption): "))
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ")
    
    image = Image.open(image_path)
    
    if choice == 'e':
        encrypted_image = encrypt_image(image, shift)
        encrypted_image.save("encrypted_image.png")
        print("Image encrypted and saved as 'encrypted_image.png'.")
        
    elif choice == 'd':
        decrypted_image = decrypt_image(image, shift)
        decrypted_image.save("decrypted_image.png")
        print("Image decrypted and saved as 'decrypted_image.png'.")
        
    else:
        print("Invalid choice! Please choose 'e' or 'd'.")

main()
