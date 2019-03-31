import pygame,random,time
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
        self.platform = platformGroup
        self.platform2 = floorGroup
        self.gravCount = 0
        self.gravCurve = [3.4113999999999995, 3.019000000000002, 2.626599999999998, 2.2341999999999995, 1.8417999999999992, 1.4494000000000042, 1.056999999999995, 0.6646000000000072, 0.27219999999999445, -0.12020000000000053, -0.5125999999999991, -0.9050000000000082, -1.2973999999999961, -1.6898000000000053, -2.082199999999993, -2.4746000000000095, -2.8670000000000044, -3.2594000000000065, -3.6517999999999944, -4.044200000000004]
        playerGroup.add(self)

    def update(self):

        if self.rect.x > 800 or self.rect.x < 0:
            print('Dead')
            self.kill()

class PlatformBlock(pygame.sprite.Sprite):
    def __init__(self,height,x,y):
        super().__init__()
        self.image = pygame.image.load("images/platform.png")
        self.image = pygame.transform.scale(self.image,[30,(30*height)])
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y-(30*height)]
        self.x_change = 1
        self.y_change = 0
        self.platform = playerGroup
        platformGroup.add(self)
    
    def update(self):
        if self.rect.x > 800 or self.rect.x == 0:
            self.kill()

        self.rect.x -= self.x_change
        block_hit_list = pygame.sprite.spritecollide(self,self.platform,False)
        for Q in block_hit_list:
            player.rect.x -= self.x_change
            if self.x_change < 0:
                self.rect.right = Q.rect.left
            else:
                self.rect.left = Q.rect.right
                
        self.rect.y - self.y_change
        block_hit_list = pygame.sprite.spritecollide(self,self.platform,False)
        for Q in block_hit_list:
            if self.y_change > 0:
                self.rect.bottom = Q.rect.top
            else:
                self.rect.top = Q.rect.bottom
        

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
        floor = floorBlock(startX,370)
        startX += 30
    startX = 0
    for Q in range(length+1):
        floor = floorBlock(startX,340)
        startX += 30
        
def makePlatform():
    height = random.randint(1,4)
    platfrom = PlatformBlock(height,730,340)

######################

# Main Loop

def main():
    genCycle = 1
    makeObj = True
    run = True
    jump = False
    
    
    makeFloor() # This makes the floor ... derrrr

    bg = pygame.image.load("images/bg.png")
    black = [0,0,0]
    
    while (run):

        for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    run = False
                if Event.type == pygame.KEYDOWN:
                    if Event.key == pygame.K_SPACE:
                        jump = True

        ######################

        # Logic Stuff

        # Makes the platforms appear 
        genCycle -= 1
        if genCycle == 0 and makeObj:
            makePlatform()
            genCycle = 200

        
        # Jumpy Code
        if jump == True:
            player.rect.y -= player.gravCurve[player.gravCount]
            player.gravCount += 1
            if player.gravCount == len(player.gravCurve):
                player.gravCount = 0
                jump = False
            if player.rect.y > 310:
                player.rect.y = 310

            
        ######################

        # Drawing All the stuff on the screen 
        
        gameDisplay.fill(black)
        gameDisplay.blit(bg,(0,0))

        floorGroup.draw(gameDisplay)
        platformGroup.draw(gameDisplay)

        platformGroup.update()
        playerGroup.draw(gameDisplay)
        playerGroup.update()
        pygame.display.update()



    gameDisplay.close()

main()



















