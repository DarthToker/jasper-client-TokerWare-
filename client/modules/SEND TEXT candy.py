# -*- coding: utf-8-*-
import random
import re
import jasperpath
import os
#mark1
new_word = "TEXT CANDY" 
message = "sending text"

WORDS = ("%s" %new_word)

PRIORITY = 4


    

def handle(self, text, mic, profile):

    mic.say("what would you like to say to her")
    texta = mic.activeListen()

    mic.say("%s" %message)


    num = "717-715-2087"

    msg =('"message=%s"' %texta)

    os.system('curl -X POST http://textbelt.com/text -d number=%s    -d %s'%(num, msg))




    


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
