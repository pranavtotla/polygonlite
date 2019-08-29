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
