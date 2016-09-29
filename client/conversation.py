# -*- coding: utf-8-*-
import logging
from notifier import Notifier
from brain import Brain
import random
import sys, pygame
import jasperpath
import time

image = 'nu.png'
size = width, height = 320, 320
screensize = 480, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0



class Conversation(object):

    def __init__(self, persona, mic, profile, pygm):
        self._logger = logging.getLogger(__name__)
        self.persona = persona
        self.mic = mic
        self.pygm = pygm
        self.profile = profile
        self.brain = Brain(mic, profile, pygm)
        self.notifier = Notifier(profile)
    def handleForever(self):
        """
        Delegates user input to the handling function when activated.
        """
        self._logger.info("Starting to handle conversation with keyword '%s'.",
                          self.persona)


        while self.pygm.on == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on = False
                if event.type == pygame.KEYDOWN:           
                    if event.key == pygame.K_RIGHT:
                        self.pygm.on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pygm.on = False
                    
            self.pygm.blitimg(image, size, black, x, y)   
            # Print notifications until empty
            notifications = self.notifier.getAllNotifications()
            for notif in notifications:
                self._logger.info("Received notification: '%s'", str(notif))

            self._logger.debug("Started listening for keyword '%s'",
                               self.persona)
            threshold, transcribed = self.mic.passiveListen(self.persona)
            self._logger.debug("Stopped listening for keyword '%s'",
                               self.persona)

            if not transcribed or not threshold:
                self._logger.info("Nothing has been said or transcribed.")
                continue
            self._logger.info("Keyword '%s' has been said!", self.persona)

            self._logger.debug("Started to listen actively with threshold: %r",
                               threshold)
            input = self.mic.activeListenToAllOptions(threshold)
            self._logger.debug("Stopped to listen actively with threshold: %r",
                               threshold)

            if input:
                self.brain.query(input)
            else:
                self.pygm.blittxt('???', 400, red, black)

                messages = ["what?",
                            "what did you say",
                            "Say that again?", "speak the fuck up", "i cant fucking hear you", "blah blah blah", "did you say something?"]

                message = random.choice(messages)
                self.mic.say(message)
        pygame.quit()
