import sys
import pygame


def check_events():
    """ Обрабатываем нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, blob):
    """ Обновление изображения на экране и обновляет новый экран."""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(settings.bg_color)
    blob.blitme()

    # Отображение последнего прорисованного экрана
    pygame.display.flip()
