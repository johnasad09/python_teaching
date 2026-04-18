# CONTROL FLOW, CONDITIONAL OPERATORS, IF ELSE
# if condition:
#     do this
# elif condition:
#     do this
# else:
#     do this
# park entry ticket free < 5 years
# < 18 yrs, half ticket
# > 18 yrs full ticket
# print("Welcome to the Park")
# age = int(input("What is your age?"))

# with logical operators
# if age <= 5:
#     print("You are free")
# elif age > 5 and age < 18:
#     print("You will pay half ticket")
# elif age >= 18 and age <= 120:
#     print("You will pay full ticket")
# else:
#     print("Please enter your correct age.")

# with nested- if/else
# if age <= 5:
#     print("You are free.")
# elif age > 5:
#     if age < 18:
#         print("You will pay half ticket.")
#     elif age > 120:
#         print("Please enter your correct age.")
#     else:
#         print("You will pay full ticket")
#

# checks if the even or odd
# number = int(input("Enter an integer"))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")



# Randomization

# import asad
# import random
# generates a random integer between range.
# print(random.randint(1,100))

# generates a random number between 0.0 and 1.0
# print(random.random())

# print(asad.my_name)
# print(asad.full_name)

import random
head = 0
tail = 1
head_or_tail = random.randint(head,tail)
if head_or_tail == 0:
    print("heads")
else:
    print("tails")
