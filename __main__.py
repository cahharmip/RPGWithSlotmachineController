'''
Created on 15 11 2557

@author: champ_krup
'''
#add Status Dex and level with 3 stage 

import pygame, sys, pyganim
from pygame.locals import *
from random import randint
# from gamelib import SimpleGame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')

class Cycle(object):
    def __init__(self):
        self.RUNNING_IMG_WIDTH = 291
        self.RUNNING_IMG_HEIGHT = 291
#         self.TARGET_IMG_WIDTH = 0
#         self.TARGET_IMG_HEIGHT = 0
        self.status = 'stopped'
        self.targetFrame = 0
        self.wasPopup = False
        self.x = WINDOW_WIDTH/2 - (self.RUNNING_IMG_WIDTH/2)
        self.y = WINDOW_HEIGHT/2 - (self.RUNNING_IMG_HEIGHT/2)
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
    
    def blitAnimaton(self):
        self.cycleAni.blit(gameDisplay, (self.x,self.y))
        
    def popUp(self):
        self.targetFrame = randint(0,7)
        self.pauseAnimation()
        self.drawTarget()
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
    
    def drawTarget(self):
        targetFrameDraw = BASICFONT.render('Target: %d' %self.targetFrame, True, BLACK)
        targetFrameRect = targetFrameDraw.get_rect()
        targetFrameRect.topleft = (600 , 130)
        gameDisplay.blit(targetFrameDraw,targetFrameRect)
    
##################################################

class Player(object):
    def __init__(self):
        self.maxHP = 100.0
        self.minHP = 0
        self.currentHP = 100.0
        self.initDamage = 10.0
        self.totalDamage = 0.0
        self.bonusDamage = 0.0
    
    def wasBuff(self):
        self.bonusDamage = 0.15 * self.currentHP
        self.totalDamage = self.initDamage + self.bonusDamage
    
    def wasAttacked(self):
        self.currentHP -= 10;
    
    def printDamage(self):
        totalDamageDraw = BASICFONT.render('Player\'s Damage: %d' %self.totalDamage, True, BLACK)
        totalDamageRect = totalDamageDraw.get_rect()
        totalDamageRect.topleft = (100, 130)
        gameDisplay.blit(totalDamageDraw,totalDamageRect)
    
    def printHP(self):
        currentHPDraw = BASICFONT.render('Player\'s HP: %d' %self.currentHP, True, BLACK)
        currentHPRect = currentHPDraw.get_rect()
        currentHPRect.topleft = (100, 230)
        gameDisplay.blit(currentHPDraw,currentHPRect)
        
##################################################

class Enemy(object):
    def __init__(self):
        self.maxHP = 100
        self.minHP = 0
        self.currentHP = 100
        self.initDamage = 10
        canAttack = False

    def attackPlayer(self,player):
        player.wasAttacked

    def setCooldown(self):
        pass

    def onCooldown(self):
        return canAttack

    def wasAttackedBy(self,player):
        self.currentHP -= player.totalDamage

##################################################

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

################################################## 
 
def main():
    roulette = Cycle()
    champ = Player()
    while True:
        gameDisplay.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_e and roulette.isPopup() == False:
                roulette.popUp()
            if event.type == KEYDOWN and event.key == K_SPACE and roulette.isPaused() == True and roulette.isPopup() == True:
                roulette.playAnimation()
            elif event.type == KEYDOWN and event.key == K_SPACE and roulette.isPaused() == False and roulette.isPopup() == True:
                roulette.pauseAnimation()
                if roulette.frameValue() == roulette.targetFrame:
                    champ.wasBuff()
                else:
                    champ.wasAttacked()
        roulette.blitAnimaton()
        roulette.drawTarget()
        champ.printDamage()
        champ.printHP()
        gameDisplay.blit          
        pygame.display.update()
        clock.tick(60) #chooseFPS

if __name__ == '__main__':
    pygame.init() 
    gameDisplay = pygame.display.set_mode(WINDOW_SIZE)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    pygame.display.set_caption('A bit Racey') 
    clock = pygame.time.Clock()
    main()
    pygame.quit()
    quit()