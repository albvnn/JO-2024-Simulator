from __future__ import annotations  # Importing annotations from the future to allow forward references

import sys
import pygame
from pygame import Vector2

# Importing necessary modules
from utils.util import utils
from utils.Button import Button
from utils.sounds import sounds
from screens.Game import Game
from screens.GameOver import GameOver
from utils.assets_manager import assetsManager

class HighScores(Game):
    def __init__(self):
        # Constructor to initialize the HighScores object
        self.gameObjects = []  # List to hold game objects (not used in this implementation)

        # List to hold Button objects
        self.buttons = []
        # Adding a button to return to the main menu
        self.buttons.append(Button(0, Vector2(650, utils.height - 50), "Menu", Vector2(1.8, 1.2), utils.font16))

        # Loading high scores from file and keeping only the top 10 scores
        self.scores = utils.loadScores()
        self.scores = self.scores[0:10]

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
        for button in self.buttons:
            button.draw()  # Draw each button

        # Drawing the title "Top 10 high scores"
        utils.drawText(Vector2(140, 40), "Top 10 high scores: ", (233, 233, 233), utils.font32)

        # Drawing high scores
        y = 100  # Initial y position
        x = 250  # Initial x position
        i = 1  # Counter for displaying ranks
        for score in self.scores:
            # Drawing rectangles for each score entry
            pygame.draw.rect(utils.screen, (23, 23, 23), (x - 200, y - 10, 450, 50), 2)  # Border rectangle
            pygame.draw.rect(utils.screen, (23, 23, 23), (x - 200, y - 10, 100, 50), 2)  # Rank rectangle

            # Drawing rank and score text
            utils.drawText(Vector2(x - 150, y), str(i), (233, 233, 233), utils.font24)  # Rank
            utils.drawText(Vector2(x, y), str(score), (23, 233, 23), utils.font24)  # Score

            y += 48  # Incrementing y position for the next entry
            i += 1  # Incrementing rank counter

    # Methods for handling keyboard and mouse events, not implemented for this class
    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        pass

    def onMouseUp(self, event):
        pass

    def onMouseWheel(self, event):
        pass