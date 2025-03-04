import Game
import PlayerA1
import random


def optimieren(liste, factor, depth):
    for i in range(depth):
        print(liste)
        print("runde " + str(i))
        liste[9] = runde(liste)
        liste = angleichen(liste[9], liste, factor)
    return liste


def eins_gegen_eins(spieler_0, spieler_1):
    game1 = Game.Game((spieler_0, spieler_1))
    game1.play()
    return [game1.state.winner, game1.moves]


def runde(liste):
    spieler_x = PlayerA1.PlayerA1(liste[0], liste[1], liste[2], 2)
    spieler_y = PlayerA1.PlayerA1(liste[3], liste[4], liste[5], 2)
    spieler_z = PlayerA1.PlayerA1(liste[6], liste[7], liste[8], 2)
    score_x = [0, 0]
    score_y = [0, 0]
    score_z = [0, 0]
    for i in range(10):
        print(str(i) + "/10")
        spieler_rand = PlayerA1.PlayerA1(random.random(), random.random(), random.random(), 2)
        vergleich_xrand = vergleich(spieler_x, spieler_rand)
        vergleich_yrand = vergleich(spieler_y, spieler_rand)
        vergleich_zrand = vergleich(spieler_z, spieler_rand)
        score_x = [score_x[0] + vergleich_xrand[0], score_x[1] + vergleich_xrand[1]]
        score_y = [score_y[0] + vergleich_yrand[0], score_y[1] + vergleich_yrand[1]]
        score_z = [score_z[0] + vergleich_zrand[0], score_z[1] + vergleich_zrand[1]]
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


def vergleich(spieler_0, spieler_rand):
    game_01 = eins_gegen_eins(spieler_0, spieler_rand)
    game_10 = eins_gegen_eins(spieler_rand, spieler_0)
    if game_01[0] == 0:
        if game_10[0] == 1:
            score_0 = [2, (game_01[1] + game_10[1])]
        else:
            score_0 = [1, game_01[1]]
    else:
        if game_10[0] == 0:
            score_0 = [0, 0]
        else:
            score_0 = [1, game_10[1]]
    return score_0


def angleichen(win, liste, factor):
    match win:
        case "x":
            for i in range(6):
                liste[i + 3] = liste[i + 3] + (liste[i % 3] - liste[i + 3]) * factor
        case "y":
            for i in range(6):
                liste[(i + 6) % 9] = liste[(i + 6) % 9] + (liste[i % 3 + 3] - liste[(i + 6) % 9]) * factor
        case "z":
            for i in range(6):
                liste[i] = liste[i] + (liste[i % 3 + 6] - liste[i]) * factor
    return liste
