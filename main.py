import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ## draw game to screen ##
    while True:

        # make window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        # update player pos
        player.update(dt)

        # draw and refresh    
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
