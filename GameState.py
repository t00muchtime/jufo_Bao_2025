class GameState:
    def __init__(self, board, current_player):
        self.board = board
        self.current_player = current_player
        self.winner = self.is_game_over()
        self.moves = self.list_moves()
        # self.children = []

    def list_moves(self):
        moves = []
        if self.winner is None:
            for i in range(16):
                if self.board[self.current_player][i] > 1:
                    moves.append(i)
        return moves

    def is_game_over(self):
        if (not any(x > 0 for x in self.board[self.current_player][8:16])
                or not any(x > 1 for x in self.board[self.current_player])):
            return self.current_player ^ 1
        if (not any(x > 0 for x in self.board[self.current_player ^ 1][8:16])
                or not any(x > 1 for x in self.board[self.current_player ^ 1])):
            return self.current_player
        return None

    def generate_child(self, pit):
        board = [self.board[0][:], self.board[1][:]]

        hand = board[self.current_player][pit]
        board[self.current_player][pit] = 0
        pit = (pit + 1) % 16
        n = 0
        while hand > 1:
            n += 1
            while hand > 1:
                board[self.current_player][pit] += 1
                hand -= 1
                pit = (pit + 1) % 16
            # letzte Bohne
            # Aufnehmen
            if board[self.current_player][pit] > 0:
                hand += board[self.current_player][pit]
                board[self.current_player][pit] = 0
                # Plündern
                if pit > 7:
                    hand += board[self.current_player ^ 1][23 - pit]
                    board[self.current_player ^ 1][23 - pit] = 0
                pit = (pit + 1) % 16
            else:
                board[self.current_player][pit] += 1
                hand -= 1
            if n > 1000:
                raise Exception("endloser Zug")

        return GameState(board, self.current_player ^ 1)
