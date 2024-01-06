import string
import secrets
import re

alphabet = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        n = int(input("Enter the size of the password: "))
        if n < 3 or n > 40:
            print("Password size should be between 3 and 40.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

password_requirements = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{3,}$')

while True:
    password = ''.join(secrets.choice(alphabet) for _ in range(n))
    if password_requirements.match(password):
        break

print(password)
