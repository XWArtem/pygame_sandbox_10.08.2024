import pygame
import sys

from constants.constants import BG_COLOR

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption('Sandbox game')
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BG_COLOR)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()