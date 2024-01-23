from transverseproject.built import *

pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Demo')


if __name__ == "__main__":
    main()
    pygame.quit()