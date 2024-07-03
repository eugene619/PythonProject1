# (1)While Loop
# Incrementing a value
number = 20
while number <= 25:
    print(number)
    number += 2

# Decrementing a value
num = 10
while num >= 1:
    print(num)
    num -= 1

# Break statement
no = 25
while no <= 30:
    print(no)
    if no == 27:
        break
    no += 1

# Continue statement- 0-5,skip 3
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

# (2)For Loop
for y in range(7):
    print(y)

for z in range(40, 45):
    print(z)

for mynumber in range(100, 110, 3):
    print(mynumber)

languages = ["Python", "PHP", "Kotlin", "Java"]
for lang in languages:
    print(lang)