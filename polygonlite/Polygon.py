from .Point import Point
from .Edge import Edge
from .Services import orientation, SinglyLinkedList, Node


class Polygon:
    """
    Class for Polygons. Polygons can be thought of as a ordered list of points. (Meaning, the first point is connected to
    the second point, the second point is connected to the third and so on, and finally the last point is connected to
    the first.

    Polygons can be accessed as a list. For example, the first point og Polygon p can be accessed using p[0].
    """
    points = None

    def __init__(self, point_array):
        self.points = [Point(point) for point in point_array]

    def flip(self):
        """
        Flips the order of the polygon. That is, the last point becomes the first, the second last point becomes
        the second point and so on.
        :return: Polygon
        """
        return self.__class__(self.points[::-1])

    def simplify(self):
        """
        Removes all the collinear and duplicate points from the polygon.
        :return: Polygon
        """
        def are_collinear(x, y, z):
            if (x.x * (y.y - z.y) + y.x * (z.y - x.y) + z.x * (x.y - y.y)) == 0:
                return True
            return False

        new_points = self.points[:]
        for i in range(len(self.points)):
            if are_collinear(new_points[(i - 1) % len(new_points)], new_points[i % len(new_points)], new_points[(i + 1) % len(new_points)]):
                del new_points[i]
        return self.__class__(new_points)

    def is_clockwise(self):
        """
        Returns true if the order of the points in the polygon is clockwise.
        :return: bool
        """
        if self._signed_area() < 0:
            return True
        return False

    def is_anticlockwise(self):
        """
        Returns true if the order of the points in the polygon is anti clockwise.
        :return: bool
        """
        if self._signed_area() > 0:
            return True
        return False

    def contains(self, point):
        """
        Checks if the point lies inside the polygon.
        :param point: Point
        :return: bool
        """
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

    def as_array(self):
        """
        Gives the polygon as a list of points, which in turn are a list of numbers.
        :return: list
        """
        return [point.as_array() for point in self.points]

    def max_x(self):
        """
        Returns the maximum x coordinate of the polygon.
        :return: float
        """
        return max(point.x for point in self.points)

    def min_x(self):
        """
        Returns the minimum x coordinate of the polygon.
        :return: float
        """
        return min(point.x for point in self.points)

    def max_y(self):
        """
        Returns the maximum y coordinate of the polygon.
        :return: float
        """
        return max(point.y for point in self.points)

    def min_y(self):
        """
        Returns the minimum y coordinate of the polygon.
        :return:
        """
        return min(point.y for point in self.points)

    def to_linked_list(self):
        simplified = self.simplify()
        linked_list = SinglyLinkedList()
        for i in range(len(simplified.points)):
            linked_list.append(simplified.points[i])
        return linked_list

    def area(self):
        return abs(self._signed_area())

    def _signed_area(self):
        area = 0.0
        n = len(self.points)
        for i in range(n):
            j = (i + 1) % n
            area += self.points[i][0] * self.points[j][1]
            area -= self.points[j][0] * self.points[i][1]
        return area / 2.0

    def __repr__(self):
        return str(self.points)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value

    def __len__(self):
        return len(self.points)



