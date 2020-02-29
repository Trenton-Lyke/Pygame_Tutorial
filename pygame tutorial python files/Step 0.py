
##Your original code##

import pygame
pygame.init()

window_width = 500
window_height = 480
win = pygame.display.set_mode((window_width,window_height))

pygame.display.set_caption("First Game")

      
        
        

x = 50
y = 400
width = 64
height = 64
velocity = 5


clock = pygame.time.Clock()


left = False
right = False
walkCount = 0


bg = pygame.image.load('bg.jpg')


standingCharacter = pygame.image.load('standing.png')
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]

isJumping = False
jumpTimeCount = 10



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
    
    walkCount %= 27
    
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
    
    
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
    else:
        win.blit(standingCharacter, (x,y))
    
    
    
    pygame.display.update() 
    clock.tick(27)
    
pygame.quit()
