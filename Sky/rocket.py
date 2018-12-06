import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Инициализация pygame, settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Rocket")

    #Создаем ракету
    rocket = Ship(ai_settings,screen)

    while True:
        #Отслеживание событий мыши и клавиатуры
        gf.check_events(rocket)
        rocket.update()
        #Ототбражение последнего прорисованного экрана.
        gf.update_screen(ai_settings,screen,rocket)
run_game()
