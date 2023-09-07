from abc import ABC, abstractmethod
import pygame
import sys
BLOCK_SIZE=50


class Block:
    def __init__(self,color="red",position=[0,0],surface : pygame.Surface = None) -> None:
        self.color = color 
        self.surface = surface 
        self.image_surface = pygame.transform.scale(pygame.image.load("./pic/"+color+".png"),[BLOCK_SIZE,BLOCK_SIZE])
        self.position = self.image_surface.get_rect()
        self.position.topleft = position

    def move(self,site):
        if self.isInsurface(site):
            self.position=self.position.move(site)
            return True
        else:
            return False
        
    def upBlock(self):
        return self.move([0,0-BLOCK_SIZE]) 

    def downBlock(self):
        return self.move([0,BLOCK_SIZE])

    def leftBlock(self):
        return self.move([0-BLOCK_SIZE,0])

    def rightBlock(self):
        return self.move([BLOCK_SIZE,0])

    def updata(self):
        self.surface.blit(self.image_surface,self.position)

    def isInsurface(self,site):
        return self.surface.get_rect().contains(self.position.move(site))
        
class BlockGroup(ABC):
    blocks=[Block() for i in range(4)]
    def __init__(self,name="Teewee",color="red",position=[0,0],surface : pygame.Surface =None) -> None:
        self.name = name
        self.color = color 
        self.position = position
        self.surface = surface
        self.creat()

    @abstractmethod
    def creat(self):
        pass

    def move(self,site):
        if self.isInsurface(site):
            [block.move(site) for block in self.blocks]
            return True
        else:
            return False
    
    def upBlock(self):
        return self.move([0,0-BLOCK_SIZE]) 

    def downBlock(self):
        return self.move([0,BLOCK_SIZE])
    
    def leftBlock(self):
        return self.move([0-BLOCK_SIZE,0])

    def rightBlock(self):
        return self.move([BLOCK_SIZE,0])
    
    def updata(self):
        [block.updata() for block in self.blocks]

    def isInsurface(self,site):
        flag=1
        for block in self.blocks:
            flag &= block.isInsurface(site)
        return flag