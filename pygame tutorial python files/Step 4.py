##Lastly we will add in the jump() method so that the player can jump.
##Like the walk_left() and walk_right() methods the jump() method will
##have the self the universal self parameter and the additional key
##parameter. We will be doing the same thing that we did for the
##walk_left() and walk_right() methods adding the if and else statements
##controlling the jump mechanics for the player into the jump() method and
##replace keys[pygame.K_SPACE] with the key parameter key.

import pygame
pygame.init()

window_width = 500
window_height = 480
win = pygame.display.set_mode((window_width,window_height))

pygame.display.set_caption("First Game")


class player():
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.isJumping = False
        self.jumpTimeCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standingCharacter = pygame.image.load('standing.png')
        self.walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
        self.walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
    
    
    def draw(self, win):
        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
        else:
            win.blit(self.standingCharacter, (self.x,self.y))
            
           
    def walk_left(self, key):
        ##Changed from keys[pygame.K_LEFT] in past code##
        if key:
            self.x -= self.velocity
            self.left = True
            self.right = True
            self.walkCount += 1
        ##Slightly different than we had before##
            self.walkCount %= 27
    def walk_right(self, key):
        ##Changed from keys[pygame.K_RIGHT] in past code##
        if key:
            self.x += self.velocity
            self.left = False
            self.right = True
            self.walkCount += 1
        ##Slightly different than we had before##
            self.walkCount %= 27
            
            
    def jump(self, key):        
        #Newly Added#        
        if not(self.isJumping):
            ##Changed from keys[pygame.K_SPACE] in past code##
            if key:
                self.isJumping = True
        else:
            if self.jumpTimeCount >= -10:

                self.-y -= self.jumpTimeCount * abs(self.jumpTimeCount) 
                self.jumpTimeCount -= 1

            else:
                self.isJumping = False
                self.jumpTimeCount = 10
        #         #   


clock = pygame.time.Clock()



bg = pygame.image.load('bg.jpg')



userIsPlaying = True

while userIsPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            userIsPlaying = False
    keys = pygame.key.get_pressed()
        
    
    win.blit(bg, (0,0))
    
    #Newly Moved#
    #if not(isJumping):
    #    if keys[pygame.K_SPACE]:
    #        isJumping = True
    #else:
    #    if jumpTimeCount >= -10:
    #        
    #        y -= jumpTimeCount * abs(jumpTimeCount) 
    #        jumpTimeCount -= 1
    #        
    #    else:
    #        isJumping = False
    #        jumpTimeCount = 10
    #          #        
    
    pygame.display.update() 
    clock.tick(27)
    
pygame.quit()
