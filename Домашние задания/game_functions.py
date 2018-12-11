import sys
import pygame

def check_events(rocket):
    """
    Обрабатывает нажатия клавиш и события мыши
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False


def update_screen(settings,screen,rocket):
    #Перерисовка при каждом цикле
    screen.fill(settings.bg_color)

    rocket.blitme()
    #Отобрвжение последнего прорисованного экрана.
    pygame.display.flip()
                

