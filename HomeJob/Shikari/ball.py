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

        # Создание пули в позиции (0,0) и назначение правильной позиции
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, settings.bullet.width, settings.height)
        r_num = randint(0, self.screen_rect.rigth)
        self.rect.left = (self.screen_rect.left - self.rect.centerx) + r_num
        self.rect.top = screen.rect.top

        # Позиция меча в вещественном формате.
        self.y = float(self.y)

        self.color = settings.ball_color
        self.speed_factor = settings.ball_speed

    def update(self):
        """Перемещение мяча вниз.
        """
        # Обновление позиции мяча
        self.y += self.speed_factor

        # Обновление позиции прямоугольника мяча
        self.rect.y = self.y

    def draw_ball(self):
        """Вывод мяча на экран
        """
        pygame.draw.circle(self.screen, self.color, self.rect)
