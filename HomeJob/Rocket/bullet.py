import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Класс для управления пулями
    """
    def __init__(self, settings, screen, rocket):
        """
        Создает объект пули в текущей позиции ракеты
        """
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение правиьной позиции
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.left = rocket.rect.right
        self.rect.centery = rocket.rect.centery

        # Позиция пули в вещественном формате
        self.x = float(self.rect.x)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """
        Перемещение пули по экрану
        """
        # обновление позиции пули в вещественном виде
        self.x += self.speed_factor

        # Обновление позиции прямоугольника
        self.rect.x = self.x

    def draw_bullet(self):
        # Вывод пули на экран
        pygame.draw.rect(self.screen, self.color, self.rect)
