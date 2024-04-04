import pygame
import window_parameters as wp 

from Projectile import Projectile 

width = 50
height = 50  

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 5
        elif direction == "right" and self.x < wp.window_width - self.width:
            self.x += 5

    def shoot_projectile(self):
        projectile = Projectile(self.x + self.width // 2, self.y)
        return projectile
    
    
