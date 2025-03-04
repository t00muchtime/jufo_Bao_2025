import Game
import PlayerA
import PlayerA1
import PlayerB
import GameState
import Optimierung

'''
player_a_1 = PlayerA1.PlayerA1(3, 7, 0, 4)
player_a_2 = PlayerA1.PlayerA1(3, 7, 0, 4)

game1 = Game.Game((player_a_1, player_a_2))
game1.play()'''

print(Optimierung.optimieren([1, 0, 0, 0, 1, 0, 0, 0, 1, "x"], 10, 0.2, 10))
