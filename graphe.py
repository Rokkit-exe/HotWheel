from noeud import Noeud
class Graphe:
    def __init__(self,matrice_distance):
        self.matrice = matrice_distance
        self.fin_explorer = False
        self.courant = None
        self.index_courant = None
        self.prochain = None
        self.index_prochain = None
        self.min_distance = Noeud.Inf
        
        self.chemin = []

    def plus_court_chemin(self, depart, fin):
        # Initialiser la liste de noeuds
        noeuds = []
        for i in range(len(self.matrice)):
            noeuds.append(Noeud())
        noeuds[depart].distance = 0
        noeuds[depart].vu = True
        noeuds[depart].prec = noeuds[depart]
        self.courant = noeuds[depart]
        self.index_courant = depart
        self.chemin.append(self.index_courant)

        #boucle
        #while not self.fin_explorer:
        for f in range(5):
            for i in range(self.index_courant, len(self.matrice[self.index_courant])):
                distance_voisin = self.matrice[self.index_courant][i]
                if (distance_voisin != Noeud.Inf):
                    if (distance_voisin < self.min_distance and distance_voisin != 0):
                        print(f"distance voisin: {distance_voisin}")
                        self.index_prochain = i
                        noeuds[self.index_prochain].distance = distance_voisin + self.courant.distance
                        self.min_distance = distance_voisin

            if (self.courant == noeuds[fin]):
                print("fini")
                self.fin_explorer = True

            noeuds[self.index_prochain].prec = self.courant
            self.courant = noeuds[self.index_prochain]
            self.index_courant = self.index_prochain
            self.courant.vu = True
            self.courant.distance = distance_voisin
            self.min_distance = Noeud.Inf

            self.chemin.append(self.index_courant)

            print(f"index courant: {self.index_courant}")
            print()

        return self.chemin



