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
        self.path_trouver = None
        self.toute_vue = None
        self.chemin = []

    def plus_court_chemin(self, depart, fin):
        # Initialiser la liste de noeuds
        noeuds = []
        for i in range(len(self.matrice)):
            noeuds.append(Noeud())
        noeuds[depart].distance = 0
        noeuds[depart].prec = 0

#self.index_courant,
        while(not self.fin_explorer):
            if(noeuds[fin] == self.courant):
                        self.fin_explorer = True
            else:
                plus_petite_distance = Noeud.Inf
                for i in range(len(noeuds)):
                    if(noeuds[i].distance < plus_petite_distance and not noeuds[i].vu):
                        self.index_courant = i
                        plus_petite_distance = noeuds[i].distance
                        
                            
                self.courant = noeuds[self.index_courant]
                self.courant.vu = True
                #print(f"noeud courant => {self.index_courant}")

                for i in range(len(self.matrice[self.index_courant])):
                    if not noeuds[i].vu:                    
                        distance_voisin = self.matrice[self.index_courant][i] + self.courant.distance
                    
                        if(distance_voisin < noeuds[i].distance):
                            noeuds[i].distance = distance_voisin
                            noeuds[i].prec = self.index_courant
                            #print(f"nouvelle distance du noeuds {i} => {distance_voisin}")
                    
        self.index_courant = fin
        bool = True
        while(bool):
            if(self.index_courant == depart):
                bool = False
            self.chemin.append(self.index_courant)
            self.index_courant = noeuds[self.index_courant].prec
        self.chemin.reverse()
        return self.chemin



