# Task-01: Caesar Cipher Encryption & Decryption

## 📌 Description
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. The program allows users to input a message and a shift value to perform encryption and decryption.

## 🔐 What is Caesar Cipher?
Caesar Cipher is one of the simplest encryption techniques. Each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

Example: With shift 3, `A` becomes `D`, `B` becomes `E`, etc.

## ✨ Features
- Encrypt any text with custom shift value
- Decrypt cipher text back to original
- Handles uppercase, lowercase, and preserves spaces/symbols
- User-friendly input

## ⚙️ How It Works
- **Encryption:** `encrypted_char = (original_char + shift) % 26`
- **Decryption:** `decrypted_char = (encrypted_char - shift) % 26`

## 🚀 How to Run

1. Clone the repo
```bash
git clone https://github.com/your-username/your-repo.git
Run the programbashpython caesar_cipher.pyEnter your choice:Type encrypt to encryptType decrypt to decryptEnter message and shift value💻 ExamplejavascriptEnter message: Hello World
Enter shift: 3
Encrypted: Khoor Zruog

Enter message: Khoor Zruog
Enter shift: 3
Decrypted: Hello World🛠️ Tech Stack
Python 3.x📁 File StructurejavascriptTask-01/
├── caesar_cipher.py
└── README.md👨‍💻 Authorjavascript
---

Code kuda kavala? Nenu Python code kuda ready chesi ista Task-01 ki.
