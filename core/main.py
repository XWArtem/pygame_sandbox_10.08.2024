import pygame
import sys

from constants.constants import BG_COLOR
from constants.constants import PLAYER_COLOR

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

player = pygame.Rect(300, 250, 50, 50)

def main():
    pygame.init()
    
    pygame.display.set_caption('Sandbox game')
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, PLAYER_COLOR, player)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()