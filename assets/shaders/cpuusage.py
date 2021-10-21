import random
from math import floor
import psutil

def shader(x, y, z):
    g = floor(psutil.cpu_percent() * 2.55)
    return (0, g, floor(g / 2))
