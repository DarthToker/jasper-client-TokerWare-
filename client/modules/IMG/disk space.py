# -*- coding: utf-8-*-
import random
import re
import jasperpath
import os
import sys, pygame
import time
from pygame.locals import *
#mark1


new_word = "DISK SPACE" 
WORDS = ("%s" %new_word)

PRIORITY = 4
size = width, height = 320, 320
black = 0, 0, 0
red = (255,0,0)
white = (255,255,255)
##
##screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
##
##def blittxt(text, size, color):
##    background = pygame.Surface(screen.get_size())
##    background = background.convert()
##    background.fill(black)
##    font = pygame.font.Font(None, (size))
##    text = font.render("%s" %text, True, (color))
##    textx = text.get_rect()
##    textx.center = background.get_rect().center
##    background.blit(text, textx)
##    screen.fill(black)
##    screen.blit(background, (0, 0))
##    pygame.display.flip()
##    
def handle(self, text, mic, profile):
    

    def getdiskspace():
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i==2:
                return(line.split()[1:5])
    w = getdiskspace()
    w1 = w[3]
    w2 = w[2].replace("M","megabytes").replace("G", "gigabytes")

    self.blittxt(w1, 110, white, black)
    mic.say("your disk is %s full" %w1)
    self.blittxt(w2, 75, red, black)
    mic.say("and has %s left" %w2)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
