import gpiozero

class InfraRouge():
    def __init__(self):
        
        self.IRG = gpiozero.DigitalInputDevice(23)
        self.IRD = gpiozero.DigitalInputDevice(24)

        self.IRG.when_deactivated 
        self.IRD.when_deactivated 
        self.IRG.when_activated
        self.IRD.when_activated
    

   
