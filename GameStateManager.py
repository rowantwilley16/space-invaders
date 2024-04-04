import pygame
import window_parameters as wp
import sys

class GameStateManager:

    def __init__(self):
        self.states         = {"MENU": MenuState(self), "PLAY": PlayState(self)}
        self.current_state  = "MENU"  

    def switch_state(self, new_state):
        self.current_state = new_state

    def handle_events(self, event):
        self.states[self.current_state].handle_events(event)

    def update(self):
        self.states[self.current_state].update()

    def draw(self, window):
        self.states[self.current_state].draw(window)


class GameState:
    def __init__(self, manager):
        self.manager = manager

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass


class MenuState(GameState):

    def handle_events(self, event, window):

        button_rect = wp.draw_start_screen(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    GameStateManager.switch_state(1)  #switch to gamestate 1
                    print("Begin Game")

    def draw(self):
        # Draw menu screen with button
        pass


class PlayState(GameState):
    def update(self):
        # Update game logic for play state (e.g., player movement, enemy behavior)
        pass

    def draw(self):
        # Draw game elements (e.g., player, enemies, projectiles)
        pass
