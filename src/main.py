from abc import ABC, abstractmethod
import pygame
import sys
from block import *
import time
import numpy as np

BG=(0,0,0)

def refresh():
    screen.fill('black')       
    screen.blit(gamePlace,[0,0])
    block1.updata()
    teewee.updata()
    pygame.display.flip()

GameMaps= np.ones((3, 3), dtype=np.int32)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
gamePlace = pygame.Surface((500,800))
gamePlace.fill("white")
pygame.display.set_caption("Tetris demo")
block1=Block("red",[0,0],screen)
teewee=Teewee("Teewee","red",[BLOCK_SIZE*3,BLOCK_SIZE*3],screen)
times=0
while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                block1.rightBlock()
                teewee.rightBlock()
            if event.key == pygame.K_LEFT:
                block1.leftBlock()
                teewee.leftBlock()
            if event.key == pygame.K_UP:
                block1.upBlock()
                teewee.upBlock()
            if event.key == pygame.K_DOWN:
                block1.downBlock()
                teewee.downBlock()
            refresh()
    times+=1000/50
    if times%500 == 0:
        block1.downBlock()
        teewee.downBlock() 
    
    print(clock.get_time())
    refresh()


