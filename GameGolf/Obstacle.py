import os
import pygame
import math

# Barrier class for handling barriers in the game
class Barrier(pygame.sprite.Sprite):
    def __init__(self, game):
        # Load barrier images and initialize lists to hold barrier rectangles and their information
        self.bricksimg = pygame.image.load(os.path.join('assets', 'bricksTile.png'))
        self.halfbricksimg = pygame.image.load(os.path.join('assets', 'bricksHalfTile.png'))
        self.game = game
        self.rectlistinfo = []  # Holds information about full bricks
        self.rectlist = []  # Holds full brick rectangles
        self.rectlisthalfinfo = []  # Holds information about half bricks
        self.rectlisthalf = []  # Holds half brick rectangles

    # Method to create a full wall
    def wall(self, pos_start: tuple, pos_end: tuple):
        rectwall = pygame.Rect(0, 0, 0, 0)
        if pos_start[1] == pos_end[1] and pos_start[0] != pos_end[0] and abs(pos_start[0] - pos_end[0]) % 20 == 0:
            rectwall.center = (pos_start[0], pos_start[1])
            rectwall.height = 20
            rectwall.width = pos_end[0] - pos_start[0]
            if rectwall not in self.rectlist:
                self.rectlistinfo.append((rectwall, "horizontal", (pos_start, pos_end)))
                self.rectlist.append(rectwall)
            return True
        elif pos_start[1] != pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectwall.center = (pos_start[0], pos_start[1])
            rectwall.height = abs(pos_start[1] - pos_end[1])
            rectwall.width = 20
            if rectwall not in self.rectlist:
                self.rectlistinfo.append((rectwall, "vertical", (pos_start, pos_end)))
                self.rectlist.append(rectwall)
            return True
        elif pos_start[1] == pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectwall.center = (pos_start[0], pos_start[1])
            rectwall.height = 20
            rectwall.width = 20
            if rectwall not in self.rectlist:
                self.rectlistinfo.append((rectwall, "block", (pos_start, pos_end)))
                self.rectlist.append(rectwall)
            return True
        else:
            return False

    # Method to create a half brick
    def halfbricks(self, pos: tuple, n: int):
        rectwall = pygame.Rect(0, 0, 0, 0)
        rectwall.center = (pos[0], pos[1])
        rectwall.height = 20
        rectwall.width = 20
        if rectwall not in self.rectlisthalf:
            self.rectlisthalf.append((rectwall, n))

    # Method to create all half bricks
    def allhalfbricks(self, pos_halfbricks: list):
        for halfbrick in pos_halfbricks:
            self.halfbricks((halfbrick[0][0], halfbrick[0][1]), halfbrick[1])

    # Method to create barriers from a list of positions
    def wall_maker(self, pos_walls: list):
        for wall in pos_walls:
            self.wall(wall[0], wall[1])

    # Method to display full walls and half bricks
    def display_walls(self):
        # Display full walls
        for i in self.rectlistinfo:
            if i[1] == "horizontal":
                for k in range(i[2][0][0], i[2][1][0], 20):
                    self.game.screen.blit(self.bricksimg, (k, i[2][0][1]))
            elif i[1] == "vertical":
                for k in range(i[2][0][1], i[2][1][1], 20):
                    self.game.screen.blit(pygame.transform.rotate(self.bricksimg, 90), (i[2][0][0], k))
            elif i[1] == "block":
                self.game.screen.blit(self.bricksimg, (i[2][0][0], i[2][0][1]))

        # Display half bricks
        for k in self.rectlisthalf:
            if k[1] == 0:
                self.game.screen.blit(self.halfbricksimg, (k[0][0], k[0][1]))
            else:
                self.game.screen.blit(pygame.transform.rotate(self.halfbricksimg, 90 * k[1]), (k[0][0], k[0][1]))


# Water class for handling water obstacles
class Water:
    def __init__(self, game):
        # Load water image and initialize lists to hold water rectangles and their information
        self.watersimg = pygame.image.load(os.path.join('assets', 'waterTile.png'))
        self.game = game
        self.rectlistinfo = []  # Holds information about water rectangles
        self.rectlist = []  # Holds water rectangles

    # Method to create a river
    def river(self, pos_start, pos_end):
        rectriver = pygame.Rect(0, 0, 0, 0)
        if pos_start[1] == pos_end[1] and pos_start[0] != pos_end[0] and abs(pos_start[0] - pos_end[0]) % 20 == 0:
            rectriver.center = (pos_start[0], pos_start[1])
            rectriver.height = 20
            rectriver.width = pos_end[0] - pos_start[0]
            if rectriver not in self.rectlist:
                self.rectlistinfo.append((rectriver, "horizontal", (pos_start, pos_end)))
                self.rectlist.append(rectriver)
            return True
        elif pos_start[1] != pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectriver.center = (pos_start[0], pos_start[1])
            rectriver.height = abs(pos_start[1] - pos_end[1])
            rectriver.width = 20
            if rectriver not in self.rectlist:
                self.rectlistinfo.append((rectriver, "vertical", (pos_start, pos_end)))
                self.rectlist.append(rectriver)
            return True
        elif pos_start[1] == pos_end[1] and pos_start[0] == pos_end[0] and abs(pos_start[1] - pos_end[1]) % 20 == 0:
            rectriver.center = (pos_start[0], pos_start[1])
            rectriver.height = 20
            rectriver.width = 20
            if rectriver not in self.rectlist:
                self.rectlistinfo.append((rectriver, "block", (pos_start, pos_end)))
                self.rectlist.append(rectriver)
            return True
        else:
            return False

    # Method to create rivers from a list of positions
    def river_maker(self, pos_rivers: list):
        for river in pos_rivers:
            self.river(river[0], river[1])

    # Method to display rivers
    def display_rivers(self):
        for i in self.rectlistinfo:
            if i[1] == "horizontal":
                for k in range(i[2][0][0], i[2][1][0], 20):
                    self.game.screen.blit(self.watersimg, (k, i[2][0][1]))
            elif i[1] == "vertical":
                for k in range(i[2][0][1], i[2][1][1], 20):
                    self.game.screen.blit(self.watersimg, (i[2][0][0], k))
            elif i[1] == "block":
                self.game.screen.blit(self.watersimg, (i[2][0][0], i[2][0][1]))


# Palmer class for handling palm trees
class Palmer:
    def __init__(self, game):
        # Load palm tree image and initialize lists to hold palm tree rectangles and their information
        self.palmersimg = pygame.image.load(os.path.join('assets', 'obstacleTile.png'))
        self.game = game
        self.rectlistinfo = []  # Holds information about palm tree rectangles
        self.rectlist = []  # Holds palm tree rectangles

    # Method to create a palm tree
    def palmer(self, pos):
        rectpalmer = pygame.Rect(0, 0, 20, 20)
        rectpalmer.center = pos
        if rectpalmer not in self.rectlist:
            self.rectlistinfo.append((rectpalmer, pos))
            self.rectlist.append(rectpalmer)
            return True
        else:
            return False

    # Method to create palm trees from a list of positions
    def palmer_maker(self, pos_palmers: list):
        for palmer in pos_palmers:
            self.palmer(palmer)

    # Method to display palm trees
    def display_palmers(self):
        for i in self.rectlistinfo:
            self.game.screen.blit(self.palmersimg, i[1])


# Sand class for handling sand traps
class Sand:
    def __init__(self, game):
        # Load sand trap image and initialize lists to hold sand trap rectangles and their information
        self.sandimg = pygame.image.load(os.path.join('assets', 'sandTile.png'))
        self.game = game
        self.rectlistinfo = []  # Holds information about sand trap rectangles
        self.rectlist = []  # Holds sand trap rectangles

    # Method to create a sand trap
    def sand(self, pos):
        rectsand = pygame.Rect(0, 0, 20, 20)
        rectsand.center = pos
        if rectsand not in self.rectlist:
            self.rectlistinfo.append((rectsand, pos))
            self.rectlist.append(rectsand)
            return True
        else:
            return False

    # Method to create sand traps from a list of positions
    def sand_maker(self, pos_sands: list):
        for sand in pos_sands:
            self.sand(sand)

    # Method to display sand traps
    def display_sand(self):
        for i in self.rectlistinfo:
            self.game.screen.blit(self.sandimg, i[1])
