import sys
import pygame

def check_events(rocket):
    """
    Обработка нажатия клавиш и события мыши
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_RIGHT:
                rocket.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_RIGHT:
                rocket.moving_right = False

def update_screen(ai_settings,screen, rocket):
    #Перерисовка экрана
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    #Отображение последнего прорисованного экрана
    pygame.display.flip()
