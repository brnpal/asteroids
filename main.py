# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")      

    #draw game to screen
    while True:
        # make window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # make black screen and refresh
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()

#