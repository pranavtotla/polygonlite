from .Services import dot
import math
from .config import THRESHOLD


class Point:
    """
    Class for Points.

    A Point p can be accessed in various ways:
    1. p[0], p[1]
    2. p.x, p.y
    3. p['x'], p['y']
    """
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.point = args[0]
            self.x = self.point[0]
            self.y = self.point[1]
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
            self.point = [self.x, self.y]
        elif len(args) == 0:
            self.x = kwargs.get('x')
            self.y = kwargs.get('y')
            self.point = [self.x, self.y]

    def clone(self):
        """
        Returns a new Point object with same parameters as the point.
        :return: Point
        """
        return Point(self.x, self.y)

    def square(self):
        """
        Returns a new Point object which has squared x and squared y values.
        For example:
        (2,5) -> (4,25)
        (-2,5) -> (4,25)
        :return: Point
        """
        return self.__class__(self.x * self.x, self.y * self.y)

    def sum(self):
        """
        Returns the sum of parameters of x and y of the Point object.
        For example:
        (1,2) -> 3
        (-1,0) -> -1
        :return:
        """
        return self.x + self.y

    def distance(self, other):
        """
        Returns the distance between two points.
        For example:

        distance between (0,2) and (0,5) is 3.

        :param other: Point
        :return: float
        """
        return math.sqrt((self - other).square().sum())

    def project(self, edge):
        """
        Projects the point on a given Edge.
        :param edge: Edge
        :return: Point
        """
        vector = edge.unit_vector()
        edge_to_point = self - edge.point1
        return edge.point1 + (vector * dot(edge_to_point, vector))

    def as_array(self):
        return [self.x, self.y]

    def __repr__(self):
        return str([self.x, self.y])

    def __getitem__(self, key):
        if (key == 0) or (key == 'x'):
            return self.x
        if (key == 1) or (key == 'y'):
            return self.y
        raise KeyError('Invalid key: %s. Valid keys are 0, 1, "x" and "y"' % key)

    def __setitem__(self, key, value):
        if (key == 0) or (key == 'x'):
            self.x = value
        elif (key == 1) or (key == 'y'):
            self.y = value
        raise KeyError('Invalid key: %s. Valid keys are 0, 1, "x" and "y"' % key)

    def __eq__(self, other):
        if not isinstance(other, Point): return False
        if (self.x - other.x) < THRESHOLD:
            if (self.y - other.y) < THRESHOLD:
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __add__(self, other):
        return self.__class__([self.x + other.x, self.y + other.y])

    def __sub__(self, other):
        return self.__class__([self.x - other.x, self.y - other.y])

    def __mul__(self, other):
        return self.__class__([self.x * other, self.y * other])

    def __div__(self, other):
        return self.__class__([self.x / float(other), self.y / float(other)])

    def __len__(self):
        return 2

