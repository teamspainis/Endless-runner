import pygame
from src.settings import SCREEN_HEIGHT


class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rotated_img = None
        self.rect = self.image.get_rect(bottomleft=(123, SCREEN_HEIGHT - 128))
        self.rotated_rect = None
        self.angle = 0

    def update(self):
        self.angle -= 3
        self.rotated_img = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated_img.get_rect(
            center=self.rect.center
        )  # Keep rotation centered

    def draw(self, screen):
        screen.blit(self.rotated_img, self.rotated_rect.topleft)
