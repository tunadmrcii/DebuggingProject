class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increaseAge(self):
        self.age += 1

    def decreaseAge(self):
        if self.age > 0:
            self.age -= 1

    def __str__(self):
        return f"{self.name} is {self.age} years old!"

tuna = Person("tuna", 5)
tuna.decreaseAge()
tuna.decreaseAge()
tuna.decreaseAge()
tuna.decreaseAge()
tuna.decreaseAge()
tuna.decreaseAge()
print(tuna)

class MyClass:

    def __init__(self):
        print("initialized")

    def printSomething(self):  # Define printSomething as a method
        print("python")

myClass = MyClass()
myClass.printSomething()  # Now this should work without errors