class Student:
    def __init__(self, firstname, course, language):
        self.firstname = firstname
        self.course = course
        self.language = language

    def sleep(self):
        print(self.firstname, "is sleeping")

c = Student("Caleb", "MIT", "Python")
print(c.firstname)
print(c.course)
print(c.language)
c.sleep()

S2= Student("Vivian", "Datascience", "Kotlin")
print(S2.firstname)
print(S2.course)
print(S2.language)
S2.sleep()