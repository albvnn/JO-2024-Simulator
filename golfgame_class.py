import os
import pygame
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, game, pos: list, velocity: int):
        self.ballimg = pygame.image.load(os.path.join('spirit', 'ball.png'))
        self.rect = self.ballimg.get_rect()
        self.rect.center = pos
        self.game = game
        self.velocity = 0
        self.victory_condition = False
        self.circledrag_area = math.pi * 100 ** 2

    def get_pos(self):
        return self.rect.center

    def get_victory_condition(self):
        return self.victory_condition

    def victory(self):
        self.victory_condition = True
        return self.victory_condition

    def update_pos(self, change: list = [0,0]):
        self.rect.center[0] += change[0]
        self.rect.center[1] += change[1]

    def check_mouse_in_circledrag(self, pos_mouse):
        dist = [abs(self.rect.center[0]-pos_mouse[0]),abs(self.rect.center[1]-pos_mouse[1])]
        dist_c = math.sqrt(dist[0]**2+dist[1]**2)
        if dist_c <= 100:
            return True
        return False

class Arrow(pygame.sprite.Sprite):
    def __init__(self, game, pos: list):
        self.angle = 0
        self.arrowimg = pygame.transform.rotate(pygame.image.load(os.path.join('spirit', 'arrow_direction.png')), self.angle)
        self.rect = self.arrowimg.get_rect()
        self.rect.midbottom = pos
        self.game = game
        self.circledrag_area = math.pi * 100 ** 2

    def rotate(self, degree):
        self.angle += degree

class Hole:
    def __init__(self):
        pass

class Barrier:
    def __init__(self):
        pass

class Water:
    def __init__(self):
        pass