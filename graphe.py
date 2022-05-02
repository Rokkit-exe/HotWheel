from noeud import Noeud
class Graphe:
    def __init__(self,matrice_distance):
        self.__distances = matrice_distance
        self.fin_explorer = False
        self.noeud_courrant = None
        self.plus_petit = None

    def plus_court_chemin(self, depart, fin):
        # Initialiser la liste de noeuds
        noeuds = []
        for i in range(len(self.__distances)):
            noeuds.append(Noeud())
        noeuds[depart].distance = 0
        self.noeud_courrant = noeuds[depart]


        while not self.fin_explorer:
            for i in self.__distances[depart]:
                if (self.__distances[i] + self.noeud_courrant.distance < Noeud.Inf and not self.__distances[i] == 0):
                    noeuds[i].distance = self.__distances[i]
                    noeuds[i].vu = True # pas sur
                    

