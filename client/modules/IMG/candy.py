# -*- coding: utf-8-*-
import random
import re
import pygame
import time
import jasperpath

WORDS = ["I", "LOVE", "CANDY"]

PRIORITY = 4

image = 'kiss.png'

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
    messages = ["yes, I love her too.",
                "she rocks"]

    message = random.choice(messages)
    self.blitimg(image, size, black, x, y)
    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bi love candy\b', text, re.IGNORECASE))
