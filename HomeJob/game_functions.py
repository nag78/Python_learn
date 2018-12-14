import sys
import pygame
from bullet import Bullet

def check_events(settings,screen,rocket,bullets):
    """
    Обрабатывает событий
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings,screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket)

def check_keydown_events(event,settings,screen,rocket,bullets):
    """
    Обработка нажатий клавиш
    """
    # Для текущего проекта движения право-лево заглушены
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings,screen,rocket)
        bullets.add(new_bullet)
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

def update_screen(settings,screen,rocket,bullets):
    #Перерисовка при каждом цикле
    screen.fill(settings.bg_color)
    #Пули выводятся позади изображений коробля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    #Отобрвжение последнего прорисованного экрана.
    pygame.display.flip()


