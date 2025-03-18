import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from src.ground import Ground
from src.player import Player


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.ground = Ground()
        self.player = Player()

    def update(self):
        self.ground.update()
        self.player.update()

    def draw(self):
        self.ground.draw(self.screen)
        self.player.draw(self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((66, 197, 245))

            self.update()
            self.draw()

            pygame.display.flip()

            self.clock.tick(60)
