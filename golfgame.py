import pygame
import golfgame_class
import os


def rungolfgame():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('JO GAME')
    while True:
        pygame.display.update()
        bg = pygame.image.load(os.path.join('spirit', 'background.png'))
        screen.blit(bg, (0, 0))
        clock.tick(60)
    pygame.quit()

rungolfgame()
