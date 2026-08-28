def check_password_strength(password):
    feedback = []
    score = 0

    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password length at least 8 undali")

    # 2. Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("❌ Oka capital letter (A-Z) add chey")

    # 3. Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("❌ Oka small letter (a-z) add chey")

    # 4. Number check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("❌ Oka number (0-9) add chey")

    # 5. Special character check
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("❌ Oka special character (@,#,$,%) add chey")

    # Strength decide cheyadam
    if score == 5:
        strength = "VERY STRONG 🔥"
    elif score >= 3:
        strength = "MEDIUM / MODERATE ⚠️"
    else:
        strength = "WEAK ❌"

    return score, strength, feedback

# Main program
print("=== Password Complexity Checker ===")
user_pass = input("Enter your password: ")

score, strength, feedback = check_password_strength(user_pass)

print(f"\nPassword: {user_pass}")
print(f"Score: {score}/5")
print(f"Strength: {strength}")

if feedback:
    print("\nSuggestions:")
    for msg in feedback:
        print(msg)
else:
    print("\nPerfect! Nee password chala strong ga undi.")