import gpiozero
import time

class InfraRouge():
    def __init__(self):   
        self.IRG = gpiozero.DigitalInputDevice(23)
        self.IRD = gpiozero.DigitalInputDevice(24)
        self.compteur_gauche = None
        self.compteur_droite = None
        self.gauche_actif = None
        self.droite_actif = None
        self.doit_arreter = False
        self.IRG.when_deactivated = self.actif_gauche
        self.IRD.when_deactivated = self.actif_droite
        self.IRG.when_activated = self.inactif_gauche
        self.IRD.when_activated = self.inactif_droite
    

    def actif_gauche(self):
        if(self.compteur_gauche == None):
            self.doit_arreter = False
            self.compteur_gauche = time.perf_counter()
        if(self.compteur_droite - time.perf_counter() > 0.1 and not self.doit_arreter):
            self.doit_arreter = True
            self.compteur_gauche = None
            self.compteur_droite = None

        
        
    def actif_droite(self):
        if(self.compteur_droite == None):
            self.doit_arreter = False
            self.compteur_droite = time.perf_counter()
        if(self.compteur_gauche - time.perf_counter() > 0.1 and not self.doit_arreter):
            self.doit_arreter = True
            self.compteur_gauche = None
            self.compteur_droite = None


    def inactif_gauche(self):
        pass
        
    def inactif_droite(self):
        pass

    
