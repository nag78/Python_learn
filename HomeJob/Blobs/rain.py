import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf


def run_game():
    """
    Основное тело игры.
    """
    pygame.init()
    pygame.display.set_caption("Rain")
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    blobs = Group()
    gf.create_stars(settings, screen, blobs)


# Основной цикл игры
    while True:
        # Обработка событий клавиатуры и мышы
        gf.check_events()
        gf.update_screen(settings, screen, blobs)
        blobs.draw(screen)


run_game()
