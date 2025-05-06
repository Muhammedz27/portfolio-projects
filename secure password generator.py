import random
import string
import time

# Secure password generation
def generate_secure_password(length=12):
    if length < 12:
        raise ValueError("Password must be at least 12 characters long")

    chars = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice(string.punctuation)
    )
    remaining = ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=length - 4
    ))

    password = list(chars + remaining)
    random.shuffle(password)
    return ''.join(password)

# Password strength checking
def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    length_ok = len(password) >= 12

    score = sum([has_upper, has_lower, has_digit, has_special, length_ok])

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Mild"
    else:
        return "Weak"

# OTP-based MFA system
def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    return otp

def verify_otp(real_otp, time_generated):
    user_otp = input("Enter the OTP: ")
    if time.time() - time_generated > 60:
        print("OTP has expired.")
        return False
    if user_otp == real_otp:
        print("OTP verified successfully.")
        return True
    else:
        print("Incorrect OTP.")
        return False

# Menu interface
def main():
    while True:
        print("\n--- Secure Password & MFA System ---")
        print("1. Generate a new password")
        print("2. Check password strength")
        print("3. Verify login using OTP")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            password = generate_secure_password()
            print(f"Generated secure password: {password}")
        elif choice == '2':
            password = input("Enter a password to check its strength: ")
            strength = check_password_strength(password)
            print(f"Password strength: {strength}")
        elif choice == '3':
            otp = generate_otp()
            print(f"Your OTP is: {otp} (valid for 60 seconds)")
            generated_time = time.time()
            verify_otp(otp, generated_time)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
