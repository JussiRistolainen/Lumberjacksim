import math


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return self

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def getDistanceFromPosition(self, point):
        return math.sqrt(
            (self.x - point.x) * (self.x - point.x)
            + (self.y - point.y) * (self.y - point.y)
        )
