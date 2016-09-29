# -*- coding: utf-8-*-
import random
import re
import jasperpath
import os
import subprocess
import sys
image = 'nu.png'
size = width, height = 320, 320
screensize = 480, 320
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

x=0
y=0

#mark1
new_word = "DESKTOP" 
message = "starting"

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
##    os.system((jasperpath.data('vnc.sh &')))
##    subprocess.call((jasperpath.data(['vnc.sh', '&'])))
##    subprocess.call('/home/pi/vnc.sh')
##    subprocess.call('vncserver :1 -geometry 1280x800 -depth 24 -dpi 96')
    self.pygm.on = False
    os.system('vncserver :1 -geometry 1280x800 -depth 24 -dpi 96 &')
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
