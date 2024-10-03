import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        split_velocity1 = self.velocity.rotate(random_angle) 
        split_velocity2 = self.velocity.rotate(-random_angle) 
        self.old_radius = self.radius
        self.radius = self.old_radius - ASTEROID_MIN_RADIUS
        asteroid_break1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_break2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_break1.velocity = split_velocity1 * 1.2
        asteroid_break2.velocity = split_velocity2 * 1.2