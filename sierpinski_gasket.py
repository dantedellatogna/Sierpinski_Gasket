import pygame
import sys
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH = 800
HEIGHT = 800

main_dots = [(200, 200), (-200, 0), (0, -200)]
dots = []  # list that will contain all the dots except for the main 3


def adjust(x, y):
    # adjusting the position values so they match the pygame coordinates before drawing the dots
    x_adjusted = x + WIDTH / 2
    y_adjusted = y + HEIGHT / 2
    return x_adjusted, y_adjusted


def draw_dots(dot):
    x, y = adjust(dot[0], dot[1])
    pygame.draw.circle(surface=screen, color=RED, center=(x, y), radius=1)


def first_dot():
    # randomly choosing the position of the initial dot
    random_x = random.randint(0, WIDTH)
    random_y = random.randint(0, HEIGHT)
    return (random_x, random_y)


def new_dot():
    # randomly choosing one of the 3 main dots
    n_dice = random.randint(0, 2)

    # calculating the middle point between the newest dot and the chosen main dot
    x = (dots[-1][0] + main_dots[n_dice][0]) / 2
    y = (dots[-1][1] + main_dots[n_dice][1]) / 2

    return (x, y)


def main_loop(screen, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        dots.append(new_dot())
        draw_dots(dots[-1])

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    for i in range(len(main_dots)):
        x, y = adjust(main_dots[i][0], main_dots[i][1])
        pygame.draw.circle(surface=screen, color=WHITE, center=(x, y), radius=5)

    dots.append(first_dot())  # random initial dot
    main_loop(screen, clock)
