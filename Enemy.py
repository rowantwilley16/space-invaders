import random
import pygame 
import window_parameters as wp

width   =   50 
height  =   40

# Set the image path for the enemy
enemy_image_path = "assets/enemy.png"

class Enemy:
    def __init__(self, x, y):
        # x and y positions 
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #image of the enemy
        self.image = pygame.image.load(enemy_image_path)

        # Scale the enemy image to fit the enemy dimensions
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        #health bar 
        self.health = 100
        self.max_health = 100
        self.health_bar_width = self.width
        self.health_bar_height = 5
        self.health_bar_color = (0, 255, 0)  # Green color for health bar
        self.health_bar_bg_color = (255, 0, 0)  # Red color for background of health bar

    def draw(self, window):
        #pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

        # Draw the enemy image
        window.blit(self.image, (self.x, self.y))

        pygame.draw.rect(window, self.health_bar_bg_color, (self.x, self.y - 10, self.width, self.health_bar_height))
        pygame.draw.rect(window, self.health_bar_color, (self.x, self.y - 10, int(self.health_bar_width), self.health_bar_height))

    def move(self):

        changeDir = random.randint(0,10)

        if (changeDir == 0):
            randomDir = random.choice(["left", "right"])

            if randomDir == "left": 
                self.x -= 5
            elif randomDir == "right":
                self.x += 5

        if self.x < 0:
            self.x = 0
        elif self.x >wp.window_width - self.width:
            self.x = wp.window_width - self.width
        if self.y < 0:
            self.y = 0
        elif self.y > wp.window_height // 2 - self.height:
            self.y = wp.window_height // 2 - self.height

    def take_damage(self, damage=10):

        self.health -= damage
        self.update_health_bar()
        if self.health <= 0:
            return True
        return False

    def get_rect(self): 
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def collides_with(self, projectile): 
        enemy_rect = self.get_rect()
        projectile_rect = projectile.get_rect()
        return enemy_rect.colliderect(projectile_rect)
    
    def update_health_bar(self): 
        # Calculate the width of the health bar based on current health
        self.health_bar_width = (self.health / self.max_health) * self.width

    