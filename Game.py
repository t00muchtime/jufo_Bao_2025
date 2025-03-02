
class Game:
    def __init__(self):
        self.board = [[2] * 16, [2] * 16]
        self.player_turn = 0
        self.direction = 1
        self.moves = 0
        self.move_history = []

    def spiel(self, player_0, player_1):
        game_running = True
        self.show_board(self.board)
        while game_running:
            print("zug: " + str(self.moves + 1))
            if self.player_turn == 0:
                print("mulde: " + str(player_0.best_move(self)))
                self.move(player_0.best_move(self))
                print(player_0.total_stat_val(self))
            else:
                print("mulde: " + str(player_1.best_move(self)))
                self.move(player_1.best_move(self))
                print(player_1.total_stat_val(self))

            game_running = not (self.win(self.player_turn) or self.board in self.move_history)

            self.show_board(self.board)

        print("spiel zu ende")

    def move(self, pit):
        self.move_history.append([self.board[0][:], self.board[1][:]])
        hand = self.board[self.player_turn][pit]
        self.board[self.player_turn][pit] = 0
        pit = (pit + self.direction) % 16
        while hand > 1:
            while hand > 1:
                self.board[self.player_turn][pit] += 1
                hand -= 1
                pit = (pit + self.direction) % 16
            # letzte Bohne
            # Aufnehmen
            if self.board[self.player_turn][pit] > 0:
                hand += self.board[self.player_turn][pit]
                self.board[self.player_turn][pit] = 0
                # Pluendern
                if pit > 7:
                    hand += self.board[self.player_turn ^ 1][23 - pit]
                    self.board[self.player_turn ^ 1][23 - pit] = 0
                pit = (pit + self.direction) % 16
            else:
                self.board[self.player_turn][pit] += 1
                hand -= 1

        self.moves += 1
        self.player_turn = self.player_turn ^ 1

    def status(self):
        print("~~~")
        self.show_board(self.board)
        for i in self.move_history:
            self.show_board(i)
        print(self.moves)
        print(self.player_turn)
        print("~~~")

    def go_back(self):
        self.board = self.move_history.pop()
        self.moves -= 1
        self.player_turn ^= 1

    def win(self, player):
        if (not any(x > 0 for x in self.board[player ^ 1][8:16])
                or not any(x > 1 for x in self.board[player ^ 1])):
            return True
        else:
            return False

    def show_board(self, board):
        print(board[1][7::-1])
        print(board[1][8:])
        print(board[0][15:7:-1])
        print(board[0][:8])
        print()
