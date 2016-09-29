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



WORDS = ["COMPUTER"]

PRIORITY = 4

def handle(self, text, mic, profile):
       GPIO.output(12,1)

       randomfile = random.choice(os.listdir(jasperpath.data("audio/com/")))
       rfile = jasperpath.data('audio/com/'+ randomfile)
       mic.speaker.play(rfile)
       GPIO.output(12,0)




def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bcomputer\b', text, re.IGNORECASE))
