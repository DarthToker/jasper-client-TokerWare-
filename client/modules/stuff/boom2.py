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


##WORDS = ["SELF DESTRUCT", "YES", "NO"]

PRIORITY = 4
size = width, height = 320, 320
black = 0, 0, 0
red = (255,0,0)
white = (255,255,255)
x=0
y=0
##screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
shock = (jasperpath.data('img/shock.png'))
die = (jasperpath.data('img/die.png'))
boom = (jasperpath.data('img/boom2.jpg'))
bton = (jasperpath.data('img/bton2.png'))
clock = pygame.time.Clock()

##def boom():    
##    boom = pygame.image.load(jasperpath.data('img/boom2.jpg'))
##    boom = pygame.transform.smoothscale(boom, (size))
##    screen.fill(black)
##    screen.blit(boom, (x,y))
##    pygame.display.flip()
##def die():    
##    die = pygame.image.load(jasperpath.data('img/die.png'))
##    die = pygame.transform.smoothscale(die, (size))
##    screen.fill(black)
##    screen.blit(die, (x,y))
##    pygame.display.flip()
##def shock():    
##    shock = pygame.image.load(jasperpath.data('img/shock.png'))
##    shock = pygame.transform.smoothscale(shock, (size))
##    screen.fill(black)
##    screen.blit(shock, (x,y))
##    pygame.display.flip() 
##def blink():
##    GPIO.output(17,1)
##    time.sleep(0.05)
##    GPIO.output(17,0)
##    time.sleep(0.05)
##    GPIO.output(27,1)
##    time.sleep(0.05)
##    GPIO.output(27,0)
##    time.sleep(0.05)
##def blink2():
##    GPIO.output(17,1)
##    GPIO.output(27,1)
##    time.sleep(0.03)
##    GPIO.output(17,0)
##    GPIO.output(27,0)
##    time.sleep(0.03)
def blitimg(image, size, color):
    global img
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color)
    img = pygame.image.load(image)
    img = pygame.transform.smoothscale((img), (size))
    imgc = img.get_rect()
    imgc.center = background.get_rect().center
    background.blit(img, imgc)
    screen.fill(color)
    screen.blit(background, (x,y))
    pygame.display.flip()
    




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
                blitimg(bton, size, black)
                br = img.get_rect()
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
                clock.tick(60)
                
        self.blitimg(shock, size, black)
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
        
        blitimg(boom, size, black)
        mic.say("boom!")
        time.sleep(1)
        blitimg(die, size, black)
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
