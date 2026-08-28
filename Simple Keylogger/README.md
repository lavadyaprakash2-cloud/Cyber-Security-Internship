markdown# Task-04: Simple Keylogger (Educational Purpose)

## 📌 Description
Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file.

> ⚠️ **ETHICAL DISCLAIMER:** This project is strictly for educational purposes and to understand how keyloggers work. Use it ONLY on your own device with your own permission. Unauthorized use on others' devices without consent is illegal and unethical.

## 🔐 What is a Keylogger?
A keylogger is a program that captures and records keystrokes typed on a keyboard. In cybersecurity, it's studied to understand threats and to build defenses.

**Legitimate Uses:**
- Parental control (with consent)
- Monitoring your own system
- Cybersecurity research & awareness

## ✨ Features
- Records all key presses (letters, numbers, special keys)
- Saves logs to a text file (`keylog.txt`)
- Handles special keys: Space, Enter, Backspace etc.
- Stops on ESC key

## ⚙️ How It Works
1. Listens to keyboard events using `pynput`
2. On each key press, writes the character to a file
3. Runs in background until user stops it

## 🚀 How to Run (Only on your own PC)

```bash
pip install pynput
python keylogger.pyType something, it will be logged to keylog.txtPress ESC to stop logging💻 Example LogjavascriptH e l l o [Space] W o r l d [Enter]
test@gmail.com [Enter]🛠️ Tech StackPython 3.xpynput library📁 File StructureTask-04/
├── keylogger.py
├── keylog.txt (generated after running)
└── README.md⚠️ Ethical NoteNever use this on someone else's system without explicit written permissionThis is for Prodigy Infotech internship learning purpose onlyMisuse can lead to legal action👨‍💻 Authorjavascript


Code kuda kavala? Neeku ethical version (only logs with visible console warning) code ichesta.
