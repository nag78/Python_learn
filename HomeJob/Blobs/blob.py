import pygame
from pygame.sprite import Sprite


class Blob(Sprite):
    """
    Звезда и ее начальное положение.
    """
    def __init__(self, settings, screen):
        """ Инициализация звезды и ее начальной позиции
        """
        super(Blob, self).__init__()
        self.screen = screen
        self.settings = settings

        # Загрузка изображения звезды
        self.image = pygame.image.load('.\\images\\blob.png')
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

    def update(self):
        """
        Перемещение вниз
        """
        self.y += 5
        self.rect.y = self.y

    def check_edge(self):
        """Возвращает True если капля дошла до края
        """
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.height:
            return True
