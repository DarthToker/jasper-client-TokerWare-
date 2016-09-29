# -*- coding: utf-8-*-
import re
import random
import os
import jasperpath

WORDS = ["R2D2"]

PRIORITY = 4

def handle(self, text, mic, profile):

    randomfile = random.choice(os.listdir(jasperpath.data("audio/r2/")))
    rfile = jasperpath.data('audio/r2/'+ randomfile)
    mic.speaker.play(rfile)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\R2D2\b', text, re.IGNORECASE))
