from blockBase import *

class Teewee(BlockGroup):
    
    def creat(self):
        self.blocks[0]=Block(self.color,self.position,self.surface)
        self.blocks[1]=Block(self.color,[self.position[0],self.position[0]-BLOCK_SIZE],self.surface)
        self.blocks[2]=Block(self.color,[self.position[0]-BLOCK_SIZE,self.position[1]],self.surface)
        self.blocks[3]=Block(self.color,[self.position[0]+BLOCK_SIZE,self.position[1]],self.surface)

class OrangeRicky(BlockGroup):
    def creat(self):
        self.blocks[0]=Block(self.color,self.position,self.surface)
        self.blocks[1]=Block(self.color,[self.position[0],self.position[0]-BLOCK_SIZE],self.surface)
        self.blocks[2]=Block(self.color,[self.position[0]-BLOCK_SIZE,self.position[1]],self.surface)
        self.blocks[3]=Block(self.color,[self.position[0]+BLOCK_SIZE,self.position[1]],self.surface)

class Hero(BlockGroup):
    def creat(self):
        self.blocks[0]=Block(self.color,self.position,self.surface)
        self.blocks[1]=Block(self.color,[self.position[0],self.position[0]-BLOCK_SIZE],self.surface)
        self.blocks[2]=Block(self.color,[self.position[0]-BLOCK_SIZE,self.position[1]],self.surface)
        self.blocks[3]=Block(self.color,[self.position[0]+BLOCK_SIZE,self.position[1]],self.surface)

class BlueRick(BlockGroup):
    def creat(self):
        self.blocks[0]=Block(self.color,self.position,self.surface)
        self.blocks[1]=Block(self.color,[self.position[0],self.position[0]-BLOCK_SIZE],self.surface)
        self.blocks[2]=Block(self.color,[self.position[0]-BLOCK_SIZE,self.position[1]],self.surface)
        self.blocks[3]=Block(self.color,[self.position[0]+BLOCK_SIZE,self.position[1]],self.surface)

class ClevelandZ(BlockGroup):
    def creat(self):
        self.blocks[0]=Block(self.color,self.position,self.surface)
        self.blocks[1]=Block(self.color,[self.position[0],self.position[0]-BLOCK_SIZE],self.surface)
        self.blocks[2]=Block(self.color,[self.position[0]-BLOCK_SIZE,self.position[1]],self.surface)
        self.blocks[3]=Block(self.color,[self.position[0]+BLOCK_SIZE,self.position[1]],self.surface)

class RhodeIslandZ(BlockGroup):
    def creat(self):
        self.blocks[0]=Block(self.color,self.position,self.surface)
        self.blocks[1]=Block(self.color,[self.position[0],self.position[0]-BLOCK_SIZE],self.surface)
        self.blocks[2]=Block(self.color,[self.position[0]-BLOCK_SIZE,self.position[1]],self.surface)
        self.blocks[3]=Block(self.color,[self.position[0]+BLOCK_SIZE,self.position[1]],self.surface)

class SmashBoy(BlockGroup):
    def creat(self):
        self.blocks[0]=Block(self.color,self.position,self.surface)
        self.blocks[1]=Block(self.color,[self.position[0],self.position[0]-BLOCK_SIZE],self.surface)
        self.blocks[2]=Block(self.color,[self.position[0]-BLOCK_SIZE,self.position[1]],self.surface)
        self.blocks[3]=Block(self.color,[self.position[0]+BLOCK_SIZE,self.position[1]],self.surface)