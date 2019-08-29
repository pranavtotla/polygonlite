import math
from Polygon.Point import Point, THRESHOLD
from Polygon.Services import dot


class Edge:
    def __init__(self, point1, point2):
        self.point1 = Point(point1)
        self.point2 = Point(point2)

    def length(self):
        return math.sqrt(self.vector().square().sum())

    def vector(self):
        return Point(self.point2 - self.point1)

    def unit_vector(self):
        return self.vector() / self.length()

    def slope(self):
        if self.point2.x - self.point1.x < THRESHOLD:
            return 'inf'
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

    def midpoint(self):
        return (self.point1 + self.point2) / 2

    def angle_between(self, other, radians=False):
        dot_product = dot(self.vector(), other.vector())
        if dot_product != 0:
            normalized_product = float(dot_product) / (float(self.length()) * float(other.length()))
        else:
            normalized_product = dot_product

        if radians:
            return math.acos(normalized_product)
        return math.acos(normalized_product) * 180 / math.pi