import pygame, sys

def loop(tick):
    """
    Args
        tick - fn that is called on each loop iteration (frame)
    """
    pygame.init()
    clock = pygame.time.Clock()

    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Visuals
        tick(clock)

        # Updating the window
        pygame.display.update()
        clock.tick(60)