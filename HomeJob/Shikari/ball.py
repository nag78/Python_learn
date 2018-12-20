import pygame
from pygame.sprite import Sprite
from random import randint


class Ball(Sprite):
    """Класс создающий и управляющий мячем.
    """
    def __init__(self, settings, screen):
        """Создаем объект мяча
        """
        super().__init__()
        self.screen = screen
        self.setings = settings

        # Загрузка изображения мяча и задание начальной позиции
        self.image = pygame.image.load('.\\images\\ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        r_num = randint(10, 1000)
        self.rect.x = self.rect.width + r_num
        self.rect.y = self.rect.height

        # Позиция меча в вещественном формате.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_factor = settings.ball_speed

    def update(self):
        """Перемещение мяча вниз.
        """
        # Обновление позиции мяча
        self.y += self.speed_factor

        # Обновление позиции прямоугольника мяча
        self.rect.y = self.y

    def blitme(self):
        """Вывод пришельца на экран
        """
        self.screen.blit(self.image, self.rect)

    def draw_ball(self):
        """Вывод мяча на экран
        """
        pygame.draw.circle(self.screen, self.color, self.rect)
