import gpiozero
import time

class InfraRouge():
    def __init__(self):   
        self.IRG = gpiozero.DigitalInputDevice(23)
        self.IRD = gpiozero.DigitalInputDevice(24)
        self.gauche_actif = None
        self.droite_actif = None
        
        self.doit_arreter = False
        self.IRG.when_deactivated = self.actif_gauche
        self.IRD.when_deactivated = self.actif_droite
        self.IRG.when_activated = self.inactif_gauche
        self.IRD.when_activated = self.inactif_droite
    

    def actif_gauche(self):
        #time.sleep(0.05)
        if(self.droite_actif):
            self.doit_arreter = True

        
        
    def actif_droite(self):
        #time.sleep(0.05)
        if(self.gauche_actif):
            self.doit_arreter = True


    def inactif_gauche(self):
        self.doit_arreter = False
        
    def inactif_droite(self):
        self.doit_arreter = False

    
