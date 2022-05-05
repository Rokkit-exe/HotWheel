import sys
from graphe import Graphe
from mouvement import Mouvement
from infrarouge import InfraRouge
Inf = sys.maxsize

matrice_distances =  [ [  0,   3,   1,   Inf, Inf, Inf ],  
                       [  3,   0,   1,   3,   Inf, Inf ],
                       [  1,   1,   0,   3,   5,   Inf ],
                       [  Inf, 3,   3,   0,   1,   3   ],
                       [  Inf, Inf, 5,   1,   0,   1   ],
                       [  Inf, Inf, Inf, 3,   1,   0   ] ]

graphe = Graphe(matrice_distances)

M = Mouvement()
Infra = InfraRouge()

M.forward(100, 1);


#print(graphe.plus_court_chemin(0, 5)) # [0, 2, 3, 4, 5]
#print(graphe.plus_court_chemin(5, 0)) # [5, 4, 3, 2, 0]
