import Game
import PlayerA
import PlayerB
import GameState

game1 = Game.Game()
player_a_1 = PlayerA.PlayerA(6, 0, 0, 2)
player_a_2 = PlayerA.PlayerA(3, 2, 1, 2)
player_b_1 = PlayerB.PlayerB()

# game1.spiel(player_a_1, player_a_2)
game_state_1 = GameState.GameState([[1, 4, 3, 0, 3, 0, 1, 4, 3, 6, 14, 1, 2, 9, 1, 3], [0, 2, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]], 0)

game_state_2 = game_state_1.generate_child(7).generate_child(5).generate_child(1)
game1.show_board(game_state_2.board)

print(game_state_2.winner)
