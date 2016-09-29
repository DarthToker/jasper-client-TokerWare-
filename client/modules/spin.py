# -*- coding: utf-8-*-
import random
import re
import jasperpath

image = 'nu.png'
size = width, height = 320, 320
screensize = 480, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0
color = black
#mark1
new_word = "SPIN" 
message = "spinning master"

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
        
    for i in range(0,360,5):
        self.pygm.blitimgspin(image, size, color, x, y, i)
        self.pygm.clock.tick(60)
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
