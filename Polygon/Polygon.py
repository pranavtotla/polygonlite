from .Point import Point
from .Edge import Edge


class Polygon:
    def __init__(self, point_array):
        self.points = point_array

    def flip(self):
        return self.__class__(self.points[::-1])

    def __repr__(self):
        return str(self.points)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value

    def __len__(self):
        return len(self.points)



