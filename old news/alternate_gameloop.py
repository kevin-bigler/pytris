import pygame, sys

screen_width = 200
screen_height = 400
bg_color = pygame.Color('grey12')

class GameLoop:
    def __init__(self, screen):
        self.running = False
        
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Tetris!')
        self.clock = pygame.time.Clock()


    def loop(self, tick):
        """
        Args
            tick - fn that is called on each loop iteration (frame), called like tick(screen)
        """
        self.running = True

        while self.running:
            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Visuals
            self.screen.fill(bg_color)
            tick(self.screen)

            # Updating the window
            pygame.display.update()
            self.clock.tick(60)