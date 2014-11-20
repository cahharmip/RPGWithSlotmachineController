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
        self.frameDuration = 0.07
        self.wasPopup = False
        self.x = window_width/2 - (self.RUNNING_IMG_WIDTH/2)
        self.y = window_height/2 - (self.RUNNING_IMG_HEIGHT/2)
        self.cycleAni = pyganim.PygAnimation([('CYCLE/cycle-01.png',self.frameDuration),
                                              ('CYCLE/cycle-02.png',self.frameDuration),
                                              ('CYCLE/cycle-03.png',self.frameDuration),
                                              ('CYCLE/cycle-04.png',self.frameDuration),
                                              ('CYCLE/cycle-05.png',self.frameDuration),
                                              ('CYCLE/cycle-06.png',self.frameDuration),
                                              ('CYCLE/cycle-07.png',self.frameDuration),
                                              ('CYCLE/cycle-08.png',self.frameDuration)])
        
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

######## May Be This class will inherit with Cycle and name it as BasicHUD #######

class ChoiceBox(object):
    def __init__(self,window_width,window_height):
        self.x = 20
        self.y = window_height/1.45
        self.status = 'stopped'
        self.wasPopup = False
        self.choiceBoxAni = pyganim.PygAnimation([('CHOICEBOX/test_choiceBox-01.jpg',0.1),
                                                 ('CHOICEBOX/test_choiceBox-02.jpg',0.1),
                                                 ('CHOICEBOX/test_choiceBox-03.jpg',0.1)])

    def playAnimation():
        pass

    def pauseAnimation(self):
        self.choiceBoxAni.pause()
        self.status = 'paused'

    def stopAnimation(self):
        self.choiceBoxAni.stop()
        self.status = 'stopped'

    def playNextFrame(self):
        self.choiceBoxAni.nextFrame()

    def playPrevFrame(self):
        self.choiceBoxAni.prevFrame()

    def blitAnimaton(self,surface):
        self.choiceBoxAni.blit(surface, (self.x,self.y))

    def frameValue(self):
        return self.choiceBoxAni.currentFrameNum

    def popUp(self,surface):
        self.pauseAnimation()
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

##########################################################

class CooldownBox(object):
    def __init__(self):
        pass
