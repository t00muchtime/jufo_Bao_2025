import Game
import PlayerA
import PlayerB
import GameState

player_a_1 = PlayerA.PlayerA(6, 0, 0, 2)
player_a_2 = PlayerA.PlayerA(3, 2, 1, 2)

game1 = Game.Game((player_a_1, player_a_2))
game1.play()
