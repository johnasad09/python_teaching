# while loop
# while True:
#     name = input("What's your name")
#     num = int(input("What's the number?"))
#     if num > 0:
#         break
#
# for _ in range(num):
#     print(name, num)

# ls = [1,2,3,4,5]
# print(len(ls))
#
# def main():
#     is_even()
#
#
# def is_even():
#     n = int(input("Enter number"))
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# main()

# function parameters / arguments
# def main():
#     number = get_number()
#     show_name(number)
#
# def get_number():
#     while True:
#         n = int(input("Enter n"))
#         if n > 0:
#             break
#     return n
#
# def show_name(x):
#     for _ in range(x):
#         print("Hello")
#
# main()
# function with default parameter
# def hello(user="world"):
#     print("Hello", user)
#
# hello()
# name = input("Enter your name?")
# hello(name)

# def is_even(n):
#     # if n % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     # return True if n % 2 == 0 else False
#     return n % 2 == 0
#
# x = int(input("What's x? "))
# if is_even(x):
#     print("Even")
# else:
#     print("odd")

# fizz buzz
# if divisible by 3 print fizz
# if divisible by 5 print buzz
# if divsible by 5 and 3 FizzBuzz


for n in range(1,20):
    if n % 5== 0 and n % 3 == 0:
        print(n, "FizzBuzz")
    elif n % 3 == 0:
        print(n, "Fizz")
    elif n % 5 == 0:
        print(n, "Buzz")

# task
# put this in a function
# call it in a main function
