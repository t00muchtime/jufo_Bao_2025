import Game
import PlayerA1
import random


def optimieren(liste, number_games, factor, depth):
    for i in range(depth):
        print(liste)
        print("runde " + str(i))
        liste[9] = runde(liste, number_games)
        liste = angleichen(liste[9], liste, factor)
    return liste


def eins_gegen_eins(spieler_0, spieler_1):
    game1 = Game.Game((spieler_0, spieler_1))
    game1.play()
    return [game1.state.winner, game1.moves]


def runde(liste, number_games):
    spieler_x = PlayerA1.PlayerA1(liste[0], liste[1], liste[2], 2)
    spieler_y = PlayerA1.PlayerA1(liste[3], liste[4], liste[5], 2)
    spieler_z = PlayerA1.PlayerA1(liste[6], liste[7], liste[8], 2)

    score_x = score_y = score_z = [0, 0]
    for i in range(number_games):
        print(str(i) + "/" + str(number_games))
        spieler_rand = PlayerA1.PlayerA1(random.random(), random.random(), random.random(), 2)
        score_x = liste_addieren(score_x, vergleich(spieler_x, spieler_rand))
        score_y = liste_addieren(score_y, vergleich(spieler_y, spieler_rand))
        score_z = liste_addieren(score_z, vergleich(spieler_z, spieler_rand))
    print(score_x)
    print(score_y)
    print(score_z)
    siege = {score_x[0], score_y[0], score_z[0]}
    meiste_siege = max(siege)
    if len(siege) == 3:  # überprüfen
        if meiste_siege == score_x[0]:
            win = "x"
        elif meiste_siege == score_y[0]:
            win = "y"
        elif meiste_siege == score_z[0]:
            win = "z"
    else:
        züge = [x[1] for x in (score_x, score_y, score_z) if x[0] == meiste_siege]
        if len(set(züge)) == len(züge):
            wenigste_züge = min(züge)
            if wenigste_züge == score_x[1]:
                win = "x"
            elif wenigste_züge == score_y[1]:
                win = "y"
            elif wenigste_züge == score_z[1]:
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


def liste_addieren(liste1, liste2):
    return [a + b for a, b in zip(liste1, liste2)]
