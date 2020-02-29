##Now we'll have to add attributes and a method to our player class so our player can have health shoot
##the projectiles. First we will add the **health** and **bullets** attributes to the player class. 
##**health** will be an integer that stores the player's health and **bullets** will be a list of 
##of the player's projectiles that they have shot. Next we will add a shoot method that like the jump()
##method will take the universal self parameter and the key parameter for the key the user hits to make
##the player shoot. Since the length of the bullets list is the number of bullets that the player has
##shot and I only want the player to be able to shoot 3 bullets at a time, while I am checking to see
##if the user hit the shoot key I will also check if the length of the bullets list is less than 3 with
##the built-in len() function. Within that if statement their is an if-else statement checking the 
##which direction the player is facing (its used to decide if the velocity given to the projectile
##should be negative i.e. player is facing the left or positive otherwise so if the player is facing
##right). Then we will add a projectile to the bullets list utilizing the list datatype's append
##method, the projectile constructor, and the attributes of the player. **We'll use + self.width//2
##and + self.height//2 to center the bullet relative to the player when it is shot and set the velocity
##to 8 (right) or -8 (left) depending on if the player is facing right or left.** Outside of those if
##statements we will use an enrinched for loop to go throught the projectiles in the player's bullets
##list. We will call the move() and draw() methods on each bullet in the for loop and check if the
##bullet should still exist because if a bullet is off screen we need to get rid of it so the player
##can shoot more bullets. We'll use an if statement with the bullets x value and the window_width
##variable to check if the bullet is on screen and we will also check if the bullet's done attribute
##is True because if it is that means that it hit another player and it needs to disapear so the player
##can shoot more bullets. In this if statement to get rid of these bullets we will use the
##list datatype's pop() method which gets rid of an element in a list at a certain index along with
##the list datatype's index() method which returns the index of a certain element in a list.

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
        health = 0
        bullets = []
        #           #
    
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

    #Newly added#            
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
    #          #
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
   
    
    player2.walk_left(keys[pygame.K_a])
    player2.walk_right(keys[pygame.K_d])
    player2.jump(keys[pygame.K_w])
    player2.draw(win)
    
    
    pygame.display.update() 
    clock.tick(27)
    
pygame.quit()
