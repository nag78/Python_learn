import sys
import pygame
from blob import Blob


def check_events():
    """ Обрабатываем нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, blobs):
    """ Обновление изображения на экране и обновляет новый экран."""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(settings.bg_color)
    blobs.draw(screen)

    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def get_number_blob_x(settings, blob_width):
    """Вычисляет количество капель в ряду"""
    avaliable_space_x = settings.screen_width - 2 * blob_width
    number_blob_x = int(avaliable_space_x / (2 * blob_width))
    return number_blob_x


def create_blobs_line(settings, screen, blobs):
    """Создает ряд капель"""
    blob = Blob(settings, screen)
    blob_width = blob.rect.width
    blob_number_x = get_number_blob_x(settings, blob_width)

    # Создаем ряд капель
    for blob_number in range(blob_number_x):
        # Создание капли и размещение ее в ряду
        blob = Blob(settings, screen)
        blob.x = blob_width + 2 * blob_width * blob_number
        blob.rect.x = blob.x
        blobs.add(blob)


def update_blobs(settings, screen, blobs):
    """Обновление позиции всех капель."""

    blobs.update()

