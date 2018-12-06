import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """
        Инициализация ракеты и начальной позиции.
        """
        self.screen = screen
        self.ai_settings = ai_settings

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False

        #Загрузка изображения ракеты
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Новый корабль появляется по центру экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.center_x = float(self.rect.centerx)


    def update(self):
        """
        Обновление позиций ракеты
        """
        if self.moving_left:
##            self.center_x -= self.ai_settings.rocket_speed_factor
            self.center_x -= 1.5
        elif self.moving_right:
            self.center_x += self.ai_settings.rocket_speed_factor

            self.rect.centerx = self.center_x

    def blitme(self):
        """
        Рисуем ракету в исходной позиции
        """
        self.screen.blit(self.image,self.rect)

