import gpiozero
import time

class Mouvement:
    def __init__(self, capteur_infrarouge):
        self.IN1 = gpiozero.DigitalOutputDevice(6)
        self.IN2 = gpiozero.DigitalOutputDevice(5)  # moteur G
        self.ENA = gpiozero.PWMOutputDevice(13)

        self.IN3 = gpiozero.DigitalOutputDevice(15)
        self.IN4 = gpiozero.DigitalOutputDevice(14) # moteur D
        self.ENB = gpiozero.PWMOutputDevice(18)
        
        self.capteur_infrarouge = capteur_infrarouge
        self.Initialise()

    def Avancer(self):
        pass
            
    def main(self, est_detecter=False):
        while (not est_detecter):
            self.Initialise()
            self.IN1.on()
            self.IN3.on()
            self.ENA.value = 0.3
            self.ENB.value = 0.3
            time.sleep(0.01)
            if(self.capteur_infrarouge.gauche_actif and self.capteur_infrarouge.droite_actif):
                print("J'arrête")
                est_detecter = True
            else:
                if(self.capteur_infrarouge.gauche_actif):
                    print("Correction gauche")
                    self.Correction("gauche")
                if(self.capteur_infrarouge.droite_actif):
                    print("Correction droite")
                    self.Correction("droite")

    def Correction(self, dir, wait=0.06):
        self.Initialise()
        if (dir == "gauche"):
            self.IN2.on()
            self.IN3.on()
            self.ENA.value = 0.3
            self.ENB.value = 0.3
        elif (dir == "droite"):
            self.IN1.on()
            self.IN4.on()
            self.ENA.value = 0.3
            self.ENB.value = 0.3
        time.sleep(wait)
    
    def Tourner(self, dir, est_detecter = False,  wait=0.5):
        time.sleep(0.4)
        self.Initialise()
        while(not est_detecter):
            if (dir == "gauche"):
                self.IN2.on()
                self.IN3.on()
                self.ENA.value = 0.5
                self.ENB.value = 0.5
                if(self.capteur_infrarouge.gauche_actif):
                    print("IR activé")
                    est_detecter=True
                    self.Initialise()
            elif (dir == "droite"):
                self.IN1.on()
                self.IN4.on()
                self.ENA.value = 0.5
                self.ENB.value = 0.5
        
                if(self.capteur_infrarouge.droite_actif):
                    print("IR activé")
                    est_detecter=True
                    self.Initialise()
            
            

    def Initialise(self):
        self.ENA.off()
        self.ENB.off()
        self.IN1.off()
        self.IN2.off()
        self.IN3.off()
        self.IN4.off()
