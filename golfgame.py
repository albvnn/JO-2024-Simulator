import pygame
import golfgame_class
import os
import sys
#import pymunk
#import pymunk.pygame_util
import math
class GolfGame:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('JO 2024 Simulator')
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_img = pygame.image.load(os.path.join('spirit', 'golfBackground.png'))
        self.clock = pygame.time.Clock()
        self.ball = golfgame_class.Ball(self, (300, 200), 0)
        self.arrow = golfgame_class.Arrow(self, self.ball.rect.center)
        self.hole = golfgame_class.Hole(self, (500, 50))
        self.barrier = golfgame_class.Barrier(self)
        self.river = golfgame_class.Water(self)
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join('music', 'REQUIEM.mp3'))

    def display_text(self, text, pos):
        img = pygame.font.SysFont("Lato", 30).render(text, True, "WHITE")
        self.screen.blit(img, (pos[0], pos[1]))

    def run(self):
        running = True
        taking_shoot = False
        shoot_in_gestion = False
        termined_shoot = False
        end_game = False
        shoot_angle = 0
        distance = 0
        power = 1
        #pygame.mixer.music.play()
        while running:
            self.screen.blit(self.bg_img, (0, 0))
            if not self.hole.check_ball_in_hole(self.ball.rect.center):
                self.screen.blit(self.ball.ballimg, self.ball.rect)
            self.screen.blit(self.hole.holeimg, self.hole.rect)
            #self.barrier.wall_maker((40, 60), (180, 60))
            #self.river.river_maker((560, 40), (780, 40))


            if taking_shoot:
                shoot_angle = -math.degrees(math.atan2(self.ball.dist_mous_ball(pygame.mouse.get_pos())[1], self.ball.dist_mous_ball(pygame.mouse.get_pos())[0]))
                self.arrow.rotate_angle(-shoot_angle, self.ball.dist_mous_ball(pygame.mouse.get_pos())[2])
                self.arrow.draw()
                power = self.ball.dist_mous_ball(pygame.mouse.get_pos())[2]/40
                distance = 100

            for i in self.barrier.rectlist:
                if pygame.Rect.colliderect(i[0], self.ball.rect):
                    shoot_angle = self.ball.recalculate_shootangle_wall(i, shoot_angle)

            for k in self.river.rectlist:
                if pygame.Rect.colliderect(k[0], self.ball.rect):
                    self.ball.rect.center = self.ball.last_pos
                    distance = 0

            if shoot_in_gestion and distance != 0:
                taking_shoot = False
                termined_shoot = False
                self.ball.update_pos(-shoot_angle, power)
                distance -= 1
                power /= 1.005

            if distance == 0:
                distance = 100
                self.ball.last_pos = self.ball.rect.center
                shoot_in_gestion = False
                termined_shoot = True
                self.ball.counter_shot += 1

            if self.hole.check_ball_in_hole(self.ball.rect.center):
                distance = -1
                self.display_text("VICTORY IN " + str(self.ball.counter_shot), (100, 100))
                end_game = True
                taking_shoot = False
                shoot_in_gestion = False

            if self.ball.counter_shot >= 10:
                self.display_text("GAME OVER", (100, 100))
                end_game = True


            if not end_game and termined_shoot:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        taking_shoot = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        taking_shoot = False
                        shoot_in_gestion = True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

GolfGame().run()
pygame.quit()
sys.exit()
