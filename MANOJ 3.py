#  USN 1RUA25BCA0059  NAME MANOJ C

a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
c = int(input("Enter value 3: "))
d = int(input("Enter value 4: "))
e = int(input("Enter value 5: "))

maximum = a
minimum = a

if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
if d > maximum:
    maximum = d
if e > maximum:
    maximum = e

if b < minimum:
    minimum = b
if c < minimum:
    minimum = c
if d < minimum:
    minimum = d
if e < minimum:
    minimum = e

print("Maximum value:", maximum)
print("Minimum value:", minimum)
