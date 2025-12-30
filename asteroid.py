import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH,
        )

    def update(self, dt):
        asteroid_movement = self.velocity * dt
        self.position += asteroid_movement

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            split_one_velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)
            split_two_velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)

            self.split_one_radius = self.radius - ASTEROID_MIN_RADIUS
            self.split_two_radius = self.radius - ASTEROID_MIN_RADIUS

            self.split_one_asteroid = Asteroid(self.position.x, self.position.y, self.split_one_radius)
            self.split_two_asteroid = Asteroid(self.position.x, self.position.y, self.split_two_radius)

            self.split_one_asteroid.velocity = split_one_velocity * 1.2
            self.split_two_asteroid.velocity = split_two_velocity * 1.2
