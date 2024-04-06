import pygame


class AssetsManager:
    def __init__(self):
        self.assets = {
            'button': pygame.image.load("runnerV3/assets/btn.png").convert_alpha(),
            'clickButton': pygame.image.load("runnerV3/assets/clickBtn.png").convert_alpha(),
            'bottom': pygame.image.load("runnerV3/assets/bottom.png").convert_alpha(),
            'upper': pygame.image.load("runnerV3/assets/upper.png").convert_alpha(),
            'road': pygame.image.load("runnerV3/assets/road.png").convert_alpha(),

            'audience': pygame.image.load("runnerV3/assets/audience.png").convert_alpha(),
            'audience2': pygame.image.load("runnerV3/assets/audience2.png").convert_alpha(),

            'obstacle': pygame.image.load("runnerV3/assets/obstacle.png").convert_alpha(),
            'obstacle_fall': pygame.image.load("runnerV3/assets/obstacle_fall.png").convert_alpha(),

            'run': pygame.image.load("runnerV3/assets/run.png").convert_alpha(),
        }

    def get(self, key):
        return self.assets[key]


assetsManager = AssetsManager()

"""This file defines a class named AssetsManager, which is responsible for loading and storing various images used in the game."""
