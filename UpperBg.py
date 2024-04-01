from pygame import Vector2

from Game.GameObject import GameObject
from utils.assets_manager import assetsManager
from utils.util import utils


class UpperBg(GameObject):
    def __init__(self):
        super().__init__(Vector2(-utils.width,0),None)
        self.objects = [
            GameObject(Vector2(-utils.width, 0), assetsManager.get("upper")),
            GameObject(Vector2(0,0),assetsManager.get("upper")),
            GameObject(Vector2(utils.width, 0), assetsManager.get("upper"))
        ]
        self.speed = -6
        self.vel.x = self.speed

    def update(self):
        self.speed = -utils.speed
        self.vel.x = self.speed

        self.pos.x += self.vel.x
        if self.pos.x <= -utils.width:
            self.pos.x = 0
            firstObj = self.objects[0]
            firstObj.pos = Vector2(utils.width,0)
            self.objects.pop(0)
            self.objects.append(firstObj)

        for obj in self.objects:
            obj.vel.x = self.vel.x
            obj.update()

    def draw(self):
        for obj in self.objects:
            obj.draw()