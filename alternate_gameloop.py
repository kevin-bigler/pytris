import pygame, sys

class GameLoop:
    def __init__(self, fps=60):
        self.running = False
        self.fps = fps
        self.clock = pygame.time.Clock()

    def start(self, tick):
        """
        Args
            tick - fn that is called on each loop iteration (frame), called like tick(clock)
        """
        self.running = True

        while self.running:
            # Handle exit-input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Game Tick
            tick(self.clock)

            # Updating the window
            pygame.display.update()
            self.clock.tick(self.fps)

    def stop():
        self.running = False
