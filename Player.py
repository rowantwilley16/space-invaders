import pygame
import window_parameters as wp 

from Projectile import Projectile 

width = 50
height = 50  

# Set the image path for the player
player_image_path = "assets/player.png"

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.image.load(player_image_path)

        # Scale the player image to fit the player dimensions
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def draw(self, window):
        #pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height))
        window.blit(self.image, (self.x, self.y))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 5
        elif direction == "right" and self.x < wp.window_width - self.width:
            self.x += 5

    def shoot_projectile(self):
        projectile = Projectile(self.x + self.width // 2, self.y)
        return projectile
    
    
