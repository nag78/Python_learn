import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (143,110,255)


class Star(Sprite):
    def __init__(self,screen):
        super(Star, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    pygame.display.set_caption("Stars")
    game_set = Settings()
    screen = pygame.display.set_mode(
        (game_set.screen_width,game_set.screen_height))
    star = Star(screen)
    star_width = star.rect.width
    star_heigth = star.rect.height
    avaliable_x = game_set.screen_width - 2 * star_width
    avaliable_y = game_set.screen_height - 2 * star_heigth
    number_stars_x = int(avaliable_x / (2 * star_width))
    number_rows = int(avaliable_y / (2 * star_heigth))
    stars = Group()

    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            star = Star(screen)
            r_num = randint(-10,10)
            star.x = star_width + 2 * star_width * star_number
            star.y = star_heigth + 2 * star_heigth * row_number
            star.rect.x = star.x * r_num
            star.rect.y = star.y * r_num
            stars.add(star)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(game_set.bg_color)
        stars.draw(screen)
        pygame.display.flip()
run_game()