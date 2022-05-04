from noeud import Noeud
class Graphe:
    def __init__(self,matrice_distance):
        self.matrice = matrice_distance
        self.fin_explorer = False
        self.courant = None
        self.index_courant = None
        self.prochain = None
        self.index_prochain = None
        self.index_prec = None
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

#self.index_courant,
        for i in range(5): # tent que la fin n'est pas explorer
            for i in range(len(self.matrice[self.index_courant])):
                distance_voisin = self.matrice[self.index_courant][i]
                print(f"distance voisin: {distance_voisin}")
                if (not noeuds[i].vu and distance_voisin != Noeud.Inf):
                    noeuds[i].distance = distance_voisin + self.courant.distance
                    print(f"noeud[{i}]: {noeuds[i].distance}")
                    if (distance_voisin < self.min_distance):
                        self.index_prochain = i
                        self.min_distance = distance_voisin + self.courant.distance
                        print(f"min_distance: {self.min_distance}" )
            
            if (noeuds[fin] == self.courant):
                self.fin_explorer = True
            else:
                print(f"INDEX PROCHAIN: {self.index_prochain}")
                if (self.min_distance <= noeuds[self.index_prochain].distance):
                    noeuds[self.index_prochain].prec = self.courant
                    self.courant = noeuds[self.index_prochain]
                    self.index_prec = self.index_courant
                    self.index_courant = self.index_prochain
                    self.courant.vu = True
                    self.chemin.append(self.index_courant)
                    self.min_distance = Noeud.Inf
                    print(f"NOEUD COURANT: {self.index_courant}")
                else:
                    self.courant = self.courant.prec
                    self.index_courant = self.index_prec
                    self.chemin.pop()
                    print(f"index_courant {self.index_courant}")
            

        return self.chemin



