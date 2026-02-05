#  USN 1RUA25BCA0059  NAME MANOJ C

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")
temp = float(input("Enter temperature: "))

match choice:
    case "1":
        fahrenheit = (temp * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    case "2":
        celsius = (temp - 32) * 5/9
        print("Temperature in Celsius:", celsius)

    case _:
        print("Invalid choice")
