# -*- coding: utf-8-*-
import random
import re
import subprocess
import jasperpath
import os

#WORDS = ["NEW WORD", "YES", 'NO']

PRIORITY = 4

def getword(text, mic):
    global new_word
    mic.say("What word would you like to add?")
    new_word = mic.activeListen()
    mic.say("did you say %s?" %new_word)
    reply1 = mic.activeListen()
    if no(reply1):
        getword(text, mic)
    if yes(reply1):
        return
    
def getsay(text, mic):
    global new_message
    mic.say("And how should I respond to %s" %new_word)
    new_message = mic.activeListen()
    nm = new_message.lower()
    mic.say("did you say %s?" %nm)
    reply2 = mic.activeListen()
    if no(reply2):
        getsay(text, mic)
    if yes(reply2):
        nm = new_word
        return

def makefile():
    new_name = jasperpath.mod("%s.py" %new_word)
    f_old = open(jasperpath.mod("templet.txt"))
 
    f_new = open((new_name), "w")

    for line in f_old:
        f_new.write(line)
        if 'mark1' in line:
            nm = new_message.lower()
            f_new.write('new_word = "%s" \nmessage = "%s"' %(new_word, nm))

    f_old.close()
    f_new.close()

def reboot(text, mic):
    mic.say("I will have to reboot for changes to take affect")
    mic.say("Should I do that now?")
    reply3 = mic.activeListen()
    if no(reply3):
        return
    if yes(reply3):
        mic.say("rebooting")
        subprocess.call(["sudo", "reboot"])
    

def yes(text):
    return bool(re.search(r'\b(yes)\b', text, re.IGNORECASE))

def no(text):
    return bool(re.search(r'\b(no)\b', text, re.IGNORECASE))

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

    getword(text, mic)
    getsay(text, mic)
    makefile()
    mic.say("%s added" %new_word)
    reboot(text, mic)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bNEW WORD\b', text, re.IGNORECASE)) 
