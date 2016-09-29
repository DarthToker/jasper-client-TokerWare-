# -*- coding: utf-8-*-
import random
import re
import jasperpath
import pygame
import time
WORDS = ["SUCK"]


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
    messages = ["no, you suck", "fuck off", "go suck a cock", "blow me"]

    message = random.choice(messages)
    self.blitimg(image, size, black, x, y)
    mic.say(message)
    time.sleep(1)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bsuck\b', text, re.IGNORECASE))
