import pygame
from pygame import Vector2

# Importing necessary modules
from screens.Game import Game
from utils.Button import Button
from utils.assets_manager import assetsManager
from utils.util import utils


class YouWin(Game):
    def __init__(self):
        # Constructor to initialize the YouWin object
        self.buttons = []  # List to hold Button objects

        # Creating buttons for "You Win!" message and quit option
        self.buttons.append(Button(0, Vector2(300, 350), "You Win!", Vector2(3, 2)))
        self.buttons.append(Button(3, Vector2(300, 500), "Quit", Vector2(3, 2)))

    def update(self):
        for button in self.buttons:
            if button.clicked:
                if button.id == 0:  # "You Win!" button clicked
                    from screens.MainMenu import MainMenu
                    utils.currentScreen = MainMenu()  # Switch to the MainMenu screen
                    break
                if button.id == 3:  # Quit button clicked
                    exit(1)  # Exit the game

    def draw(self):
        # Method to draw game elements
        for button in self.buttons:
            button.draw()  # Draw each button


    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        pass

    def onMouseUp(self, event):
        pass


