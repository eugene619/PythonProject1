# A Class is a blueprint of an object.
# An Object is an instance of a Class.

class Person:
    # Properties/ Attribute/ Variable/ Characteristic
    name = "Patrick"
    age = 18
    height = 178

    # Method/ Function (Behaviour)
    def walk(self):
        print("Person is walking")

# Creating an Object
accountant = Person()
accountant.walk()