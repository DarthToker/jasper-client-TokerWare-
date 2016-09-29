# -*- coding: utf-8-*-
import random
import re
import jasperpath


#mark1
new_word = 'BOOGER' 
message = 'YUM YUM YUM'

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
    mic.speaker.play(jasperpath.data('audio/bender/', 'ststart.wav'))

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
