class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name, "is studying")

accountant = Person("Joe","28", "Male")
print(accountant.name)
print(accountant.age)
consultant = Person("Kylie","22", "Female")
print(consultant.gender)
doctor = Person("Kevin","35", "Male")
print(doctor.name)
doctor.details()