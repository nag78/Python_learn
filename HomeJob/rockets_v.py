import sys
import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf
from pygame.sprite import Group
pygame.init()


def run_game():
    # Инициализация игры и создание объект экрана
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_height))
    pygame.display.set_caption("Rocket")

    # Создание ракеты
    rocket = Rocket(screen)

    # Создание группы хранения пуль
    bullets = Group()

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мышы
        gf.check_events(gs, screen, rocket, bullets)
        rocket.update()
        gf.update_bullets(screen, bullets)
        gf.update_screen(gs, screen, rocket, bullets)


run_game()
