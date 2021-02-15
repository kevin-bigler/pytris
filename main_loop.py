import pygame, sys #, random
from main import tick

screen_width = 200
screen_height = 400
bg_color = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris!')

# ball = pygame.Rect((0, 0), (10, 10))
# paddle = pygame.Rect((100, 300), (50, 10))
# brick = pygame.Rect((100, 50), (30, 20))

# light_grey = (200, 200, 200)

# ball_speed_x = 3
# ball_speed_y = 3

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # ball.x += ball_speed_x
    # ball.y += ball_speed_y

    # if ball.top <= 0 or ball.bottom >= screen_height:
    #     ball_speed_y *= -1
    # if ball.left <= 0 or ball.right >= screen_width:
    #     ball_speed_x *= -1
    
    # if ball.colliderect(paddle):
    #     ball_speed_y *= -1
    #     # ball_speed_x *= random.randrange(0.1, 2.0)

    # Visuals
    screen.fill(bg_color)
    # pygame.draw.rect(screen, light_grey, paddle)
    # pygame.draw.rect(screen, light_grey, brick)
    # pygame.draw.ellipse(screen, light_grey, ball)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)