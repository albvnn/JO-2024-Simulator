import pygame
import golfgame_class
import os
import sys
#import pymunk
#import pymunk.pygame_util
import math

os.chdir(os.path.join(os.getcwd(), "GameGolf"))

map = ["-------H--------------------------------", 
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------WWWWWWWWWWWWWWWWW-",
"---------W------------------------------",
"---------W------------------------------",
"---------W------------------------------",
"---------W------------B-----------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"-------------R-RRRRRRRRRRR--------------",
"-------------R--------------------------",
"-------------R--------------------------",
"-------------R--------------------------",
"-------------R--------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",
"----------------------------------------",]

def display_matrix(matp):
    for i in range(len(matp)):
        for j in range(len(matp)):
            print(matp[i][j], end="")
        print("\n")


class GolfGame:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('JO 2024 Simulator')
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_img = pygame.image.load(os.path.join('spirit', 'golfBackground.png'))
        self.clock = pygame.time.Clock()
        self.ball = golfgame_class.Ball(self, (0, 0), 0)
        self.arrow = golfgame_class.Arrow(self, self.ball.rect.center)
        self.hole = golfgame_class.Hole(self, (100, 0))
        self.barrier = golfgame_class.Barrier(self)
        self.river = golfgame_class.Water(self)
        pygame.mixer.init()
        #pygame.mixer.music.load(os.path.join('music', 'REQUIEM.mp3'))

    def display_text(self, text, pos):
        img = pygame.font.SysFont("Lato", 30).render(text, True, "WHITE")
        self.screen.blit(img, (pos[0], pos[1]))

    def map_maker(self, map : list):
        wall_pos = []
        river_pos = []
        for i in range(0, len(map)):
            map[i] = [*map[i]]
        for i in range(0, len(map)):
            for j in range(0, 40):
                if map[i][j] == "B":
                    self.ball.rect.center = (((j+1)*20)-10, ((i+1)*20)-10)
                elif map[i][j] == "H":
                    self.hole.rect.center = (((j+1)*20)-10, ((i+1)*20)-10)
                elif map[i][j] == "W":
                    if map[i][j+1] == "W":
                        k = 0
                        while(map[i][j+k] == "W"):
                            map[i][j+k] = "-"
                            k += 1
                        wall_pos.append([(j*20, i*20), ((j+k)*20, i*20)])
                    elif map[i+1][j] == "W":
                        k = 0
                        while(map[i+k][j] == "W"):
                            map[i+k][j] = "-"
                            k += 1
                        wall_pos.append([(j*20, i*20), (j*20, (i+k+1)*20)])
                    else:
                        map[i][j] = '-'
                        wall_pos.append([(j*20, i*20), (j*20, i*20)])
                elif map[i][j] == "R":
                    if map[i][j+1] == "R":
                        k = 0
                        while(map[i][j+k] == "R"):
                            map[i][j+k] = "-"
                            k += 1
                        river_pos.append([(j*20, i*20), ((j+k)*20, i*20)])
                    elif map[i+1][j] == "R":
                        k = 0
                        while(map[i+k][j] == "R"):
                            map[i+k][j] = "-"
                            k += 1
                        river_pos.append([(j*20, i*20), (j*20, (i+k)*20)])
                    else:
                        map[i][j] = '-'
                        river_pos.append([(j*20, i*20), (j*20, i*20)])
                elif map[i][j] == "R":
                    pass

        self.barrier.wall_maker(wall_pos)
        self.river.river_maker(river_pos)
                        


    def run(self):
        self.map_maker(map)
        running = True
        taking_shoot = False
        shoot_in_gestion = False
        termined_shoot = True
        end_game = False
        shoot_angle = 0
        velocity = -1
        power = 1
        #pygame.mixer.music.play()

        while running:
            self.screen.blit(self.bg_img, (0, 0))
            if not self.hole.check_ball_in_hole(self.ball.rect.center):
                self.screen.blit(self.ball.ballimg, self.ball.rect)
            self.screen.blit(self.hole.holeimg, self.hole.rect)
            self.barrier.display_walls()
            self.river.display_rivers()


            if taking_shoot:
                shoot_angle = -math.degrees(math.atan2(self.ball.dist_mous_ball(pygame.mouse.get_pos())[1], self.ball.dist_mous_ball(pygame.mouse.get_pos())[0])) % 360
                self.arrow.rotate_angle(-shoot_angle, self.ball.dist_mous_ball(pygame.mouse.get_pos())[2])
                self.arrow.draw()
                power = self.ball.dist_mous_ball(pygame.mouse.get_pos())[2]/40

            for i in self.barrier.rectlist:
                if pygame.Rect.colliderect(i[0], self.ball.rect):
                    shoot_angle = self.ball.recalculate_shootangle_wall(i, shoot_angle)

            for k in self.river.rectlist:
                if pygame.Rect.colliderect(k[0], self.ball.rect):
                    self.ball.rect.center = self.ball.last_pos
                    velocity = 0
            
            print(shoot_angle, velocity)

            if shoot_in_gestion:
                taking_shoot = False
                termined_shoot = False
                self.ball.update_pos(-shoot_angle, power)
                velocity -= 1/power

            if velocity == 0:
                self.ball.last_pos = self.ball.rect.center
                shoot_in_gestion = False
                termined_shoot = True
                self.ball.counter_shot += 1

            if self.hole.check_ball_in_hole(self.ball.rect.center):
                velocity = -1
                self.display_text("VICTORY IN " + str(self.ball.counter_shot), (100, 100))
                end_game = True
                taking_shoot = False
                shoot_in_gestion = False

            if self.ball.counter_shot >= 10:
                self.display_text("GAME OVER", (100, 100))
                end_game = True

            if not end_game and termined_shoot:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        taking_shoot = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        taking_shoot = False
                        shoot_in_gestion = True
                        termined_shoot = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

GolfGame().run()
pygame.quit()
sys.exit()

