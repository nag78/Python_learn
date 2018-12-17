import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf


def run_game():
    """
    Основное тело игры.
    """
    pygame.init()
    pygame.display.set_caption("Stars")
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    stars = Group()
    gf.create_stars(settings, screen, stars)


# Основной цикл игры
    while True:
        # Обработка событий клавиатуры и мышы
        gf.check_events()
        gf.update_screen(settings, screen, stars)
        stars.draw(screen)


run_game()
