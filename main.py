import pygame,random
from pygame.locals import *

# Start Stuff

pygame.init()

screenW,screenH = 800,400
gameDisplay = pygame.display.set_mode([screenW,screenH])

######################

# Groupes

playerGroup = pygame.sprite.Group()
platformGroup = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()

######################

# Classes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/playerImg.png")
        self.image = pygame.transform.scale(self.image,[30,30])
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 310
        self.x_change = 0
        self.y_change = 0
        self.platform = platformGroup
        playerGroup.add(self)

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
    def Move(self):
        self.rect.x -= 1

class floorBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/platform.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        floorGroup.add(self)
    
######################

# Objects

player = Player()

######################

# Functions

def makeFloor():
    length = screenW//30
    startX = 0
    for Q in range(length+1):
        floor = PlatformBlock(startX,370)
        startX += 30
    startX = 0
    for Q in range(length+1):
        floor = PlatformBlock(startX,340)
        startX += 30
        
def makePlatform():
    length = random.randint(2,10)
    height = random.randint(1,4)
    StartY = 340
    for Q in range(height):
        platfrom = PlatformBlock(730,StartY)
        StartY -= 30
######################

# Main Loop

def main():
    genCycle = 1
    run = True

    makeFloor() # This makes the floor ... derrrr

    bg = pygame.image.load("images/bg.png")
    black = [0,0,0]
    
    while (run):

        for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    run = False
                if Event.type == pygame.KEYDOWN:
                    if Event.key == pygame.K_SPACE:
                        Jump()

        ######################
        # Obsticle Generation
        genCycle -= 1
        if genCycle == 0:
            makePlatform()
            genCycle = 50
        ######################

        # Drawing All the stuff on the screen 
        
        gameDisplay.fill(black)
        gameDisplay.blit(bg,(0,0))

        floorGroup.draw(gameDisplay)
        platformGroup.draw(gameDisplay)
        for Q in platformGroup:
            Q.Move()
        playerGroup.draw(gameDisplay)
        playerGroup.update()
        pygame.display.update()



    gameDisplay.close()

main()



















