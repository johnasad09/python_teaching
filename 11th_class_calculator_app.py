def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("-" * 20)
print("Calculator App")
print("-" * 20)

num1 = float(input("Enter the first number: "))

cont = True
while cont:
    operation = input("Enter the operation [ +, - *, / ]: ")
    num2 = float(input("Enter the second number: "))
    answer = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    decision = input(f"Do you wish to continue with {answer}? [y/n]: ").lower()

    if decision == "y":
        num1 = answer
    else:
        cont = False
