import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20,50)

        pos_vector = self.velocity.rotate(angle)
        neg_vector = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_roid1 = Asteroid(*self.position, new_radius)
        split_roid1.velocity = pos_vector * 1.2

        split_roid2 = Asteroid(*self.position, new_radius)
        split_roid2.velocity = neg_vector * 1.2
