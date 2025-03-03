import Game
import PlayerA
import random

class Optimierung:
    def __init__(self):
        pass

    def eins_gegen_eins(self, spieler_0, spieler_1):
        game1 = Game.Game()
        game1.spiel(spieler_0,spieler_1)
        return game1.moves

    def runde(self, liste):
        spieler_x = PlayerA.PlayerA(liste[0], liste[1], liste[2], 2)
        spieler_y = PlayerA.PlayerA(liste[3], liste[4], liste[5], 2)
        spieler_z = PlayerA.PlayerA(liste[6], liste[7], liste[8], 2)
        score_x = [0,0]
        score_y = [0,0]
        score_z = [0,0]
        i = 0
        while i < 100:
            spieler_rand = PlayerA.PlayerA(random.random(), random.random(), random.random(), 2)
            vergleich_xrand = self.vergleich(spieler_x, spieler_rand)
            vergleich_yrand = self.vergleich(spieler_y, spieler_rand)
            vergleich_zrand = self.vergleich(spieler_z, spieler_rand)
            score_x = [score_x[0] + vergleich_xrand[0], score_x[1] + vergleich_xrand[1]]
            score_y = [score_y[0] + vergleich_yrand[0], score_y[1] + vergleich_yrand[1]]
            score_z = [score_z[0] + vergleich_zrand[0], score_z[1] + vergleich_zrand[1]]
            i += 1
        print(score_x)
        print(score_y)
        print(score_z)
        if score_x[0] > score_y[0]:
            if score_x[0] > score_z[0]:
                win = "x"
            elif score_x[0] < score_z[0]:
                win = "z"
            elif score_x[1] < score_z[1]:
                win = "x"
            elif score_z[1] < score_x[1]:
                win = "z"
            else:
                win = liste[9]
        elif score_y[0] > score_x[0]:
            if score_y[0] > score_z[0]:
                win = "y"
            elif score_y[0] < score_z[0]:
                win = "z"
            elif score_y[1] < score_z[1]:
                win = "y"
            elif score_z[1] < score_y[1]:
                win = "z"
            else:
                win = liste[9]
        elif score_z[0] > score_x[0]:
            win = "z"
        elif score_x[0] > score_z[0]:
            if score_x[1] < score_y[1]:
                win = "x"
            elif score_y[1] < score_x[1]:
                win = "y"
            else:
                win = liste[9]
        else:
            if score_x[1] < score_y[1]:
                if score_x[1] < score_z[1]:
                    win = "x"
                elif score_z[1] < score_x[1]:
                    win = "z"
                else:
                    win = liste[9]
            else:
                if score_y[1] < score_z[1]:
                    win = "y"
                elif score_z[1] < score_y[1]:
                    win = "z"
                else:
                    win = liste[9]
        print(win)
        return win


    def vergleich(self, spieler_0, spieler_rand):
        game_01 = self.eins_gegen_eins(spieler_0, spieler_rand)
        game_10 = self.eins_gegen_eins(spieler_rand, spieler_0)
        if game_01 % 2 ^ 1 < 1:
            if game_10 % 2 ^ 1 > 0:
                score_0 = [2, (game_01 + game_10)/2]
            else:
                score_0 = [1, game_01]
        else:
            if game_10 % 2 ^ 1 < 1:
                score_0 = [0, 0]
            else:
                score_0 = [1, game_10]
        return score_0

    def angleichen(self, win, liste, factor):
        i = 0
        if win == "x":
            while i < 6:
                liste[i+3] = liste[i+3] + (liste[i%3] - liste[i+3]) * factor
                i += 1
        elif win == "y":
            while i < 6:
                liste[(i+6)%9] = liste[(i+6)%9] + (liste[i%3+3] - liste[(i+6)%9]) * factor
                i += 1
        else:
            while i < 6:
                liste[i] = liste[i] + (liste[i%3+6]-liste[i]) * factor
                i += 1
        return liste

    def optimieren(self, liste, factor, depth):
        if depth == 0:
            return liste
        liste[9] = self.runde(liste)
        liste = self.angleichen(liste[9], liste, factor)
        print(liste)
        return self.optimieren(liste, factor, depth-1)