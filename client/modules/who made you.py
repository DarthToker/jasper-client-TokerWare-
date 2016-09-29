# -*- coding: utf-8-*-
import random
import re
import jasperpath
import time
image = 'nu.png'
size = width, height = 320, 320
screensize = 480, 320
x=0
y=0
gray     = (100, 100, 100)
nvb = ( 60,  60, 100)
white    = (255, 255, 255)
red      = (255,   0,   0)
green    = (  0, 255,   0)
blue     = (  0,   0, 255)
yellow   = (255, 255,   0)
orang   = (255, 128,   0)
purple   = (255,   0, 255)
cyan     = (  0, 255, 255)
black = (0, 0, 0)

#mark1
new_word = "WHO MADE YOU" 
message = "you did master"

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

    mic.say("%s" %message)
    tx=240
    ty=160
    step=5
    for i in range(0,320,step):

        size2 = (i,i)
        self.pygm.blittxtimgam('', 50, red, tx, ty, tx, ty, 'dtoker.jpg', size2, 0, 0, black)
        self.pygm.clock.tick(60)


    for i in range(-20,300,step):
        self.pygm.blittxtimgam('TokerWare', 50, red, tx, i, tx, ty, 'dtoker.jpg', size2, 0, 0, black)
        self.pygm.clock.tick(60)


    time.sleep(1)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
