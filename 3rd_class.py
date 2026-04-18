# print("-" * 20)
# print("BMI Calculator")
# print("-" * 20)
# weight = float(input("Enter your weight in kg: \n"))
# height_in_feets = float(input("Enter your height in feet:\n"))
# height_in_meters = height_in_feets / 3.281
# bmi = weight / (height_in_meters ** 2)
# # round function , round(number, no_of_digits_to_round)
# bmi = round(bmi,2)
# print(f"Your BMI is: {bmi}")

# Number Manipulations
# score = 5
# print(score)
# score = score + 1
# score += 4
# print(score)
# score =- 3
# print(score)
# score *= 10
# print(score)
# score /= 5
# print(score)

# f string
# score = 5
# height = 6.1
# is_wining = True
#
# print(f"Your score is: {score}, your height is: {height}, and you are wining: {is_wining}")
# # the below code will run as above
# print("Your score is:" + score + "your height is: " + height + "and you are wining:" + is_wining)
#

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
print("Welcome to the Park")
age = int(input("What is your age?"))
# >, <, ==, !=, >=, <=
if age >=18:
    print("You have to buy a full ticket.")
elif age > 5 and age < 18:
    print("You have to buy a half ticket.")
else:
    print("You are free.")

