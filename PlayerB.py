
class PlayerB:
    def input(self, spiel):
        pit = int(input("Mulde: "))
        while spiel.board[spiel.current_player][pit] < 2:
            pit = int(input("Mulde muss mindestens 2 Bohnen enthalten: "))
        return pit

    def best_move(self, spiel):
        return self.input(spiel)

    def total_val(self, game):
        return None
