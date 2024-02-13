import os
import pygame
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, game, pos: list, velocity: int):
        self.ballimg = pygame.image.load(os.path.join('spirit', 'golfBall.png'))
        self.rect = self.ballimg.get_rect()
        self.rect.center = pos
        self.last_pos = pos
        self.game = game
        self.victory_condition = False
        self.circledrag_area = math.pi * 100 ** 2
        self.counter_shot = 0

    def victory(self):
        self.victory_condition = True
        return self.victory_condition

    def update_pos(self,shoot_angle=0, power=1):
        x = math.cos(math.radians(shoot_angle))
        y = math.sin(math.radians(shoot_angle))
        ball_pos = self.rect.center
        self.rect.center = (ball_pos[0] - x*power, ball_pos[1] + y*power)

    def dist_mous_ball(self, pos_mouse):
        dist = [abs(self.rect.center[0] - pos_mouse[0]), abs(self.rect.center[1] - pos_mouse[1])]
        dist_c = math.sqrt(dist[0] ** 2 + dist[1] ** 2)
        if dist_c > 150:
            dist_c = 150
        return -(self.rect.center[0]-pos_mouse[0]), self.rect.center[1]-pos_mouse[1], dist_c

    def check_ball_stop(self, previous_ball_rect_center):
        if previous_ball_rect_center == self.rect.center:
            return True
        else:
            return False

    def recalculate_shootangle_wall(self, wall: list, shootangle):
        if wall[1] == "horizontal":
            return -shootangle
        elif wall[1] == "vertical":
            return 180-shootangle


class Arrow(pygame.sprite.Sprite):
    def __init__(self, game, pos: list):
        self.original_img = pygame.image.load(os.path.join('spirit', 'golfArrow.png')).convert_alpha()
        self.angle = 0
        self.rect = self.original_img.get_rect()
        self.rect.center = pos
        self.game = game

    def rotate_angle(self, new_angle, dist_mous_ball):
        self.angle = new_angle
        arrowimg1 = pygame.transform.smoothscale_by(self.original_img, (dist_mous_ball/100, 0.5))
        self.arrowimg  = pygame.transform.rotate(arrowimg1, self.angle)

    def draw(self):
        self.rect.center = self.game.ball.rect.center
        self.game.screen.blit(self.arrowimg,
                         (self.rect.centerx - self.arrowimg.get_width() / 2,
                          self.rect.centery - self.arrowimg.get_height() / 2))

class Hole(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        self.holeimg = pygame.image.load(os.path.join('spirit', 'golfHole.png'))
        self.rect = self.holeimg.get_rect()
        self.rect.center = pos
        self.game = game
        self.victory_condition = False

    def check_ball_in_hole(self, ball_pos):
        dist = [abs(self.rect.center[0] - ball_pos[0]), abs(self.rect.center[1] - ball_pos[1])]
        dist_c = math.sqrt(dist[0] ** 2 + dist[1] ** 2)
        if dist_c < 10:
            return True
        return False


class Barrier(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        self.bricksimg = pygame.image.load(os.path.join('spirit', 'bricksTile.png'))
        self.rect = self.bricksimg.get_rect()
        self.rect.center = pos
        self.game = game
        self.rectlist = []

    def wall_maker(self, pos_start: tuple, pos_end: tuple):
        rectwall = pygame.Rect(0, 0, 0, 0)
        if pos_start[1] == pos_end[1] and pos_start[0] != pos_end[0] and abs(pos_start[0] - pos_end[0]) % 20 == 0:
            rectwall.center = (pos_start[0], pos_start[1])
            rectwall.height = 20
            rectwall.width = pos_end[0] - pos_start[0]
            for i in range(pos_start[0], pos_end[0], 20):
                self.game.screen.blit(self.bricksimg, (i, pos_start[1]))
            if rectwall not in self.rectlist:
                self.rectlist.append((rectwall, "horizontal"))
            return True
        elif pos_start[1] != pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectwall.center = (pos_start[0], pos_start[1])
            rectwall.height = abs(pos_start[1] - pos_end[1])
            rectwall.width = 20
            for i in range(pos_start[1], pos_end[1], 20):
                self.game.screen.blit(pygame.transform.rotate(self.bricksimg, 90), (pos_start[0], i))
            if rectwall not in self.rectlist:
                self.rectlist.append((rectwall, "vertical"))
            return True
        else:
            return False

class Water:
    def __init__(self, game, pos):
        self.watersimg = pygame.image.load(os.path.join('spirit', 'waterTile.png'))
        self.rect = self.watersimg.get_rect()
        self.rect.center = pos
        self.game = game
        self.rectlist = []

    def river_maker(self, pos_start, pos_end):
        rectriver = pygame.Rect(0, 0, 0, 0)
        if pos_start[1] == pos_end[1] and pos_start[0] != pos_end[0] and abs(pos_start[0] - pos_end[0]) % 20 == 0:
            rectriver.center = (pos_start[0], pos_start[1])
            rectriver.height = 20
            rectriver.width = pos_end[0] - pos_start[0]
            for i in range(pos_start[0], pos_end[0], 20):
                self.game.screen.blit(self.watersimg, (i, pos_start[1]))
            if rectriver not in self.rectlist:
                self.rectlist.append((rectriver, "horizontal"))
            return True
        elif pos_start[1] != pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectriver.center = (pos_start[0], pos_start[1])
            rectriver.height = abs(pos_start[1] - pos_end[1])
            rectriver.width = 20
            for i in range(pos_start[1], pos_end[1], 20):
                self.game.screen.blit(pygame.transform.rotate(self.watersimg, 90), (pos_start[0], i))
            if rectriver not in self.rectlist:
                self.rectlist.append((rectriver, "vertical"))
            return True
        else:
            return False