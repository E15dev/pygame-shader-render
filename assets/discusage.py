import random
from math import floor
import psutil
def shader(x, y, z):
    return (0, floor(psutil.disk_usage('c:/').percent * 2.55), 0)
