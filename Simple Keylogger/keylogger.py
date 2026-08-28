from datetime import datetime

print("=== Safe Keylogger Demonstration ===")
print("This program records only the text entered in this terminal.")
print("Type 'exit' to stop.\n")

with open("keystrokes.txt", "a", encoding="utf-8") as file:
    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"[{timestamp}] {text}\n")
        file.flush()

print("\nLogging stopped.")
print("Keystrokes have been saved to keystrokes.txt")