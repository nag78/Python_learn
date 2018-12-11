import sys
import pygame
from pygame.sprite import Group
from random import randint
from settings import Settings
from star import Star



def run_game():
    """
    Основное тело игры.
    """
    pygame.init()
    pygame.display.set_caption("Stars")
    game_set = Settings()
    screen = pygame.display.set_mode(
        (game_set.screen_width,game_set.screen_height))
    star = Star(screen)
#Расчет сетки
    star_width = star.rect.width
    star_heigth = star.rect.height
    avaliable_x = game_set.screen_width - 2 * star_width
    avaliable_y = game_set.screen_height - 2 * star_heigth
    number_stars_x = int(avaliable_x / (2 * star_width))
    number_rows = int(avaliable_y / (2 * star_heigth))
    stars = Group()
# Размещение звезд на сетке.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            star = Star(screen)
# Введение случайного элемента в размещении
            r_num = randint(-10,10)
            star.x = (star_width + 2 * star_width * star_number) * r_num
            star.y = (star_heigth + 2 * star_heigth * row_number) * r_num
            if star.x <= game_set.screen_width:
                if star.x >= 0:
                    star.rect.x = star.x
            if star.y <= game_set.screen_height:
                if star.y >= 0:
                    star.rect.y = star.y
            stars.add(star)



# Основной цикл игры
    while True:
# Обработка событий клавиатуры и мышы
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(game_set.bg_color)
        stars.draw(screen)

        pygame.display.flip()
run_game()