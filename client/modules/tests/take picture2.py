# -*- coding: utf-8-*-
import random
import re
import jasperpath
import sys, pygame
import time
import pygame.camera
from pygame.locals import *
import pygame.image
import os

pygame.camera.init()

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders











#mark1
new_word = "TAKE PICTURE" 
message = "taking picture"

WORDS = ("%s" %new_word)
PRIORITY = 4
size = width, height = 480, 320
black = 0, 0, 0
x=0
y=0
#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
cam = pygame.camera.Camera("/dev/video0",(640,480))

##def pic(self):
##    cam.start()
##
##    pic = cam.get_image()
##    self.screen.fill(black)
##    self.screen.blit(pic, (x,y))
##    pygame.display.flip()
##    cam.stop()
##








def handle(self,text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    stuff = os.listdir(jasperpath.data('img/'))
    count = len(stuff)
    count +=1
    cam.start()
    pic = cam.get_image()
    pygame.image.save(pic,(jasperpath.data('img/pic%s.jpg' %count)))
    self.pygm.blitimg(("pic%s.jpg" %count), size, black, x, y)

    mic.say("%s" %message)
##    pic(self)
    cam.stop()
    time.sleep(5)

    fromaddr = "projectjarvis76@gmail.com"
    #toaddr = "6103041966@txt.att.net"
    #toaddr = "carldirz1@comcast.net"
    toaddr = "6103041966@mms.att.net"

    sub = "test"
    msg = MIMEMultipart()
    pasw = "Garfield76"
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "pic"
     
    body = "blah blah"
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = ("pic%s.jpg" %count)
    attachment = open((jasperpath.data('img/pic%s.jpg' %count)), "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pasw)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()









    
def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b%s\b' %new_word, text, re.IGNORECASE)) 
