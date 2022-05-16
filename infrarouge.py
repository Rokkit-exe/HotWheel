import gpiozero

class InfraRouge():
    def __init__(self):
        
        # -------------  Sonars  --------------
        #self.SGT = gpiozero.DigitalInputDevice(8, bounce_time=0.1)
        #self.SGE = gpiozero.DigitalInputDevice(25, bounce_time=0.1)
        #self.SDT = gpiozero.DigitalInputDevice(21, bounce_time=0.1)
        #self.SDE = gpiozero.DigitalInputDevice(20, bounce_time=0.1)
        
        self.IRG = gpiozero.DigitalInputDevice(23)
        self.IRD = gpiozero.DigitalInputDevice(24)

        self.gauche_actif = None
        self.droite_actif = None
        self.aucun_actif = not self.gauche_actif and not self.droite_actif if True else False

        self.IRG.when_deactivated = self.actif_gauche
        self.IRD.when_deactivated = self.actif_droite
        self.IRG.when_activated = self.inactif_gauche
        self.IRD.when_activated = self.inactif_droite
    

    def actif_gauche(self):
        print("Actif gauche")
        self.gauche_actif = True
        self.aucun_actif = not self.gauche_actif and not self.droite_actif if True else False
    def actif_droite(self):
        print("Actif droite")
        self.droite_actif = True
        self.aucun_actif = not self.gauche_actif and not self.droite_actif if True else False

    def inactif_gauche(self):
        self.gauche_actif = False
        self.aucun_actif = not self.gauche_actif and not self.droite_actif if True else False
    def inactif_droite(self):
        self.droite_actif = False
        self.aucun_actif = not self.gauche_actif and not self.droite_actif if True else False
