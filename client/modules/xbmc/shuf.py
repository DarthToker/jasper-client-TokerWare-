# -*- coding: utf-8-*-
import random
import re
import jasperpath
from xbmcjson import XBMC, PLAYER_VIDEO
#mark1

WORDS = "SHUFFLE"

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
    xbmc = XBMC("http://192.168.42.142/jsonrpc", "darthtoker", "Garfield76")
    xbmc.Player.SetShuffle({"playerid":1, "shuffle":True})

def isValid(text):
    

    return bool(re.search(r'\bshuffle\b', text, re.IGNORECASE)) 
