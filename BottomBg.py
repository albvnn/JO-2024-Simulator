from pygame import Vector2

from Game.GameObject import GameObject
from utils.assets_manager import assetsManager
from utils.util import utils


class BottomBg(GameObject):
    def __init__(self):
        super().__init__(Vector2(-utils.width,0),None)
        self.objects = [
            GameObject(Vector2(-utils.width, 0), assetsManager.get("bottom")),
            GameObject(Vector2(0,0),assetsManager.get("bottom")),
            GameObject(Vector2(utils.width, 0), assetsManager.get("bottom"))
        ]
        self.speed = -6
        self.vel.x = self.speed

    def update(self):
        self.speed = -utils.speed
        self.vel.x = self.speed
        for obj in self.objects:
            obj.vel.x = self.vel.x
            obj.update()

        self.pos.x += self.vel.x
        if self.pos.x <= -utils.width:
            self.pos.x = 0
            firstObj = self.objects[0]
            firstObj.pos = Vector2(utils.width , 0)
            self.objects.pop(0)
            self.objects.append(firstObj)

    def draw(self):
        for obj in self.objects:
            obj.draw()