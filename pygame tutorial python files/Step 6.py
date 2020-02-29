##Now we will create another instance of our class (also known as an object)
##utilizing the player class's constructor and we will call the methods on
##the object to draw the player and make it move. We will create a
##variable called **player2** this time before the while loop giving the player the
##following initial attributes (x: 100, y: 410, width: 64, height: 64,
##velocity: 5). Under where we called **win.blit(bg, (0,0))** to draw the
##background we will call the walk_left() method with the argument (key:
##keys[pygame.K_LEFT]), the walk_right() method with the argument (key:
##keys[pygame.K_RIGHT]), the jump() method with the argument (key:
##keys[pygame.K_UP]), and the draw() method with the argument (win:
##win).

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
              
        if not(self.isJumping):
            ##Changed from keys[pygame.K_SPACE] in past code##
            if key:
                self.isJumping = True
        else:
            if self.jumpTimeCount >= -10:

                self.y -= self.jumpTimeCount * abs(self.jumpTimeCount) 
                self.jumpTimeCount -= 1

            else:
                self.isJumping = False
                self.jumpTimeCount = 10
          


        
clock = pygame.time.Clock()



bg = pygame.image.load('bg.jpg')


player1 = player(300, 410, 64, 64, 5)

#Newly added#
player2 = player(100, 410, 64, 64, 5)
#           #

userIsPlaying = True

while userIsPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            userIsPlaying = False
    keys = pygame.key.get_pressed()
    
    
    
    win.blit(bg, (0,0))

    
    player1.walk_left(keys[pygame.K_LEFT])
    player1.walk_right(keys[pygame.K_RIGHT])
    player1.jump(keys[pygame.K_UP])
    player1.draw(win)
   
    #Newly Added#
    player2.walk_left(keys[pygame.K_a])
    player2.walk_right(keys[pygame.K_d])
    player2.jump(keys[pygame.K_w])
    player2.draw(win)
    #           # 
    
    pygame.display.update() 
    clock.tick(27)
    
pygame.quit()
