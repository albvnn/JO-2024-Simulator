import pygame

# Importing necessary modules
from Game.GameObject import GameObject
from utils.assets_manager import assetsManager
from utils.util import utils


class Obstacle(GameObject):
    def __init__(self, pos, speed):
        # Constructor to initialize the Obstacle object
        super().__init__(pos, assetsManager.get("obstacle"))  # Calling the constructor of the parent class
        self.vel.x = speed  # Setting horizontal velocity of the obstacle
        self.isFall = False  # Flag to indicate if the obstacle is falling

    def getRect(self):
        # Method to get the bounding rectangle of the obstacle
        rect = pygame.rect.Rect(self.pos.x + 70, self.pos.y + 20, self.img.get_width() - 80, self.img.get_height() - 10)
        return rect

    def setFall(self):
        # Method to set the obstacle to falling state
        self.isFall = True  # Setting isFall flag to True
        self.img = assetsManager.get("obstacle_fall")  # Changing obstacle image to falling state image

    def draw(self):
        # Method to draw the obstacle on the screen
        super().draw()  # Calling the draw method of the parent class
