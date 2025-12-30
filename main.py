import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids with pygame version: pygame.version.ver")
    print("Screen width: 1280")
    print("Screen height: 720")

    #asteroid group
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    #asteroidfield group
    AsteroidField.containers = (updatable)
    AsteroidField()

    #shot group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ms = clock.tick(60)
        dt = ms / 1000
        updatable.update(dt)
        screen.fill("black")

        for sprite in asteroids:
            if sprite.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        #shots destroying asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip()



if __name__ == "__main__":
    main()
