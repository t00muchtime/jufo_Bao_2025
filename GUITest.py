import pygame as pg

# Vielleicht könnte man so oder so ähnlich verschiedene Bildschirme machen?

pg.init()

SIZE = WIDTH, HEIGHT = 500, 300
SCREEN_START, SCREEN_GAME, SCREEN_GAMEOVER = 0, 1, 2

screen_id = 0
screen = pg.display.set_mode(SIZE, pg.RESIZABLE)
clock = pg.time.Clock()

# onscreen objects
start_button = pg.Rect(10, 20, 30, 30)
win_button = pg.Rect(30, 30, 30, 30)
menu_button = pg.Rect(10, 20, 30, 30)
restart_button = pg.Rect(50, 20, 30, 30)
quit_button = pg.Rect(90, 20, 30, 30)
# game loop
while True:
    if screen_id == SCREEN_START:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            elif event.type == pg.MOUSEBUTTONDOWN:
                if start_button.collidepoint(pg.mouse.get_pos()):
                    print("start button pressed")
                    screen_id = SCREEN_GAME

        screen.fill("black")
        pg.draw.rect(screen, "white", start_button)
        pg.display.flip()
        clock.tick(60)

    elif screen_id == SCREEN_GAME:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            elif event.type == pg.MOUSEBUTTONDOWN:
                if win_button.collidepoint(pg.mouse.get_pos()):
                    print("game over")
                    screen_id = SCREEN_GAMEOVER

        screen.fill("black")
        pg.draw.rect(screen, "red", win_button)
        pg.display.flip()
        clock.tick(60)

    elif screen_id == SCREEN_GAMEOVER:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            elif event.type == pg.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(pg.mouse.get_pos()):
                    print("menu button pressed: returning to start")
                    screen_id = SCREEN_START
                elif restart_button.collidepoint(pg.mouse.get_pos()):
                    print("restart button pressed: new game")
                    screen_id = SCREEN_GAME
                elif quit_button.collidepoint(pg.mouse.get_pos()):
                    print("quit button pressed: quit game")
                    pg.quit()
                    raise SystemExit

        screen.fill("black")
        pg.draw.rect(screen, "green", menu_button)
        pg.draw.rect(screen, "yellow", restart_button)
        pg.draw.rect(screen, "red", quit_button)
        pg.display.flip()
        clock.tick(60)
