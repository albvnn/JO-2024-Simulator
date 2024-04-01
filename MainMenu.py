import pygame
from pygame import Vector2

# Importing necessary modules
from screens.Game import Game
from screens.MainGame import MainGame
from utils.Button import Button
from utils.assets_manager import assetsManager
from utils.sounds import sounds
from utils.util import utils


class MainMenu(Game):
    def __init__(self):
        # Constructor to initialize the MainMenu object
        self.buttons = []  # List to hold Button objects

        # Creating buttons for start, high scores, and quit options
        self.buttons.append(Button(0, Vector2(300, 200), "Start", Vector2(3, 2)))
        self.buttons.append(Button(1, Vector2(300, 300), "High Scores", Vector2(3, 2)))
        self.buttons.append(Button(3, Vector2(300, 400), "Quit", Vector2(3, 2)))

        # Playing background music
        sounds.playMusic()

    def update(self):
        # Method to update game logic
        for button in self.buttons:
            if button.clicked:
                if button.id == 0:  # Start button clicked
                    utils.currentScreen = MainGame()  # Switch to the MainGame screen
                    break
                if button.id == 1:  # High Scores button clicked
                    from screens.HighScores import HighScores
                    utils.currentScreen = HighScores()  # Switch to the HighScores screen
                    break
                if button.id == 3:  # Quit button clicked
                    exit(1)  # Exit the game


    def draw(self):

        for button in self.buttons:
            button.draw()

    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        pass

    def onMouseUp(self, event):
        pass


