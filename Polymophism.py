class Shape:
    def draw(self):
        print("Drawing a shape")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

class Square:
    def draw(self):
        print("Drawing a square")

sh = Shape()
sh.draw()

rec = Rectangle()
rec.draw()

sq = Square()
sq.draw()

# Encapsulation

class Employee:
    def __init__(self, fullname, position, salary):
        self.fullname = fullname
        self.position = position
        self.__salary = salary

    def details(self):
        print(self.fullname, self.position, self.__salary)

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount

emp = Employee("Mary Thompson", "Administrator",50000)
print(emp.fullname)
print(emp.position)
emp.details()
emp.increase_salary(6100)
emp.details()
