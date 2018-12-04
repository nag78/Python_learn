import pygame
import sys

class Crocodile():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('crocodile.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image,self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Sky")
    bg_color = (0,180,255)
    croc = Crocodile(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        croc.blitme()
        pygame.display.flip()

run_game()
