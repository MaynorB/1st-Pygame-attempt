# Example file showing a circle moving on screen
import pygame

import random


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK = pygame.time.Clock()
FPS = 60  # frame rate
ANI = 4  # animation cycles
PLAYER_MOVE_CONSTANT = 5
ENEMY_SPEED_CONSTANT = 2

#Player, Enemies, Bullet Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.position = (x, y)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (80, 60))
        self.rect = self.image.get_rect()
        self.faceRight = False
    

    # Update to how the image is drawn on the screen
    def draw(self, surface):
        surface.blit(self.image, self.position)


    def update(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if not self.facingRight():
                    player.flipTheImage()
            if event.key == pygame.K_LEFT:
                if self.facingRight():
                    self.flipTheImage()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pmove_left()
        if keys[pygame.K_RIGHT]:
            self.pmove_right()
        if keys[pygame.K_UP]:
            self.pmove_up()
        if keys[pygame.K_DOWN]:
            self.pmove_down()

    def flipTheImage(self):
        self.image =  pygame.transform.flip(self.image, True, False)
        self.faceRight = not self.faceRight

    def facingRight(self):
         return self.faceRight


    def getPosition(self):
         return self.position

    #Position Based Movement meaning it moves in x or y direction based on a constant delta
    def pmove_left(self):
        self.position = (self.position[0] - PLAYER_MOVE_CONSTANT, self.position[1])
    
    def pmove_right(self):
        self.position = (self.position[0] + PLAYER_MOVE_CONSTANT, self.position[1])
    
    def pmove_up(self):
        self.position = (self.position[0], self.position[1] - PLAYER_MOVE_CONSTANT)

    def pmove_down(self):
        self.position = (self.position[0], self.position[1] + PLAYER_MOVE_CONSTANT)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.position = pygame.math.Vector2((x,y)) 
        self.speed = ENEMY_SPEED_CONSTANT
    
    def update(self, player):
        self.hunt_player(player)

    def hunt_player(self, player):
        player_position = player.position
        direction = player_position - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.topleft = self.position
    
    def draw(self, surface):
        surface.blit(self.image, self.position)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, Player):
        self.position = Player.getPosition()//2

# Functions for new bullet and enemies
def newEnemy():
    e = Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), "Enemy_Images/Mickey.png")
    enemies.add(e)

# pygame setup
# Initialize Pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a player sprite
player = Player(SCREEN_WIDTH// 2 , SCREEN_HEIGHT // 2, "Player_images/Kermitgun.png")


#Sprite groups
enemies = pygame.sprite.Group()


for i in range(2):
    newEnemy()






# Main game loop
while True:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet(player)



    
    player.update()
    enemies.update(player)

    window.fill((0,0,0))

    
    player.draw(window)
    enemies.draw(window)
    

    # *after* drawing everything, flip the display
    pygame.display.flip()

    CLOCK.tick(FPS)