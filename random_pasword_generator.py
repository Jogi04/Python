import random
import string


def main_menu():
    print('Which characters do you want to include in the password?')
    print('1. Digits only')
    print('2. Digits and lowercase letters')
    print('3. Digits, lowercase letters and uppercase letters')
    print('4. Digits, lowercase letters, uppercase letters and special characters (recommended)')
    return int(input('Enter the number of your choice: ')), int(input('Enter the length for the password: '))


def generate(choice_of_chars, length):
    password = ''
    if choice_of_chars == 1:
        for i in range(length):
            password += random.choice(string.digits)
    elif choice_of_chars == 2:
        for i in range(length):
            password += random.choice(string.digits + string.ascii_lowercase)
    elif choice_of_chars == 3:
        for i in range(length):
            password += random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase)
    else:
        for i in range(length):
            password += random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
    return password


if __name__ == '__main__':
    character_choice, password_length = main_menu()
    print(generate(character_choice, password_length))
