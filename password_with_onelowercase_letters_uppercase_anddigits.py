import string
import secrets
alphabet = string.ascii_letters + string.digits
n=int(input("Enter the size of the password: "))
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(n))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
print(password)
