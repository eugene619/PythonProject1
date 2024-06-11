number = 60 #Int
num = 45.36 #Float
greeting = "Hello there" #Str
isPythoninteresting = True #Boolean
fruits = ["banana", "mango", "apple"] #List
cars = ("bmw", "mercedes", "toyota", "audi") #Tuple
countries = {"kenya", "tanzania", "uganda"} #Set
student = {
    "firstname": "Gold",
    "age": 19,
    "course": "MIT",
    "nationality": "kenya"
} #Dictionary

print(num)
print(isPythoninteresting)
print(fruits)
print(cars)
print(countries)
print(student["firstname"])

#Determining Data type
print(type(isPythoninteresting))
print(type(cars))

#Typecasting is converting one datatype to another
print(int(num))
print(float(number))