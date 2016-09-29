# -*- coding: utf-8-*-
import random
import re
import jasperpath
import sys, pygame
import os
image = 'sm2.png'
size = width, height = 480, 320
screensize = 480, 320
imsize = 100, 100
speed = [1, 1]

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

x=123
y=147

#mark1
new_word = "BOUNCE" 
message = "bouncing"

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
    global ball

    def getpic():

        randomfile = random.choice(os.listdir(jasperpath.data("img/")))
        rfile = jasperpath.data('img/'+ randomfile)
        ball = pygame.image.load(rfile)                      
        ball = pygame.transform.smoothscale(ball, imsize)
        global ball

    getpic()
    ballrect = ball.get_rect()
    done = False
    count=0
    deg=0
    while done == False:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                done = True
            if event2.type == pygame.MOUSEBUTTONDOWN:
                done = True
        count +=1
##        deg +=1
        if count == 1000:
            count = 0
            getpic()
##        if deg == 360:
##            deg=0

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        pos = pygame.mouse.get_pos()
        #ball = pygame.transform.rotate(ball, deg)
        self.screen.fill(black)
        self.screen.blit(ball, ballrect)
        pygame.display.flip()
        #print deg
        clock.tick(60)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
