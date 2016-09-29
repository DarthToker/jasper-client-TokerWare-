# -*- coding: utf-8-*-
import datetime
import re
from client.app_utils import getTimezone
from semantic.dates import DateService
import time
import pygame
import alteration

WORDS = ["CLOCK MODE"]

black = 0, 0, 0
red = (255,0,0)
white = (255,255,255)

def handle(self, text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """ 


    mic.say("clock mode on")
    done=False
    while done == False:
        
        t =(time.strftime("%m/%d/%Y"))
        a,b,c = t.split('/')

        if a == '01':
            a = 'January'

        if a == '02':
            a = 'February'
            
        if a == '03':
            a = 'March'
             
        if a == '04':
            a = 'April'
             
        if a == '05':
            a = 'May'
             
        if a == '06':
            a = 'June'
             
        if a == '07':
            a = 'July'
         
        if a == '08':
            a = 'August'
               
        if a == '09':
            a = 'September'
            
        if a == '10':
            a = 'October'
            
        if a == '11':
            a = 'November'
            
        if a == '12':
            a = 'December'
            
        d,e = b
        if d == '0':
            b = e
            
        date = ('%s %s %s'%(a,b,c)) 
        
        self.background.fill(black)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                                  done = True
        tz = getTimezone(profile)
        now = datetime.datetime.now(tz=tz)
        service = DateService()
        response = service.convertTime(now)       
        self.pygm.blitjtxt(response, 150, 0, 240, 160, white)
        self.pygm.blitjtxt(date, 40, 0, 240, 220, white)

        pygame.display.flip()
        time.sleep(1)    


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bclock mode\b', text, re.IGNORECASE))
