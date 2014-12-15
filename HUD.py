import pygame, sys, pyganim
from pygame.locals import *
from random import randint

class BasicHUD(object):
    def __init__(self,x,y):
        pass
    def playAnimation(self,objAnimation):
        self.objAnimation.play()
        self.status = 'playing'
        
    def pauseAnimation(self,objAnimation):
        self.objAnimation.pause()
        self.status = 'paused'
    
    def stopAnimation(self,objAnimation):
        self.objAnimation.stop()
        self.status = 'stopped'
    
    def blitAnimaton(self,objAnimation,surface):
        self.objAnimation.blit(surface, (self.x,self.y))
        
    def popUp(self,objAnimation,surface,font,color):
        self.targetFrame = randint(0,7)
        self.pauseAnimation(self.objAnimation);
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
            
    def frameValue(self,objAnimation):
        return self.objAnimation.currentFrameNum

##########################################################

class Cycle(BasicHUD):
    def __init__(self,window_width,window_height):
        self.RUNNING_IMG_WIDTH = 291
        self.RUNNING_IMG_HEIGHT = 291
        self.status = 'stopped'
        self.targetFrame = 0
        self.frameDuration = 0.07
        self.wasPopup = False
        self.x = window_width/2 - (self.RUNNING_IMG_WIDTH/2)
        self.y = window_height/2 - (self.RUNNING_IMG_HEIGHT/2)
        self.objAnimation = pyganim.PygAnimation([('CYCLE/cycle-01.png',self.frameDuration),
                                              ('CYCLE/cycle-02.png',self.frameDuration),
                                              ('CYCLE/cycle-03.png',self.frameDuration),
                                              ('CYCLE/cycle-04.png',self.frameDuration),
                                              ('CYCLE/cycle-05.png',self.frameDuration),
                                              ('CYCLE/cycle-06.png',self.frameDuration),
                                              ('CYCLE/cycle-07.png',self.frameDuration),
                                              ('CYCLE/cycle-08.png',self.frameDuration)])

    
    def drawTarget(self,surface,font,color):
        targetFrameDraw = font.render('Target: %d' %self.targetFrame, True, color)
        targetFrameRect = targetFrameDraw.get_rect()
        targetFrameRect.topleft = (600 , 130)
        surface.blit(targetFrameDraw,targetFrameRect)

    def update(self,event,player,surface,font,color):
        if event.type == KEYDOWN and event.key == K_e and self.isPopup() == False and self.isPopup() == False:
            self.popUp(self.objAnimation,surface,font,color)
        if event.type == KEYDOWN and event.key == K_SPACE and self.isPaused() == True and self.isPopup() == True:
            self.playAnimation(self.objAnimation)
        elif event.type == KEYDOWN and event.key == K_SPACE and self.isPaused() == False and self.isPopup() == True:
            self.pauseAnimation(self.objAnimation)
            if self.frameValue(self.objAnimation) == self.targetFrame:
                player.wasBuff()
            else:
                player.wasAttacked()

##########################################################

class ChoiceBox(BasicHUD):
    def __init__(self,window_width,window_height):
        self.x = 20
        self.y = window_height/1.45
        self.status = 'stopped'
        self.wasPopup = False
        self.objAnimation = pyganim.PygAnimation([('CHOICEBOX/test_choiceBox-01.jpg',0.1),
                                                 ('CHOICEBOX/test_choiceBox-02.jpg',0.1),
                                                 ('CHOICEBOX/test_choiceBox-03.jpg',0.1)])

    def playNextFrame(self):
        self.objAnimation.nextFrame()

    def playPrevFrame(self):
        self.objAnimation.prevFrame()

    def popUp(self,objAnimation,surface):
        self.pauseAnimation(objAnimation)
        self.wasPopup = True

    def update(self,event,surface):
        if event.type == KEYDOWN and event.key == K_e and self.isPopup() == False:
            self.popUp(self.objAnimation,surface)
        if event.type == KEYDOWN and event.key == K_DOWN and self.isPaused() == True and self.isPopup() == True:
            self.playNextFrame()
        elif event.type == KEYDOWN and event.key == K_UP and self.isPaused() == True and self.isPopup() == True:
            self.playPrevFrame()

##########################################################

class CooldownBox(BasicHUD):
    def __init__(self,window_width,window_height):
        self.x = 20
        self.y = window_height/1.45
        self.status = 'stopped'
        self.wasPopup = False
        self.choiceBoxAni = pyganim.PygAnimation([('CHOICEBOX/test_choiceBox-01.jpg',0.1),
                                                 ('CHOICEBOX/test_choiceBox-02.jpg',0.1),
                                                 ('CHOICEBOX/test_choiceBox-03.jpg',0.1)])

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
    # def update(self,event,surface):
