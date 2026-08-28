from PIL import Image
import os

def encrypt_image(input_path, output_path, key=50):
    """Pixel manipulation tho encrypt"""
    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y][:3]
                # Basic math operation + swapping
                # Encrypt: (r,g,b) -> (255-r+key, 255-g+key, 255-b+key) and swap R and B
                new_r = (255 - r + key) % 256
                new_g = (255 - g + key) % 256
                new_b = (255 - b + key) % 256
                # swapping R and B
                pixels[x, y] = (new_b, new_g, new_r)
        
        img.save(output_path)
        print(f"[+] Encrypted and saved as: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path, key=50):
    """Decrypt - encrypt ki reverse operation"""
    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        for y in range(height):
            for x in range(width):
                b, g, r = pixels[x, y][:3] # because we swapped before
                # Reverse math
                orig_r = (255 - (r - key)) % 256
                orig_g = (255 - (g - key)) % 256
                orig_b = (255 - (b - key)) % 256
                pixels[x, y] = (orig_r, orig_g, orig_b)

        img.save(output_path)
        print(f"[+] Decrypted and saved as: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# --- Main Part ---
if __name__ == "__main__":
    print("Pixel Manipulation for Image Encryption")
    choice = input("Encrypt (e) or Decrypt (d)?: ").lower()
    input_img = input("Input image path (ex: test.jpg): ")
    output_img = input("Output image path (ex: encrypted.jpg): ")
    key = int(input("Enter key (number 1-100, default 50): ") or 50)

    if choice == 'e':
        encrypt_image(input_img, output_img, key)
    elif choice == 'd':
        decrypt_image(input_img, output_img, key)
    else:
        print("Invalid choice!")