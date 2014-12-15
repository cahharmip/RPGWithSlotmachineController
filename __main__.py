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
from HUD import Cycle , ChoiceBox

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
        self.choicebox = ChoiceBox(SlotMachineGame.WINDOW_WIDTH,SlotMachineGame.WINDOW_HEIGHT)

    def init(self):
        super(SlotMachineGame, self).init()
        
    def update(self,event):
        self.roulette.update(event,self.champ,self.surface,self.font,SlotMachineGame.BLACK)
        self.choicebox.update(event,self.surface)

    def render(self, surface):
        self.roulette.blitAnimaton(self.roulette,surface)
        self.choicebox.blitAnimaton(self.choicebox,surface)
        self.roulette.drawTarget(surface,self.font,SlotMachineGame.BLACK)
        self.champ.printDamage(surface,self.font,SlotMachineGame.BLACK)
        self.champ.printHP(surface,self.font,SlotMachineGame.BLACK)    
        surface.blit
        
def main():
    game = SlotMachineGame()
    game.run()

if __name__ == '__main__':
    main()