# -*- coding: utf-8-*-
import random
import re
import jasperpath
import pygame
import os
import time
size = 100,100
screensize = 480, 320
gray     = (100, 100, 100)
nvb = ( 60,  60, 100)
white    = (255, 255, 255)
red      = (255,   0,   0)
green    = (  0, 255,   0)
blue     = (  0,   0, 255)
yellow   = (255, 255,   0)
orang   = (255, 128,   0)
purple   = (255,   0, 255)
cyan     = (  0, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()

x=0
y=0

#mark1
new_word = "SCREENSAVER" 
message = "screen saver on"

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
    done = False

    self.pygm.background.fill(black)
    self.pygm.screen.blit(self.background, (0, 0))
    pygame.display.flip()
    mic.say("%s" %message)

    while done == False:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                done = True
            if event2.type == pygame.MOUSEBUTTONDOWN:
                done = True
        rf = random.choice(os.listdir(jasperpath.data("img/")))
        for i in range(30):
            for event2 in pygame.event.get():
                if event2.type == pygame.QUIT:
                    done = True
                if event2.type == pygame.MOUSEBUTTONDOWN:
                    done = True
            ix = random.randint(0,480)
            iy = random.randint(0,320)
            self.pygm.blitjimg(ix,iy,rf,size,0)
            pygame.display.flip()
            time.sleep(.5)

        


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
