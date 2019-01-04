import sys
import pygame
from settings import Settings


def run_game():
    # Инициализирует pygame, settings и создает объект ээкрана
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((
                                      settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Дождь")

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # При каждом проходе перерисовывается экран
        screen.fill(settings.bg_color)
        # Отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()
