# -*- coding: utf-8-*-
from sys import maxint
import random

WORDS = []

PRIORITY = -(maxint + 1)

red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
def handle(self, text, mic, profile):
    """
        Reports that the user has unclear or unusable input.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    messages = ["did you say something?",
                "what did you say",
                "Say that again?", "speak the fuck up", "i cant fucking hear you", "blah blah blah", "did you say something?"]

    message = random.choice(messages)
    self.blittxt('???', 400, red, black)
    mic.say(message)


def isValid(text):
    return True
