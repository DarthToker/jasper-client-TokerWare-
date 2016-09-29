# -*- coding: utf-8-*-
import random
import re
import time
import RPi.GPIO as GPIO
import jasperpath
import pygame
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)


#WORDS = ["SELF DESTRUCT", "YES", "NO"]

PRIORITY = 4
size = width, height = 320, 320
black = 0, 0, 0
x=0
y=0
#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

def boom():    
    boom = pygame.image.load(jasperpath.data('img/boom2.jpg'))
    boom = pygame.transform.smoothscale(boom, (size))
    screen.fill(black)
    screen.blit(boom, (x,y))
    pygame.display.flip()
def die():    
    die = pygame.image.load(jasperpath.data('img/die.png'))
    die = pygame.transform.smoothscale(die, (size))
    screen.fill(black)
    screen.blit(die, (x,y))
    pygame.display.flip()
def shock():    
    shock = pygame.image.load(jasperpath.data('img/shock.png'))
    shock = pygame.transform.smoothscale(shock, (size))
    screen.fill(black)
    screen.blit(shock, (x,y))
    pygame.display.flip() 
def blink():
    GPIO.output(17,1)
    time.sleep(0.05)
    GPIO.output(17,0)
    time.sleep(0.05)
    GPIO.output(27,1)
    time.sleep(0.05)
    GPIO.output(27,0)
    time.sleep(0.05)
def blink2():
    GPIO.output(17,1)
    GPIO.output(27,1)
    time.sleep(0.03)
    GPIO.output(17,0)
    GPIO.output(27,0)
    time.sleep(0.03)





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
    mic.say("are you sure?")
    response = mic.activeListen()
    if yes(response):
        shock()
        blink()
        blink()
        blink()
        blink()
        blink()
        mic.say("self destruct sequence Activated")
        blink()
        blink()
        blink()
        blink()
        blink()
        time.sleep(1)
        mic.say("10")
        time.sleep(1)
        mic.say("9")
        time.sleep(1)
        mic.say("8")
        time.sleep(1)
        mic.say("7")
        time.sleep(1)
        mic.say("6")
        time.sleep(1)
        mic.say("5")
        time.sleep(1)
        mic.say("4")
        time.sleep(1)
        mic.say("3")
        time.sleep(1)
        mic.say("2")
        time.sleep(1)
        mic.say("1")
        time.sleep(1)
        boom()
        mic.say("boom!")
        time.sleep(1)
        die()
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
