import Game
import PlayerA
import PlayerA1
import PlayerB
import GameState

player_a_1 = PlayerA1.PlayerA1(1, 3, 0, 5)
player_a_2 = PlayerA1.PlayerA1(1, 3, 0, 5)

game1 = Game.Game((player_a_1, player_a_2))
game1.play()
