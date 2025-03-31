import math


class PlayerA1:
    def __init__(self, x, y, z, depth):
        self.x, self.y, self.z = x, y, z
        self.depth = depth

    class Cache:
        def __init__(self):
            self.table = {}

        def lookup(self, hash_key, depth):
            if hash_key in self.table:
                entry = self.table[hash_key]
                if entry['depth'] >= depth:
                    return entry['score']
            return None

        def store(self, hash_key, score, depth):
            self.table[hash_key] = {'score': score, 'depth': depth}

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

    def minimax(self, node, depth, table, alpha=-math.inf, beta=math.inf):
        hash_key = hash(node)  # !
        cached = table.lookup(hash_key, depth)

        if cached is not None:
            return cached

        if depth == 0 or node.winner is not None:
            return self.total_stat_val(node)

        if node.current_player == 0:
            max_value = -math.inf
            for move in node.moves:
                child = node.generate_child(move)
                val = self.minimax(child, depth - 1, table, alpha, beta)
                max_value = max(val, max_value)
                alpha = max(val, alpha)
                if beta <= alpha:
                    break
            table.store(hash_key, max_value, depth)
            return max_value

        if node.current_player == 1:
            min_value = math.inf
            for move in node.moves:
                child = node.generate_child(move)
                val = self.minimax(child, depth - 1, table, alpha, beta)
                min_value = min(val, min_value)
                beta = min(val, beta)
                if beta <= alpha:
                    break
            table.store(hash_key, min_value, depth)
            return min_value

    def total_val(self, node):
        return self.minimax(node, self.depth, self.Cache())

    def best_move(self, node):
        depth = self.depth
        if depth == 0 or node.winner is not None:
            return

        if node.current_player == 0:
            max_value = -math.inf
            for move in node.moves:
                child = node.generate_child(move)
                val = self.minimax(child, depth - 1, self.Cache())
                if val >= max_value:
                    max_value = val
                    best_move = move

        else:
            min_value = math.inf
            for move in node.moves:
                child = node.generate_child(move)
                val = self.minimax(child, depth - 1, self.Cache())
                if val <= min_value:
                    min_value = val
                    best_move = move
        return best_move
