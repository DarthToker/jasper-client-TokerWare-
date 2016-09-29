# -*- coding: utf-8-*-
import random
import re
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.OUT) #head light

WORDS = ["HEADLIGHT", "ON"]
hlight = False
PRIORITY = 4



def handle(text, mic, profile):


    messages = ["HEADLIGHT ON"]
    message = random.choice(messages)
    GPIO.output(24,1)
    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\headlight on\b', text, re.IGNORECASE))
