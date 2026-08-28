Task-02 README:
# Task-02: Pixel Manipulation for Image Encryption

## 📌 Description
Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

## 🔐 Concept
Image pixels ni direct ga change chestam:
- RGB values swap cheyadam
- Prathi pixel ki key add / XOR cheyadam
- Pixel positions shuffle cheyadam

Key lekunda original image raadu.

## ✨ Features
- Any JPG/PNG encrypt & decrypt
- Key-based simple encryption
- RGB channel manipulation

## ⚙️ How It Works
1. Image ni PIL tho load chey
2. Pixel data teesuko (R,G,B)
3. Operation apply: encrypted = (original + key) % 256
4. Decryption ki reverse: decrypted = (encrypted - key) % 256

## 🚀 How to Run
```bash
pip install Pillow numpy
python image_encrypt.py
Input:
- image path: cat.jpg
- key: 80
- encrypt / decrypt

## 💻 Example
Enter image path: cat.jpg
Enter key: 80
-> Encrypted saved as encrypted_cat.jpg
## 🛠️ Tech Stack
- Python 3.x, Pillow, NumPy

## 📁 File Structure
Task-02/
├── image_encrypt.py
└── http://README.md
