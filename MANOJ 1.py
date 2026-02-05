#  USN 1RUA25BCA0059  NAME MANOJ C
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("%  Modulus")
print("** Power")

op = input("Enter operator: ")

match op:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")

    case "%":
        if num2 != 0:
            print("Result:", num1 % num2)
        else:
            print("Error: Modulus by zero")

    case "**":
        print("Result:", num1 ** num2)

    case _:
        print("Invalid operator")
