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
        self.image = pygame.image.load("images/playerImg.png") # image loading
        self.image = pygame.transform.scale(self.image,[30,30])
        self.rect = self.image.get_rect()
        self.rect.x = 370 
        self.rect.y = 310 # These are the starting positions 
        self.gravCount = 0 # This is the grav jumping curve
        self.gravCurve = [1.7547500000000005, 1.656649999999999, 1.5585500000000003, 1.4604499999999998, 1.362350000000001, 1.264249999999997, 1.1661500000000036, 1.0680499999999977, 0.9699499999999972, 0.871850000000002, 0.7737499999999997, 0.6756500000000045, 0.5775499999999951, 0.47945000000000704, 0.38134999999999764, 0.28324999999999534, 0.1851500000000037, 0.08704999999999785, -0.01104999999999734, -0.10915000000000319, -0.20725000000000193, -0.3053500000000007, -0.403450000000003, -0.5015500000000017, -0.599650000000004, -0.6977499999999992, -0.7958499999999944, -0.8939500000000038, -0.9920500000000061, -1.0901500000000084, -1.1882500000000036, -1.2863500000000059, -1.3844500000000082, -1.482549999999975, -1.5806500000000128, -1.678750000000008, -1.776849999999996, -1.8749499999999983, -1.9730500000000006]
        playerGroup.add(self) # Obviously adding self to group

    def update(self):
        if self.rect.x > 800 or self.rect.x < 0:
            print('Dead') # Check on screen 
            self.kill()

class PlatformBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.height = random.randint(1,3)
        self.image = pygame.image.load("images/platform.png")
        self.image = pygame.transform.scale(self.image,[30,(30*self.height)])
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y-(30*self.height)]
        self.x_change = 1.5
        self.y_change = 0
        self.platform = playerGroup
        platformGroup.add(self)
    
    def update(self):
        if self.rect.x > 800 or self.rect.x == 0:
            self.kill()

        
        self.x_change = 1
        self.rect.x -= self.x_change
        block_hit_list = pygame.sprite.spritecollide(self,self.platform,False)
        for Q in block_hit_list:
            player.rect.x -= self.x_change
            if Q.gravCount > ((len(Q.gravCurve)-1)/2)+1:
                self.rect.right = Q.rect.left
            else:
                self.rect.left = Q.rect.right

        '''
        block_hit_list2 = pygame.sprite.spritecollide(self,self.platform,False)
        for Q in block_hit_list2:
            Q.rect.x += 2
        '''
                
        

class floorBlock(pygame.sprite.Sprite): # Floor 
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
        floor = floorBlock(startX,340) # I'm lazy, there are 2 so it is ticker 
        startX += 30

######################

# Main Loop

def main():
    genCycle = 1
    makeObj = True
    run = True
    jump = False
    
    clock = pygame.time.Clock()
    fps = 120
    
    makeFloor() # This makes the floor ... derrrr

    bg = pygame.image.load("images/bg.png")
    black = [0,0,0]

    slow = False
    
    while (run):

        for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    run = False
                if Event.type == pygame.KEYDOWN:
                    if Event.key == pygame.K_SPACE:
                        jump = True
                    if Event.key == pygame.K_s:
                        slow = True
                    if Event.key == pygame.K_f:
                        slow = False
        ######################

        # Logic Stuff

        if slow == True:
            time.sleep(0.1)
            print(player.rect.y)

        # Makes the platforms appear 
        genCycle -= 1
        if genCycle == 0 and makeObj:
            platfrom = PlatformBlock(730,340)
            genCycle = 200

        
        # Jumpy Code
        if jump == True:
            player.rect.y -= player.gravCurve[player.gravCount]*10
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

        clock.tick(fps)

main()

pygame.display.quit()

















