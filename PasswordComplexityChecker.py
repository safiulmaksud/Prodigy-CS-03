import re

def check_password_complexity(password):
    # Defines regular expressions for checking different password criteria
    has_lowercase = re.search(r'[a-z]', password)
    has_uppercase = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*()-+=]', password)
    
    # Check if all criteria are met
    if (has_lowercase and has_uppercase and 
        has_digit and has_special and len(password) >= 8):
        return True
    else:
        return False

# Testing the function
password = input("Enter your password: ")
if check_password_complexity(password):
    print("Password is complex enough.")
else:
    print("Password is not complex enough. It should have at least 8 characters, including uppercase, lowercase, digits, and special characters.")