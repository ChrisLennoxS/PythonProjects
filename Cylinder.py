import math


class Cylinder(object):

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return f"The volume of this cylinder is {math.pi * pow(self.radius, 2) * self.height}"

    def surface_area(self):
        return f"The surface area of this cylinder is {(2 * math.pi * self.radius * self.height) + ( 2 * math.pi * pow(self.radius, 2))}"


c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())
