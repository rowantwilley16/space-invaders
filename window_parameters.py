# Set up the window
import pygame 
import sys
import pygame

window_width    = 800
window_height   = 600

centre_vertical     = window_height //2
centre_horizontal   = window_width  //2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()

# Define font
font = pygame.font.Font(None, 36)

def draw_start_screen(window):
    window.fill(BLACK)
    text = font.render("Space Invaders", True, WHITE)
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 50))
    window.blit(text, text_rect)

    # Draw "Begin Game" button
    button_text = font.render("Begin Game", True, WHITE)
    button_rect = pygame.Rect(window_width // 2 - 100, window_height // 2 + 50, 200, 50)
    pygame.draw.rect(window, WHITE, button_rect)
    window.blit(button_text, button_rect.move(50, 10))

    pygame.display.flip()

    return button_rect