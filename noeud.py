import sys
class Noeud:

    Inf = sys.maxsize
    def __init__(self):
        self.distance = Noeud.Inf
        self.prec = None
        self.vu = False
