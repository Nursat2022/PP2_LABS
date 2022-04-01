import pygame 
from datetime import datetime
pygame.init()

WIDTH, HEIGHT = 800, 600

RED = (255, 0, 0)

clock_img = pygame.image.load('./image/clock.jpeg')
right_h = pygame.image.load('./image/right.png')
left_h = pygame.image.load('./image/left.png')

clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))
right_h = pygame.transform.scale(right_h, (330, 330))
left_h = pygame.transform.scale(left_h, (330, 330))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
font = pygame.font.SysFont('Verdana', 40)

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

def angle(an):
    return an * -6

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(clock_img, (0, 0))

    now = datetime.now()
    minute = now.minute
    second = now.second
    text = font.render(now.strftime('%H:%M:%S'), True, RED)
    screen.blit(text, (0, 0))
    blitRotateCenter(screen, left_h, (235, 130), angle(second + 1)) 
    blitRotateCenter(screen, right_h, (235, 127), angle(minute))
    pygame.display.flip()
    
pygame.quit()            


