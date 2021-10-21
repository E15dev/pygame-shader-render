# pygame-shader-render
render easy shaders ('procedural images'), (assets/testshader.py)

# example shaders
## random
import random

def shader(x, y, z):
    # return (255, 255, 255)
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

render random color for all pixels

## gradient
from math import floor

def shader(x, y, z):
    # return (255, 255, 255)
    return (floor((x  + 100) / 2), floor((y  + 100) / 2), 127)

render easy gradient (work only on -100 to 100 render)

#features
auto set fps in name.
good to learns how procedural textures/images work.
fast.
