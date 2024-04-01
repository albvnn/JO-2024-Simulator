import pygame.rect
from pygame.math import Vector2

# Importing necessary modules
from utils.util import utils

from enum import Enum


class GameObject:
    def __init__(self, pos, img):
        # Constructor to initialize the GameObject object
        self.pos = pos  # Position of the object
        self.img = img  # Image associated with the object
        self.vel = Vector2(0, 0)  # Velocity of the object
        self.acc = Vector2(0, 0)  # Acceleration of the object

        self.destroyFlag = False  # Flag to indicate if the object should be destroyed

    def update(self):
        # Method to update the object's position based on velocity and acceleration
        self.vel = Vector2(self.vel.x + self.acc.x, self.vel.y + self.acc.y)
        self.pos = Vector2(self.pos.x + self.vel.x, self.pos.y + self.vel.y)
        self.acc = Vector2(0, 0)  # Resetting acceleration after applying it

    def applyForce(self, f):
        # Method to apply a force to the object
        self.acc = Vector2(self.acc.x + f.x, self.acc.y + f.y)

    def draw(self):
        # Method to draw the object on the screen
        utils.screen.blit(self.img, (self.pos.x, self.pos.y))

    def getRect(self):
        # Method to get the bounding rectangle of the object
        rect = pygame.rect.Rect(self.pos.x, self.pos.y, self.img.get_width(), self.img.get_height())
        return rect

    def setPos(self, pos):
        # Method to set the position of the object
        self.pos = pos

    def getPos(self):
        # Method to get the position of the object
        return self.pos

    def getCenter(self):
        # Method to get the center position of the object
        return Vector2(self.pos.x + self.getRect().w / 2, self.pos.y + self.getRect().h / 2)