# -*- coding: utf-8-*-
import random
import re
import jasperpath
from xbmcjson import XBMC, PLAYER_VIDEO
#mark1
new_word = "CHANGE IT" 
message = "changing it"
xbmc = XBMC("http://192.168.42.142/jsonrpc", "darthtoker", "Garfield76")

WORDS = ("%s" %new_word)

PRIORITY = 4

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
    

    mic.say("%s" %message)
    xbmc.Player.GoTo({"playerid":1, "to":"next"})

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
