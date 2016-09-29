# -*- coding: utf-8-*-
import random
import re
import os
import jasperpath
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)

#mark1
new_word = "FIRE PHOTON TORPEDOES" 
message = "firing photon torpedoes"

WORDS = ("%s" %new_word)

PRIORITY = 4
image = 'photon.png'

size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0
def handle(self, text, mic, profile):
    

       mic.say("%s" %message)
       GPIO.output(12,1)
       self.blitimg(image, size, black, x, y)
       randomfile = random.choice(os.listdir(jasperpath.data("audio/tor/")))
       rfile = jasperpath.data('audio/tor/'+ randomfile)
       mic.speaker.play(rfile)
       GPIO.output(12,0)



def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
