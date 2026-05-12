# saving /writing data to a file
# names = []
# for _ in range(2):
#     name = input("Enter your name: ")
#     names.append(name)
#
# for name in names:
#     print(f"Name: {name}")

# name = input("Enter your name: ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# reading a file
# with open("names.txt",) as file:
#     # print(file.readlines())
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

# with open("names.txt") as file:
#     for line in file:
#         print(f"Hello {line.strip()}!")

# content = {"name": "asad", "roll_no":12}
# with open("contents.txt", "a") as file:
#     file.write(str(content))

# import json
#
# content = {"name": "asad", "roll_no":12}
#
# with open("con.txt", "a") as file:
#     file.write(json.dumps(content))

# functions - parameters
# *args
# def add(*args):
#     return sum(args)
#
# print(add(2))
# print(add(2,3))
# print(add(2,3,5,4,10))

# def names(**kwargs):
#     return kwargs
#
# print(names(hello="hello", name="asad", age=28))

# ANONYMOUS FUNCTION
# lambda functions
# double = lambda x: x * 2
# print(double(5))

# add = lambda x,y,z: x + y + z
# print(add(5,10, 20))

# high order functions
# def apply_operation(func, x, y):
#     return func(x, y)
#
# def add(a,b):
#     return a+b
#
# def multiply(a,b):
#     return a*b
#
# print(apply_operation(add,2,5))

# a = [1,2,3]
# b = [4,5,6]
# print(list(map(lambda x,y: x*y, a, b)))
#
# fruits = ['apple', 'banana', 'cherry']
# print(list(map(lambda fruit: fruit.upper(), fruits)))
# print(fruits)

# is_even = lambda x: x % 2 == 0
# print(is_even(51))

text = lambda x: print(x)
text("hello")
