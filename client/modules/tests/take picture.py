# -*- coding: utf-8-*-
import random
import re
import jasperpath
import sys, pygame
import time
import pygame.camera
from pygame.locals import *
import pygame.image
pygame.camera.init()

#mark1
new_word = "TAKE PICTURE" 
message = "taking picture"

#WORDS = ("%s" %new_word)
PRIORITY = 4
size = width, height = 480, 320
black = 0, 0, 0
x=0
y=0
#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
cam = pygame.camera.Camera("/dev/video0",(640,480))

##def pic(self):
##    cam.start()
##
##    pic = cam.get_image()
##    self.screen.fill(black)
##    self.screen.blit(pic, (x,y))
##    pygame.display.flip()
##    cam.stop()
##


def handle(self,text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    cam.start()
    pic = cam.get_image()
    pygame.image.save(pic,(jasperpath.data('img/pic.jpg')))

    self.pygm.blitimg('pic.jpg', size, black, x, y)

    mic.say("%s" %message)
##    pic(self)
    cam.stop()
    time.sleep(5)
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
