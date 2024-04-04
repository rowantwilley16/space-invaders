import pygame
import sys

import graphics as gfx
import Player as Player             #imports the module 
import Enemy as Enemy
import window_parameters as wp
import GameStateManager as GameStateManager
from Projectile import Projectile   #imports the class 

# Initialize Pygame
pygame.init()

#player dimensions 
player_width    = 50
player_height   = 50

window = pygame.display.set_mode((wp.window_width, wp.window_height))
pygame.display.set_caption("Space Invaders")

#setup a rectangle that the player can move around on the screen
player  = Player.Player(wp.centre_horizontal - player_width // 2, wp.window_height - player_height)
enemy   = Enemy.Enemy(wp.centre_horizontal , wp.window_height - 500)

# Game loop
running = True
game_states = ["MENU","PLAY"] #add more game states as needed
current_game_state = 0

# FPS counter
clock           = pygame.time.Clock()
fps_font        = pygame.font.Font(None, 15)

# List to hold active projectiles
active_projectiles = []

# Cooldown variables
shoot_cooldown = 200
shoot_delay = 200  # Delay between shots in milliseconds

def handle_events():
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while running:
    
    if game_states[current_game_state] == "MENU":
        button_rect = wp.draw_start_screen(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_states[current_game_state] == "MENU":
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    current_game_state = 1 #switch to gamestate 1
                    # Start the game here or transition to the game state
                    print("Begin Game")    

    if game_states[current_game_state] == "PLAY":
        handle_events()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.move("left")
        elif keys[pygame.K_d] and player.x < wp.window_width - player_width:
            player.move("right")

        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - shoot_cooldown > shoot_delay:
            projectile = player.shoot_projectile()
            active_projectiles.append(projectile)
            shoot_cooldown = pygame.time.get_ticks()

        # Game logic
        enemy.move()

        # Update projectiles if there are any active projectiles
        if active_projectiles:
            for projectile in active_projectiles:
                projectile.update(window)
                #check if the projectile collides with the enemy 
                if projectile.collides_with(enemy):
                    enemy.take_damage()
                    active_projectiles.remove(projectile)
                    break
                if projectile.off_screen(wp.window_height):
                    active_projectiles.remove(projectile)

        #print the number of active porjectiles 
        print(len(active_projectiles))

        # Drawing code
        gfx.drawBackground(window)
        player.draw(window)
        enemy.draw(window)

        # Draw projectiles
        for projectile in active_projectiles:
            projectile.update(window)
        
            
        # FPS counter
        fps = clock.get_fps()
        fps_text = fps_font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
        window.blit(fps_text, (10, 10))

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit the frame rate to 60 FPS
