import math


def shader(x, y, z, cw=0, ch=0):
    color = (dist2d(cw, ch, x, y) < 75) * 255
    print(dist2d(0, 0, x, y))
    return (color, color, color)


def dist2d(x0, y0, x1, y1):
    return math.sqrt(((x0 - x1) ** 2) + ((y0 - y1) ** 2))
