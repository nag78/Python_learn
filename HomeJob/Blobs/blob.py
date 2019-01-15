import pygame
from pygame.sprite import Sprite


class Blob(Sprite):
    def __init__(self, settings, screen):
        """Инициализирум каплю и задает начальную позицию"""
        super(Blob, self).__init__()
        self.screen = screen
        self.settings = settings

        # Загрузка изображения капли и назначения аттрибута rect
        self.image = pygame.image.load('.\\images\\blob.png')
        self.rect = self.image.get_rect()

        # Каждая новая капля появляется в левом верхнем углу.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной позиции капли
        self.x = float(self.rect.x)

    def blitme(self):
        """ Вывод на экран в текущем положении"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Падение капель."""
        self.rect.y += self.settings.drop_speed

    def check_edges(self):
        """Проверка достижения края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.bottom:
            return True
