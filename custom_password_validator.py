import string

def validate_password(password: str) -> str:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)  # ✅ strict symbol check

    score = 0
    feedback = []

    # Length rules
    if length < 8:
        feedback.append("Password is too short (minimum 8 characters).")
    elif length >= 12:
        score += 2
    else:
        score += 1

    # Character variety
    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if has_digit:
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if has_symbol:
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%).")

    # Final status
    if score <= 2:
        status = "Weak"
    elif 3 <= score <= 4:
        status = "Moderate"
    elif score == 5:
        status = "Strong"
    else:
        status = "Very Strong"

    # Output status + feedback
    return status, feedback


if __name__ == "__main__":
    pwd = input("Enter a password to validate: ")
    status, feedback = validate_password(pwd)
    print(f"\nPassword Strength: {status}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f" - {f}")
