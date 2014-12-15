import pygame, sys, pyganim
from pygame.locals import *

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
    
    def printDamage(self,surface,font,color):
        totalDamageDraw = font.render('Player\'s Damage: %d' %self.totalDamage, True, color)
        totalDamageRect = totalDamageDraw.get_rect()
        totalDamageRect.topleft = (100, 130)
        surface.blit(totalDamageDraw,totalDamageRect)
    
    def printHP(self,surface,font,color):
        currentHPDraw = font.render('Player\'s HP: %d' %self.currentHP, True, color)
        currentHPRect = currentHPDraw.get_rect()
        currentHPRect.topleft = (100, 230)
        surface.blit(currentHPDraw,currentHPRect)

    def update(self):
        pass
        
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