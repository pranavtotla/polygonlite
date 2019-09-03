import math
from .Point import Point, THRESHOLD
from .Services import dot, det, is_between


class Edge:
    """
    Class for Edges. Edges can be thought of as line segments too. In simple terms, an edge is a connection between
    two points. Thus, simplistically, it can be represented as a list of two points.

    An Edge e can be accessed in various ways:
    1. e[0], e[1]
    2. e.point1, e.point2
    3. e['point1'], e['point2']
    """
    def __init__(self, point1, point2):
        self.point1 = Point(point1)
        self.point2 = Point(point2)

    def length(self):
        """
        Returns the length of the Edge.
        :return: float
        """
        return math.sqrt(self.vector().square().sum())

    def vector(self):
        """
        Returns the vector representation of the Edge.
        :return: Point
        """
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

    def is_parallel(self, other):
        if (self.slope() - other.slope()) < THRESHOLD:
            return True
        return False

    def is_between(self, point):
        if is_between(self.point1.x, point.x, self.point2.x):
            if is_between(self.point1.y, point.y, self.point2.y):
                return True
        return False

    def on_segment(self, point):
        # return point.x <= max(self.point1.x, self.point2.x) and point.x >= min(self.point1.x, self.point2.x) and point.y <= max(self.point1.y, self.point2.y) and point.y >= min(self.point1.y, self.point2.y)
        # return max(self.point1.x, self.point2.x) >= point.x >= min(self.point1.x, self.point2.x) and point.y <= max(self.point1.y, self.point2.y) and point.y >= min(self.point1.y, self.point2.y)
        return max(self.point1.x, self.point2.x) >= point.x >= min(self.point1.x, self.point2.x) and max(self.point1.y,self.point2.y) >= point.y >= min(self.point1.y, self.point2.y)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if (key == 0) or (key == 'point1') or (key == 'pt1'):
            return self.point1
        if (key == 1) or (key == 'point2') or (key == 'pt2'):
            return self.point2
        raise KeyError('Invalid key: %s. Valid keys are 0, 1, "point1", "point2", "pt1" or "pt2"' % key)

    def __repr__(self):
        return str([self.point1, self.point2])