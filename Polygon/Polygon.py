from .Point import Point
from .Edge import Edge
from .Services import orientation


class Polygon:
    def __init__(self, point_array):
        self.points = [Point(point) for point in point_array]

    def flip(self):
        return self.__class__(self.points[::-1])

    def simplify(self):
        def are_collinear(x, y, z):
            if (x.x * (y.y - z.y) + y.x * (z.y - x.y) + z.x * (x.y - y.y)) == 0:
                return True
            return False

        new_points = self.points[:]
        for i in range(len(self.points)):
            if are_collinear(new_points[(i - 1) % len(new_points)], new_points[i], new_points[(i + 1) % len(new_points)]):
                del new_points[i]
        self.points = new_points

    def is_clockwise(self):
        if orientation(self.points[0], self.points[1], self.points[2]) == 1:
            return True
        return False

    def is_anticlockwise(self):
        if orientation(self.points[0], self.points[1], self.points[2]) == 2:
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



