# PASSWORD GENERATOR APP

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
    '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>',
    ',', '.', '?', '/', '~', '`'
]

import random
print("Welcome to the Python Password Generator!")

no_of_letters = int(input("How many letters would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))

# Method 1: with string
# password = ''
#
# for char in range(no_of_letters):
#     password += random.choice(letters)
#     # print(f"the password variable contains: {password}")
# for num in range(no_of_numbers):
#     password += random.choice(numbers)
#
# for symbol in range(no_of_symbols):
#     password += random.choice(special_characters)
#
# print(f"Your generated password is:  {password}")


# method 2 with list
password = []

for char in range(no_of_letters):
    password.append(random.choice(letters))
    # print(f"the password list contains: {password}")
for num in range(no_of_numbers):
    password.append(random.choice(numbers))

for symbol in range(no_of_symbols):
    password.append(random.choice(special_characters))

random.shuffle(password)
shuffled_password = "".join(password)
# print(f"Your generated password is:  {password}")
print(f"Your generated password is:  {shuffled_password}")

