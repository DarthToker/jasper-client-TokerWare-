# -*- coding: utf-8-*-
import random
import re
#mark1
new_word = "CLOSE GOOGLE" 
message = "closing google"

WORDS = ("%s" %new_word)

PRIORITY = 4

def handle(text, mic, profile):
    global google_s

    mic.say("%s" %message)
    google_s.kill()



def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
