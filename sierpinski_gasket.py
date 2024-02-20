import pygame
import sys
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


WIDTH = 800
HEIGHT = 800
main_dots = {'1': (400, 0), '2':(-400, 0), '3': (400, 0)}

def draw_dots():
    dot_list = list(main_dots.keys())
    for i in dot_list:
        pygame.draw.circle(surface=screen, color=WHITE, center=main_dots[dot_list[i]], radius=1)

def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":


    draw_dots()


    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    main_loop()