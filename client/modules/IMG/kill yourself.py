# -*- coding: utf-8-*-
import random
import re
import jasperpath
import sys, pygame
import time
import subprocess
import os
#mark1
new_word = "KILL YOURSELF" 
message = "good by"

WORDS = ("%s" %new_word)

PRIORITY = 4
image = 'die.png'

size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0



def handle(self, text, mic, profile):
    mic.say("%s" %message)    
    self.blitimg(image, size, black, x, y)
    time.sleep(2)
    self.pygm.on = False

    
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
