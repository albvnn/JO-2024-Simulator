import random

from pygame import Vector2

# Importing necessary modules
from Game.Obstacle import Obstacle
from utils.util import utils


class Spawner:
    def __init__(self, addObjCallBack):
        # Constructor to initialize the Spawner object
        self.addObjCallBack = addObjCallBack  # Callback function to add spawned objects to the game
        self.lastSpawnObj = None  # Reference to the last spawned object
        self.spawnTime = 3  # Initial spawn time threshold
        self.maxDst = random.randrange(300, 1500)  # Maximum distance between spawned obstacles

    def spawn(self):
        # Method to spawn obstacles
        self.spawnTime += utils.deltaTime()  # Increment spawn time based on delta time
        if self.spawnTime >= 1:  # Check if spawn time threshold is met
            obstacle = Obstacle(Vector2(utils.width + 100, 300), -utils.speed)  # Create a new obstacle object
            if self.lastSpawnObj is not None:  # Check if there was a previously spawned object
                # Check if the distance between the last spawned object and the new obstacle is within the maximum distance
                if utils.distance(self.lastSpawnObj.pos.x, self.lastSpawnObj.pos.y, obstacle.pos.x, obstacle.pos.y) < self.maxDst:
                    return  # Return if the distance threshold is not met
            self.spawnTime = 0  # Reset spawn time
            self.lastSpawnObj = obstacle  # Update last spawned object reference
            self.addObjCallBack(obstacle)  # Add the obstacle to the game using the callback function
            self.maxDst = random.randrange(300, 1500)  # Update maximum distance for next spawn


