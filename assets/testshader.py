import math


def shader(x, y, z):
    color = (dist2d(250, 250, x, y) < 75) * 255  # '255' is center of the screen
    print(dist2d(0, 0, x, y))
    return (color, color, color)


def dist2d(x0, y0, x1, y1):
    return math.sqrt(((x0 - x1) ** 2) + ((y0 - y1) ** 2))
