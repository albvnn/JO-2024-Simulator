import pygame
from pygame import Vector2

# Importing necessary modules
from screens.Game import Game
from utils.Button import Button
from utils.assets_manager import assetsManager
from utils.util import utils


class GameOver(Game):
    def __init__(self, score):
        # Constructor to initialize the GameOver object
        self.buttons = []  # List to hold Button objects
        self.score = score  # Score of the game

        # Creating buttons and adding them to the list
        self.buttons.append(Button(0, Vector2(550, 500), "GAME OVER", Vector2(3, 2)))
        self.buttons.append(Button(3, Vector2(300, 500), "Quit", Vector2(3, 2)))

        # Saving score
        utils.saveScore(score)

    def update(self):
        # Method to update game logic
        for button in self.buttons:
            if button.clicked:
                if button.id == 0:
                    from screens.MainMenu import MainMenu
                    utils.currentScreen = MainMenu()  # Switch to the main menu screen
                    break
                if button.id == 3:
                    exit(1)  # Exit the game

    def draw(self):
        # Method to draw game elements
        utils.drawText(Vector2(300, 200), "Your score: " + str(self.score), (255, 255, 255), utils.font24)
        for button in self.buttons:
            button.draw()  # Draw each button

    def onKeyDown(self, key):
        pass  # Method called when a key is pressed

    def onKeyUp(self, key):
        pass  # Method called when a key is released

    def onMouseDown(self, event):
        pass  # Method called when a mouse button is pressed

    def onMouseUp(self, event):
        pass  # Method called when a mouse button is released