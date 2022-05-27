import gpiozero
import time

class InfraRouge():
    def __init__(self):   
        self.IRG = gpiozero.DigitalInputDevice(23)
        self.IRD = gpiozero.DigitalInputDevice(24)

        self.gauche_actif = None
        self.droite_actif = None

        #self.IRG.when_deactivated = self.actif_gauche
        #self.IRD.when_deactivated = self.actif_droite
        #self.IRG.when_activated = self.inactif_gauche
        #self.IRD.when_activated = self.inactif_droite
    

    def actif_gauche(self):
        self.gauche_actif = True
        
    def actif_droite(self):
        self.droite_actif = True

    def inactif_gauche(self):
        time.sleep(0.3)
        self.gauche_actif = False
        
    def inactif_droite(self):
        time.sleep(0.3)
        self.droite_actif = False

    
