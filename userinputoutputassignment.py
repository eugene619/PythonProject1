# A python program that returns the smallest number among three numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")
