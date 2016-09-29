# -*- coding: utf-8-*-
import logging
import pkgutil
import jasperpath
import threading
from threading import Thread
#import sys, pygame
size = width, height = 320, 320
screensize = 480, 320
#screen = pygame.display.set_mode((screensize), pygame.FULLSCREEN)
#screen = pygame.display.set_mode(screensize)

red = (255,0,0)
white = (255,255,255)
black = 0, 0, 0
x=0
y=0
class Brain(object):

    def __init__(self, mic, profile, pygm):
        """
        Instantiates a new Brain object, which cross-references user
        input with a list of modules. Note that the order of brain.modules
        matters, as the Brain will cease execution on the first module
        that accepts a given input.

        Arguments:
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
        """
        self.pygm = pygm
        self.screen = self.pygm.screen
        self.blitimg = self.pygm.blitimg
        self.blittxt = self.pygm.blittxt
        self.mic = mic
        self.profile = profile
        self.modules = self.get_modules()
        self._logger = logging.getLogger(__name__)
        self.background = self.pygm.background
        #self.screen = pygame.display.set_mode((screensize), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode(screensize)
        
##        self.background = pygame.Surface(self.screen.get_size())
##        self.background = self.background.convert()
##        self.background.fill(black)

        
##    def blitimg(self, image, size, color, x, y):
##        self.background.fill(color)
##        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
##        self.img = pygame.transform.smoothscale((self.img), (size))
##        self.imgc = self.img.get_rect()
##        self.imgc.center = self.background.get_rect().center
##        self.background.blit(self.img, self.imgc)
##        self.screen.blit(self.background, (x,y))
##        pygame.display.flip()
##
##
##    def blittxt(self, txt, txts, color, bcolor):
##        self.background.fill(bcolor)
##        self.font = pygame.font.Font(None, txts)
##        self.txt = self.font.render("%s" %txt, True, (color))
##        self.textx = self.txt.get_rect()
##        self.textx.center = self.background.get_rect().center
##        self.background.blit(self.txt, self.textx)
##        self.screen.blit(self.background, (0, 0))
##        pygame.display.flip()
##
##    def bton(self, color, bx, by, txt, txts, tcolor):
##        self.background.fill(black)
##        self.font = pygame.font.Font(None, txts)
##        self.button = pygame.draw.rect(self.background, color, (bx,by,80,80), 0)
##        self.txt = self.font.render("%s" %txt, True, (tcolor))
##        self.bc = self.txt.get_rect()
##        self.bc.center = self.button.center
##        self.background.blit(self.txt, self.bc)
##        pygame.display.flip()
##
##            
    @classmethod
    def get_modules(cls):
        """
        Dynamically loads all the modules in the modules folder and sorts
        them by the PRIORITY key. If no PRIORITY is defined for a given
        module, a priority of 0 is assumed.
        """

        logger = logging.getLogger(__name__)
        locations = [jasperpath.PLUGIN_PATH]
        logger.debug("Looking for modules in: %s",
                     ', '.join(["'%s'" % location for location in locations]))
        modules = []
        for finder, name, ispkg in pkgutil.walk_packages(locations):
            try:
                loader = finder.find_module(name)
                mod = loader.load_module(name)
            except:
                logger.warning("Skipped module '%s' due to an error.", name,
                               exc_info=True)
            else:
                if hasattr(mod, 'WORDS'):
                    logger.debug("Found module '%s' with words: %r", name,
                                 mod.WORDS)
                    modules.append(mod)
                else:
                    logger.warning("Skipped module '%s' because it misses " +
                                   "the WORDS constant.", name)
        modules.sort(key=lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY')
                     else 0, reverse=True)
        return modules

    def query(self, texts):
        """
        Passes user input to the appropriate module, testing it against
        each candidate module's isValid function.

        Arguments:
        text -- user input, typically speech, to be parsed by a module
        """
        for module in self.modules:
            for text in texts:
                if module.isValid(text):
                    self._logger.debug("'%s' is a valid phrase for module " +
                                       "'%s'", text, module.__name__)
                    try:
                        module.handle(self, text, self.mic, self.profile)
                    except Exception:
                        self._logger.error('Failed to execute module',
                                           exc_info=True)
                        self.mic.say("I'm sorry." +
                                     "I fucked up. Please try again")
                    else:
                        self._logger.debug("Handling of phrase '%s' by " +
                                           "module '%s' completed", text,
                                           module.__name__)
                    finally:
                        return
        self._logger.debug("No module was able to handle any of these " +
                           "phrases: %r", texts)
