# -*- coding: utf-8-*-
import random
import re
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT) #head light

WORDS = ["HEADLIGHT", "OFF"]

PRIORITY = 4



def handle(text, mic, profile):


    message = ["HEADLIGHT OFF"]    
    message = random.choice(messages)
    GPIO.output(24,0)
    mic.say(message)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\headlight off\b', text, re.IGNORECASE))
