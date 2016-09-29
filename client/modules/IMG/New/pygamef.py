import random
import re
import time
import RPi.GPIO as GPIO
import jasperpath
import pygame
import time
size = width, height = 320, 320
black = 0, 0, 0
red = (255,0,0)
white = (255,255,255)
x=0
y=0
##screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
def blitimg(image, size, color):
    global img
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color)
    img = pygame.image.load(image)
    img = pygame.transform.smoothscale((img), (size))
    imgc = img.get_rect()
    imgc.center = background.get_rect().center
    background.blit(img, imgc)
    screen.fill(color)
    screen.blit(background, (x,y))
    pygame.display.flip()
    

def blittxt(txt, txts, color, bcolor):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(bcolor)
    font = pygame.font.Font(None, txts)
    txt = font.render("%s" %txt, True, (color))
    textx = txt.get_rect()
    textx.center = background.get_rect().center
    background.blit(txt, textx)
    screen.fill(color)
    screen.blit(background, (0, 0))
    pygame.display.flip()
