import sys
import pygame
from star import Star
from random import randint


def check_events():
    """
    Обрабатывает событий
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def check_keydown_events(event, settings, screen, rocket):
    """
    Обработка нажатий клавиш
    """
    # Для текущего проекта движения право-лево заглушены
    # if event.key == pygame.K_RIGHT:
    #     rocket.moving_right = False
    # elif event.key == pygame.K_LEFT:
    #     rocket.moving_left = False
    # elif event.key == pygame.K_UP:
    #     rocket.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     rocket.moving_down = True
    # elif event.key == pygame.K_SPACE:
    #     new_bullet = Bullet(settings, screen, rocket)
    #     bullets.add(new_bullet)
    if event.key == pygame.K_q:
        sys.exit()


# def check_keyup_events(event, rocket):
#     """
#     Обработка отпуска клавиш
#     """
#     if event.key == pygame.K_RIGHT:
#         rocket.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         rocket.moving_left = False
#     elif event.key == pygame.K_UP:
#         rocket.moving_up = False
#     elif event.key == pygame.K_DOWN:
#         rocket.moving_down = False


def update_screen(settings, screen, stars):
    # Перерисовка при каждом цикле
    screen.fill(settings.bg_color)
    # Пули выводятся позади изображений коробля и пришельцев
    # rocket.blitme()
    # star.blitme()
    for star in stars:
        stars.draw(screen)
    # Отобрвжение последнего прорисованного экрана.
    pygame.display.flip()


# def update_bullets(screen, bullets):
#     """Обновление позиции пуль и уничтожение старых пуль.
#     """
#     bullets.update()
#     scr_rect = screen.get_rect()
#     # Удаление пуль, вышедших за край экрана.
#     for bullet in bullets.copy():
#         if bullet.rect.right >= scr_rect.right:
#             bullets.remove(bullet)
#             # print(len(bullets))

def create_stars(settings, screen, stars):
    # Расчет сетки
    star = Star(settings, screen)
    star_width = star.rect.width
    star_heigth = star.rect.height
    avaliable_x = settings.screen_width - 2 * star_width
    avaliable_y = settings.screen_height - 2 * star_heigth
    number_stars_x = int(avaliable_x / (2 * star_width))
    number_rows = int(avaliable_y / (2 * star_heigth))
# Размещение звезд на сетке.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            star = Star(settings, screen)
# Введение случайного элемента в размещении
            r_num = randint(-10, 10)
            star.x = (star_width + 2 * star_width * star_number)
            star.y = (star_heigth + 2 * star_heigth * row_number)
            star.rect.x = star.x * r_num
            star.rect.y = star.y * r_num
            stars.add(star)
