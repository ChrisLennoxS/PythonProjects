import math


class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return f"The distance between these two points are {math.sqrt(((self.coor2[1] - self.coor1[1])**2) + ((self.coor2[0] - self.coor1[0])**2))}"

    def slope(self):
        return f"The slope of these two lines is {(self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])}"


coordinate1 = (3, 2)
coordinate2 = (8, 10)

Line1 = Line(coordinate1, coordinate2)
print(Line1.distance())
print(Line1.slope())

