import pygame

class Rocket():
    def __init__(self,screen):
        """
        Инициализация ракеты
        """
        self.screen = screen
        self.image = pygame.image.load('.\images\\rocket_horizont.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Новая ракета появляется по центру
        # self.rect.centerx = self.screen_rect.centerx
        self.rect.left = self.screen_rect.left
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
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        """
        Рисует ракету в текущей позиции
        """
        self.screen.blit(self.image, self.rect)
