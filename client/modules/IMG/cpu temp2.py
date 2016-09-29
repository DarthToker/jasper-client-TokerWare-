# -*- coding: utf-8-*-
import re
import jasperpath
import os
import jasperpath
import sys, pygame
import time
from pygame.locals import *


#mark1


new_word = "CPU TEMPERATURE" 
WORDS = ("%s" %new_word)

PRIORITY = 4

size = width, height = 320, 320
black = 0, 0, 0
red = (255,0,0)
white = (255,255,255)

x=0
y=0


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
    t = os.popen('vcgencmd measure_temp&').readline()
    temp = t.replace("temp=","").replace("'C\n","")
    tempf = str(float(temp) * 9 / 5 + 32) #C to F
    message = ("%s degrees celsius." %temp)
    message2 = ('cpu temperature is %s degrees fahrenheit'%tempf)
    msg2 = ('%sC' %temp)
    msg = ('%sF'%tempf)
    
    self.blittxt(msg, 200, white, black)
    mic.say(message2)
    self.blittxt(msg2, 250, white, black)
    mic.say(message)

    time.sleep(1)    


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
