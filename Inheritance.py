
# Parent Class
class Animal:
    def Speak(self):
        print("Animal is speaking")

# Child Class
class Bee:
    def Buzz(self):
        print("Bee is buzzing")

class Duck:
    def Quack(self):
        print("Duck is quacking")

a = Animal()
a.Speak()

b = Bee()
b.Buzz()

d = Duck()
d.Quack()

class Duck(Bee):
    def Quacks(self):
        print("Duck is quacking")

