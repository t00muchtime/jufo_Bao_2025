import Game
import PlayerA0
import PlayerA1
import PlayerB
import GameState
import Optimierung
import random


player_a_1 = PlayerA1.PlayerA1(3, 7, 0, 3)
player_a_2 = PlayerA1.PlayerA1(3, 7, 0, 3)

game1 = Game.Game((player_a_1, player_a_2))
game1.play()

test = Optimierung.optimieren([1, 0, 0, 0, 1, 0, 0, 0, 1, "x"], 20, 0.2, 15)
print(test[:3])
print(test[3:6])
print(test[6:9])
print(test[9])


