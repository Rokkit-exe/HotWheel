import time, threading


class Controleur: 
    def __init__(self, mouvement, graphe, tab_points, direction, infra):
        self.dir_courante = direction
        self.dir_suivante = None
        self.mouvement = mouvement
        self.graphe = graphe
        self.chemin = None
        self.tab_points = tab_points
        self.point_courant = None
        self.prochain_point = None
        self.stop = False
        self.infra = infra
        self.thread_gauche = threading.Thread(target=self.set_value_capteur, args=(self.infra, 'left'))
        self.thread_droite = threading.Thread(target=self.set_value_capteur, args=(self.infra, 'right'))
        self.lock = threading.Lock()

    def Demarrer(self, depart, fin):
        self.chemin = self.graphe.plus_court_chemin(depart, fin)
        index = 0
        self.thread_droite.start()
        self.thread_gauche.start()
        while index != len(self.chemin) - 1:
            
            self.mouvement.Initialiser()
            self.point_courant = self.chemin[index]
            self.prochain_point = self.chemin[index+1]

            self.dir_suivante = self.get_direction(self.point_courant, self.prochain_point)
            if (self.dir_courante != self.dir_suivante):
                self.mouvement.Tourner(self.get_direction(self.dir_courante, self.dir_suivante))
                self.dir_courante = self.dir_suivante
            else:
                self.mouvement.Initialiser()
                time.sleep(0.5)
            
            self.mouvement.Avancer()
            index += 1

        self.stop = True
        self.thread_droite.join()
        self.thread_gauche.join()

    def set_value_capteur(self, infra, dir):
        while not self.stop:
            time.sleep(0.01)
            if (dir == 'left'):
                with self.lock:
                    if infra.IRG.value:
                        infra.gauche_actif =  True 
                    else:
                        time.sleep(0.04)
                        infra.gauche_actif = False
            elif(dir == 'right'):
                with self.lock:
                    if infra.IRD.value:
                        infra.droite_actif = True 
                    else:
                        time.sleep(0.04)
                        infra.droite_actif = False


    def get_direction(self, point_courant, prochain_point):
        if (self.tab_points[point_courant][0] == self.tab_points[prochain_point][0]): # x
            if (self.tab_points[point_courant][1] > self.tab_points[prochain_point][1]):
                return 's'
            elif (self.tab_points[point_courant][1] < self.tab_points[prochain_point][1]):
                return 'n'
        elif (self.tab_points[point_courant][1] == self.tab_points[prochain_point][1]): #y
            if (self.tab_points[point_courant][0] > self.tab_points[prochain_point][0]):
                return 'e'
            elif (self.tab_points[point_courant][0] < self.tab_points[prochain_point][0]):
                return 'w'
        return None

    def get_direction(self, dir_courante, dir):
        
        if (dir_courante == 'n'):
            if (dir == 'e'):
                return 'right'
            if (dir == 'w'):
                return 'left'
        if (dir_courante == 'e'):
            if (dir == 's'):
                return 'right'
            if (dir == 'n'):
                return 'left'
        if (dir_courante == 's'):
            if (dir == 'w'):
                return 'right'
            if (dir == 'e'):
                return 'left'
        if (dir_courante == 'w'):
            if (dir == 'n'):
                return 'right'
            if (dir == 's'):
                return 'left'

