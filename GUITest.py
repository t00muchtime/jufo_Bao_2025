import pygame as pg

import GameState

pg.init()

# font = pg.font.Font(None, 40)

SIZE = WIDTH, HEIGHT = 500, 300
SCREEN_START, SCREEN_GAME, SCREEN_GAMEOVER = 0, 1, 2

PIT_SIZE = 40
MID_GAP = 5
l = 10
t = 30

screen_id = 0
screen = pg.display.set_mode(SIZE, pg.RESIZABLE)
clock = pg.time.Clock()

# board
board = [[2] * 16] * 2
game_state = GameState.GameState(board, 0)
current_player = 0
move = False
pit = 0
hand = 0

# onscreen objects
rects = [
    [pg.Rect(l + j * PIT_SIZE, t + i * PIT_SIZE, PIT_SIZE, PIT_SIZE) for i in range(2)
        for j in range(8)]
] + [
    [pg.Rect(l + j * PIT_SIZE, t + 2 * PIT_SIZE + MID_GAP + i * PIT_SIZE, PIT_SIZE, PIT_SIZE) for i in range(2)
        for j in range(8)]
]
rects = [rects[1][8:] + rects[1][7::-1], rects[0][7::-1] + rects[0][8:]]

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
            elif event.type == pg.MOUSEBUTTONDOWN and not move:
                for i in game_state.moves:
                    if rects[current_player][i].collidepoint(pg.mouse.get_pos()):
                        pit = i
                        print("pit: " + str(pit))

                        move = True
                        pg.time.set_timer(pg.event.Event(3), 100)
                        temp = game_state.generate_child(pit)
                        hand += board[current_player][pit]
                        board[current_player][pit] = 0
                        print(temp.board)
                        print("hello")
                        pit = (pit + 1) % 16
                        # else:

            elif move and event.type == 3:
                print("move")
                print(board)
                if hand > 1:
                    board[current_player][pit] += 1
                    hand -= 1
                    pit = (pit + 1) % 16
                elif board[current_player][pit] > 0:
                    hand += board[current_player][pit]
                    board[current_player][pit] = 0
                    # Plündern
                    if pit > 7:
                        hand += board[current_player ^ 1][23 - pit]
                        board[current_player ^ 1][23 - pit] = 0
                    pit = (pit + 1) % 16
                else:
                    board[current_player][pit] += 1
                    hand = 0
                    pg.time.set_timer(pg.event.Event(3), 0)
                    move = False
                    current_player ^= 1
                    game_state = GameState.GameState(board, current_player)
                    if game_state.winner is not None:
                        board = [[2] * 16] * 2
                        game_state = GameState.GameState(board, 0)
                        screen_id = SCREEN_GAMEOVER
                    print(game_state.board)
                    print(temp.board)
                    print(game_state.board == temp.board)
                    print(current_player)

        screen.fill("black")
        for i in range(2):
            for j in range(16):
                if i == current_player and j in game_state.moves:
                    pg.draw.rect(screen, "green", rects[i][j])
                else:
                    pg.draw.rect(screen, "red", rects[i][j])
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
