class Point:
    def __init__(self, *args):
        if len(args) == 1:
            self.point = args[0]
            self.x = self.point[0]
            self.y = self.point[1]
        if len(args) == 2:
            self.point = [args[0], args[1]]
            self.x = args[0]
            self.y = args[1]
