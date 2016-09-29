# -*- coding: utf-8-*-
import re
import random
import os
import jasperpath


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)



WORDS = ["KIT"]

PRIORITY = 4
image = 'kitt.jpg'

size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0
def handle(self, text, mic, profile):

       GPIO.output(12,1)


       randomfile = random.choice(os.listdir(jasperpath.data("audio/kitt/")))
       rfile = jasperpath.data('audio/kitt/'+ randomfile)
       self.blitimg(image, size, black, x, y)
       mic.speaker.play(rfile)
       GPIO.output(12,0)




def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bKIT\b', text, re.IGNORECASE))
