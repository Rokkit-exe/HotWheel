import sys
from graphe import Graphe
from mouvement import Mouvement
from infrarouge import InfraRouge
from controleur import Controler
Inf = sys.maxsize


                      #0   1    2     3     4     5     6     7     8    9     10    11    12    13    14    15    16    17    18
matrice_distances = [ #1   2    3     4     5     6     7     8     9    10    11    12    13    14    15    16    17    18    19
                     [ 0,  1,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 0
                     [ 1,  0,   2,    3,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 1
                     [Inf, 2,   0,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 2
                     [Inf, 3,  Inf,   0,    1,    3,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 3
                     [Inf,Inf, Inf,   1,    0,    3,   Inf,   3,   Inf,  Inf,   2,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 4
                     [Inf,Inf, Inf,   3,   Inf,   0,    2,    1,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 5
                     [Inf,Inf, Inf,  Inf,  Inf,   2,    0,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 6
                     [Inf,Inf, Inf,  Inf,   3,    1,   Inf,   0,    3,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 7
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,   3,    0,    1,   Inf,  Inf,  Inf,  Inf,   2,  Inf,   Inf,  Inf,  Inf], # 8
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   1,    0,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 9
                     [Inf,Inf, Inf,  Inf,   2,   Inf,  Inf,  Inf,  Inf,  Inf,   0,    2,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 10
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,    0,    1,   Inf,  Inf,  Inf,  Inf,  Inf,  Inf], # 11
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   1,    0,    3,   Inf,   4,   Inf,  Inf,  Inf], # 12
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   3,    0,    4,   Inf,   2,   Inf,  Inf], # 13
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,   Inf,  Inf,  Inf,  Inf,   4,    0,   Inf,  Inf,  Inf,   2],  # 14
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   4,   Inf,  Inf,   0,   Inf,  Inf,  Inf], # 15
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,   Inf,  Inf,   0,    2,    4],  # 16
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,    0,   Inf], # 17
                     [Inf,Inf, Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,  Inf,   2,   Inf,   4,   Inf,   0]]  # 18

tab_direction = [(1,2), (1,3), (1,5), (4,3), (5,3), (4,6), (2,6), (5,6), (5,9), (5,10), (5,1), (7,1), (7,2), (7,5), (7,9), (11,2), (9,5), (11,5), (9,9)]


graphe = Graphe(matrice_distances)
Infra = InfraRouge()
M = Mouvement(Infra)
C = Controler(M, graphe, tab_direction, 'n', Infra)

#noeud_depart = input("Entrez le noeud de départ:")
#noeud_fin = input("Entrez le noeud de fin:")

#C.Demarer(noeud_depart, noeud_fin)
C.Demarer(0, 15)



#M.main()

#M.Initialise()



#print(graphe.plus_court_chemin(18, 1)) # [0, 2, 3, 4, 5]
# print(graphe.plus_court_chemin(5, 0)) # [5, 4, 3, 2, 0]
#print(graphe.plus_court_chemin(0, 5)) # [0, 2, 3, 4, 5]
#print(graphe.plus_court_chemin(5, 0)) # [5, 4, 3, 2, 0]
