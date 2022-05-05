import gpiozero

class InfraRouge():
    def __init__(self):
        self.SGT = gpiozero.DigitalInputDevice(8, bounce_time=0.1)
        self.SGE = gpiozero.DigitalInputDevice(25, bounce_time=0.1)
        self.SDT = gpiozero.DigitalInputDevice(21, bounce_time=0.1)
        self.SDE = gpiozero.DigitalInputDevice(20, bounce_time=0.1)

        self.gauche_actif = None
        self.droite_actif = None

        self.SGE.when_deactivated = self.actif_gauche
        self.SDE.when_deactivated = self.actif_droite
        self.SGE.when_activated = self.inactif_gauche
        self.SDE.when_activated = self.inactif_droite


    def actif_gauche(self):
        self.gauche_actif = True
    def actif_droite(self):
        self.droite_actif = True

    def inactif_gauche(self):
        self.gauche_actif = False
    def inactif_droite(self):
        self.droite_actif = False
