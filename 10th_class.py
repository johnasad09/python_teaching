# match-case
# day = "Monday"
# match day:
#     case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#         print("School is open.")
#     case "Saturday" | "Sunday":
#         print("School is off")
#     case _:
#         print("Day is wrong!")

# Dictionary
# key: value
# empty_dict = {}
# students = {
#     "id":1,
#     "name": "Asad",
#     "age": 28,
# }

# for student in students:
#     print(student)

# print(students["age"])

# List
# students = ["Asad", "Tariq", "Zeerak"]
#
# for student in students:
#     print(student)

# students = [
#     { "id": 1, "name": "Asad", "grade": 70 },
#     { "id": 2, "name": "Tariq", "grade": 80 },
#     { "id": 3, "name": "Zeerak", "grade": 90 },
# ]

# print(students[1]["name"])

# students = {
#     "id": 1, "name": "Asad", "grade": 70,
# }

# print(students.get("name"))
# print(students.keys())
# print(students.values())

# print(students["id"])
# print(students["name"])
# print(students["grade"])
#
# for s in students:
#     print(s, students[s])

def format_name(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    return first_name, last_name

print(format_name("ASaD", "ullAH"))
# format_name("ASaD", "ullAH")