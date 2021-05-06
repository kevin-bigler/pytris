import pygame
from game_loop import GameLoop


def main():
    screen_width = 200
    screen_height = 400
    bg_color = pygame.Color('grey12')

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Tetris!')

    # run on the game loop
    def run_tick(dt):
        screen.fill(bg_color)
        pygame.display.update()

    loop = GameLoop()
    loop.start(run_tick)

main()