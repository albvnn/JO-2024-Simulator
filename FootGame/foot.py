import pygame
import math
import os

os.chdir(os.path.join(os.getcwd(), "FootGame"))

v = 100
g = 9.81
h = 0
ball_x = 0
ball_y = 600

pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Football")


background = pygame.image.load('assets/football-bg.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))
ball_image = pygame.image.load('assets/ball.png')
ball_image = pygame.transform.scale(ball_image, (40, 29))

# Define initial shooting angle (adjust as needed)
initial_angle = 45  # Example: 45 degrees

def calculate_trajectory(g, v, h, alpha, t, screen_height):
    y = screen_height - int((-1 / 2) * g * t ** 2 + v * math.sin(math.radians(alpha)) * t + h)
    x = int(v * math.cos(math.radians(alpha)) * t)
    return x, y

def draw_trajectory(screen, g, v, h, alpha, t, screen_height):
    ball_x, ball_y = calculate_trajectory(g, v, h, alpha, t, screen_height)
    return ball_x, ball_y

running = True
clock = pygame.time.Clock()
time_step = 0
fps = 60
taking_shoot = False
shoot_ingestion = False
score = 0
mous_x, mous_y = 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            taking_shoot = True
        elif event.type == pygame.MOUSEBUTTONUP:
            taking_shoot = False

    if taking_shoot:
        mous_x, mous_y = pygame.mouse.get_pos()
        diffx = mous_x - ball_x
        diffy = mous_y - ball_y
        alpha = math.degrees(math.atan2(diffy, diffx))
        shoot_ingestion = True

    if shoot_ingestion:
        ball_x, ball_y = draw_trajectory(screen, g, v, h, initial_angle, time_step, screen_height)
        score += 1
        if ball_y > screen_height - 29:
            shoot_ingestion = False
            time_step = 0


    screen.blit(background, (0, 0))
    screen.blit(ball_image, (ball_x, ball_y))
    pygame.display.update()
    time_step += clock.tick(fps) / 200
    print("x: ", ball_x, "y: ", ball_y, "score: ", score)


pygame.quit()
