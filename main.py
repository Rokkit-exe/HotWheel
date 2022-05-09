import sys
from graphe import Graphe
from mouvement import Mouvement
from infrarouge import InfraRouge
Inf = sys.maxsize

matrice_distances = [[0,   3,   1,   Inf, Inf, Inf],
                     [3,   0,   1,   3,   Inf, Inf],
                     [1,   1,   0,   3,   5,   Inf],
                     [Inf, 3,   3,   0,   1,   3],
                     [Inf, Inf, 5,   1,   0,   1],
                     [Inf, Inf, Inf, 3,   1,   0]]

matrice_distances = [ #1   2    3     4     5     6     7     8     9    10    11    12    13    14    15    16    17    18    19
                     [ 0,  1,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [ 1,  0,   2,    3,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf, 2,   0,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf, 3,  Inf,   0,    1,    3,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,   1,    0,    3,   Inf,   3,   Inf,  Inf,   2,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,   3,   Inf,   0,    2,    1,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,   2,    0,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,   3,    1,   Inf,   0,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,   3,    0,    1,   Inf,  Inf,  Inf,  Inf,  Inf,   2,   Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   1,    0,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,   2,   Inf,  Inf,  Inf,  Inf,  Inf,   0,    2,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,    0,    1,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   1,    0,    3,   Inf,   4,   Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   3,    0,    4,   Inf,   2,   Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,   Inf,  Inf,  Inf,  Inf,   4,    0,   Inf,  Inf,  Inf,   2],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   4,   Inf,  Inf,   0,   Inf,  Inf,  Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,   Inf,  Inf,   0,    2,    4],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,    0,   Inf],
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,   Inf,   4,   Inf,   0]]

graphe = Graphe(matrice_distances)

M = Mouvement()
Infra = InfraRouge()

M.turn("left", Infra, 1)


# print(graphe.plus_court_chemin(0, 5)) # [0, 2, 3, 4, 5]
# print(graphe.plus_court_chemin(5, 0)) # [5, 4, 3, 2, 0]
