# -*- coding: utf-8-*-
import logging
from notifier import Notifier
from brain import Brain
import random
import sys, pygame
import jasperpath
import time

pygame.init()
size = width, height = 320, 320
black = 0, 0, 0
x=0
y=0
##screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
pygame.display.set_caption('jarvis')
pygame.mouse.set_visible(False)
def nu():
    nu = pygame.image.load(jasperpath.data('img/nu.png'))
    nu = pygame.transform.smoothscale(nu, (size))
    screen.fill(black)
    screen.blit(nu, (x,y))
    pygame.display.flip()
def zip2():
    zip2 = pygame.image.load(jasperpath.data('img/zip2.png'))
    zip2 = pygame.transform.smoothscale(zip2, (size))
    screen.fill(black)
    screen.blit(zip2, (x,y))
    pygame.display.flip()
global on
on = True

class Conversation(object):

    def __init__(self, persona, mic, profile):
        self._logger = logging.getLogger(__name__)
        self.persona = persona
        self.mic = mic
        self.profile = profile
        self.brain = Brain(mic, profile)
        self.notifier = Notifier(profile)

    def handleForever(self):
        """
        Delegates user input to the handling function when activated.
        """
        self._logger.info("Starting to handle conversation with keyword '%s'.",
                          self.persona)
        while on == True:

            nu()
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
                messages = ["what?",
                            "what did you say",
                            "Say that again?", "speak the fuck up", "i cant fucking hear you", "blah blah blah", "did you say something?"]

                message = random.choice(messages)
                zip2()
                self.mic.say(message)
                #time.sleep(1)
