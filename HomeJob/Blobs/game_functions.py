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
    blob.y = 0
    blob_width = blob.rect.width
    avaliable_x = settings.screen_width - 2 * blob_width
    number_blobs_x = int(avaliable_x / (2 * blob_width))
    # Размещение звезд на сетке.
    for blob_number in range(number_blobs_x):
        blob = Blob(settings, screen)
# Введение случайного элемента в размещении
        # r_num = randint(-10, 10)
        blob.x = (blob_width + 2 * blob_width * blob_number)
        blob.rect.x = blob.x
        blobs.add(blob)


def update_blobs(settings, screen, blobs):
    """Обновление позиции всех капель.
    """
    check_bloob_edges(settings, screen, blobs)
    blobs.update()


def check_bloob_edges(settings, screen, blobs):
    """Реакция на достижение каплями края
    """
    for blob in blobs.sprites():
        if blob.check_edge():
            blobs.remove(blob)
            create_blobs(settings, screen, blobs)
            break
