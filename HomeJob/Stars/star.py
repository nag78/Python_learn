import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """
    Звезда и ее начальное положение.
    """
    def __init__(self, settings, screen):
        """ Инициализация звезды и ее начальной позиции
        """
        super(Star, self).__init__()
        self.screen = screen
        self.settings = settings

        # Загрузка изображения звезды
        self.image = pygame.image.load('.\\images\\star.png')
        self.rect = self.image.get_rect()
        # Звезда в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной позиции звезды
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # Вывод звезды в текущем положении
        self.screen.blit(self.image, self.rect)
