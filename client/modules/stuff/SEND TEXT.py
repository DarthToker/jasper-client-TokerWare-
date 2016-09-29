# -*- coding: utf-8-*-
import random
import re
import jasperpath
import os
#mark1
#new_word = ["SEND TEXT", "YES", "NO"]

message = "sending text"

WORDS = ["SEND TEXT", "YES", "NO"]

PRIORITY = 4

def yes(text):
    return bool(re.search(r'\b(yes)\b', text, re.IGNORECASE))

def no(text):
    return bool(re.search(r'\b(no)\b', text, re.IGNORECASE))


def handle(text, mic, profile):

    def getnum():
        global num        
        mic.say("what number should i send it to?")
        num = mic.activeListen()
        mic.say("did you say %s?" %num)
        reply1 = mic.activeListen()
        if no(reply1):
            getnum()
        if yes(reply1):
            return

        

    def getmsg():
        global msg_a
        mic.say("what is your message?")
        msg_a = mic.activeListen()
        mic.say("did you say %s?" %msg_a)
        reply2 = mic.activeListen()
        if no(reply2):
            getmsg()
        if yes(reply2):
            return
        


    getnum()    
    getmsg()

    mic.say("%s" %message)



   # num = "610-304-1966"

    msg =('"message=%s"' %msg_a)

    os.system('curl -X POST http://textbelt.com/text -d number=%s    -d %s'%(num, msg))




    


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bSEND TEXT\b', text, re.IGNORECASE)) 
