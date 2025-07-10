import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        tick = clock.tick(60)
        dt = tick / 1000



if __name__ == "__main__":
    main()
