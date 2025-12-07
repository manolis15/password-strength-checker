# 🔐 Password Strength Checker & Entropy Calculator

A Python-based tool that evaluates password strength based on entropy mathematics, dictionary attacks, and character set analysis. It supports both English and **Greek** characters.
## Features

-   **Entropy Calculation:** Calculates the mathematical difficulty (bits of entropy) based on the character pool size.
-   **Brute-Force Estimation:** Estimates how long it would take to crack the password using a brute-force attack (assuming 10 billion guesses/second).
-   **Multi-Language Support:** Specifically designed to handle **Greek characters** (Lower & Upper) correctly, increasing the entropy pool.
-   **Dictionary Attack Check:** Instantly flags passwords found in common password lists (e.g., `common_passwords.txt`).
-   **Input Validation:** Ensures only supported characters are used (English, Greek, Digits, Symbols).
## How it Works

The script analyzes the password using the formula:
> Combinations = (Pool Size) ^ (Password Length)

Where **Pool Size** adapts dynamically:
-   English Lowercase: +26
-   Greek Lowercase: +24
-   Numbers: +10
-   Symbols: +32
-   Mixed Case Bonus: etc.
## How to Run

1.  Clone the repository.
2.  Ensure python is installed
3.  Ensure `common_passwords.txt` is in the same folder.
4.  Run the script:
    ```bash
    python password_checker.py
    ```
