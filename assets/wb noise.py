import random

def shader(x, y, z):
#     return (255, 255, 255)
    color = (random.randint(0,1) == 1) * 255
    return (color, color, color)
