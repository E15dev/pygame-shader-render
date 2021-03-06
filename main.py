import pygame
from assets.colorlist import *
from math import floor
from assets.testshader import shader
import time


def refresh():
    pygame.display.flip()
    return 0


def pixel(surface, color, pos):
    pygame.draw.line(surface, color, pos, pos)
    return 0

def clamp(fl):
    if fl < 0:
        return 0
    elif fl > 255:
        return 255
    else:
        return fl

def drawshader():
    for i in range(centerwidth - 100, centerwidth + 100):
        for j in range(centerheight - 100, centerheight + 100):
            sh = shader(i, j, 0, cw=centerwidth, ch=centerheight)
            pixel(screen, (clamp(sh[0]), clamp(sh[1]), clamp(sh[2])), (i, j))


def setwindowfps(fps):
    pygame.display.set_caption('pygame render ' + str(fps) + ' fps')


# config
(width, height) = (500, 500)  # screen resolution
a = pygame.image.load('./assets/icon.png')  # old icon, it was supposed to be a game

# init
centerwidth = floor(width / 2)
centerheight = floor(width / 2)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The game')
iteration = 0
framestime = []

# more config
screen.fill(Black)
pygame.display.flip()
pygame.display.set_icon(a)

running = True
while running:
    iteration += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    try:
        fps = 1 / (time.time() - lfps)
    except:
        fps = "error"
    setwindowfps(fps)
    lfps = time.time()
    drawshader()  # pre-rendering shader
    refresh()  # swap buffer to screen

print('end')
