class Animal():

    def __init__(self):
        print("Animal has been created")

    def who_am_i(self):
        print("I am eating")

    def eat(self):
        print("I am eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("BARK")


new_dog = Dog()
new_dog.who_am_i()
new_dog.bark()
