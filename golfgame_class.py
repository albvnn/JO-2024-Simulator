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

    def recalculate_shootangle_halfbricks(self, n: int, shootangle):
        if n == 0:
            return shootangle + 90
        elif n == 1:
            return shootangle - 90
        elif n == 2:
            return shootangle + 90
        elif n == 3:
            return shootangle - 90


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
    def __init__(self, game):
        self.bricksimg = pygame.image.load(os.path.join('spirit', 'bricksTile.png'))
        self.halfbricksimg = pygame.image.load(os.path.join('spirit', 'bricksHalfTile.png'))
        self.game = game
        self.rectlist = []
        self.rectlisthalf = []

    def wall(self, pos_start: tuple, pos_end: tuple):
        rectwall = pygame.Rect(0, 0, 0, 0)
        if pos_start[1] == pos_end[1] and pos_start[0] != pos_end[0] and abs(pos_start[0] - pos_end[0]) % 20 == 0:
            rectwall.center = (pos_start[0], pos_start[1])
            rectwall.height = 20
            rectwall.width = pos_end[0] - pos_start[0]
            if rectwall not in self.rectlist:
                self.rectlist.append((rectwall, "horizontal", (pos_start, pos_end)))
            return True
        elif pos_start[1] != pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectwall.center = (pos_start[0], pos_start[1])
            rectwall.height = abs(pos_start[1] - pos_end[1])
            rectwall.width = 20
            if rectwall not in self.rectlist:
                self.rectlist.append((rectwall, "vertical", (pos_start, pos_end)))
            return True
        else:
            return False

    def halfbricks(self, pos: tuple, n: int):
        rectwall = pygame.Rect(0, 0, 0, 0)
        rectwall.center = (pos[0], pos[1])
        rectwall.height = 20
        rectwall.width = 20
        if rectwall not in self.rectlisthalf:
            self.rectlisthalf.append((rectwall, n))

    def allhalfbricks(self, pos_halfbricks: list):
        for halfbrick in pos_halfbricks:
            self.halfbricks((halfbrick[0][0], halfbrick[0][1]), halfbrick[1])
    def wall_maker(self, pos_walls: list):
        for wall in pos_walls:
            self.wall(wall[0], wall[1])

    def display_walls(self):
        for i in self.rectlist:
            if i[1] == "horizontal":
                for k in range(i[2][0][0], i[2][1][0], 20):
                    self.game.screen.blit(self.bricksimg, (k, i[2][0][1]))
            elif i[1] == "vertical":
                for k in range(i[2][0][1], i[2][1][1], 20):
                    self.game.screen.blit(pygame.transform.rotate(self.bricksimg, 90), (i[2][0][0], k))
        for k in self.rectlisthalf:
            if k[1] == 0:
                self.game.screen.blit(self.halfbricksimg, (k[0][0], k[0][1]))
            else:
                self.game.screen.blit(pygame.transform.rotate(self.halfbricksimg, 90*k[1]), (k[0][0], k[0][1]))


class Water:
    def __init__(self, game):
        self.watersimg = pygame.image.load(os.path.join('spirit', 'waterTile.png'))
        self.game = game
        self.rectlist = []

    def river(self, pos_start, pos_end):
        rectriver = pygame.Rect(0, 0, 0, 0)
        if pos_start[1] == pos_end[1] and pos_start[0] != pos_end[0] and abs(pos_start[0] - pos_end[0]) % 20 == 0:
            rectriver.center = (pos_start[0], pos_start[1])
            rectriver.height = 20
            rectriver.width = pos_end[0] - pos_start[0]
            if rectriver not in self.rectlist:
                self.rectlist.append((rectriver, "horizontal", (pos_start, pos_end)))
            return True
        elif pos_start[1] != pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectriver.center = (pos_start[0], pos_start[1])
            rectriver.height = abs(pos_start[1] - pos_end[1])
            rectriver.width = 20
            if rectriver not in self.rectlist:
                self.rectlist.append((rectriver, "vertical", (pos_start, pos_end)))
            return True
        else:
            return False

    def river_maker(self, pos_rivers: list):
        for river in pos_rivers:
            self.river(river[0], river[1])

    def display_rivers(self):
        for i in self.rectlist:
            if i[1] == "horizontal":
                for k in range(i[2][0][0], i[2][1][0], 20):
                    self.game.screen.blit(self.watersimg, (k, i[2][0][1]))
            elif i[1] == "vertical":
                for k in range(i[2][0][1], i[2][1][1], 20):
                    self.game.screen.blit(self.watersimg, (i[2][0][0], k))