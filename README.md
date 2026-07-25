# Task-1-Password-Strength-Analyzer
A Python tool that evaluates password strength using length, complexity, and entropy checks, while preventing reuse and suggesting strong alternatives.  Topics/Tags: cybersecurity, python, password-security, cryptography, thiranex-internship
# 🔐 Password Strength Analyzer

A Python-based utility that evaluates user-entered passwords against security best practices, checks for password reuse using a database, and generates cryptographically secure alternatives.

Developed as part of the **Thiranex Cyber Security Internship**.

---

## 🚀 Key Features
- **Length & Complexity Evaluation:** Checks for minimum length, uppercase, lowercase, digits, and special characters using Regex.
- **Password Reuse Prevention:** Integrated database simulation to prevent users from reusing past passwords.
- **Secure Alternative Generator:** Generates strong, high-entropy password recommendations using Python's `secrets` module.
- **Detailed Feedback:** Provides actionable steps for users to improve their password security.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Modules:** `re` (Regular Expressions), `secrets`, `string`

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/venkatesh4059/Thiranex-Task-1-Password-Strength-Analyzer.git
   python password_analyzer.py
