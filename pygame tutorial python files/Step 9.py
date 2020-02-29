##Now we will call the shoot method for each player in the main loop giving the shoot keys as
##keys[pygame.K_s] for player 1 and keys[pygame.K_s] for player 2. Try running it... cool right. But
##hitting each other is not decreasing the other player's health we can fix this by adding a
##isInHitBox() method to the player class. We will return the boolean result (True or False) of if the
##x and y coordinate given as parameters is within the players hit box. We'll then use this
##method in the main loop within a enriched for loop going through each bullet. We'll check if
##each bullet of the player is in the the hit box of the opposing player with the isInHitBox() method
##with the x and y coordinates of the bullet. If the bullet is in the hit box we will set the bullet's
##done property to True since the bullet hit something and should disapear, subtract 5 from the
##health of the player that was hit, and display the player's health in the console with the built-in
##print() function.

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
        self.health = 100
        self.bullets = []
    
    def draw(self, win):
        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
        else:
            win.blit(self.standingCharacter, (self.x,self.y))
            
           
    def walk_left(self, key):
        if key:
            self.x -= self.velocity
            self.left = True
            self.right = True
            self.walkCount += 1
            self.walkCount %= 27
    def walk_right(self, key):
        if key:
            self.x += self.velocity
            self.left = False
            self.right = True
            self.walkCount += 1
            self.walkCount %= 27
            
            
    def jump(self, key):        
              
        if not(self.isJumping):
            
            if key:
                self.isJumping = True
        else:
            if self.jumpTimeCount >= -10:

                self.y -= self.jumpTimeCount * abs(self.jumpTimeCount) 
                self.jumpTimeCount -= 1

            else:
                self.isJumping = False
                self.jumpTimeCount = 10

               
    def shoot(self, key):
        if key and len(self.bullets) < 3:
            
            if self.left:
                ##scroll to the right to see the rest##
                self.bullets.append(projectile(self.x + self.width//2, self.y + self.height//2, 5, (0,0,0), -8))
            else:
                ##scroll to the right to see the rest##
                self.bullets.append(projectile(self.x + self.width//2, self.y + self.height//2, 5, (0,0,0), 8))
        for bullet in self.bullets:
            
            bullet.move()
            bullet.draw(win)
            if bullet.x > window_width or bullet.x < 0 or bullet.done:
                self.bullets.pop(self.bullets.index(bullet))

    def isInHitBox(self,x,y):
        return x > self.x + 7 and x < self.x + self.width - 7 and y < self.y + self.height and y > self.y
    
class projectile(object):
    
    def __init__(self, x, y, radius, color, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = velocity
        self.done = False                       

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velocity

        
clock = pygame.time.Clock()



bg = pygame.image.load('bg.jpg')


player1 = player(300, 410, 64, 64, 5)


player2 = player(100, 410, 64, 64, 5)


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
    player1.shoot(keys[pygame.K_SPACE])
    #           #
    
    player2.walk_left(keys[pygame.K_a])
    player2.walk_right(keys[pygame.K_d])
    player2.jump(keys[pygame.K_w])
    player2.draw(win)

    #Newly Added#
    player2.shoot(keys[pygame.K_s])
    #Newly Added#

    #Newly Added#
    for bullet in player1.bullets:
        if player2.isInHitBox(bullet.x,bullet.y):
            player2.health -= 5
            bullet.done = True
            print("player2 health: " + str(player2.health))

    for bullet in player2.bullets:
        if player1.isInHitBox(bullet.x,bullet.y):
            player1.health -= 5
            bullet.done = True
            print("player1 health: " + str(player1.health))
    #          #       

    
    
    
    pygame.display.update() 
    clock.tick(27)
    
pygame.quit()
