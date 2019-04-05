import math


def triangle_square(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.real = img


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def abs(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def arg(self):
        return None


def cross_product(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


print(cross_product(4, 2, 1, 2))


def subtract(x1, y1, x2, y2):
    return ((x1 - x2), (y1 - y2))


def point_location(x, y, sx1, sy1, sx2, sy2):
    p1 = subtract(x, y, sx1, sy1)
    p2 = subtract(x, y, sx2, sy2)
    res = cross_product(p1[0], p1[1], p2[0], p2[1])
    if res > 0:
        return "left"
    if res < 0:
        return "right"
    return "same line"


print(point_location(4, 2, 2, 2, 5, 4))


def manhattan_dist(x1, y1, x2, y2):
    return math.abs(x1 - x2) + math.abs(y1 - y2)
