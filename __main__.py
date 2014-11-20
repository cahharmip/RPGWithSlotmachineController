'''
Created on 15 11 2557

@author: champ_krup
'''
#add Status Dex and level with 3 stage 

import pygame, sys, pyganim
from pygame.locals import *
from gamelib import SimpleGame
from random import randint
from element import Player,Enemy
from HUD import Cycle

class  SlotMachineGame(SimpleGame):
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    WHITE = pygame.Color('white')
    BLACK = pygame.Color('black')

    def __init__(self):
        super(SlotMachineGame, self).__init__('SlotMachineGame',SlotMachineGame.WHITE,SlotMachineGame.WINDOW_SIZE)
        self.roulette = Cycle(SlotMachineGame.WINDOW_WIDTH,SlotMachineGame.WINDOW_HEIGHT)
        self.champ = Player()

    def init(self):
        super(SlotMachineGame, self).init()
        
    def update(self,event):
        # if self.is_key_pressed(K_e) and self.roulette.isPopup() == False:
        #     self.roulette.popUp(self.surface,self.font,SlotMachineGame.BLACK)
        # if self.is_key_pressed(K_SPACE) and self.roulette.isPaused() == True and self.roulette.isPopup() == True:
        #     self.roulette.playAnimation()
        # elif self.is_key_pressed(K_SPACE) and self.roulette.isPaused() == False and self.roulette.isPopup() == True:
        #     self.roulette.pauseAnimation()
        #     if self.roulette.frameValue() == self.roulette.targetFrame:
        #         self.champ.wasBuff()
        #     else:
        #         self.champ.wasAttacked()
        if event.type == KEYDOWN and event.key == K_e and self.roulette.isPopup() == False:
            self.roulette.popUp(self.surface,self.font,SlotMachineGame.BLACK)
        if event.type == KEYDOWN and event.key == K_SPACE and self.roulette.isPaused() == True and self.roulette.isPopup() == True:
            self.roulette.playAnimation()
        elif event.type == KEYDOWN and event.key == K_SPACE and self.roulette.isPaused() == False and self.roulette.isPopup() == True:
            self.roulette.pauseAnimation()
            if self.roulette.frameValue() == self.roulette.targetFrame:
                self.champ.wasBuff()
            else:
                self.champ.wasAttacked()
    
    def render(self, surface):
        self.roulette.blitAnimaton(surface)
        self.roulette.drawTarget(surface,self.font,SlotMachineGame.BLACK)
        self.champ.printDamage(surface,self.font,SlotMachineGame.BLACK)
        self.champ.printHP(surface,self.font,SlotMachineGame.BLACK)    
        surface.blit
        
def main():
    game = SlotMachineGame()
    game.run()

if __name__ == '__main__':
    main()