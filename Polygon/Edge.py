import math
from Polygon.Point import Point


class Edge:
    def __init__(self, point1, point2):
        self.point1 = Point(point1)
        self.point2 = Point(point2)

    def length(self):
        return math.sqrt(self.vector().square().sum())

    def vector(self):
        return Point(self.point2 - self.point1)

