# -*- coding: utf-8-*-
import jasperpath
import sys, pygame
import time
import pygame.camera
from pygame.locals import *
pygame.init()
pygame.camera.init
pygame.display.set_caption('jarvis')
pygame.mouse.set_visible(False)


image = 'nu.png'
size = width, height = 320, 320
screensize = 480, 320
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
x=0
y=0


class Pygm(object):

    def __init__(self):
        
        self.screen = pygame.display.set_mode((screensize), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        #self.screen = pygame.display.set_mode(screensize)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.on = True
        #self.background.fill(black)

    def fbackground(self, color):
        self.background.fill(color)

    def bbackground(self):
        self.screen.blit(self.background, (0, 0))
    
    def flip(self):
        pygame.display.flip()

    def blitimg(self, image, size, color, x, y):

        self.background.fill(color)
        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.imgc = self.img.get_rect()
        self.imgc.center = self.background.get_rect().center
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))
        pygame.display.flip()
        imgc = self.imgc
        return imgc


    def blittxt(self, txt, txts, color, bcolor):

        self.background.fill(bcolor)
        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.textx = self.txt.get_rect()
        self.textx.center = self.background.get_rect().center
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def blitimg2(self, image, size,  x, y):

        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.imgc = self.img.get_rect()
        self.imgc.center = self.background.get_rect().center
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))
        pygame.display.flip()

    def blittxt2(self, txt, txts, color, bcolor):

        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.textx = self.txt.get_rect()
        self.textx.center = self.background.get_rect().center
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        
    def blittxt3(self, txt, txts, color, tx, ty):

        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.textx = self.txt.get_rect()
        self.textx.center = (tx, ty)
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()


    def bton(self, color, bx, by, txt, txts, tcolor):

        self.font = pygame.font.Font(None, txts)
        self.button = pygame.draw.rect(self.background, color, (bx,by,80,80), 0)
        self.txt = self.font.render("%s" %txt, True, (tcolor))
        self.bc = self.txt.get_rect()
        self.bc.center = self.button.center
        self.background.blit(self.txt, self.bc)
        pygame.display.flip()
        
    def bton2(self, color, bx, by, txt, txts, tcolor):
        font = pygame.font.Font(None, txts)
        button = pygame.draw.rect(self.background, color, (bx,by,80,80), 0)
        txt = font.render("%s" %txt, True, (tcolor))
        bc = txt.get_rect()
        bc.center = button.center
        self.background.blit(txt, bc)

    def takepic():
        self.cam = pygame.camera.Camera('/dev/video0', (640, 480))
        self.cam.start()
        self.background.fill(color)
        pic = cam.get_image()
        pygame.image.save(image,'abc.jpg')
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.imgc = self.img.get_rect()
        self.imgc.center = self.background.get_rect().center
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))
        pygame.display.flip()

    def blitimgspin(self, image, size, color, x, y, deg):

        self.background.fill(color)
        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.img = pygame.transform.rotate(self.img, deg)
        self.imgc = self.img.get_rect()
        self.imgc.center = self.background.get_rect().center
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))
        pygame.display.flip()

    def blittxtimgam(self, txt, txts, color, tx, ty, ix, iy, image, size, imgdeg, txtdeg, bcolor):
        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.img = pygame.transform.rotate(self.img, imgdeg)
        self.imgc = self.img.get_rect()
        self.imgc.center = (ix,iy)
        self.background.fill(bcolor)
        self.background.blit(self.img, self.imgc)
        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.txt = pygame.transform.rotate(self.txt, txtdeg)
        self.textx = self.txt.get_rect()
        self.textx.center = (tx, ty)
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def cam1(self, image, size, color, x, y):

        self.background.fill(color)
        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.imgc = self.img.get_rect()
        self.imgc.center = self.background.get_rect().center
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))
        pygame.display.flip()

        
    def blitjimg(self, ix, iy, image, size, imgdeg):
        self.img = pygame.image.load(jasperpath.data('img/%s' %image))
        self.img = pygame.transform.smoothscale((self.img), (size))
        self.img = pygame.transform.rotate(self.img, imgdeg)
        self.imgc = self.img.get_rect()
        self.imgc.center = (ix,iy)
        self.background.blit(self.img, self.imgc)
        self.screen.blit(self.background, (x,y))

    def blitjtxt(self, txt,txts,txtdeg,tx,ty,color):
        self.font = pygame.font.Font(None, txts)
        self.txt = self.font.render("%s" %txt, True, (color))
        self.txt = pygame.transform.rotate(self.txt, txtdeg)
        self.textx = self.txt.get_rect()
        self.textx.center = (tx, ty)
        self.background.blit(self.txt, self.textx)
        self.screen.blit(self.background, (0, 0))















        
