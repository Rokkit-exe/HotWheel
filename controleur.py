
class Controler: 
    def __init__(self, mouvement, graphe, matrice, tab_points, direction) -> None:
        self.cur_direction = direction
        self.next_direction = None
        self.mouvement = mouvement
        self.graphe = graphe
        self.matrice = matrice
        self.chemin = None
        self.tab_points = tab_points
        self.point_courant = None
        self.prochain_point = None

    def main(self, depart, fin):
        self.chemin = self.graphe.plus_court_chemin(depart, fin)
        index = 0
        while index != len(self.chemin - 1):
            self.mouvement.avancer()
            self.point_courant = self.chemin[index]
            self.prochain_point = self.chemin[index+1]

            self.next_direction = self.get_direction(self.point_courant, self.prochain_point)
            if (self.cur_direction != self.next_direction):
                self.mouvement.turn(self.get_turn(self.cur_direction, self.next_direction))
                self.cur_direction = self.next_direction
            index += 1




    def get_direction(self, point1, point2):
        if (point1[0] == point2[0]): # x
            if (point1[1] > point2[1]):
                return 'n'
            elif (point1[1] < point2[1]):
                return 's'
        elif (point1[1] == point2[1]): #y
            if (point1[0] > point2[0]):
                return 'w'
            elif (point1[0] < point2[0]):
                return 'e'
        return None

    def get_turn(self, cur_dir, dir):
        #directions = ['n', 'e', 's', 'w']
        if (cur_dir == 'n'):
            if (dir == 'e'):
                return 'right'
            if (dir == 's'):
                return 'right', 'right'
            if (dir == 'w'):
                return 'left'
        if (cur_dir == 'e'):
            if (dir == 's'):
                return 'right'
            if (dir == 'w'):
                return 'right', 'right'
            if (dir == 'n'):
                return 'left'
        if (cur_dir == 's'):
            if (dir == 'w'):
                return 'right'
            if (dir == 'n'):
                return 'right', 'right'
            if (dir == 'e'):
                return 'left'
        if (cur_dir == 'w'):
            if (dir == 'n'):
                return 'right'
            if (dir == 'e'):
                return 'right', 'right'
            if (dir == 's'):
                return 'left'

