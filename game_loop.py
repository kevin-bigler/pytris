import pygame, sys


class GameLoop:
    def __init__(self):
        self.running = False
        pygame.init()
    
    def start(self, run_tick=lambda dt: {}, fps=60):
        self.running = True
        clock = pygame.time.Clock()

        dt = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
            
            run_tick(dt)
            dt = clock.tick(fps)
        
        pygame.quit()
        sys.exit()

    def stop(self):
        self.running = False