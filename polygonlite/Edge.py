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
        Returns the length of the edge.
        :return: float
        """
        return math.sqrt(self.vector().square().sum())

    def vector(self):
        """
        Returns the vector representation of the edge.
        :return: Point
        """
        return Point(self.point2 - self.point1)

    def unit_vector(self):
        """
        Returns the unit vector in the direction of the edge.
        :return: Point
        """
        return self.vector() / self.length()

    def slope(self):
        """
        Returns the slope of the line made by the edge, returns "inf" if slope is infinity.
        :return: union([float, string])
        """
        if self.point2.x - self.point1.x < THRESHOLD:
            return 'inf'
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

    def y_intercept(self):
        """
        Returns the y intercept formed by the line defined by the edge. Returns 'inf' line is parallel to y axis.
        :return: union([float, string])
        """
        if self.slope() == 'inf':
            return 'inf'
        return (-self.slope() * self.point1.x) + self.point1.y

    def line_coeff(self):
        """
        Returns the slope and y intercept of the line formed by the edge.
        :return: dict
        """
        return {'slope': self.slope(), 'y_intercept': self.y_intercept()}

    def midpoint(self):
        """
        Returns the mid point of the edge.
        :return: Point
        """
        return (self.point1 + self.point2) / 2

    def angle_between(self, other, radians=False):
        """
        Returns the angle between the two edges, in degrees by default.
        :param other: Edge
        :param radians: bool
        :return: float
        """
        dot_product = dot(self.vector(), other.vector())
        if dot_product != 0:
            normalized_product = float(dot_product) / (float(self.length()) * float(other.length()))
        else:
            normalized_product = dot_product

        if radians:
            return math.acos(normalized_product)
        return float(math.acos(normalized_product)) * 180 / math.pi

    def is_parallel(self, other):
        """
        Returns true if the two edges are parallel.
        :param other: Edge
        :return: bool
        """
        if (self.slope() - other.slope()) < THRESHOLD:
            return True
        return False

    def is_between(self, point):
        """
        To be deprecated. Use on_segment.
        Returns true if the point lies on the edge.
        :param point: Point
        :return: bool
        """
        if is_between(self.point1.x, point.x, self.point2.x):
            if is_between(self.point1.y, point.y, self.point2.y):
                return True
        return False

    def on_segment(self, point):
        """
        Returns true if the point lies on the edge.
        :param point: Point
        :return: bool
        """
        return max(self.point1.x, self.point2.x) >= point.x >= min(self.point1.x, self.point2.x) and max(self.point1.y,self.point2.y) >= point.y >= min(self.point1.y, self.point2.y)

    def intersect(self, other):
        """
        Returns the intersection point of two edges (line segments, not lines).
        Returns 'collinear' if the edges are collinear (again, line segments, not lines).
        Returns None if the edges are parallel.
        :param other: Edge
        :return: union(Point, string, None)
        """
        if self.on_segment(other.point1) or self.on_segment(other.point2):
            return 'collinear'
        intersection = self.intersect_lines(self, other)
        if intersection:
            if self.on_segment(intersection):
                return Point(intersection)
        return None

    def project_point(self, point):
        """
        Projects the given point on the Edge.
        :param point: Point
        :return: Point
        """
        vector = self.unit_vector()
        edge_to_point = point - self.point1
        return self.point1 + (vector * dot(edge_to_point, vector))

    def _y_for_x(self, x):
        """
        Returns the y value for some input x value considering the line formed by the edge.
        :param x: float
        :return: float
        """
        if self.slope() == 'inf':
            return None
        return self.slope() * x + self.y_intercept()

    def _x_for_y(self, y):
        """
        Returns the x value for some input y value considering the line formed by the edge.
        :param y: float
        :return: float
        """
        if self.slope() == 0:
            return None
        return (y - self.y_intercept()) / float(self.slope())

    @staticmethod
    def intersect_lines(line1, line2):
        """
        Gives the intersection point of the two lines
        :param line1: Edge
        :param line2: Edge
        :return: union(Point, None)
        """
        def coeffs(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0] * p2[1] - p2[0] * p1[1])
            return A, B, -C

        def intersection(equation1, equation2):
            D = equation1[0] * equation2[1] - equation1[1] * equation2[0]
            Dx = equation1[2] * equation2[1] - equation1[1] * equation2[2]
            Dy = equation1[0] * equation2[2] - equation1[2] * equation2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return x, y
            else:
                return False

        eq1 = coeffs(line1[0], line1[1])
        eq2 = coeffs(line2[0], line2[1])
        solution = intersection(eq1, eq2)
        if solution:
            return Point(solution)
        return None

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