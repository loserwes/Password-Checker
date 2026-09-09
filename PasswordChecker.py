import re

def check_password_strength(password: str) -> dict:
    feedback = []
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long (12+ recommended).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    rating = "Weak"  
    if score >= 6:
        rating = "Very Strong"
    elif score >= 4:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"

    return {
        "is_valid": not feedback,
        "score": score,
        "rating": rating,
        "feedback": feedback
    }

if __name__ == "__main__":
    user_password = input("Enter a password to test: ")
    result = check_password_strength(user_password)

    print(f"\n--- Password Analysis ---")
    print(f"Rating: {result['rating']} (Score: {result['score']}/6)")

    if result["is_valid"]:
        print("Success: Password meets all security requirements!")
    else:
        print("Suggestions for improvement:")
        for tip in result["feedback"]:
            print(f"- {tip}")
