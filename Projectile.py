import pygame

projectile_speed = 1

class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = projectile_speed

    def move(self):
        self.y -= self.speed

    def draw(self,window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, 10 , 10))

    def update(self,window):
        self.move()
        self.draw(window)

    def off_screen(self, height):
        return self.y < 0 or self.y > height
    
    def get_rect(self): 
        return pygame.Rect(self.x, self.y, 10, 10)
    
    def collides_with(self, enemy):
        projectile_rect = self.get_rect()
        enemy_rect = enemy.get_rect()
        return projectile_rect.colliderect(enemy_rect)
     
