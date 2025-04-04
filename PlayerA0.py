import math


class PlayerA0:
    def __init__(self, x, y, z, depth):
        self.x, self.y, self.z = x, y, z
        self.depth = depth

    def stat_value(self, node, player):
        board = node.board
        if node.winner == player:
            return math.inf
        else:
            m = 0
            for i in board[player][8:]:
                if i > 2:
                    m += (i / sum(board[player])) ** 2

            return self.x * sum(board[player]) / 64 - self.y * board[player].count(0) / 16 - self.z * m

    def total_stat_val(self, node):
        return self.stat_value(node, 0) - self.stat_value(node, 1)

    def negamax(self, node, depth):
        if depth == 0 or node.winner is not None:
            return (-1) ** node.current_player * self.total_stat_val(node)

        max_value = -math.inf
        for move in node.moves:
            child = node.generate_child(move)
            val = -self.negamax(child, depth - 1)
            max_value = max(val, max_value)
        return max_value

    def total_val(self, node):
        return (-1) ** node.current_player * self.negamax(node, self.depth)

    def best_move(self, node):
        depth = self.depth
        if depth == 0 or node.winner is not None:
            return

        max_value = -math.inf
        for move in node.moves:
            child = node.generate_child(move)
            val = -self.negamax(child, depth - 1)
            if val >= max_value:
                max_value = val
                best_move = move
        return best_move
