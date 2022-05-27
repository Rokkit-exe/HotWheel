import sys
from graphe import Graphe
from mouvement import Mouvement
from infrarouge import InfraRouge
from controleur import Controler
Inf = sys.maxsize


Infra = InfraRouge()
M = Mouvement(Infra)
M.Initialise()