
try:
    print(number)
except:
    print("An error occurred")
finally:
    print("Success")

x = 7
y = 0
try:
    print(x / y)
except:
    print("Cannot divide")
finally:
    print("Success")