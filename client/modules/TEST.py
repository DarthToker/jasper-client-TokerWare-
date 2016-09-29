# -*- coding: utf-8-*-
import random
import re
import jasperpath
import sys, pygame
from pygame.locals import *

#mark1
new_word = "TEST" 
message = "booger booger booger"
image = 'nu.png'
image2 = 'zip2.png'
size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0


WORDS = ("%s" %new_word)

PRIORITY = 4

def handle(self, text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    self.blitimg(image2, size, black, x, y)
    self.blittxt('test', 400, white, black)
    #self.bton(red, 400, 240, 'test', 50, white)

    mic.say("%s" %message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
