import random
from math import floor

def shader(x, y, z):
    # return (255, 255, 255)
    return (floor((x  + 100) / 2), floor((y  + 100) / 2), 127)
