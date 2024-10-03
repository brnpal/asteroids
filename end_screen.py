import pygame
import sys
from main import screen
from main import asteroids

### WIP, NOT IN USE ###

def run_end_screen():

    global asteroids
    for asteroid in asteroids:
        asteroid.kill()

    font = pygame.font.Font(None, 36)

    def display_text(text, pos):
        text_surface = font.render(text, True, (255, 255, 255))  # White text
        screen.blit(text_surface, pos)

    display_text("Game Over! Press 'R' to Restart", (200, 250))