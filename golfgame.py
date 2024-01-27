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
        self.bg_img = pygame.image.load(os.path.join('spirit', 'golfBackground.png'))
        self.hole_img = pygame.image.load(os.path.join('spirit', 'golfHole.png'))
        self.clock = pygame.time.Clock()
        self.ball = golfgame_class.Ball(self, (300, 200), 0)
        self.arrow = golfgame_class.Arrow(self, self.ball.rect.center)

    def run(self):
        running = True
        taking_shoot = False
        shoot_in_gestion = False
        shoot_angle = 0
        distance = 0
        power = 1
        while running:
            self.screen.blit(self.bg_img, (0, 0))
            self.screen.blit(self.ball.ballimg, self.ball.rect)
            self.screen.blit(self.hole_img, (0, 0))

            if taking_shoot:
                shoot_angle = math.degrees(math.atan2(self.ball.dist_mous_ball(pygame.mouse.get_pos())[1], self.ball.dist_mous_ball(pygame.mouse.get_pos())[0]))
                self.arrow.rotate_angle(shoot_angle, self.ball.dist_mous_ball(pygame.mouse.get_pos())[2])
                self.arrow.draw()
                power = self.ball.dist_mous_ball(pygame.mouse.get_pos())[2]/40
                distance = 100


            if shoot_in_gestion and distance != 0:
                taking_shoot = False
                self.ball.update_pos(shoot_angle, power)
                distance -= 1
                power /= 1.005

            if distance == 0:
                distance = 100
                shoot_in_gestion = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    taking_shoot = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    taking_shoot = False
                    shoot_in_gestion = True

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

Game().run()
