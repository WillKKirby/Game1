import pygame
from pygame.locals import *

# Start Stuff

pygame.init()

screenW,screenH = 800,400
gameDisplay = pygame.display.set_mode([screenW,screenH])

######################

# Groupes

playerGroup = pygame.sprite.Group()
platformGroup = pygame.sprite.Group()

######################

# Classes

class Player:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/playerImg.png")
        self.image = pygame.transform.scale(self.image,[50,50])
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.x_change = 0
        self.y_change = 0
        self.platform = platformGroup

    def update(self):
        self.rect.x += self.x_change
        block_hit_list = pygame.sprite.spritecollide(self,self.platform,False)
        for Q in block_hit_list:
            if self.x_change > 0:
                self.rect.right = Q.rect.left
            else:
                self.rect.left = Q.rect.right
        self.rect.y += self.y_change
        block_hit_list = pygame.sprite.spritecollide(self,self.platform,False)
        for Q in block_hit_list:
            if self.y_change > 0:
                self.rect.bottom = Q.rect.top
            else:
                self.rect.top = Q.rect.bottom

class PlatformBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/platform.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        platformGroup.add(self)

######################

# Objects

player = Player()
playerGroup.add(player)

######################

# Functions

def makeFloor():
    length = screenW//30
    startX = 0
    for Q in range(length+1):
        floor = PlatformBlock(startX,600)
        startX += 30


######################

# Main Loop


run = True
while (run):

    for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                run = False
            if Event.type == pygame.KEYDOWN:
                if Event.key == pygame.K_SPACE:
                    Jump()


    bg = pygame.image.load("images/bg.png")
    black = [0,0,0]
    
    gameDisplay.fill(black)
    gameDisplay.blit(bg,(0,0))
    
    playerGroup.draw(gameDisplay)
    pygame.display.update()



gameDisplay.close()





















