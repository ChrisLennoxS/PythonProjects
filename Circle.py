class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2

    def get_area(self):
        return (self.radius**2) * self.pi


circle_one = Circle(12)
print(circle_one.get_circumference())
print(circle_one.get_area())