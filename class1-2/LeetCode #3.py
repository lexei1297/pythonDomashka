import random
import string


def generate_password():
    # Ask the user for the desired password length
    length = int(input("Enter the password length: "))

    # Define the character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + numbers + symbols

    # Make sure the password contains at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to make it random
    random.shuffle(password)

    # Join the list into a single string and return it
    return ''.join(password)


# Example usage
print("Your generated password is:", generate_password())