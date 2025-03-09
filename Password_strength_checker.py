import re


def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[@$!%*?&]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    score = 5 - sum(errors)

    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return strength[score]


password = input("Enter a password: ")
print(f"Password Strength: {check_password_strength(password)}")