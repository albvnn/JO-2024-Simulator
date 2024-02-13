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
        self.jo_img = pygame.transform.scale(jo_img_original, (270, 120))
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.screen.blit(self.bg_img, (0, 0))
            self.screen.blit(self.jo_img, (265, 60))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

Menu().run()