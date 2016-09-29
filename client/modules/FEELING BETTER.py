# -*- coding: utf-8-*-
import random
import re
import jasperpath

#mark1
new_word = "FEELING BETTER" 
message = "yes i feel great now"

WORDS = ("%s" %new_word)

PRIORITY = 4
image = 'h9.png'

size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0
def handle(self, text, mic, profile):
    

    self.blitimg(image, size, black, x, y)

    mic.speaker.play(jasperpath.data("audio/hal/better.wav"))


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
