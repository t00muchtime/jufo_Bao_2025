
class PlayerB:
    def __init__(self):
        pass

    def input(self, spiel):
        pit = int(input("Mulde: "))
        while spiel.board[spiel.player_turn][pit] < 2:
            pit = int(input("Mulde muss mindestens 2 Bohnen enthalten: "))
        return pit

    def best_move(self, spiel):
        return self.input(spiel)

    def total_val(self, game):
        return None
