import os
import pygame
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, game, pos: list, velocity: int):
        self.ballimg = pygame.image.load(os.path.join('assets', 'golfBall.png'))
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
    

    def update_pos(self,shoot_angle=0, power=0):
        x = math.cos(math.radians(shoot_angle)) * power
        y = math.sin(math.radians(shoot_angle)) * power
        ball_pos = self.rect.center
        self.rect.center = (ball_pos[0] - x, ball_pos[1] + y)


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
            if pygame.Rect.collidepoint(wall[0], (self.rect.center[0] + 15, self.rect.center[1])) or pygame.Rect.collidepoint(wall[0], (self.rect.center[0] - 15, self.rect.center[1])):
                return 180-shootangle % 360
            else:
                return -shootangle % 360
        elif wall[1] == "vertical":
            if pygame.Rect.collidepoint(wall[0], (self.rect.center[0], self.rect.center[1] + 15)) or pygame.Rect.collidepoint(wall[0], (self.rect.center[0], self.rect.center[1] - 15)):
                return -shootangle % 360
            else:
                return 180-shootangle % 360
        elif wall[1] == "block":
            if pygame.Rect.collidepoint(wall[0], (self.rect.center[0], self.rect.center[1] + 15)) or pygame.Rect.collidepoint(wall[0], (self.rect.center[0], self.rect.center[1] - 15)):
                return -shootangle % 360
            elif pygame.Rect.collidepoint(wall[0], (self.rect.center[0] + 15, self.rect.center[1])) or pygame.Rect.collidepoint(wall[0], (self.rect.center[0] - 15, self.rect.center[1])):
                return 180-shootangle % 360
            else:
                return shootangle

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
        self.original_img = pygame.image.load(os.path.join('assets', 'golfArrow.png')).convert_alpha()
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
        self.holeimg = pygame.image.load(os.path.join('assets', 'golfHole.png'))
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
    
