import pygame

class Rocket():
    def __init__(self,screen):
        """
        Инициализация ракеты
        """
        self.screen = screen
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Новая ракета появляется по центру
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Флаг перемещения 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """
        Обновляет позицию ракеты в зависимости от флага
        """
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
        elif self.moving_up:
            self.rect.centery -= 1
        elif self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """
        Рисует ракету в текущей позиции
        """
        self.screen.blit(self.image, self.rect)
