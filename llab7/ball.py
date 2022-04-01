import pygame 
pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()

x, y = WIDTH // 2, HEIGHT // 2
r = 25
step = 20

while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), r)

    if keys[pygame.K_LEFT] and x -r > 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + r < WIDTH:
        x += step
    if keys[pygame.K_UP] and y - r > 0:
        y -= step
    if keys[pygame.K_DOWN] and y + r < HEIGHT:
        y += step
    
    pygame.display.flip()
pygame.quit()