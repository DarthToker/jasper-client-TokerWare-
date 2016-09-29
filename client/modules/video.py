# -*- coding: utf-8-*-
import random
import re
import jasperpath
import sys, pygame
import time
import pygame.camera
from pygame.locals import *
import pygame.image
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))


image = 'nu.png'
size = width, height = 480, 320
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

x=0
y=0
nsize = 160,120

#mark1
new_word = "VIDEO" 
message = "camera on"

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
    cam.start()
    pic = cam.get_image()
    pic = pygame.transform.smoothscale(pic, nsize)

    done = True
    while done == True :
        for e in pygame.event.get() :
            if e.type == pygame.QUIT :
                done = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                done = False


        self.pygm.background.fill(black)
        picc = pic.get_rect()
        picc.center = self.pygm.background.get_rect().center
        self.pygm.background.blit(pic, picc)
        self.screen.blit(self.pygm.background, (x,y))
             
        #self.pygm.screen.blit(pic, (x, y))
        pygame.display.flip()
        pic = cam.get_image()
        pic = pygame.transform.smoothscale(pic, nsize)

    cam.stop()




    


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
