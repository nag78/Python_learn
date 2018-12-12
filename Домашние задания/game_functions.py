import sys
import pygame

def check_events(rocket):
    """
    Обрабатывает событий
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket)

def check_keydown_events(event,rocket):
    """
    Обработка нажатий клавиш
    """
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,rocket):
    """
    Обработка отпуска клавиш
    """
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def update_screen(settings,screen,rocket):
    #Перерисовка при каждом цикле
    screen.fill(settings.bg_color)

    rocket.blitme()
    #Отобрвжение последнего прорисованного экрана.
    pygame.display.flip()
                

