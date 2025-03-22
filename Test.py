import Game
import PlayerA1
import PlayerB
import Optimierung
import cProfile
import pstats


player_a_1 = PlayerA1.PlayerA1(3, 7, 0, 3)
player_a_2 = PlayerB.PlayerB()

game1 = Game.Game((player_a_1, player_a_2))
game1.play()

