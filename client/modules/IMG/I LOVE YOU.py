# -*- coding: utf-8-*-
import random
import re
import jasperpath
import pygame
import time
#mark1
new_word = "I LOVE YOU" 
message = "you're weird"

WORDS = ("%s" %new_word)

PRIORITY = 4

image = 'whatev.png'

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
    self.blitimg(image, size, black, x, y)
    mic.say("%s" %message)
    time.sleep(1)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
