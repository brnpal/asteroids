import pygame
from constants import *
from player import *
from asteroid import *
from asteroid_field import *
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #assign groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # init asteroids
    asteroid_field = AsteroidField()

    # player size
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ## -- GAME LOOP -- ##
    ## 1. check for inputs
    ## 2. update the game world
    ## 3. draw game to screen

    while True:

        # make window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        # update positions
        for obj in updatable:
            obj.update(dt)

        # draw updated positions   
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        #detect player collision
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                sys.exit("Game over!")

        #detect shot collision
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        # refresh @ 60 FPS
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
