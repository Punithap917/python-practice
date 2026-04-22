#define a class
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age   
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

#create object
person1 = Person("Punitha", 21)

print(person1.greet())

#inheritance
class student(Person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course=course
    def study(self):
        return f" {self.name} is studying {self.course}."
student1=student("punitha",21,"cse")
print(student1.study())