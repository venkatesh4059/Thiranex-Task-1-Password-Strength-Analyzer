import re
import secrets
import string

# Optional: Simple mock database of previously used passwords
PREVIOUS_PASSWORDS = {"Password123!", "Admin2026#", "Welcome123$"}

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Check Previous Reuse (Database Check)
    if password in PREVIOUS_PASSWORDS:
        return 0, ["❌ Password has been used previously. Please choose a new password."], generate_alternative()

    # 2. Check Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password is too short (aim for at least 8–12 characters).")

    # 3. Check Complexity Requirements
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one uppercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one digit.")

    if re.search(r"[!@#$%^&*()_\-+=\[\]{}|;:,.<>?]", password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one special character (!@#$%...).")

    # 4. Rating Determination
    if score >= 6:
        rating = "Very Strong 💪"
    elif score >= 4:
        rating = "Moderate 🟡"
    else:
        rating = "Weak 🔴"

    # Generate a strong alternative if the score isn't maximum
    alternative = generate_alternative() if score < 6 else None

    return rating, feedback, alternative


def generate_alternative(length=14):
    """Generates a cryptographically secure random password."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    return "".join(secrets.choice(alphabet) for _ in range(length))


# Main Application Loop
if __name__ == "__main__":
    print("--- Password Strength Analyzer ---")
    user_input = input("Enter a password to test: ").strip()
    
    rating, suggestions, strong_alt = check_password_strength(user_input)
    
    print(f"\nPassword Strength: {rating}")
    
    if suggestions:
        print("\nSuggestions to Improve:")
        for note in suggestions:
            print(f"- {note}")
            
    if strong_alt:
        print(f"\n💡 Suggested Alternative: {strong_alt}")
