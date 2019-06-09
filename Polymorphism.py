class Animal():

    def __init__(self, name):
         self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
class Dog(Animal):

    def speak(self):
        return self.name + " says wolf!"


class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")


