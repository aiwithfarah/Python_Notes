# Password Strength Validator: Write a function that checks a password string.
#  It must be at least 8 characters long, contain a number, and contain an uppercase letter.
#  Return True or False.

def password_strength_validator(password):

    if len(password) < 8:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_upper = (char.upper() for char in password)

    if has_digit and has_upper:
        return True
    else:
        return False


x = password_strength_validator("Python2025")
r = password_strength_validator("arah")
print(x)
print(r)
