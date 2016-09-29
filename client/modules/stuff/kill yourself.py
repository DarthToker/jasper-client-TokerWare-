# -*- coding: utf-8-*-
import random
import re
import jasperpath
import sys, pygame
import time
#mark1
new_word = "KILL YOURSELF" 
message = "goodbye master"

WORDS = ("%s" %new_word)

PRIORITY = 4
size = width, height = 320, 320
black = 0, 0, 0
x=0
y=0
##screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

def die():
    die = pygame.image.load(jasperpath.data('img/die.png'))
    die = pygame.transform.smoothscale(die, (size))
    screen.fill(black)
    screen.blit(die, (x,y))
    pygame.display.flip()

def ang():
    ang = pygame.image.load(jasperpath.data('img/ang.png'))
    ang = pygame.transform.smoothscale(ang, (size))
    screen.fill(black)
    screen.blit(ang, (x,y))
    pygame.display.flip()
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
    ang()
    
    mic.say("%s" %message)
    
    time.sleep(2)
    #pygame.QUIT

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
