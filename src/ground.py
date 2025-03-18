import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_SPEED


class Ground:
    def __init__(self):
        self.image = pygame.image.load("assets/ground.png")
        self.ground_parts = []
        self.ground_parts.append(self.image.get_rect(bottomleft=(0, SCREEN_HEIGHT)))
        self.ground_parts.append(
            self.image.get_rect(bottomleft=(SCREEN_WIDTH, SCREEN_HEIGHT))
        )

    def update(self):
        for rect in self.ground_parts:
            rect.x -= GROUND_SPEED
            if rect.right <= 0:
                rect.left = SCREEN_WIDTH

    def draw(self, screen):
        for rect in self.ground_parts:
            screen.blit(self.image, rect)
