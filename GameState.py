class GameState:
    def __init__(self, board, current_player):
        self.board = board
        self.current_player = current_player
        self.moves = self.list_moves()
        self.is_terminal = self.moves == []

    def list_moves(self):
        moves = []
        if (not any(x > 0 for x in self.board[self.current_player][8:16])
                or not any(x > 0 for x in self.board[self.current_player ^ 1][8:16])
                or not any(x > 1 for x in self.board[self.current_player ^ 1])):
            return moves
        for i in range(16):
            if self.board[self.current_player][i] > 1:
                moves.append(i)
