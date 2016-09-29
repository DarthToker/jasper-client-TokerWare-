# -*- coding: utf-8-*-
import random
import re


#WORDS = ["GOOGLE"]

PRIORITY = 4

def handle(text, mic, profile):
    import subprocess
    import webbrowser
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    
    mic.say("opening google")
    subprocess.Popen(["epiphany", "--display=:0", "http://www.google.com"])

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bgoogle\b', text, re.IGNORECASE))
