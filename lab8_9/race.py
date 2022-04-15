import pygame as pg
import random
pg.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
a, b = 200, 400

background = pg.image.load('./race_image_sound/road.png')

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('./race_image_sound/player.png')
        self.surf = pg.Surface((60, 110), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center = (WIDTH // 2, 500))
        self.speed = 5

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (60, 110)), (0, 0))
        screen.blit(self.surf, self.rect)   

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)
        if keys[pg.K_s] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.speed)
        if keys[pg.K_a] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pg.K_d] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)
        
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('./race_image_sound/enemy.png')
        self.surf = pg.Surface((60, 100), pg.SRCALPHA)
        self.speed = random.randint(3, 6)
        self.rect = self.surf.get_rect(center = (random.randint(60, WIDTH - 60), -100))
    
    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (60, 100)), (0, 0))
        screen.blit(self.surf, self.rect)

    def inc_speed(self):
        if score >= a and score < b:
            self.speed = random.randint(5, 8)
        elif score >= b:
            self.speed = random.randint(10, 13)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            # self.rect.x, self.rect.y = random.randint(60, WIDTH - 60), -100
            self.rect = self.surf.get_rect(center = (random.randint(60, WIDTH - 60), -100))

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('./race_image_sound/coin.png')
        self.surf = pg.Surface((30, 30), pg.SRCALPHA)
        self.speed = random.randint(1, 8)
        self.num = random.randint(1, 8)
        self.different_coin()
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 20), -100))
    
    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (30, 30)), (0, 0))
        screen.blit(self.surf, self.rect)

    def move(self):
        self.rect.move_ip(0, self.speed)
        
    def regenerate(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def different_coin(self):
        if self.num == 2:
            self.speed = 8
            self.image = pg.image.load('./race_image_sound/diff_coin.png')

    def is_diff_coin(self):
        return self.num == 2        


BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('RACING GAME')

running = True
clock = pg.time.Clock()
score = 0
font = pg.font.SysFont('Times New Roman', 30, True)
lose = False

P = Player()
coins = pg.sprite.Group([Coin() for _ in range(5)])
enemies = pg.sprite.Group([Enemy() for _ in range(3)])
entities = pg.sprite.Group(coins, enemies)

def game_over():
    img = pg.image.load('./race_image_sound/game-over-art.jpg')
    global lose, running
    pg.mixer.music.stop()
    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                lose = False
                running = False
        screen.blit(img, (0, 0))
        pg.display.flip()

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())

    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    P.draw()
    P.move()
   
    for enemy in enemies:
        enemy.draw()
        enemy.inc_speed()
        enemy.move()

    for coin in coins:
        coin.draw()
        coin.move()
        coin.regenerate()

    if pg.sprite.spritecollideany(P, enemies):
        pg.mixer.Sound('./race_image_sound/car.wav').play()
        lose = True
        game_over()

    for coin in pg.sprite.spritecollide(P, coins, True):
        pg.mixer.Sound('./race_image_sound/coin.wav').play()
        if coin.is_diff_coin():
            score += 100
        else:    
            score += 1

    if coins.__len__() < 5:
        coins.add(Coin())

    text = font.render(f'Score: {score}', True, RED)
    screen.blit(text, (0, 0))

    pg.display.flip()
pg.quit()
    