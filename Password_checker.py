import string

def check_password_strength(password):
    score = 0
    length = len(password)

    # Criteria checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Length scoring
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 17:
        score += 1
    if length >= 20:
        score += 1

    # Character type scoring (each type counts as one point)
    score += sum([has_upper, has_lower, has_digit, has_special])

    # Provide feedback based on score
    if score <= 2:
        strength = "Weak"
    elif 3 <= score <= 4:
        strength = "Moderate"
    elif 5 <= score <= 6:
        strength = "Good"
    else:
        strength = "Strong"

    return strength

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
