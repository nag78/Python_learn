import sys
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """
    Звезда и ее начальное положение.
    """
    def __init__(self,screen):
        super(Star, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
