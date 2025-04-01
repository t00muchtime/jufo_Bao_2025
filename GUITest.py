import pygame as pg

import GameState
import PlayerA1

pg.init()

font = pg.font.Font(pg.font.match_font("comicsansms", True), 30)
font2 = pg.font.Font(pg.font.match_font("comicsansms", True), 14)

SIZE_BOARD = WIDTH_BOARD, HEIGHT_BOARD = 570, 310
SCREEN_START, SCREEN_GAME, SCREEN_GAMEOVER = 0, 1, 2

COLORS = {"light blue": (220, 243, 247), "light yellow": (251, 250, 174), "light pink": (253, 216, 242)}

PIT_SIZE = WIDTH_BOARD // (57 / 7)
MID_GAP = HEIGHT_BOARD // 31 + PIT_SIZE / 6
LEFT_GAP = 20
TOP_GAP = 20

SIZE_WINDOW = WIDTH, HEIGHT = 2*LEFT_GAP + 10*PIT_SIZE, 2*TOP_GAP + HEIGHT_BOARD

screen_id = 0
screen = pg.display.set_mode(SIZE_WINDOW)
pg.display.set_caption("Mancala oder so ka hab das noch nie gespielt")
clock = pg.time.Clock()

# board
human = 0
computer = PlayerA1.PlayerA1(0.3766, 0.09, 0.5338811, 4)
board = [[2] * 16, [2] * 16]
game_state = GameState.GameState(board, 0)
current_player = 0
move = False
pit = 0
hand = 0

# onscreen objects
board_img = pg.transform.scale(pg.image.load("Bilder/Hintergrund.png"), SIZE_BOARD)
PIT_IMAGES = {"pit_1": pg.transform.scale(pg.image.load("Bilder/Bohne 1.PNG"), (PIT_SIZE, PIT_SIZE)),
              "pit_2": pg.transform.scale(pg.image.load("Bilder/Bohne 2.PNG"), (PIT_SIZE, PIT_SIZE)),
              "pit_3": pg.transform.scale(pg.image.load("Bilder/Bohne 3.PNG"), (PIT_SIZE, PIT_SIZE)),
              "pit_4": pg.transform.scale(pg.image.load("Bilder/Bohne 4.PNG"), (PIT_SIZE, PIT_SIZE)),
              "pit_5": pg.transform.scale(pg.image.load("Bilder/Bohne 5.PNG"), (PIT_SIZE, PIT_SIZE)),
              "pit_more": pg.transform.scale(pg.image.load("Bilder/Bohne Viele.PNG"), (PIT_SIZE, PIT_SIZE))}

rects = [
            [pg.Rect(LEFT_GAP + (1 / 12 + j) * PIT_SIZE, TOP_GAP + (i + 1 / 12) * PIT_SIZE, PIT_SIZE, PIT_SIZE) for i in
             range(2)
             for j in range(8)]
        ] + [
            [pg.Rect(LEFT_GAP + (1 / 12 + j) * PIT_SIZE, TOP_GAP + 2 * PIT_SIZE + MID_GAP + (i + 1 / 12) * PIT_SIZE,
                     PIT_SIZE, PIT_SIZE) for i in range(2)
             for j in range(8)]
        ]
rects = [rects[1][8:] + rects[1][7::-1], rects[0][7::-1] + rects[0][8:]]

first_button = pg.Rect(1/5*HEIGHT, 1/4*HEIGHT, WIDTH-2/5*HEIGHT, 1/5*HEIGHT)
second_button = pg.Rect(1/5*HEIGHT, 11/20*HEIGHT, WIDTH-2/5*HEIGHT, 1/5*HEIGHT)
restart_button = pg.Rect(LEFT_GAP + 8.5 * PIT_SIZE, HEIGHT-(1/5*HEIGHT+MID_GAP), 7/5*PIT_SIZE, 1/5*HEIGHT)
quit_button = pg.Rect(LEFT_GAP + 8.5 * PIT_SIZE, HEIGHT-2*(1/5*HEIGHT+MID_GAP), 7/5*PIT_SIZE, 1/5*HEIGHT)

# game loop
while True:
    if screen_id == SCREEN_START:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            elif event.type == pg.MOUSEBUTTONDOWN:
                if first_button.collidepoint(pg.mouse.get_pos()):
                    human = 0
                    print("first button pressed")
                    screen_id = SCREEN_GAME
                elif second_button.collidepoint(pg.mouse.get_pos()):
                    human = 1
                    print("second button pressed")
                    screen_id = SCREEN_GAME

        screen.fill(COLORS["light blue"])
        pg.draw.rect(screen, COLORS["light yellow"], first_button)
        text_1 = font.render("Ich fange an!", True, "black")
        screen.blit(text_1, text_1.get_rect(center=first_button.center).topleft)
        pg.draw.rect(screen, COLORS["light pink"], second_button)
        text_2 = font.render("Der Computer fängt an!", True, "black")
        screen.blit(text_2, text_2.get_rect(center=second_button.center).topleft)
        pg.display.flip()
        clock.tick(60)

    elif screen_id == SCREEN_GAME:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            elif not move and event.type == pg.MOUSEBUTTONDOWN:
                if current_player == human:
                    for i in game_state.moves:
                        if rects[current_player][i].collidepoint(pg.mouse.get_pos()):
                            pit = i
                            print("pit: " + str(pit))
                            game_state = game_state.generate_child(pit)
                            move = True
                            pg.time.set_timer(pg.event.Event(3), 500)
                            hand += board[current_player][pit]
                            board[current_player][pit] = 0
                            pit = (pit + 1) % 16
                else:
                    pit = computer.best_move(game_state)
                    print("pit (c): " + str(pit))
                    game_state = game_state.generate_child(pit)
                    move = True
                    pg.time.set_timer(pg.event.Event(3), 500)
                    hand += board[current_player][pit]
                    board[current_player][pit] = 0
                    pit = (pit + 1) % 16

            elif move and event.type == pg.MOUSEBUTTONDOWN:
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
                    if game_state.winner is not None:
                        screen_id = SCREEN_GAMEOVER
                    print(game_state.board)
                    print(current_player)

        # screen.blit(BG, (0, 0))
        screen.fill(COLORS["light blue"])
        screen.blit(board_img, (LEFT_GAP, TOP_GAP))
        for i in range(2):
            for j in range(16):
                num = board[i][j]
                show_num = False
                if num == 0:
                    continue
                if num == 1:
                    img = PIT_IMAGES["pit_1"]
                elif num == 2:
                    img = PIT_IMAGES["pit_2"]
                elif num == 3:
                    img = PIT_IMAGES["pit_3"]
                elif num == 4:
                    img = PIT_IMAGES["pit_4"]
                elif 4 < num < 8:
                    img = PIT_IMAGES["pit_5"]
                    show_num = True
                else:
                    img = PIT_IMAGES["pit_more"]
                    show_num = True
                screen.blit(img, img.get_rect(center=rects[i][j].center).topleft)
                if show_num:
                    number = font.render(str(num), True, "black")
                    screen.blit(number, number.get_rect(center=rects[i][j].center).topleft)

        show_hand = False
        if hand == 1:
            img = PIT_IMAGES["pit_1"]
        elif hand == 2:
            img = PIT_IMAGES["pit_2"]
        elif hand == 3:
            img = PIT_IMAGES["pit_3"]
        elif hand == 4:
            img = PIT_IMAGES["pit_4"]
        elif 4 < hand < 8:
            img = PIT_IMAGES["pit_5"]
            show_hand = True
        else:
            img = PIT_IMAGES["pit_more"]
            show_hand = True

        if hand != 0:
            screen.blit(img, img.get_rect(center=(LEFT_GAP + 9 * PIT_SIZE, TOP_GAP + HEIGHT_BOARD / 2)))
        if show_hand and hand != 0:
            number = font.render(str(hand), True, "black")
            screen.blit(number, number.get_rect(center=(LEFT_GAP + 9 * PIT_SIZE, TOP_GAP + HEIGHT_BOARD / 2)).topleft)

        pg.display.flip()
        clock.tick(60)

    elif screen_id == SCREEN_GAMEOVER:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            elif event.type == pg.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(pg.mouse.get_pos()):
                    board = [[2] * 16, [2] * 16]
                    game_state = GameState.GameState(board, 0)
                    print("restart button pressed: new game")
                    screen_id = SCREEN_START
                elif quit_button.collidepoint(pg.mouse.get_pos()):
                    board = [[2] * 16, [2] * 16]
                    game_state = GameState.GameState(board, 0)
                    print("quit button pressed: quit game")
                    pg.quit()
                    raise SystemExit

        screen.fill(COLORS["light blue"])
        screen.blit(board_img, (LEFT_GAP, TOP_GAP))
        for i in range(2):
            for j in range(16):
                num = board[i][j]
                show_num = False
                if num == 0:
                    continue
                if num == 1:
                    img = PIT_IMAGES["pit_1"]
                elif num == 2:
                    img = PIT_IMAGES["pit_2"]
                elif num == 3:
                    img = PIT_IMAGES["pit_3"]
                elif num == 4:
                    img = PIT_IMAGES["pit_4"]
                elif 4 < num < 8:
                    img = PIT_IMAGES["pit_5"]
                    show_num = True
                else:
                    img = PIT_IMAGES["pit_more"]
                    show_num = True
                screen.blit(img, img.get_rect(center=rects[i][j].center).topleft)
                if show_num:
                    number = font.render(str(num), True, "black")
                    screen.blit(number, number.get_rect(center=rects[i][j].center).topleft)

        show_hand = False
        if hand == 1:
            img = PIT_IMAGES["pit_1"]
        elif hand == 2:
            img = PIT_IMAGES["pit_2"]
        elif hand == 3:
            img = PIT_IMAGES["pit_3"]
        elif hand == 4:
            img = PIT_IMAGES["pit_4"]
        elif 4 < hand < 8:
            img = PIT_IMAGES["pit_5"]
            show_hand = True
        else:
            img = PIT_IMAGES["pit_more"]
            show_hand = True

        if hand != 0:
            screen.blit(img, img.get_rect(center=(LEFT_GAP + 9 * PIT_SIZE, TOP_GAP + HEIGHT_BOARD / 2)))
        if show_hand and hand != 0:
            number = font.render(str(hand), True, "black")
            screen.blit(number, number.get_rect(center=(LEFT_GAP + 9 * PIT_SIZE, TOP_GAP + HEIGHT_BOARD / 2)).topleft)

        pg.draw.rect(screen, COLORS["light yellow"], restart_button)
        text_3 = font2.render("Neues Spiel", True, "black")
        screen.blit(text_3, text_3.get_rect(center=restart_button.center).topleft)
        pg.draw.rect(screen, COLORS["light pink"], quit_button)
        text_4 = font2.render("Mir reichts!", True, "black")
        screen.blit(text_4, text_4.get_rect(center=quit_button.center).topleft)

        pg.display.flip()
        clock.tick(60)
