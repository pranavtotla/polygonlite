import math
from Polygon.Point import Point

class Edge:
    def __init__(self, point1, point2):
        self.point1 = Point(point1)
        self.point2 = Point(point2)

    def length(self):
        return math.sqrt(((self.point2.x - self.point1.x) ** 2) + ((self.point2.y - self.point1.y) ** 2))