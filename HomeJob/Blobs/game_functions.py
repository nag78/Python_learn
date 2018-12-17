import sys
import pygame
from blob import Blob
# from random import randint


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


def update_screen(settings, screen, blobs):
    # Перерисовка при каждом цикле
    screen.fill(settings.bg_color)
    # Пули выводятся позади изображений коробля и пришельцев
    # rocket.blitme()
    # blob.blitme()
    for blob in blobs:
        blobs.draw(screen)
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

def create_blobs(settings, screen, blobs):
    # Расчет сетки
    blob = Blob(settings, screen)
    blob_width = blob.rect.width
    blob_heigth = blob.rect.height
    avaliable_x = settings.screen_width - 2 * blob_width
    avaliable_y = settings.screen_height - 2 * blob_heigth
    number_blobs_x = int(avaliable_x / (2 * blob_width))
    number_rows = int(avaliable_y / (2 * blob_heigth))
# Размещение звезд на сетке.
    for row_number in range(number_rows):
        for blob_number in range(number_blobs_x):
            blob = Blob(settings, screen)
# Введение случайного элемента в размещении
            # r_num = randint(-10, 10)
            blob.x = (blob_width + 2 * blob_width * blob_number)
            blob.y = (blob_heigth + 2 * blob_heigth * row_number)
            blob.rect.x = blob.x
            blob.rect.y = blob.y
            blobs.add(blob)
