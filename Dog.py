class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY IINSTANCE OF THIS CLASS
    species = "mammal"


    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    def bark(self, age):
        print("My name is {}, and I am {} years old!".format(self.name, age))
new_dog = Dog("Jack Russell Terrier", "Jack Jack", True)

print(new_dog.spots)
new_dog.bark(13)

