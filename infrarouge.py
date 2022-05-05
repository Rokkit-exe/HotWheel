import gpiozero

class InfraRouge():
    def __init__(self):
        self.SGT = gpiozero.DigitalInputDevice(8)
        self.SGE = gpiozero.DigitalInputDevice(25)
        self.SDT = gpiozero.DigitalInputDevice(21)
        self.SDE = gpiozero.DigitalInputDevice(20)

        self.SGE.when_deactivated = self.inactif_gauche()
        self.SDE.when_deactivated = self.inactif_droit()


    def inactif_gauche():
        print("gauche")
    def inactif_droit():
        print("droite")
