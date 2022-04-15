from subprocess import BELOW_NORMAL_PRIORITY_CLASS
import pygame 
import time
from random import randint
pygame.init()

WIDTH, HEIGHT = 500, 500
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')

running = True
lose = False
clock = pygame.time.Clock()
score = 0
level = 1
font = pygame.font.SysFont('Times New Roman', 30)

BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)

BLOCK_SIZE = 20

def game_over():
    global running, lose
    lose = True
    
    while lose:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose = False
                running = False

        screen.fill(GREEN)
        text1 = font.render('GAME OVER', True, BLACK)
        text2 = font.render(f'Your score: {score}', True, BLACK)
        screen.blit(text1, (150, 100))
        screen.blit(text2, (150, 200))

        pygame.display.update()

class Food:
    def __init__(self):
        self.generate_random_pos()
        self.num = randint(1, 6)
        self.image = pygame.image.load('green.png')
    
    def generate_random_pos(self):
        self.x = self.own_round(randint(BLOCK_SIZE, WIDTH - BLOCK_SIZE))
        self.y = self.own_round(randint(BLOCK_SIZE, HEIGHT - BLOCK_SIZE))
        self.check_pos()

    def own_round(self, value, base=BLOCK_SIZE):
        return base * round(value / base)

    def check_pos(self):
        #doesn't fall on a wall or a snake
        for x, y in S.body[1:]:
            if self.x == x * BLOCK_SIZE and self.y == y * BLOCK_SIZE:
                self.generate_random_pos()
                
        for x, y in W.body:
            if self.x == x * BLOCK_SIZE and self.y == y * BLOCK_SIZE:
                self.generate_random_pos()

    def draw(self):
        if self.is_green() == True:
            self.surf = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.surf.blit(pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE)), (0, 0))
            screen.blit(self.surf, (self.x, self.y))
        else:
            pygame.draw.rect(screen, BLUE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def redraw(self):
        self.num = randint(1, 6)

    def is_green(self):
        return self.num == 5

class Wall:
    def __init__(self):
        self.body = []
        self.load_wall()

    def load_wall(self):
        global FPS, level
        if score == 5:
            FPS = 15
            level = 2
        elif score == 10:
            FPS = 20
            level = 3
        elif score == 15:
            FPS = 25
            level = 4
        with open(f'level{level}.txt', 'r') as f:
            wall_body = f.readlines()
        
        self.body = []
        for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
                if value == '#':
                    self.body.append([j, i])

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def collision(self):
            # collision with wall         
            for x, y in self.body:
                if x * BLOCK_SIZE == S.body[0][0] * BLOCK_SIZE and y * BLOCK_SIZE == S.body[0][1] * BLOCK_SIZE:   
                    game_over()    
            
class Snake:
    def __init__(self):
        self.body = [[11, 10], [10, 10]]
        self.dx, self.dy = 1, 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

    def draw(self):
        for i, (x, y) in enumerate(self.body):
            color = RED if i == 0 else GREEN
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def collision(self):
        #collision with self body
        if self.body[0] in self.body[1:]:
            print("Collision with body")
        #leave the area    
        if self.body[0][0] > 25:
            self.body[0][0] = 0
        if self.body[0][1] > 25:
            self.body[0][1] = 0
        if self.body[0][0] < 0:
            self.body[0][0] = 25
        if self.body[0][1] < 0:
            self.body[0][1] = 25

W = Wall()
    
def draw_grid():
    for i in range(0, WIDTH, BLOCK_SIZE):
        for j in range(0, HEIGHT, BLOCK_SIZE):
            pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)

S = Snake()
F = Food()
block = 1

APPLE = pygame.USEREVENT + 1
pygame.time.set_timer(APPLE, 5000)
    
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == APPLE:
            print("event")
            F.redraw()
            F.generate_random_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                S.dx = -block
                S.dy = 0
            if event.key == pygame.K_RIGHT:
                S.dx = block
                S.dy = 0
            if event.key == pygame.K_UP:
                S.dx = 0
                S.dy = -block
            if event.key == pygame.K_DOWN:
                S.dx = 0
                S.dy = block

    if S.body[0][0] * BLOCK_SIZE == F.x and S.body[0][1] * BLOCK_SIZE == F.y:
        if F.is_green():
            score += 5
        else:
            score += 1
        F.redraw()
        F.generate_random_pos()
        S.body.append([0, 0])
    
    screen.fill(BLACK)

    W.load_wall()
    W.draw()
    draw_grid()
    W.collision()
    S.draw()
    S.collision()
    S.move()
    F.check_pos()
    F.draw()
    
    level_text = font.render(f'LEVEL {level}', True, (255, 0, 0))
    text = font.render(f'Score: {score}', True, (255, 0, 0))
    screen.blit(text, (20, 20))
    screen.blit(level_text, (200, 20))
    pygame.display.flip()
pygame.quit()