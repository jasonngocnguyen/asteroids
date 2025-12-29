import pygame
from constants import *
from logger import log_state
from player import Player

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



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ms = clock.tick(60)
        dt = ms / 1000
        updatable.update(dt)
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()



if __name__ == "__main__":
    main()
