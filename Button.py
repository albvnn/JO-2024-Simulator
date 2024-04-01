import pygame

# Importing necessary modules
from utils.assets_manager import assetsManager
from utils.sounds import sounds
from utils.util import utils


class Button:
    def __init__(self, id, pos, text, scale, font=utils.font32):
        # Constructor to initialize the Button object
        self.id = id  # Identifier for the button
        self.text = text  # Text displayed on the button

        # Loading button images
        self.img = assetsManager.get("button")  # Default button image
        self.clickImg = assetsManager.get("clickButton")  # Button image when clicked
        self.drawImg = self.img  # Initially set to default button image
        self.pos = pos  # Position of the button

        # Scaling button images based on the provided scale
        width = self.img.get_width()
        height = self.img.get_height()
        self.img = pygame.transform.scale(self.img, (int(width * scale.x), int(height * scale.y)))
        self.clickImg = pygame.transform.scale(self.clickImg, (int(width * scale.x), int(height * scale.y)))

        self.drawImg = self.img  # Initially set to default button image
        self.rect = self.drawImg.get_rect()  # Rectangle representing the button's area
        self.rect.topleft = (pos.x, pos.y)  # Positioning the button rectangle
        self.clicked = False  # Flag to indicate whether the button has been clicked

    def draw(self):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.drawImg = self.clickImg
                action = True
                sounds.play("click")  # Play click sound
                print("play")  # Print message (for debugging)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            self.drawImg = self.img

        # Draw button on screen
        utils.screen.blit(self.drawImg, self.rect)

        # Draw text on the button
        if self.text != "":
            text_surface = utils.font24.render(self.text, True, (10, 77, 104))
            text_rect = text_surface.get_rect(center=(self.pos.x + self.drawImg.get_width() / 2, self.pos.y + self.drawImg.get_height() / 2))
            if self.clicked:
                text_rect.y += 4
            utils.screen.blit(text_surface, text_rect)

        return
