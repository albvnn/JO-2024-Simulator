import pygame
import golfgame_class
import os
import sys
import pymunk
import pymunk.pygame_util
import math
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('JO 2024 Simulator')
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_img = pygame.image.load(os.path.join('spirit', 'background.png'))
        self.hole_img = pygame.image.load(os.path.join('spirit', 'hole.png'))
        self.clock = pygame.time.Clock()
        self.ball = golfgame_class.Ball(self, (300, 200), 0)
        self.arrow = golfgame_class.Arrow(self, self.ball.rect.center)

    def run(self):
        while True:
            self.screen.blit(self.bg_img, (0, 0))
            self.screen.blit(self.ball.ballimg, self.ball.rect)
            self.screen.blit(self.hole_img, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if (pygame.mouse.get_pressed()[0] == True) and (self.ball.check_mouse_in_circledrag(pygame.mouse.get_pos())):
                self.screen.blit(self.arrow.arrowimg, self.arrow.rect)
                print(pygame.mouse.get_pos())
            pygame.display.update()
            self.clock.tick(60)

Game().run()
