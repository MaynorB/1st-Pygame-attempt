# Example file showing a circle moving on screen
import pygame

import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK = pygame.time.Clock()
FPS = 60  # frame rate
ANI = 4  # animation cycles
PLAYER_MOVE_CONSTANT = 5 

    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, image_path):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image = pygame.image.load(image_path)
    
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    def draw(self, surface):
        surface.blit(self.image, self.position)

    #Position Based Movement meaning it moves in x or y direction based on a constant delta
    def pmove_left(self):
        self.position = (self.position[0] - PLAYER_MOVE_CONSTANT, self.position[1])
    
    def pmove_right(self):
        self.position = (self.position[0] + PLAYER_MOVE_CONSTANT, self.position[1])
    
    def pmove_up(self):
        self.position = (self.position[0], self.position[1] - PLAYER_MOVE_CONSTANT)

    def pmove_down(self):
        self.position = (self.position[0], self.position[1] + PLAYER_MOVE_CONSTANT)
    #Velocity Based meaning continous movement in one direction until interupted 
    def vmove_left(self):
        self.velocity = (-1,0)
    
    def vmove_right(self):
        self.velocity = (1, 0)
    
    def vmove_up(self):
        self.velocity = (0, -1)

    def vmove_down(self):
        self.velocity = (0, 1)


# pygame setup
# Initialize Pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a player sprite
player = Player(320, 240, 0, 0, "Kermitgun.png")






# Main game loop
while True:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Changes Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            player.pmove_left()
    if keys[pygame.K_RIGHT]:
            player.pmove_right()
    if keys[pygame.K_UP]:
            player.pmove_up()
    if keys[pygame.K_DOWN]:
            player.pmove_down()

        


    

    
    # Clear the window
    window.fill((255, 255, 255))
    
    # Draw the player sprite
    player.draw(window)
    
    # Update the display
    pygame.display.update()

    CLOCK.tick(FPS)