# -*- coding: utf-8-*-
import random
import re
import os


WORDS = ["SHUT UP"]

PRIORITY = 3

def handle(self, text, mic, profile):
    import subprocess
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages = ["LAA LAA LAA LAA LAA LAA", "NO!", "blow me"]

    message = random.choice(messages)

    mic.say(message)
   


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bshut up\b', text, re.IGNORECASE))
