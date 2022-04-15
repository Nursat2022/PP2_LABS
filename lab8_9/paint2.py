import pygame as pg
pg.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

d = {
    'rect' : False,
    'circle' : False,
    'erase' : False,
    'line' : False,
    'square' : False,
    'right_triangle': False,
    'rhombus' : False,
    'triangle' : False
}

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('PAINT')

running = True
erase = False
w = 2


def rectangle(surf, start, end, w, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1- x2)
    height = abs(y1 - y2)
    #4 cases to draw rect
    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(surf, color, (x1, y1, width, height), w)
        else:
            pg.draw.rect(surf, color, (x1, y2, width, height), w)
    else:
        if y1 < y2:
            pg.draw.rect(surf, color, (x2, y1, width, height), w)
        else:
            pg.draw.rect(surf, color, (x2, y2, width, height), w)

def circle(surf, start, end, w, color):            
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1- x2)
    height = abs(y1 - y2)
    #4 cases to draw circle
    if x1 <= x2:
        if y1 < y2:
            pg.draw.ellipse(surf, color, (x1, y1, width, height), w)
        else:
            pg.draw.ellipse(surf, color, (x1, y2, width, height), w)
    else:
        if y1 < y2:
            pg.draw.ellipse(surf, color, (x2, y1, width, height), w)
        else:
            pg.draw.ellipse(surf, color, (x2, y2, width, height), w)

def square(surf, pos, w, color):
    pg.draw.rect(screen, color, (pos[0] - 70, pos[1] - 70, 140, 140), w)
    
def right_t(surf, pos, w, color):
    pg.draw.polygon(screen, color, [(pos[0], pos[1]), (pos[0] + 100, pos[1]), (pos[0], pos[1] + 100)], w)

def rhombus(surf, pos , w, color): 
    x, y = pos[0], pos[1]

    pg.draw.line(screen, color, (x, y), (x + 100, y - 100), w)
    pg.draw.line(screen, color, (x, y), (x - 100, y - 100), w)
    pg.draw.line(screen, color, (x, y), (x, y + 100), w)
    pg.draw.line(screen, color, (x, y), (x, y - 100), w)

def triangle(screen, posi, d, color): 
    pg.draw.polygon(screen, color,  posi, d)

font = pg.font.SysFont('Times New Roman', 30, True)
color = BLACK

prev, cur = None, None

screen.fill(WHITE)
while running:
    pos = pg.mouse.get_pos()
    keys = pg.key.get_pressed()
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        
    if keys[pg.K_r]:
        d['rect'] = True
        for k in d.keys():
            if k != 'rect':
                d[k] = False
    if keys[pg.K_c]:
        d['circle'] = True
        for k in d.keys():
            if k != 'circle':
                d[k] = False
    if keys[pg.K_l]:
        d['line'] = True
        for k in d.keys():
            if k != 'line':
                d[k] = False
    if keys[pg.K_e]:
        d['erase'] = True
        for k in d.keys():
            if k != 'erase':
                d[k] = False
    if keys[pg.K_LALT] and keys[pg.K_r]:
        d['square'] = True
        for k in d.keys():
            if k != 'square':
                d[k] = False
    if keys[pg.K_LALT] and keys[pg.K_a]:
        d['right_triangle'] = True
        for k in d.keys():
            if k != 'right_triangle':
                d[k] = False
    if keys[pg.K_LALT] and keys[pg.K_s]:
        d['rhombus'] = True
        for k in d.keys():
            if k != 'rhombus':
                d[k] = False

    if keys[pg.K_1]:
        color = RED
    if keys[pg.K_2]:
        color = BLUE
    if keys[pg.K_3]:
        color = GREEN

    for event in events:
        if d['line']:
            if event.type == pg.MOUSEBUTTONDOWN:
                prev = pg.mouse.get_pos()
            if event.type == pg.MOUSEMOTION:
                cur = pg.mouse.get_pos()
                if prev:
                    pg.draw.line(screen, color, prev, cur, 3)
                    prev = cur
            if event.type == pg.MOUSEBUTTONUP:
                prev = None       
        if d['rect']:
            if event.type == pg.MOUSEBUTTONDOWN:
                init_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                rectangle(screen, init_pos, pos, w, color)

        elif d['circle']:
            if event.type == pg.MOUSEBUTTONDOWN:
                init_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                circle(screen, init_pos, pos, w,  color)
                
        elif d['square']:
            if event.type == pg.MOUSEBUTTONDOWN:
                square(screen, pos, w, color)

        elif d['right_triangle']:
            if event.type == pg.MOUSEBUTTONDOWN:
                right_t(screen, pos, w, color)

        elif d['rhombus']:
            if event.type == pg.MOUSEBUTTONDOWN:
                rhombus(screen, pos, w, color)

        elif d['erase']:
            if event.type == pg.MOUSEBUTTONDOWN:
                erase = True
            if event.type == pg.MOUSEMOTION:
                if erase:
                    pg.draw.rect(screen, WHITE, (pos[0] - 25, pos[1] - 25, 50, 50))
            if event.type == pg.MOUSEBUTTONUP:
                erase = False
        
    text1 = font.render('1 - RED', True, RED)
    text2 = font.render('2 - BLUE', True, BLUE)
    text3 = font.render('3 - GREEN', True, GREEN)

    screen.blit(text1, (50, 20))
    screen.blit(text2, (200, 20))
    screen.blit(text3, (350, 20))
    pg.display.flip()
pg.quit()
