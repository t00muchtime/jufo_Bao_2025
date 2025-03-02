
class PlayerA:
    def __init__(self, x, y, z, depth):
        self.x, self.y, self.z = x, y, z
        self.depth = depth

    def value(self, game, player):
        board = game.board
        if game.win(player ^ 1):
            return -(self.x+self.y+self.z)
        else:
            m = 0
            for i in board[player][8:15]:
                if i > 2:
                    m += (i / sum(board[player])) ** 2

            return self.x*sum(board[player])/64 - self.y*board[player].count(0)/16 - self.z*m

    def total_val(self, game):
        return self.value(game, 0)-self.value(game, 1)

    def val_depth(self, game, depth):
        player = (-1) ** game.player_turn
        if depth == 0:
            return player*self.total_val(game)
        max_value = -10
        for pit in range(16):
            if game.board[game.player_turn][pit] > 1:
                game.move(pit)
                value = -self.val_depth(game, depth - 1)
                game.go_back()
                if value > max_value:
                    max_value = value
        return max_value

    def best_move(self, spiel):
        max_val = -10
        max_pit = 0
        for pit in range(16):
            if spiel.board[spiel.player_turn][pit] > 1:
                spiel.move(pit)
                value = -self.val_depth(spiel, self.depth - 1)
                spiel.go_back()
                if value > max_val:
                    max_val = value
                    max_pit = pit
        return max_pit
