THRESHOLD = 0.000001


class Point:
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
        return Point(self.x, self.y)

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
