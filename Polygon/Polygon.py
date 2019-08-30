from .Point import Point
from .Edge import Edge
from .Services import orientation


class Polygon:
    def __init__(self, point_array):
        self.points = [Point(point) for point in point_array]

    def flip(self):
        return self.__class__(self.points[::-1])

    def is_clockwise(self):
        if orientation(self.points[0], self.points[1], self.points[2]) == 1:
            return True
        return False

    def __repr__(self):
        return str(self.points)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value

    def __len__(self):
        return len(self.points)



