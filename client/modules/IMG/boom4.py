# -*- coding: utf-8-*-
import random
import re
import time
import RPi.GPIO as GPIO
import pygame
import time
from modules.blinks import *
import jasperpath

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)


WORDS = ["SELF DESTRUCT", "YES", "NO"]

PRIORITY = 4
image = 'bton2.png'
image2 = 'shock.png'
image3 = 'boom2.jpg'
image4 = 'die.png'
size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0


def yes(text):
    return bool(re.search(r'\byes\b', text, re.IGNORECASE))

def no(text):
    return bool(re.search(r'\b(no)\b', text, re.IGNORECASE))


def handle(self, text, mic, profile):

##    mic.say("are you sure?")
##    response = mic.activeListen()
##    if yes(response):
    done  = False
    mic.speaker.play(jasperpath.data("audio/term/t4.wav"))

    while done == False:
            a = self.blitimg(image, size, black, x, y)
            a
            #br = self.img.get_rect()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                              done = True
            pressed = pygame.key.get_pressed()
                                
            if pressed[pygame.K_DOWN]:
                done = True
            #time.sleep(0.01)
    self.blitimg(image2, size, black, x, y)
    mic.say("self destruct sequence Activated")

    for i in range(5):
        blink()

    time.sleep(1)
    for i in range(10, 0, -1):
        self.blittxt(i, 400, white, black)
        mic.say(str(i))
        time.sleep(1)
  
    self.blitimg(image3, size, black, x, y)
    mic.say("boom!")
    time.sleep(1)
    self.blitimg(image4, size, black, x, y)
    for i in range(5):
        blink2()
    
    GPIO.output(27,1)
##    elif no(response):
##        mic.say("pussy!")
def isValid(text):

    return bool(re.search(r'\bself destruct\b', text, re.IGNORECASE))
