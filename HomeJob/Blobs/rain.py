import pygame
from settings import Settings
from blob import Blob
import game_function as gf


def run_game():
    # Инициализирует pygame, settings и создает объект ээкрана
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((
                                      settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Дождь")
    # Создание капли
    blob = Blob(settings, screen)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events()
        gf.update_screen(settings, screen, blob)


run_game()
