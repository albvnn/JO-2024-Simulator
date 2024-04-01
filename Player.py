import pygame
from pygame.math import Vector2

from Game.GameObject import GameObject
from utils.SpriteSheet import SpriteSheet
from utils.assets_manager import assetsManager
from utils.sounds import sounds
from utils.util import utils


class Player(GameObject):
    def __init__(self, pos):
        super().__init__(pos, None)

        self.sheets = {
            'run': SpriteSheet(assetsManager.get("run"), 1, 12),
            'jump': SpriteSheet(assetsManager.get("run"), 1, 12),
        }

        self.sheets['run'].setPlay(0, 11, 0.05, True)
        self.sheets['jump'].setPlay(0, 11, 0.05, True)

        self.currentSheet = 'run'
        self.img = self.sheets[self.currentSheet].getCurrentFrame()
        self.prevPos = None
        self.speed = 5
        self.jumping = False

    def update(self):
        # self.applyForce(pygame.Vector2(0, 0.52))
        # self.applyForce(pygame.Vector2(0, 0.52))
        if self.vel.y > 0:
            if self.pos.y > 250:
                self.jumping = False
                self.vel = Vector2(0,0)
                self.pos.y = 250

        if self.jumping:
            self.currentSheet = 'jump'
            self.applyForce(pygame.Vector2(0, 0.98))
            # if self.pos.y > 250:
            #     self.jumping = False
            #     self.vel = Vector2(0,0)
            #     self.pos.y = 250
        else:
            self.currentSheet = 'run'

        self.prevPos = Vector2(self.pos.x, self.pos.y)
        super().update()

        self.sheets[self.currentSheet].play()
        self.img = self.sheets[self.currentSheet].getCurrentFrame()

    def draw(self):
        super().draw()
        # pygame.draw.rect(utils.screen, (233, 23, 23), self.getRect(), 3)

    def jump(self):
        if self.jumping:
            return
        sounds.play("jump")
        self.applyForce(pygame.Vector2(0, -22))
        self.jumping = True

    def getRect(self):
        rect = pygame.rect.Rect(self.pos.x + 60, self.pos.y + 10, self.img.get_width() - 100, self.img.get_height() - 10)
        return rect

