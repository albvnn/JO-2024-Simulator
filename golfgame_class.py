import os
import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, game, pos: list, velocity: int):
        self.ballimg = pygame.image.load(os.path.join('spirit', 'ball.png'))
        self.pos = pos
        self.rect = self.ballimg.get_rect()
        self.rect.center = pos
        self.game = game
        self.velocity = 0
        self.victory_condition = False

    def get_pos(self):
        return self.pos

    def get_victory_condition(self):
        return self.victory_condition

    def victory(self):
        self.victory_condition = True
        return self.victory_condition

    def update_pos(self, change: list = [0,0]):
        self.pos[0] += change[0]
        self.pos[1] += change[1]

class Arrow:
    def __init__(self, game, pos: list):
        self.arrowimg = pygame.image.load(os.path.join('spirit', 'arrow_direction.png'))
        self.pos = pos
        self.rect = self.arrowimg.get_rect()
        self.rect.center = pos
        self.game = game
class Hole:
    def __init__(self):
        pass

class Barrier:
    def __init__(self):
        pass
