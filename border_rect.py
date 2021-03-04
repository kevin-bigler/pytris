import pygame

black = (0, 0, 0)

def boarder_rect(width, height, fill_color, border_width=1, border_color=black):
    "Create a rect surface with a border"
    surface = pygame.Surface((width, height))
    surface.fill(fill_color)

    rect = pygame.Rect((0, 0), (width, height))
    pygame.draw.rect(surface, border_color, rect, border_width)

    return surface

def draw_rect_test(screen):
    width, height = 20, 40
    box = boarder_rect(width, height, pygame.Color('red'))
    screen.blit(box, (5, 5))



screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption('Tetris!')
clock = pygame.time.Clock()

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # # Visuals
    screen.fill(pygame.Color('white'))
    # tick(self.screen)
    draw_rect_test(screen)

    # # Updating the window
    pygame.display.update()
    clock.tick(60)
