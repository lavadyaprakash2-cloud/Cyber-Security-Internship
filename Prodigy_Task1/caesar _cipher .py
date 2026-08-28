def caesar_cipher(text, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift

    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # keep spaces, numbers, punctuation unchanged
    return result


def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice == "e":
        output = caesar_cipher(message, shift, "encrypt")
        print(f"Encrypted message: {output}")
    elif choice == "d":
        output = caesar_cipher(message, shift, "decrypt")
        print(f"Decrypted message: {output}")
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")


if __name__ == "__main__":
    main()