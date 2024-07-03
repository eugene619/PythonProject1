temperature = 25

if temperature < 25:
    print("It is cold")
elif temperature > 25:
    print("It is hot")
else:
    print("Normal temparature")

# A Program that returns the largest number among three numbers
first = 56
second = 23
third = 78

if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "is the largest")
else:
    print(third, "is the largest")

# A python program that checks whether a number is even or odd
num = 0

if num == 0:
    print(num, "is neither odd nor even")
elif num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# A Python program that returns the area of a rectangle
# Area = L * W
L = 20
W = 5
A = L * W
print("The area is ",A)

# A program that returns the area of a trapezium
# A = 1/2h(a+b)
h = 10
a = 25
b = 40
sum = a + b
A = 1/2*h*sum
print(A)


