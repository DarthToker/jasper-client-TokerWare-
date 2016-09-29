# -*- coding: utf-8-*-
import random
import re
import time
import RPi.GPIO as GPIO
import jasperpath
import pygame
import time
from modules.IMG.pygamef import blittxt
from modules.blinks import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)


#WORDS = ["SELF DESTRUCT", "YES", "NO"]

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
    return bool(re.search(r'\b(yes)\b', text, re.IGNORECASE))

def no(text):
    return bool(re.search(r'\b(no)\b', text, re.IGNORECASE))


def handle(self, text, mic, profile):

    mic.say("are you sure?")
    response = mic.activeListen()
    if yes(response):
        done  = False
        mic.speaker.play(jasperpath.data("audio/term/t4.wav"))

        while done == False:
                self.blitimg(image, size, black, x, y)
                br = self.img.get_rect()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                pos = pygame.mouse.get_pos()
                                if br.collidepoint(pos):
                                  done = True
                pressed = pygame.key.get_pressed()
                                    
                if pressed[pygame.K_DOWN]:
                    done = True
                time.sleep(0.01)
        self.blitimg(image2, size, black, x, y)
        mic.say("self destruct sequence Activated")

        blink()
        blink()
        blink()
        blink()
        blink()

        time.sleep(1)
        
        blittxt(10, 120, white, black)
        mic.say("10")
        time.sleep(1)
        
        blittxt(9, 120, white, black)
        mic.say("9")
        time.sleep(1)
        
        blittxt(8, 120, white, black)
        mic.say("8")
        time.sleep(1)
        
        blittxt(7, 120, white, black)
        mic.say("7")
        time.sleep(1)

        blittxt(6, 120, white, black)
        mic.say("6")
        time.sleep(1)

        blittxt(5, 120, white, black)
        mic.say("5")
        time.sleep(1)

        blittxt(4, 120, white, black)
        mic.say("4")
        time.sleep(1)

        blittxt(3, 120, red , black)
        mic.say("3")
        time.sleep(1)

        blittxt(2, 120, red, black)
        mic.say("2")
        time.sleep(1)

        blittxt(1, 120, red, black)
        mic.say("1")
        time.sleep(1)
        
        self.blitimg(image3, size, black, x, y)
        mic.say("boom!")
        time.sleep(1)
        self.blitimg(image4, size, black, x, y)
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        blink2()
        GPIO.output(27,1)
    elif no(response):
        mic.say("pussy!")
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bself destruct\b', text, re.IGNORECASE))
