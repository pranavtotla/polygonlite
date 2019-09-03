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
            print (i - 1) % len(new_points), i,  (i + 1) % len(new_points)
            if are_collinear(new_points[(i - 1) % len(new_points)], new_points[i % len(new_points)], new_points[(i + 1) % len(new_points)]):
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

    def contains(self, point):
        infinity = Point(self.max_x() + 1, point.y)
        count = 0

        for i in range(len(self.points)):
            edge = Edge(self.points[i], self.points[(i + 1) % len(self.points)])
            ray = Edge(point, infinity)

            if ray.intersect(edge):
                if orientation(edge[0], point, edge[1]) == 0:  # Points are collinear
                    return edge.on_segment(point)
                count += 1

        return count % 2 == 1

    def max_x(self):
        return max(point.x for point in self.points)

    def min_x(self):
        return min(point.x for point in self.points)

    def max_y(self):
        return max(point.y for point in self.points)

    def min_y(self):
        return min(point.y for point in self.points)

    def __repr__(self):
        return str(self.points)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value

    def __len__(self):
        return len(self.points)



