from pygame import Vector2

from Game.GameObject import GameObject
from utils.assets_manager import assetsManager


class Road(GameObject):
    def __init__(self):
        super().__init__(Vector2(0,0), assetsManager.get("road"))