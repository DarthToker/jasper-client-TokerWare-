# -*- coding: utf-8-*-
import re
import jasperpath
import time
import alteration

black = 0, 0, 0
red = (255,0,0)
white = (255,255,255)
#mark1
new_word = "WHAT IS TODAY'S DATE" 

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
    self.pygm.blittxt(date, 75, white, black)
    message = ("today's date is %s %s %s" %(a,b,c))
    mic.say("%s" %message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
