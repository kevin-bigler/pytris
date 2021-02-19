import pygame, sys

def loop(tick):
    """
    Args
        tick - fn that is called on each loop iteration (frame), called like tick(screen)
    """
    screen_width = 200
    screen_height = 400
    bg_color = pygame.Color('grey12')

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Tetris!')

    # ball = pygame.Rect((0, 0), (10, 10))

    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Visuals
        screen.fill(bg_color)
        tick(screen)
        # pygame.draw.rect(screen, light_grey, paddle)

        # Updating the window
        pygame.display.flip()
        clock.tick(60)