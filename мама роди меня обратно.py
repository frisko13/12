import pygame as pg

W = 800
H = 600
game_over = False

pg.init()

screen = pg.display.set_mode((W, H))
pg.display.set_caption('my game')

COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

rect = pg.Rect(100, 50, 400, 300)



x = 0
y = 0


clock = pg.time.Clock()

while not game_over:
    screen.fill(COLOR_BLACK)
    for event in pg.event.get():
        print(event)
        if event.type == pg.KEYDOWN and event.key == 27 or event.type == pg.QUIT:
            game_over = True
        # if event.type == pg.KEYDOWN:
        #     if event.key == 97:
        #         x += -20
        #     if event.key == 100:
        #         x += 20
        #     if event.key == 119:
        #         y += -20
        #     if event.key == 115:
        #         y += 20
        #     if event.key == 1073741904:
        #         x += -20
        #     if event.key == 1073741903:
        #         x += 20
        #     if event.key == 1073741906:
        #         y += -20
        #     if event.key == 1073741905:
        #         y += 20
                
    if x > W + 100:
        x = -500

    x += 5

    pg.draw.rect(screen, COLOR_RED, (400+x, 250+y, 30, 90))
    pg.draw.rect(screen, COLOR_RED, (430+x, 250+y, 30, 90))
    pg.draw.rect(screen, COLOR_RED, (460+x, 250+y, 30, 90))
    pg.draw.rect(screen, COLOR_BLUE, (410+x, 280+y, 30, 15))
    pg.draw.rect(screen, COLOR_BLUE, (450+x, 280+y, 30, 15))
    pg.draw.rect(screen, COLOR_BLUE, (430+x, 310+y, 30, 15))

    # # ГОЛОВА
    # pg.draw.rect(screen, COLOR_RED, (100+x, 10+y, 10, 30))
    # pg.draw.rect(screen, COLOR_RED, (110+x, 10+y, 10, 30))
    # pg.draw.rect(screen, COLOR_RED, (120+x, 10+y, 10, 30))
    # # ТУЛОВИЩЕ
    # pg.draw.rect(screen, COLOR_GREEN, (100+x, 40+y, 30, 60))
    # pg.draw.rect(screen, COLOR_RED, (85+x, 40+y, 15, 60))
    # pg.draw.rect(screen, COLOR_RED, (130+x, 40+y, 15, 60))
    # # НОГИ
    # pg.draw.rect(screen, COLOR_BLUE, (100+x, 100+y, 15, 60))
    # pg.draw.rect(screen, COLOR_BLUE, (115+x, 100+y, 15, 60))


    pg.display.update()


    clock.tick(60)












































