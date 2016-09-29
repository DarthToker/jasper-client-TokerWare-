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



WORDS = ["9000"]

PRIORITY = 4
image = 'h9.png'

size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0
def handle(self, text, mic, profile):

       GPIO.output(12,1)

       randomfile = random.choice(os.listdir(jasperpath.data("audio/hal/")))
       rfile = jasperpath.data('audio/hal/'+ randomfile)
       self.blitimg(image, size, black, x, y)
       mic.speaker.play(rfile)
       GPIO.output(12,0)




def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b9000\b', text, re.IGNORECASE))
