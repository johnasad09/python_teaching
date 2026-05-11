# tuple
tup = (1, 2, 3)
# print(tup)

# indexing
# print(tup[1])

# out of index
# print(tup[3])

# x = (1)
# print(f"x is {type(x)}")
#
# x = (1,)
# print(f"x is {type(x)}")
#
# y = ()
# print(f"y is {type(y)}")
#
# print(len(tup))

tup1 = (1,2,3,4)
tup2 = (4,5,6)
tup3 = tup1 + tup2
# print(tup3)
tup4 = tup2 + tup1
# print(tup4)

# slicing
# print(tup4[:5])

# a = 10
# b = 20
# c = 30
# a, b, c = 10, "asad" ,30.0
# print(a)
# print(b)
# print(c)

# unpacking
# x, y, z = tup2
# print(f"the value of x is {x}")
# print(f"the value of y is {y}")
# print(f"the value of z is {z}")

# swap
# x, z = z, x
# print(f"the value of x is {x}")
# print(f"the value of y is {y}")
# print(f"the value of z is {z}")

# set
# empty_set = set()
# print(type(empty_set))

# sets do not allow duplicate values
# a = {1,1, 2, 2, 3}
# print(a)
# b = {1, 2, (2,3)}
# print(b)

# unordered list
# print(b[0])

# c = {1, 2, 3}
# print(c)
# c.add(7)
# print(c)

# accessing a set
# colors = {
#     "red",
#     "green",
# "white",
#     "blue",
# }
#
# colors = [
#     "red",
#     "white",
#     "green",
#     "blue",
#           ]
# for color in colors:
#     print(color)

# if "cyan" in colors:
#     print("Red found")

# exception handling
# try/except
# while True:
#     try:
#         number = int(input("Enter a number: "))
#     except ValueError:
#         print("That's not a number")
#     else:
#         break
#
# print(f"number is {number}")


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
with open("names.txt","r") as file:
    print(file.readlines())
