import pygame

# Color vars here

# Grid vars
WIDTH = 4
HEIGHT = 4
MARGIN = 1

# Initialize pygame
pygame.init()
WINDOW_SIZE = [820, 620]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set the screen background
    screen.fill(pygame.Color('black'))

    # Draw the grid
    for row in range(120):
        for column in range(160):
            # Set the color here

            # Draw rectangle
            pygame.draw.rect(screen, pygame.Color('green'), [
                (MARGIN + WIDTH) * column + MARGIN,
                (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Update the screen
    pygame.display.flip()

# Prevent hang if idle
pygame.quit()