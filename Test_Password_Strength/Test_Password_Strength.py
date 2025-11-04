import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (e.g., !, @, #, $).")

    # Determine strength
    if score <= 2:
        strength = "Weak"
        color = "\033[91m"  # Red
    elif score == 3 or score == 4:
        strength = "Moderate"
        color = "\033[93m"  # Yellow
    else:
        strength = "Strong"
        color = "\033[92m"  # Green

    # Reset color
    reset = "\033[0m"

    # Display results
    print("\n🔐 Password Strength:", color + strength + reset)
    if feedback:
        print("\nSuggestions for improvement:")
        for tip in feedback:
            print("-", tip)

# Main Program
print("=== PASSWORD STRENGTH TESTER ===")
password = input("Enter your password: ")

check_password_strength(password)
