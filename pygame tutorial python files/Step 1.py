##In order to optimize this game for multiplayer we will make a Player
##class to decrease the amount of code we need to add a new character.
##We'll start out by creating the class and its constructor. The
##constructor will set all the attributes that are specific to a player.
##For us attributes will include the player's x coordinate, y coordinate,
##width, height, velocity, isJuming (boolean to see if they are jumping),
##jumpTimeCount (used to track how many iterations through the **Main
##Loop** that they have been jumping), left (boolean to track if they are
##walking left), right (boolean to track if they are walking right), and
##walkCount (integer to track how many times an arrow key for walking has
##been pressed so we know which sprite to show for the player),
##StandingCharacter (the sprite for when the player is standing), walkLeft
##(the list of sprites for when the player is walking left), and walkRight
##(the list of sprites for when the player is walking right). In order to
##ensure that each individual player will have their own individual
##attributes we will use the self parameter in the contructor. The other
##parameters include x, y, width, height, and velocity we will set the
##rest of the variables to values that will be the same for the start for
##all players (like right is True).


##Don't worry you will get some errors if you run this step##

import pygame
pygame.init()

window_width = 500
window_height = 480
win = pygame.display.set_mode((window_width,window_height))

pygame.display.set_caption("First Game")

#Newly added#
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

#         #        
        
        
#Newly Moved#
#x = 50
#y = 400
#width = 64
#height = 64
#velocity = 5
#         #

clock = pygame.time.Clock()

#Newly Moved#
#left = False
#right = False
#walkCount = 0
#          #

bg = pygame.image.load('bg.jpg')

#Newly Moved#
#StandingCharacter = pygame.image.load('standing.png')
#walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
#walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
#
#isJumping = False
#jumpTimeCount = 10
#           #


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
