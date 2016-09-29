# -*- coding: utf-8-*-
import random
import re
import jasperpath
import jasperpath
import pygame
import time
#mark1

message = "giving the finger"

WORDS = ("GIVE", "THE", "FINGER")

PRIORITY = 4

image = 'fing.png'

size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
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

    text = text.replace("THE", "").replace('GIVE', '').replace('FINGER', '').replace(' ', '')
    self.blitimg(image, size, black, x, y)
    mic.say("giving %s the finger" %text)
    time.sleep(1)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bgive the finger\b', text, re.IGNORECASE)) 
