import sys
import pygame
from pygame import Vector2

from Game.Obstacle import Obstacle
from Game.Player import Player
from Game.Spawner import Spawner
from Game.bg.Audience import Audience
from Game.bg.BottomBg import BottomBg
from Game.bg.Road import Road
from Game.bg.UpperBg import UpperBg
from screens.Game import Game
from screens.YouWin import YouWin
from utils.sounds import sounds
from utils.util import utils


class MainGame(Game):
    def __init__(self):
        # Constructor to initialize the MainGame object
        # List to hold game objects representing the background elements
        self.objects = [
            BottomBg(),
            Road(),
            UpperBg(),
            Audience()
        ]

        # Creating the player object
        self.player = Player(Vector2(100, 250))

        # Creating the spawner object responsible for spawning obstacles
        self.spawner = Spawner(self.objects.append)

        # Variable to track time difference for difficulty progression
        self.diffTime = 0

        # Initial game score and lives
        self.score = 0
        self.lives = 2

    def update(self):
        # Method to update game logic
        self.score += 1  # Incrementing score
        self.diffTime += utils.deltaTime()  # Updating time difference for difficulty progression
        if self.diffTime >= 20:
            self.diffTime = 0
            utils.speed += 1  # Increasing game speed after certain time interval

        # Updating player and spawning obstacles
        self.player.update()
        self.spawner.spawn()

        # Checking collisions and updating game state accordingly
        for obj in self.objects:
            obj.update()
            if isinstance(obj, Obstacle):
                if utils.collide(self.player, obj) and not obj.isFall:
                    sounds.play("death")
                    self.lives -= 1
                    obj.setFall()
                    print(self.lives)
                    if self.lives < 0:
                        from screens.GameOver import GameOver
                        utils.currentScreen = GameOver(self.score)
                        return

        # Removing objects flagged for destruction
        for obj in self.objects:
            if obj.destroyFlag:
                self.objects.remove(obj)

    def draw(self):
        # Method to draw game elements
        utils.screen.fill((113, 238, 56), (0, 0, utils.width, utils.height))  # Filling screen with green color

        # Drawing background elements
        for obj in self.objects:
            obj.draw()

        # Drawing player character
        self.player.draw()

        # Displaying score
        utils.drawText(Vector2(5, 20), "Score: " + str(self.score), (244, 255, 233), utils.font24)

    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        self.player.jump()  # Triggering player jump on mouse down event

    def onMouseUp(self, event):
        pass

    def onMouseWheel(self, event):
        pass
