import sys
import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf
pygame.init()

def run_game():
    # Инициализация игры и создание объект экрана
    
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width,gs.screen_height))
    pygame.display.set_caption("Rocket")

    #Создание ракеты
    rocket = Rocket(screen)

    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мышы
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(gs, screen, rocket)
run_game()