# Password Strength Evaluation

## Overview
This repository contains a Python project to evaluate and understand password security. The goal is to learn what makes a password strong, test passwords of varying complexity, and summarize best practices for creating secure passwords.

---

## Objective
- Understand factors that contribute to password strength.
- Test passwords using a custom Python validator.
- Learn best practices for creating strong passwords.
- Explore common password attacks and how complexity mitigates them.

---

## Features
- **Password validation script** that evaluates:
  - Length
  - Use of uppercase and lowercase letters
  - Numbers
  - Special characters
- Provides **strength status**: Weak, Medium, Strong, Very Strong.
- Offers **feedback suggestions** for improving password security.

---

## Sample Passwords Tested
| Password                   | Strength      | Feedback                                           |
|----------------------------|---------------|--------------------------------------------------|
| abc123                     | Weak          | Too short, lacks symbols/uppercase               |
| longpassword               | Weak          | Only lowercase, predictable                      |
| P@ssw0rd!23                | Strong        | Good mix of upper/lower/number/symbols          |
| Xy!92@fG#Lm7Z              | Very Strong   | Excellent complexity and length                  |
| Sunshine!Rocks_2025#Cloud  | Very Strong   | Secure passphrase, difficult to guess           |

---

## 🚀 How to Run

### 1. Use Online Strength Checkers

* [Password Meter](https://passwordmeter.com)
* [Kaspersky Password Checker](https://password.kaspersky.com/)

### 2. Run the Password Validator in your Python environment

* Execute the following command in your terminal: python password_validator.py
*  Enter Your Password
- When prompted, type your password.
- The tool will provide:
  - **Strength Status** (Weak / Medium / Strong / Very Strong)
  - **Improvement Suggestions**

## Dependencies
- Python 3.11
- Standard Python libraries:
  - `string`

---

## Best Practices Learned
- Use at least **12 characters**.
- Include **uppercase, lowercase, digits, and symbols**.
- Avoid dictionary words or common passwords.
- Use **passphrases** for stronger and memorable passwords.
- Do not reuse passwords across accounts.
- Consider using a **password manager** to generate random secure passwords.

---

## Common Password Attacks
- **Brute Force Attack:** Tries all possible combinations.
- **Dictionary Attack:** Uses a list of common passwords to guess.
- **Phishing / Social Engineering:** Tricks users into revealing passwords.
- **Credential Stuffing:** Reuses leaked credentials on multiple sites.

> Strong and complex passwords greatly reduce vulnerability to these attacks.

---

## Summary
This project demonstrates that **password complexity and length are critical for security**.  
By testing various passwords and analyzing their strengths, users can understand what makes a password strong and adopt best practices to protect their accounts.

---

## Author
**Baji Shaik**

## License
This project is licensed under the MIT License.  
© 2025 Baji Shaik

