import GameState


class Game:
    def __init__(self, players):
        self.state = GameState.GameState([[2] * 16, [2] * 16], 0)
        self.moves = 0
        self.move_history = []
        self.players = players

    def play(self):
        # self.show_board(self.state.board)
        while self.state.winner is None:
            # print("~~~")
            # print(self.players[self.state.current_player].total_val(self.state))
            self.state = self.state.generate_child(self.players[self.state.current_player]
                                                   .best_move(self.state))
            self.moves += 1
            # print("züge: " + str(self.moves))
            # self.show_board(self.state.board)
            # print("~~~")

        # print("spiel zu ende")

    def go_back(self):
        self.state = self.move_history.pop()
        self.moves -= 1

    def show_board(self, board):
        print(board[1][7::-1])
        print(board[1][8:])
        print(board[0][15:7:-1])
        print(board[0][:8])
        print()
