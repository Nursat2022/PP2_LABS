import pygame as pg
pg.init()

WIDTH, HEIGHT = 800, 600
running = True
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pg.time.Clock()

songs = list()
songs.append('./music/Gym Class Heroes, Adam Levine - Stereo Hearts.mp3')
songs.append('./music/Tom Walker - Leave A Light On [vzvuke.net].mp3')
songs.append('./music/john-legend-all-of-me.mp3')
songs.append('./music/Mika — Relax (Take It Easy).mp3')

pg.mixer.music.load(songs[0])
current = songs[0]
a = pg.mixer.music.play()

#buttoms
left = pg.image.load('./play_image/p.png')
left = pg.transform.scale(left, (50, 50))
right = pg.image.load('./play_image/n-removebg-preview.png')
right = pg.transform.scale(right, (50, 50))
pause = pg.image.load('./play_image/p-removebg-preview.png')
pause = pg.transform.scale(pause, (56, 56))
unpause = pg.image.load('./play_image/pause-removebg-preview.png')
unpause = pg.transform.scale(unpause, (75, 50))

images = list()
img1 = pg.image.load('play_image/streo.jpg')
img1 = pg.transform.scale(img1, (WIDTH, HEIGHT))
img2 = pg.image.load('play_image/light.jpg')
img2 = pg.transform.scale(img2, (WIDTH, HEIGHT))
img3 = pg.image.load('play_image/all_of_me.jpg')
img3= pg.transform.scale(img3, (WIDTH, HEIGHT))
img4 = pg.image.load('play_image/rel.jpg')
img4= pg.transform.scale(img4, (WIDTH, HEIGHT))
images = [img1, img2, img3, img4]

d = dict()
for i, j in zip(songs, images):
    d[i] = j

def play_next_song():
    global songs, current
    songs = songs[1:] + [songs[0]]
    pg.mixer.music.load(songs[0])
    pg.mixer.music.play()
    current = songs[0]

def play_prev_song():
    global songs, current
    songs = [songs[len(songs)-1]] + songs[:len(songs)-1]
    pg.mixer.music.load(songs[0])
    pg.mixer.music.play()
    current = songs[0]

play = True
SONG_END = pg.USEREVENT + 1
pg.mixer.music.set_endevent(SONG_END)

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                play_next_song()
            if event.key == pg.K_LEFT:
                play_prev_song()    
            if event.key == pg.K_SPACE and play:
                pg.mixer.music.pause()
                play = False
            elif event.key == pg.K_SPACE and not play:
                pg.mixer.music.unpause()       
                play = True

        if event.type == pg.MOUSEBUTTONDOWN:
            keys = pg.mouse.get_pressed()
            if keys[0]:
                (x, y) = pg.mouse.get_pos()
                if x in range(260, 260 + 50 + 1) and y in range(450, 450 + 50 + 1):
                    play_prev_song()  
                elif x in range(460, 450 + 50 + 1) and y in range(450 + 50 + 1):
                    play_next_song()
                elif x in range(345, 345 + 75 + 1) and y in range(453, 453 + 50 + 1):
                    if play:
                        pg.mixer.music.pause()
                        play = False
                    else:
                        pg.mixer.music.unpause()  
                        play = True

        if event.type == SONG_END:
            play_next_song()

    screen.blit(d[current], (0, 0))
    screen.blit(left, (260, 450))
    screen.blit(right, (460, 450))
    screen.blit(unpause, (345, 453))
    if not play:
        screen.blit(pause, (356, 450))

    pg.display.flip()
pg.quit()