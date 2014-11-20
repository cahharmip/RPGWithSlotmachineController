import pygame, sys, pyganim
from pygame.locals import *
from gamelib import SimpleGame
from random import randint

class Cycle(object):
    def __init__(self,window_width,window_height):
        self.RUNNING_IMG_WIDTH = 291
        self.RUNNING_IMG_HEIGHT = 291
#         self.TARGET_IMG_WIDTH = 0
#         self.TARGET_IMG_HEIGHT = 0
        self.status = 'stopped'
        self.targetFrame = 0
        self.wasPopup = False
        self.x = window_width/2 - (self.RUNNING_IMG_WIDTH/2)
        self.y = window_height/2 - (self.RUNNING_IMG_HEIGHT/2)
        self.cycleAni = pyganim.PygAnimation([('CYCLE/cycle-01.png',0.07),
                                              ('CYCLE/cycle-02.png',0.07),
                                              ('CYCLE/cycle-03.png',0.07),
                                              ('CYCLE/cycle-04.png',0.07),
                                              ('CYCLE/cycle-05.png',0.07),
                                              ('CYCLE/cycle-06.png',0.07),
                                              ('CYCLE/cycle-07.png',0.07),
                                              ('CYCLE/cycle-08.png',0.07)])
        
    def playAnimation(self):
        self.cycleAni.play()
        self.status = 'playing'
        
    def pauseAnimation(self):
        self.cycleAni.pause()
        self.status = 'paused'
    
    def stopAnimation(self):
        self.cycleAni.stop()
        self.status = 'stopped'
    
    def blitAnimaton(self,surface):
        self.cycleAni.blit(surface, (self.x,self.y))
        
    def popUp(self,surface,font,color):
        self.targetFrame = randint(0,7)
        self.pauseAnimation()
        self.drawTarget(surface,font,color)
        self.wasPopup = True

    def isPopup(self):
        return self.wasPopup
    
    def isPlaying(self):
        if self.status == 'playing' or self.status == 'paused':
            return True
        elif self.status == 'stopped':
            return False

    def isPaused(self):
        if self.status == 'paused':
            return True
        else:
            return False
            
    def frameValue(self):
        return self.cycleAni.currentFrameNum
    
    def drawTarget(self,surface,font,color):
        targetFrameDraw = font.render('Target: %d' %self.targetFrame, True, color)
        targetFrameRect = targetFrameDraw.get_rect()
        targetFrameRect.topleft = (600 , 130)
        surface.blit(targetFrameDraw,targetFrameRect)

    def update(self):
        pass


##########################################################

class HUD(object):
    def __init__(self):
        self.x = 30
        self.y = 450
        self.choiceBoxAni = pyganim.PygAnimation([('CHOICEBOX/test_choiceBox-01',0.1),
                                                 ('CHOICEBOX/test_choiceBox-02',0.1),
                                                 ('CHOICEBOX/test_choiceBox-03',0.1)])

    def pauseAnimation(self):
        self.choiceBoxAni.pause()

    def updateHUD(self, key):
        pass

    def stopAnimation(self):
        self.choiceBoxAni.stop()
