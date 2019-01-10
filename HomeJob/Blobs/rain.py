import pygame
from settings import Settings
# from blob import Blob
import game_function as gf
from pygame.sprite import Group


def run_game():
    # Инициализирует pygame, settings и создает объект ээкрана
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((
                                      settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Дождь")
    # Создание группы капель
    blobs = Group()
    # Создание ряда капель
    gf.create_blobs_line(settings, screen, blobs)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events()
        gf.update_screen(settings, screen, blobs)


run_game()
