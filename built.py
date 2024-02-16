import os
import sys
import pygame

clock = pygame.time.Clock()
def main():
    while True:
        pygame.display.update()
        clock.tick(60)


class Menu:
    def __init__(self):
        pygame.display.set_caption('JO 2024 Simulator')
        self.screen = pygame.display.set_mode((800, 600))
        bg_img_original = pygame.image.load(os.path.join('spirit', 'backgroundMenu.png'))
        self.bg_img = pygame.transform.scale(bg_img_original, (800, 600))
        jo_img_original = pygame.image.load(os.path.join('spirit', 'anneauxJO.png'))
        self.jo_img = pygame.transform.scale(jo_img_original, (250, 120))

        game1_OFF = pygame.image.load(os.path.join('spirit', 'game1_OFF.png'))
        self.game1_OFF = pygame.transform.scale(game1_OFF, (150, 75))
        game1_ON = pygame.image.load(os.path.join('spirit', 'game1_ON.png'))
        self.game1_ON = pygame.transform.scale(game1_ON, (150, 75))

        game2_OFF = pygame.image.load(os.path.join('spirit', 'game2_OFF.png'))
        self.game2_OFF = pygame.transform.scale(game2_OFF, (150, 75))
        game2_ON = pygame.image.load(os.path.join('spirit', 'game2_ON.png'))
        self.game2_ON = pygame.transform.scale(game2_ON, (150, 75))

        game3_OFF = pygame.image.load(os.path.join('spirit', 'game3_OFF.png'))
        self.game3_OFF = pygame.transform.scale(game3_OFF, (150, 75))
        game3_ON = pygame.image.load(os.path.join('spirit', 'game3_ON.png'))
        self.game3_ON = pygame.transform.scale(game3_ON, (150, 75))

        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            mouse_X, mouse_Y =pygame.mouse.get_pos()


            self.screen.blit(self.bg_img, (0, 0))
            self.screen.blit(self.jo_img, (275, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (mouse_X >= 325 and mouse_X <= 500) and (mouse_Y >= 200 and mouse_Y <= 275) :
                        import golfgame
                    if (mouse_X >= 325 and mouse_X <= 500) and (mouse_Y >= 300 and mouse_Y <= 375) :
                        pass
                    if (mouse_X >= 325 and mouse_X <= 500) and (mouse_Y >= 400 and mouse_Y <= 475) :
                        pass  
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass




            if (mouse_X >= 325 and mouse_X <= 500) and (mouse_Y >= 200 and mouse_Y <= 275) :
                self.screen.blit(self.game1_ON,(325, 200))
            else :
                self.screen.blit(self.game1_OFF,(325, 200))


            if (mouse_X >= 325 and mouse_X <= 500) and (mouse_Y >= 300 and mouse_Y <= 375) :
                self.screen.blit(self.game2_ON,(325, 300))
            else :
                self.screen.blit(self.game2_OFF,(325, 300))


            if (mouse_X >= 325 and mouse_X <= 500) and (mouse_Y >= 400 and mouse_Y <= 475) :
                self.screen.blit(self.game3_ON,(325, 400))
            else :
                self.screen.blit(self.game3_OFF,(325, 400))


                

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

Menu().run()