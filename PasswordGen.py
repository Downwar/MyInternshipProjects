import random
import string

def generate_password(length=12):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+=-[]{}|;:'\",.<>?/"
    all_characters = lowercase + uppercase + digits + special_characters

    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def generate_passwords(num_passwords, length=12):
    passwords = []
    for i in range(num_passwords):
        password = generate_password(length)
        if password:
            passwords.append(password)
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    passwords = generate_passwords(num_passwords, password_length)

    if passwords:
        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)
    else:
        print("Password generation failed. Please check your input.")
