# -*- coding: utf-8-*-
import random
import re
import os
import jasperpath
import RPi.GPIO as GPIO
import time
import sys, pygame

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,0)

WORDS = ["SHUTDOWN"]

PRIORITY = 3


image = 'h9.png'

size = width, height = 320, 320
red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0


def handle(self, text, mic, profile):
    import subprocess
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages = ["shutting down"]

    message = random.choice(messages)
    GPIO.output(12,1)
    self.blitimg(image, size, black, x, y)
    mic.speaker.play(jasperpath.data('audio/hal/cantalow.wav'))
    GPIO.output(12,0)

    mic.say(message)
    subprocess.call(["sudo", "shutdown", "now"])


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bshutdown\b', text, re.IGNORECASE))
