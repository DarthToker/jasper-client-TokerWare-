# -*- coding: utf-8-*-
import re

import wolframalpha

#WORDS = ["WHO","WHAT","HOW MUCH", "HOW MANY", "HOW OLD"]
PRIORITY = 4


def handle(text, mic, profile):
    
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    app_id='VP8L72-VYQXEKT72A'

    client = wolframalpha.Client(app_id)

##    mic.say("what do you want to know?")
##    stuff = mic.activeListen()
    res = client.query(text)

    if len(res.pods) > 0:
        texts = ""
        pod = res.pods[1]
        if pod.text:
            texts = pod.text
        else:
            texts = "I have no answer for that"
        mic.say(texts)

    else:
    
        mic.say ("I am not sure")




   
##    
##    mic.say("what do you want to know?")
##    stuff = mic.activeListen()
##    res = client.query(stuff)
##    for pod in res.pods:
##        texts = pod.text
##        mic.say(texts)
##
##


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text.upper() for word in WORDS)
