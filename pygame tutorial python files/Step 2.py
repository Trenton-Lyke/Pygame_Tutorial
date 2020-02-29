##Now we are going to making some methods (functions specific to classes)
##to control the drawing and movement of the player with the code we used
##before. The first method we will add is the draw() method which will
##draw the player with the right sprite and in the correct position
##utilizing the players x, y, left, right, walkLeft, walkRight,
##standingCharacter, and walkCount attributes of the player and the self
##parameter along with a given window that we will take as another
##parameter for the method. We will do this by moving the if-elif-else
##statement that we had drawing the character based on the left, right,
##and walkCount variables into the draw method. **Remember we have to use
##the self parameter to access the attributes of a specific instance**.

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
    
    #Newly added#
    def draw(self, win):
        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
        else:
            win.blit(self.standingCharacter, (self.x,self.y))
     #        #   
        


clock = pygame.time.Clock()



bg = pygame.image.load('bg.jpg')



userIsPlaying = True

while userIsPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            userIsPlaying = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocity
        
        
        left = True
        right = False
        walkCount += 1
   
        
    if keys[pygame.K_RIGHT]:
        x += velocity
        
        
        left = False
        right = True
        walkCount += 1
    

    if not(isJumping):
        if keys[pygame.K_SPACE]:
            isJumping = True
    else:
        if jumpTimeCount >= -10:
            
            y -= jumpTimeCount * abs(jumpTimeCount) 
            jumpTimeCount -= 1
            
        else:
            isJumping = False
            jumpTimeCount = 10
    
   
    
    
    win.blit(bg, (0,0))
    
    #Newly Moved#
    #if left:
    #    win.blit(walkLeft[walkCount//3], (x,y))
    #elif right:
    #    win.blit(walkRight[walkCount//3], (x,y))
    #else:
    #    win.blit(standingCharacter, (x,y))
    #        #
    
    
    pygame.display.update() 
    clock.tick(27)
    
pygame.quit()
