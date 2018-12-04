import pygame
import sys

class Rocket():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """
        Обновляет позицию корабля с учетом флага.
        """
        #Обновляется аттрибут center, а не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

def check_keydown_events(event,ship):
    """
    Реагирует на нажатие клавиш.
    """
    if event.key == pygame.K_RIGHT:
        #Переместить корабль вправо.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Переместить корабль влево.
        ship.moving_left = True

def check_keyup_event(event,ship):
    """
    Реагирует на отпускание клавиш.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """
    Обрабатывает нажатия клавиш и события мыши.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)

        #Клавиша отпущена перемещение остановлено
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)




def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Sky")
    bg_color = (143,110,255)
    rocket = Rocket(screen)
    check_events(rocket)
    rocket.update()
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Отображение последнего прорисованного экрана.
    pygame.display.flip()
run_game()
