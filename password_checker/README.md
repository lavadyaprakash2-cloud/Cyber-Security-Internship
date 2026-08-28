# Task-03: Password Complexity Checker

## 📌 Description
Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

## 🔐 What it Checks
- *Length:* Minimum 8 characters (12+ is strong)
- *Uppercase:* A-Z
- *Lowercase:* a-z
- *Numbers:* 0-9
- *Special Characters:* !@#$%^&* etc.

## ✨ Features
- Checks password strength instantly
- Gives score: Weak / Moderate / Strong / Very Strong
- Provides feedback - em missing undo cheptadi
- Simple CLI tool

## ⚙️ How Strength is Calculated
- Length >= 8: +1 point
- Length >= 12: +1 point
- Has Uppercase: +1
- Has Lowercase: +1
- Has Number: +1
- Has Special Char: +1

Score:
0-2 = Weak 🔴
3-4 = Moderate 🟡
5 = Strong 🟢
6 = Very Strong 🔒

## 🚀 How to Run
```bash
python password_checker.py
## 💻 Example
Enter password: Hello123
Strength: Moderate (3/6)
Feedback:
- Add special character (!@#$)
- Increase length to 12+ for stronger password

Enter password: Hello@12345Strong
Strength: Very Strong (6/6)
Feedback: Excellent! Your password is very strong.
## 🛠️ Tech Stack
- Python 3.x
- re (regex) module

## 📁 File Structure
Task-03/
├── password_checker.py
└── http://README.md

## 👨‍💻 Author
[Your Name]
